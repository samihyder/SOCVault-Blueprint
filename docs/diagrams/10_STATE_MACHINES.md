# SOCVault — State Machines
**Version 1.0 | June 2026**

Lifecycle states for scans, incidents, subscriptions, and tenant onboarding.

---

## 1. Scan lifecycle

**Store:** MongoDB `scans.status` · **FR:** FR-019, FR-031

```mermaid
stateDiagram-v2
  [*] --> QUEUED: POST /scan/execute
  QUEUED --> RUNNING: Worker picks up
  RUNNING --> COMPLETE: Pipeline + Claude OK
  RUNNING --> FAILED: Tool error / timeout
  RUNNING --> PARTIAL: TI partial enrichment
  PARTIAL --> COMPLETE: Claude with partial flag
  FAILED --> [*]
  COMPLETE --> [*]

  note right of RUNNING
    Client polls GET /scan/id
    202 until terminal state
  end note
```

| State | Client UX | Server behaviour |
|---|---|---|
| QUEUED | Spinner | SQS message pending |
| RUNNING | Progress % optional | Worker executing steps |
| COMPLETE | Report available | Immutable record |
| FAILED | Error message | Retry manual only |
| PARTIAL | Report + warning badge | `enrichment_status: partial` |

---

## 2. L9 AI Agent scan lifecycle

**FR:** FR-130–135 · **Wireframe:** `20-l9-ai-scan.html`

```mermaid
stateDiagram-v2
  [*] --> INIT: POST /scan/l9/execute
  INIT --> PLANNING: Agent plans steps
  PLANNING --> EXECUTING: Step loop
  EXECUTING --> EXECUTING: Next step
  EXECUTING --> STOPPED: User POST stop
  EXECUTING --> COMPLETE: All steps done
  EXECUTING --> FAILED: Error / cap exceeded
  STOPPED --> [*]
  COMPLETE --> [*]
  FAILED --> [*]
```

Live log: `GET /scan/l9/{scan_id}/log` streams step events from MongoDB `agent_log`.

---

## 3. SOAR incident lifecycle

**Store:** MongoDB `incidents.execution_status` · **FR:** FR-060–069

```mermaid
stateDiagram-v2
  [*] --> QUEUED: Wazuh webhook ingest
  QUEUED --> TRIAGING: TI + Claude analysis
  TRIAGING --> AWAITING_APPROVAL: Human required
  TRIAGING --> EXECUTING: Auto-contain playbook
  AWAITING_APPROVAL --> EXECUTING: Manager approves
  AWAITING_APPROVAL --> DISMISSED: Reject / false positive
  EXECUTING --> COMPLETED: Playbook success
  EXECUTING --> FAILED: Playbook error
  DISMISSED --> [*]
  COMPLETED --> [*]
  FAILED --> [*]
```

---

## 4. Malware incident lifecycle (L8)

**FR:** FR-046–054

```mermaid
stateDiagram-v2
  [*] --> DETECTED: ClamAV/FIM alert
  DETECTED --> ANALYSING: Claude family ID
  ANALYSING --> AUTO_REMEDIATED: Low risk + policy allow
  ANALYSING --> PENDING_APPROVAL: High risk
  PENDING_APPROVAL --> REMEDIATED: Approve
  PENDING_APPROVAL --> DISMISSED: Reject FP
  AUTO_REMEDIATED --> [*]
  REMEDIATED --> [*]
  DISMISSED --> [*]
```

---

## 5. Subscription / payment tier lifecycle

**Store:** MongoDB `tenants.payment_tier` · **FR:** FR-101

```mermaid
stateDiagram-v2
  [*] --> FREEMIUM: Signup complete
  FREEMIUM --> STARTER: Stripe checkout
  FREEMIUM --> STARTER: MSP provisioned
  STARTER --> PRO: Upgrade checkout
  PRO --> ENTERPRISE: Sales contract
  STARTER --> FREEMIUM: Subscription cancelled
  PRO --> STARTER: Downgrade
  PRO --> FREEMIUM: Cancelled
  ENTERPRISE --> PRO: Contract end
```

| Transition trigger | Side effect |
|---|---|
| → STARTER/PRO | Unlock licensed targets, layer gates |
| → FREEMIUM | Revoke paid scans; retain history read-only |
| Webhook `invoice.payment_failed` | Grace period → downgrade (Phase 2) |

---

## 6. Domain verification lifecycle

**FR:** FR-010–014

```mermaid
stateDiagram-v2
  [*] --> UNVERIFIED: Signup
  UNVERIFIED --> PENDING: DNS/meta challenge issued
  PENDING --> VERIFIED: Record detected
  PENDING --> EXPIRED: Timeout 72h
  EXPIRED --> PENDING: Re-issue challenge
  VERIFIED --> [*]
```

| State | Scan capability |
|---|---|
| UNVERIFIED | L1 passive recon only (FR-015) |
| VERIFIED | Paid/active layers unlocked |

---

## 7. Tenant sub-user lifecycle

**FR:** FR-140–144 · **Store:** MongoDB `sub_users.status`

```mermaid
stateDiagram-v2
  [*] --> PENDING: Owner sends invite
  PENDING --> ACTIVE: OTP accept
  PENDING --> EXPIRED: 7 days no accept
  ACTIVE --> REVOKED: Owner revoke
  REVOKED --> [*]
  EXPIRED --> [*]
```

---

## 8. Production environment lifecycle (platform)

**ADR-006**

```mermaid
stateDiagram-v2
  [*] --> DORMANT: Phase 0
  DORMANT --> PROVISIONED: Terraform prod apply
  PROVISIONED --> CUTOVER_TEST: DNS + smoke QA
  CUTOVER_TEST --> LIVE: Checklist signed
  LIVE --> LIVE: Normal ops
  LIVE --> ROLLBACK: Critical incident
  ROLLBACK --> DORMANT: Traffic to staging
```

---

## 9. CI/CD deployment state (staging)

```mermaid
stateDiagram-v2
  [*] --> IDLE
  IDLE --> BUILDING: Push to main
  BUILDING --> TERRAFORM: Plan/apply
  TERRAFORM --> DEPLOYING: Lambda + Amplify
  DEPLOYING --> QA: run-staging-qa.sh
  QA --> IDLE: Pass
  QA --> FAILED: Fail
  FAILED --> IDLE: Fix + retry
```

---

## Related documents

| Doc | Role |
|---|---|
| [`02_SYSTEM_FLOWS.md`](./02_SYSTEM_FLOWS.md) | Transition triggers in sequences |
| [`21_MVP_FUNCTIONAL_SPEC.md`](../21_MVP_FUNCTIONAL_SPEC.md) | Business rules per state |
| [`03_DATA_FLOW_EXTENDED.md`](./03_DATA_FLOW_EXTENDED.md) | Store updates on transition |
