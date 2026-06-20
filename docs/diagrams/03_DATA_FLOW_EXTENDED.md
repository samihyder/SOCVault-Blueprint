# SOCVault — Data Flow Diagrams (Extended)
**Version 1.0 | June 2026**

Additional DFD Level 1 and Level 2 flows not in [`22_DATA_FLOW_DIAGRAMS.md`](../22_DATA_FLOW_DIAGRAMS.md). Core flows (auth, L1, TI, SOAR, CI/CD, API Explorer) remain in doc 22.

**Notation:** Rectangle = external entity · Rounded = process · Cylinder = data store

---

## 1. Billing & tier gating (Phase 2)

**FR:** FR-101, FR-072–076 · **Wireframe:** `14-billing.html`

```mermaid
flowchart TB
  U([Tenant Owner])
  ST([Stripe])
  APP[React Billing UI]
  APIGW[API Gateway]
  API[Lambda API]
  MDB[(MongoDB\ntenants · subscriptions)]
  DDB[(DynamoDB\nfeature_flags)]
  AUD[(audit_log)]

  U -->|select plan| APP
  APP -->|POST /billing/checkout| APIGW --> API
  API -->|session| ST
  ST -->|webhook events| APIGW --> API
  API -->|update tier · targets| MDB
  API -->|cache tier gates| DDB
  API -->|log change| AUD

  subgraph Runtime gating
    SCAN[Scan Orchestrator]
    API -->|read tier| MDB
    SCAN -->|FR-101 check| DDB
  end
```

| Data | Store | PII |
|---|---|---|
| `stripe_customer_id`, `payment_tier` | MongoDB `tenants` | No |
| Webhook payload | Transient | Email in Stripe object |
| Tier gate snapshot | DynamoDB | No |

---

## 2. AI Chat & credits (Phase 3)

**FR:** FR-121–129 · **Wireframe:** `12-ai-chat.html`

```mermaid
flowchart TB
  U([Tenant User])
  CHAT[AI Chat UI]
  API[Lambda API]
  CL([Claude API])
  ST([Stripe])
  MDB[(MongoDB\ncredit_ledger)]
  DDB[(DynamoDB\nchat_sessions TTL)]
  SCAN[Scan Orchestrator]

  U -->|message| CHAT --> API
  API -->|balance check| MDB
  API -->|session context| DDB
  API -->|prompt + tools| CL
  CL -->|action intent| API
  API -->|deduct credits| MDB
  API -->|dispatch scan/remediate| SCAN
  U -->|buy credits| CHAT
  API -->|checkout| ST
  ST -->|webhook| API
  API -->|credit top-up| MDB
```

---

## 3. Multi-tenant isolation boundary

**FR:** FR-005, NFR-025 · **ADR:** ADR-006

```mermaid
flowchart TB
  subgraph TenantA["Tenant A — tenant_id: uuid-a"]
    UA([User A])
    DA[(MongoDB partition\ntenant_id = uuid-a)]
    SA[(S3 prefix\nuuid-a/)]
  end

  subgraph TenantB["Tenant B — tenant_id: uuid-b"]
    UB([User B])
    DB[(MongoDB partition\ntenant_id = uuid-b)]
    SB[(S3 prefix\nuuid-b/)]
  end

  JWT[Cognito JWT\n custom:tenant_id]
  API[Lambda API\nmandatory filter]

  UA --> JWT --> API
  UB --> JWT --> API
  API -->|query filter| DA & DB
  API -->|scoped keys| SA & SB

  API -.-x|blocked cross-tenant| DA
  API -.-x|blocked cross-tenant| DB
```

**Rules:**
1. Every MongoDB query includes `tenant_id` from JWT — never from request body alone.
2. S3 keys prefixed `{tenant_id}/{scan_id}/`.
3. Super Admin cross-tenant reads require internal RBAC (FR-155+) + audit (FR-165).

---

## 4. Pass & Keys vault data flow

**FR:** FR-183–193 · **Wireframe:** `24-admin-api-explorer.html`

```mermaid
flowchart LR
  SA([Super Admin])
  UI[API Explorer / Vault UI]
  API[Admin Lambda]
  DDB[(DynamoDB vault_items\nKMS envelope)]
  KMS[AWS KMS]
  SSM[SSM bootstrap keys]
  RUN[Runtime Workers]

  SA -->|create/reveal| UI --> API
  API -->|encrypt| KMS
  API -->|store ciphertext| DDB
  API -->|audit| AUD[(audit_log)]
  RUN -->|decrypt at runtime| KMS
  RUN -->|read snapshot| DDB
  SSM -->|platform secrets MVP| RUN
```

---

## 5. Metrics Observatory & COGS telemetry

**FR:** FR-105, FR-170–182 · **Wireframe:** `23-admin-observatory.html`

