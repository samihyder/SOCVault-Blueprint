# SOCVault — System Flow Diagrams
**Version 1.0 | June 2026**

Sequence and swimlane diagrams for **key product journeys**. Complements DFDs in [`22_DATA_FLOW_DIAGRAMS.md`](../22_DATA_FLOW_DIAGRAMS.md) and [`03_DATA_FLOW_EXTENDED.md`](./03_DATA_FLOW_EXTENDED.md).

**Spec:** [`21_MVP_FUNCTIONAL_SPEC.md`](../21_MVP_FUNCTIONAL_SPEC.md)

---

## 1. Onboarding — signup to first scan (MVP)

**Wireframe:** `01-onboarding.html` · **US:** US-001–007 · **FR:** FR-001–006, FR-026

```mermaid
sequenceDiagram
  autonumber
  actor User as Tenant User
  participant App as React App
  participant GW as API Gateway
  participant API as Lambda API
  participant CGN as Cognito
  participant SNS as AWS SNS
  participant MDB as MongoDB

  User->>App: Enter email + phone
  App->>GW: POST /auth/signup
  GW->>API: Forward
  API->>CGN: Create user
  API->>MDB: Insert tenant record (tenant_id)
  API->>SNS: Send OTP
  SNS-->>User: SMS/email OTP
  API-->>App: 200 OTP sent

  User->>App: Enter OTP
  App->>GW: POST /auth/verify-otp
  GW->>API: Forward
  API->>CGN: Verify OTP
  CGN-->>API: JWT tokens
  API-->>App: access + refresh tokens

  User->>App: Start first L1 scan
  App->>GW: POST /scan/execute (JWT)
  Note over API: Freemium check FR-026<br/>1 scan/month
  API-->>App: 202 scan_id (async)
```

---

## 2. L1 scan — execute to dashboard (MVP core)

**Wireframes:** `03-l1-recon.html`, `04-l1-report.html` · **US:** US-008–020

```mermaid
sequenceDiagram
  autonumber
  actor User as Tenant User
  participant App as Dashboard
  participant API as Lambda API
  participant Q as SQS
  participant W as L1 Worker
  participant TI as ThreatIntelManager
  participant CL as Claude
  participant MDB as MongoDB
  participant S3 as S3

  User->>App: POST scan (target, consent)
  App->>API: POST /scan/execute
  API->>API: Rate limit + domain check (FR-029)
  alt Freemium exhausted
    API-->>App: 429 rate limited
  else OK
    API->>Q: Enqueue scan_id
    API-->>App: 202 { scan_id }

    Q->>W: Trigger worker
    W->>W: 15-step recon pipeline
    W->>TI: enrich_ip / lookup_cve
    TI-->>W: EnrichmentRecord
    W->>S3: Raw tool output
    W->>CL: Structured findings JSON
    CL-->>W: health_score, exposure, narratives
    W->>MDB: scans.status = COMPLETE

    loop Poll until complete
      App->>API: GET /scan/{scan_id}
      API->>MDB: Read scan
      API-->>App: RUNNING | COMPLETE
    end

    App->>API: GET /dashboard/summary
    API-->>App: Health score + top risks
  end
```

---

## 3. Domain verification gate (Phase 2)

**FR:** FR-010–014 · Blocks paid/active scans until verified.

```mermaid
sequenceDiagram
  actor User as Tenant Owner
  participant App as Settings
  participant API as Lambda API
  participant MDB as MongoDB

  User->>App: Request domain verify
  App->>API: POST /auth/domain/verify
  API-->>App: DNS TXT or meta tag instructions

  User->>User: Add DNS/meta record
  loop Poll
    App->>API: GET /auth/domain/status
    API->>MDB: Check verification flag
    API-->>App: pending | verified
  end

  Note over App,API: Pre-verify: L1 passive recon only (FR-015)<br/>Post-verify: paid layers unlocked
```

---

## 4. Upgrade path — freemium to paid (Phase 2)

**Wireframe:** `14-billing.html` · **FR:** FR-101, FR-072–076

```mermaid
sequenceDiagram
  actor User as Tenant Owner
  participant App as Billing UI
  participant API as Lambda API
  participant ST as Stripe
  participant MDB as MongoDB

  User->>App: Hit freemium limit / upgrade CTA
  App->>API: POST /billing/checkout
  API->>ST: Create checkout session
  ST-->>App: Redirect to Stripe

  User->>ST: Complete payment
  ST->>API: Webhook checkout.session.completed
  API->>MDB: Update payment_tier, licensed_targets
  API->>MDB: Audit log entry

  ST-->>User: Redirect to app
  App->>API: GET /auth/me
  API-->>App: tier = STARTER | PRO
  Note over App: Feature gates re-evaluated (FR-101)
```

---

## 5. SOAR alert pipeline (Phase 2 beta)

**Wireframe:** `13-soar.html` · **FR:** FR-060–069 · **DFD:** doc 22 §6

