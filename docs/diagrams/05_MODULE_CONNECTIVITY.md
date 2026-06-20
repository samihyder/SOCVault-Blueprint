# SOCVault — Module Connectivity Mapping
**Version 1.0 | June 2026**

Logical **product module** dependency graph — how epics connect, not AWS service wiring (see [`01_C4_CONTEXT_CONTAINER.md`](./01_C4_CONTEXT_CONTAINER.md)).

**Traceability:** 26 epics · [`16_TRACEABILITY_MATRIX.md`](../16_TRACEABILITY_MATRIX.md)

---

## 1. Module dependency graph (product level)

```mermaid
flowchart TB
  AUTH[Auth & Onboarding\nUS-001–007 · Epic 1]

  AUTH --> TENANT[Tenant Workspace\nFR-005 · tenant_id]
  TENANT --> BILLING[Billing & Tier Gating\nUS-072–076 · Epic 14]
  TENANT --> TEAMS[Tenant Teams\nUS-141–150 · Epic 21]

  TENANT --> ORCH[Scan Orchestrator\nrate limits · consent · enqueue]

  ORCH --> L1[L1 Recon]
  ORCH --> L2[L2 Web AppSec]
  ORCH --> L3[L3 Mobile]
  ORCH --> L4[L4 API Security]
  ORCH --> L5[L5 Compliance]
  ORCH --> L6[L6 Cloud]
  ORCH --> L7[L7 SOC/SIEM]
  ORCH --> L8[L8 Malware D&R]
  ORCH --> L9[L9 AI Agent Scan]

  CLAUDE[Claude Intelligence Layer\nall layers] --> L1 & L2 & L3 & L4 & L5 & L6 & L7 & L8 & L9
  TI[Threat Intel Manager\n32 feeds] --> L1 & L7 & L8 & SOAR

  L1 & L2 & L3 & L4 & L5 & L6 & L7 & L8 & L9 --> DASH[Dashboard & Reports\nUS-066–071]
  DASH --> NOTIF[Notifications\nUS-081–084]

  L7 --> SOAR[SOAR Engine\nUS-061–065 · Epic 13]
  L8 --> SOAR
  SOAR --> INC[Incident Management]

  BILLING --> GATES[Feature Gate Service]
  GATES --> ORCH & SOAR & CHAT

  CHAT[AI Chat Assistant\nUS-121–129 · Epic 12]
  CHAT -->|dispatch actions| ORCH

  subgraph SuperAdmin["Super Admin — Epic 19–25"]
    EXPL[API Explorer]
    VAULT[Pass & Keys Vault]
    TIREG[Threat Intel Registry]
    TRACK[Development Tracker]
    OBS[Metrics Observatory]
  end

  TIREG --> TI
  VAULT --> EXPL & TI
  OBS --> ORCH & CLAUDE
  EXPL --> AUTH

  TEAMS --> AUTH
  MSP[MSP Portal\nUS-077–080 · Epic 15] --> TENANT & BILLING
```

---

## 2. Module interaction legend

| Edge type | Meaning | Example |
|---|---|---|
| Solid arrow | Direct dependency / calls | Orchestrator → L1 Worker |
| Dashed (conceptual) | Shared service used by many | Claude → all scan layers |
| Bidirectional | Data read/write | Dashboard ↔ MongoDB scans |

---

## 3. Module catalogue