```mermaid
flowchart TB
  WRK[Scan Workers]
  CL([Claude])
  DDB[(DynamoDB\ncost_telemetry)]
  API[Admin API]
  OBS[Observatory UI]
  SA([Super Admin / Billing role])

  WRK -->|tokens · duration| DDB
  CL -.->|billing API| WRK
  SA --> OBS --> API
  API -->|aggregate per tenant/day| DDB
  API -->|MRR vs COGS| MDB[(MongoDB tenants)]
```

---

## 6. L2 Web AppSec scan (Level 2 DFD)

**Wireframe:** `05-l2-web.html` · **FR:** FR-032–035, FR-111

```mermaid
flowchart TB
  U([Manager role user])
  API[Scan Orchestrator]
  Q[SQS]
  W[L2 Worker\nNuclei · Semgrep · ZAP]
  S3[(S3 artifacts)]
  CL([Claude])
  MDB[(MongoDB scans)]
  TI[ThreatIntelManager]

  U -->|POST layer=L2| API
  API -->|15-day limit FR-111| DDB[(rate_limits)]
  API --> Q --> W
  W --> TI
  W --> S3
  W --> CL
  CL --> W
  W --> MDB
```

---

## 7. L9 AI Agent Scan (Phase 2)

**Wireframe:** `20-l9-ai-scan.html` · **FR:** FR-130–135

```mermaid
flowchart TB
  U([Tenant Manager])
  API[Scan Orchestrator]
  Q[SQS]
  AG[L9 Agent Worker\nClaude Opus extended]
  LOG[(MongoDB agent_log)]
  MDB[(MongoDB scans)]
  CL([Claude Opus])

  U -->|POST /scan/l9/execute| API
  API -->|7-day limit FR-115| DDB[(rate_limits)]
  API --> Q --> AG
  AG <-->|multi-step reasoning| CL
  AG -->|activity events| LOG
  AG -->|OWASP findings| MDB
  U -->|GET live log| API --> LOG
```

---

## 8. Cost flow diagram

```mermaid
flowchart LR
  subgraph Inputs
    CL[Claude tokens]
    LM[Lambda duration]
    TI[TI API calls]
  end

  subgraph PerScan["Per scan COGS"]
    TEL[DynamoDB cost_telemetry]
  end

  subgraph Revenue
    VAPT["$15 Web VAPT"]
    PRO["$199 SOC Pro"]
  end

  CL & LM & TI --> TEL
  TEL -->|aggregate| ADMIN[Admin COGS dashboard]
  VAPT & PRO --> MRR[MRR · Stripe]
  ADMIN --> MARGIN[Gross margin 97.6% VAPT]
```

---

## 9. Logical entity relationship (data stores)

```mermaid
erDiagram
  TENANTS ||--o{ SCANS : runs
  TENANTS ||--o{ SUB_USERS : has
  TENANTS ||--o{ INCIDENTS : owns
  TENANTS ||--o{ CREDIT_LEDGER : purchases
  SCANS ||--o| S3_ARTIFACTS : stores
  SCANS }o--|| ENRICHMENT : uses
  INCIDENTS ||--o{ PLAYBOOK_STEPS : executes
  INTERNAL_USERS ||--o{ AUDIT_LOG : writes
  VAULT_ITEMS }o--|| KMS : encrypted_by

  TENANTS {
    uuid tenant_id PK
    string payment_tier
    string workspace_domain
  }
  SCANS {
    uuid scan_id PK
    uuid tenant_id FK
    enum layer
    enum status
  }
  INCIDENTS {
    uuid incident_id PK
    uuid tenant_id FK
    enum execution_status
  }
```

Full schemas: [`02_TECHNICAL_STACK.md`](../02_TECHNICAL_STACK.md) §3.

---

## 10. Event-driven architecture (SQS)

```mermaid
flowchart TB
  API[Lambda API] -->|scan jobs| Q1[SQS scan-queue]
  API -->|TI correlation| Q2[SQS ti-correlation]
  API -->|SOAR async| Q3[SQS soar-queue]

  Q1 --> W1[Scan Workers L1-L9]
  Q2 --> W2[Correlation Engine]
  Q3 --> W3[SOAR Executor]

  Q1 --> DLQ1[DLQ scan-dlq]
  Q2 --> DLQ2[DLQ ti-dlq]

  W1 -->|fail retry 3x| DLQ1
```

---

## Related documents

| Doc | Role |
|---|---|
| [`22_DATA_FLOW_DIAGRAMS.md`](../22_DATA_FLOW_DIAGRAMS.md) | Core DFD L0/L1 |
| [`14_THREAT_MODEL.md`](../14_THREAT_MODEL.md) | STRIDE on flows |
| [`08_TRUST_AND_SECURITY.md`](./08_TRUST_AND_SECURITY.md) | Trust boundaries |