```mermaid
sequenceDiagram
  participant WZ as Wazuh Agent
  participant WM as Wazuh Manager
  participant API as SOAR Ingest API
  participant TI as ThreatIntelManager
  participant CL as Claude Triage
  participant AR as Active Response
  participant Q as Approval Queue
  actor Analyst as Tenant Manager
  participant MDB as MongoDB

  WZ->>WM: Alert severity 10+
  WM->>API: POST /incidents/ingest
  API->>TI: Enrich source IP
  TI-->>API: OTX / AbuseIPDB context
  API->>CL: Enriched alert JSON
  CL-->>API: CONTAIN | ESCALATE | DISMISS

  alt Auto-contain playbook
    API->>AR: Execute Wazuh command
    AR->>WZ: Block IP / isolate
  else Human approval required
    API->>Q: AWAITING_APPROVAL
    Analyst->>API: POST /incidents/{id}/approve
    API->>AR: Execute playbook
  end

  API->>MDB: Persist incident + steps
```

---

## 6. AI Chat — credit purchase to scan action (Phase 3)

**Wireframe:** `12-ai-chat.html` · **FR:** FR-121–129

```mermaid
sequenceDiagram
  actor User as Tenant User
  participant Chat as AI Chat UI
  participant API as Lambda API
  participant CL as Claude
  participant ST as Stripe
  participant Scan as Scan Orchestrator

  User->>Chat: Natural language request
  Chat->>API: POST /ai/chat
  API->>API: Check credit balance

  alt Insufficient credits
    API-->>Chat: 402 + purchase CTA
    User->>Chat: Buy credits
    Chat->>API: POST /credits/purchase
    API->>ST: Checkout session
  end

  API->>CL: Message + tool definitions
  CL-->>API: Action intent (e.g. run L1 scan)
  API->>Scan: POST /scan/execute (delegated)
  Scan-->>API: scan_id
  API-->>Chat: Stream response + action result
```

---

## 7. Super Admin — API Explorer test call (Milestone 2.9)

**Wireframe:** `24-admin-api-explorer.html` · **FR:** FR-183–193

```mermaid
sequenceDiagram
  actor Admin as Super Admin
  participant UI as API Explorer
  participant API as Admin API
  participant Vault as Pass & Keys
  participant KMS as AWS KMS
  participant Ext as External API / Staging API
  participant AUD as audit_log

  Admin->>UI: Select endpoint + Send
  UI->>API: POST /admin/explorer/test
  API->>Vault: Resolve {{variables}}
  Vault->>KMS: Decrypt secret
  KMS-->>Vault: Plaintext (ephemeral)
  API->>Ext: Proxied HTTP request
  Ext-->>API: Response
  API->>Vault: Auto-save tokens (if configured)
  API->>AUD: Log actor, endpoint, timestamp
  API-->>UI: Response body + status
```

---

## 8. Production cutover (ADR-006)

**Doc:** [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md) §7

```mermaid
sequenceDiagram
  actor Eng as Engineer
  participant CI as GitHub Actions
  participant TF as Terraform
  participant Stg as Staging
  participant Prod as Production
  participant QA as run-staging-qa.sh
  actor Lead as Release approver

  Eng->>CI: Merge release branch
  CI->>QA: Staging QA green
  Lead->>Eng: Sign cutover checklist
  Eng->>TF: terraform apply (prod)
  TF->>Prod: Provision prod pools, DB, API GW
  Eng->>Prod: DNS api.socvault.io + app.socvault.io
  CI->>Prod: Deploy Lambda + Amplify
  Eng->>Prod: Post-cutover smoke QA
  Prod-->>Eng: Health 200, Bruno green
```

---

## 9. Tenant sub-user invite (Phase 2)

**Wireframe:** `21-tenant-teams.html` · **FR:** FR-140–144

```mermaid
sequenceDiagram
  actor Owner as Tenant Owner
  participant App as Teams UI
  participant API as Lambda API
  participant CGN as Cognito
  participant MDB as MongoDB
  actor Sub as Invited Sub-user

  Owner->>App: Invite Manager slot
  App->>API: POST /team/invite
  API->>API: Max 3 slots check (FR-140)
  API->>CGN: Create/link user
  API->>MDB: sub_users role=MANAGER
  API-->>Sub: Invitation email

  Sub->>App: Accept + OTP verify
  App->>API: POST /auth/verify-otp
  Note over API: JWT includes tenant_id + role claim
  Sub->>App: Trigger L2 scan
  API->>API: RBAC: MANAGER allowed (FR-143)
```

---

## 10. Swimlane — end-to-end tenant lifecycle

```mermaid
flowchart TB
  subgraph Onboard["Onboarding"]
    A1[Signup + OTP]
    A2[First freemium L1]
  end

  subgraph Verify["Verification"]
    B1[Domain verify]
    B2[Paid tier unlock]
  end

  subgraph Operate["Operations"]
    C1[Multi-layer scans]
    C2[SOAR + Wazuh]
    C3[Compliance reports]
  end

  subgraph Scale["Scale"]
    D1[Sub-users]
    D2[AI Chat credits]
    D3[MSP channel]
  end

  A1 --> A2 --> B1 --> B2 --> C1
  C1 --> C2 & C3
  C2 --> D1 --> D2 --> D3
```

---

## Related documents

| Doc | Role |
|---|---|
| [`04_RBAC_MAPPING.md`](./04_RBAC_MAPPING.md) | Who can run each step |
| [`10_STATE_MACHINES.md`](./10_STATE_MACHINES.md) | Scan/incident/subscription states |
| [`05_MODULE_CONNECTIVITY.md`](./05_MODULE_CONNECTIVITY.md) | Module dependencies |