| Module | Epic / US range | Primary stores | External deps |
|---|---|---|---|
| Auth & Onboarding | US-001–007 | Cognito, MongoDB `tenants` | SNS |
| Tenant Workspace | FR-005 | MongoDB `tenants` | — |
| Scan Orchestrator | US-008+ | SQS, DynamoDB limits | — |
| L1–L9 Workers | Per layer | S3, MongoDB `scans` | Scanner tools |
| Claude Intelligence | FR-040–047 | DynamoDB COGS | Anthropic API |
| Threat Intel Manager | US-201–208 | DynamoDB `ti_cache` | 32 feeds (doc 20) |
| Dashboard & Reports | US-066–071 | MongoDB `scans` | Claude (cached) |
| Billing & Tier Gating | US-072–076 | MongoDB, Stripe | Stripe webhooks |
| SOAR Engine | US-061–065 | MongoDB `incidents` | Wazuh, Claude |
| AI Chat Assistant | US-121–129 | MongoDB credits | Claude tools API |
| Tenant Teams | US-141–150 | MongoDB `sub_users` | Cognito |
| Notifications | US-081–084 | MongoDB, SNS | SNS/email |
| API Explorer | US-183–193 | DynamoDB vault | Proxy to staging API |
| Pass & Keys Vault | US-183+ | DynamoDB + KMS | KMS |
| Threat Intel Registry | US-201–208 | MongoDB/DynamoDB config | — |
| Metrics Observatory | US-170–182 | DynamoDB COGS | CloudWatch |
| Development Tracker | US-194–200 | MongoDB / markdown sync | Git export |
| MSP Portal | US-077–080 | MongoDB multi-tenant | Channel billing |

---

## 4. Sync vs async connectivity

```mermaid
flowchart LR
  subgraph Sync["Synchronous — API request/response"]
    A1[Auth me]
    A2[Dashboard summary]
    A3[Billing checkout create]
    A4[Admin explorer catalog]
  end

  subgraph Async["Asynchronous — SQS workers"]
    B1[Scan execute]
    B2[TI correlation]
    B3[SOAR playbook run]
    B4[L9 agent steps]
  end

  subgraph Webhook["Inbound webhooks"]
    C1[Stripe events]
    C2[Wazuh alerts]
    C3[Claude batch — future]
  end
```

---

## 5. Infrastructure connectivity (deployable modules)

Maps product modules to AWS containers — complements C4 Container diagram.

```mermaid
flowchart TB
  AMP[Amplify — all UI modules] --> GW[API Gateway]
  GW --> LAPI[Lambda API module\nAuth · Billing · Dashboard · Admin routes]
  GW --> LADM[Lambda Admin handlers\nExplorer · Vault · TI config]

  LAPI --> SQS
  SQS --> LSCAN[Lambda Scan Workers\nL1–L9 modules]
  SQS --> LTI[Lambda TI Correlation]
  SQS --> LSOAR[Lambda SOAR]

  LAPI & LSCAN & LSOAR --> MDB[(MongoDB Atlas)]
  LAPI & LSCAN --> DDB[(DynamoDB)]
  LSCAN --> S3[(S3)]
  LSCAN & LSOAR --> CL[Claude]
  LSCAN & LTI & LSOAR --> TI[External TI]

  LAPI --> CGN[Cognito]
  LADM --> KMS[KMS Vault]
```

---

## 6. Phase connectivity (when modules land)

| Phase | Modules activated | New edges |
|---|---|---|
| Phase 0 | CI/CD, Terraform, health | Engineer → staging |
| Phase 1 | Auth, L1, Claude, Dashboard, Admin telemetry | Tenant → Orchestrator → L1 → Dashboard |
| Phase 2 | Billing, L2–L8, SOAR, Domain verify, Teams | Billing → GATES → Orchestrator |
| Phase 2.8–2.11 | Observatory, API Explorer, TI Registry | Admin → TI → Scan workers |
| Phase 3 | AI Chat, MSP, L9 production | Chat → Orchestrator |
| Phase 4 | SSO, Enterprise RBAC | IdP → Auth → Teams matrix |
| Phase 5 | EKS workers, multi-region | Orchestrator → EKS jobs |

---

## 7. Critical path for MVP build

```mermaid
flowchart LR
  P0[Phase 0 Terraform] --> AUTH[Auth module]
  AUTH --> ORCH[Scan Orchestrator]
  ORCH --> L1[L1 Worker]
  L1 --> CL[Claude module]
  CL --> DASH[Dashboard]
  DASH --> QA[Automated QA green]
```

**Build order:** [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md)

---

## Related documents

| Doc | Role |
|---|---|
| [`06_SCAN_LAYERS.md`](./06_SCAN_LAYERS.md) | Per-layer detail |
| [`02_SYSTEM_FLOWS.md`](./02_SYSTEM_FLOWS.md) | Runtime sequences |
| [`05_PRODUCT_ROADMAP.md`](../05_PRODUCT_ROADMAP.md) | Phase gates |
