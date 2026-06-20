# SOCVault — MVP Functional Specification
**Version 1.0 | June 2026**

---

## 1. Purpose & scope

This document is the **implementation-facing functional spec** for the first shippable product slice. It consolidates *what the system must do* for engineers building on AWS staging/production — without duplicating content that lives elsewhere.

| In scope (this doc) | Authoritative elsewhere (do not duplicate) |
|---|---|
| MVP feature behaviour, inputs/outputs, errors, tier gates | Full FR list → [`03_REQUIREMENTS.md`](./03_REQUIREMENTS.md) |
| Module responsibilities & acceptance checks | User stories → [`SOCVault-User-Stories.xlsx`](../userstories-wireframes/SOCVault-User-Stories.xlsx) |
| REST contracts | [`api/openapi.yaml`](../api/openapi.yaml) · [`06_API_SPECIFICATION.md`](./06_API_SPECIFICATION.md) |
| UI layout | Wireframes → [`userstories-wireframes/`](../userstories-wireframes/) |
| Threat intel feed catalogue (32 providers) | [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) |
| Infra & deploy | [`19_CI_CD_AND_ENVIRONMENTS.md`](./19_CI_CD_AND_ENVIRONMENTS.md) · [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) · [`AWS_SETUP_README.md`](./AWS_SETUP_README.md) |
| Build nano steps | [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) |

### Scope boundaries

| Phase / milestone | Included in MVP functional spec |
|---|---|
| **Phase 0** — AWS account, CI/CD, staging active / production dormant | Yes (§2) |
| **Phase 1** — Auth, L1, Claude, dashboard, admin telemetry | Yes (§3–§7) |
| **Milestone 2.9** — API Explorer & Pass & Keys | Yes (§8) |
| **Milestone 2.11** — Threat Intel Feed Registry | Yes (§9) |
| Phase 2 beta (Stripe, SOAR live, L2–L8 production) | Referenced only |
| L9, AI Chat, tenant teams, Metrics Observatory UI | Out of scope for **Phase 1 MVP** (see note below) |

> **Phase 2 vs this spec:** L9, tenant teams, and Metrics Observatory are **Phase 2 beta deliverables** (roadmap Milestones 2.6–2.8). They appear in [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) completion criteria but are intentionally excluded from this Phase 1 functional spec.

**MVP definition of done:** checklist in [`03_REQUIREMENTS.md`](./03_REQUIREMENTS.md) §4.

---

## 2. Platform foundation (Phase 0)

### 2.1 Functional summary

| ID | Function | Trigger | Success outcome |
|---|---|---|---|
| F-PLAT-01 | Environment bootstrap | Terraform staging apply | Staging API returns `200` on `GET /health` |
| F-PLAT-02 | CI deploy to staging | Push to `main` | QA suite green; Lambda/API GW updated |
| F-PLAT-03 | Promote to production | Cutover checklist + approval | Production API healthy (post-activation) |
| F-PLAT-04 | Secret management | Deploy or admin vault update | No secrets in git; SSM/KMS only |

### 2.2 Rules

1. **No local runtime** — all API and worker code runs on AWS staging (ADR-004, ADR-006).
2. **MVP = staging only** — production dormant until cutover checklist ([`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) §7).
3. **Serverless MVP** — API Gateway + Lambda + Amplify + SQS; Terraform IaC; GitHub Actions deploy.
4. **One user story at a time** — API route → QA green → wireframe → Super Admin link.
5. Bruno and automated QA target `api-staging.socvault.io` only.

### 2.3 Traceability

| Nano steps | Doc |
|---|---|
| 0.1.1–0.2.9 | [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) Phase 0 |
| INF/DEV checklist | [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) |

---

## 3. Authentication & onboarding (Phase 1.1)

**Wireframe:** `01-onboarding.html` · **Stories:** US-001–007 · **FRs:** FR-001–006

### 3.1 Signup (`POST /auth/signup`)

| Field | Type | Validation | Error |
|---|---|---|---|
| `email` | string | Business email; blocklist freemail (FR-002) | `400` invalid domain |
| `phone` | E.164 string | Valid mobile format | `400` invalid phone |

**Process:**

1. Extract domain from email → provisional `workspace_domain`.
2. Create Cognito user + MongoDB `tenants` record with new `tenant_id` (UUID).
3. Send 6-digit OTP via SNS (email-first if SMS quota constrained).
4. Return `{ message: "OTP sent" }` — no tokens yet.

**Business rules:**

- Signup completes in **≤60 seconds** to OTP screen (MVP acceptance).
- No credit card at signup.

### 3.2 Verify OTP (`POST /auth/verify-otp`)

| Input | Output |
|---|---|
| `email`, `otp` | `access_token` (15 min), `refresh_token` (30 days), `tenant_id` |

**Errors:** `401` invalid/expired OTP.

### 3.3 Session (`POST /auth/refresh`, `GET /auth/me`)

- All protected routes require `Authorization: Bearer {access_token}`.
- Missing/invalid token → `401` (MVP acceptance).
- `GET /auth/me` returns tenant profile, tier, domain.

### 3.4 Domain verification (Phase 2 gate — spec'd for MVP UI)

Pre-verification: **L1 passive recon only** (FR-015). Paid/active scans blocked until DNS TXT or meta tag verified (FR-010–014). Onboarding wireframe shows verify step; implementation may ship in Phase 1.2.

---

## 4. L1 recon scan engine (Phase 1.2–1.3)

**Wireframes:** `03-l1-recon.html`, `04-l1-report.html` · **Stories:** US-008–020 · **FRs:** FR-019, FR-026–031, FR-028–030

### 4.1 Execute scan (`POST /scan/execute`)

| Input | Rule |
|---|---|
| `layer` | MVP: `"L1"` only |
| `target` | Must match tenant's registered domain (subdomain allowed) |
| Consent | `scan_authorised: true` required (FR-028) |

**Preconditions:**

- Freemium: **1 scan per calendar month** per tenant (FR-026) — else `429`.
- Tenant has valid JWT.

**Process (async — ADR-006):**

1. API Gateway → Lambda validates request.
2. Lambda publishes message to **SQS** (`scan-jobs-staging`); returns **HTTP 202** `{ scan_id, status: "queued" }` immediately (API GW 29s limit — scan runs off-thread).
3. **Lambda worker** consumes SQS → invokes **L1 Lambda** (15 steps).
4. External enrichment via `ThreatIntelManager` when Milestone 2.11 live; MVP may stub.
5. Persist `scans` document in MongoDB (`tenant_id` partition key).
6. Status: `queued` → `running` → `completed` | `failed`.

### 4.2 Poll status (`GET /scan/{scan_id}`)

- Client polls every 3–5 s.
- Status change reflected within **5 seconds** (FR-031).
- Response includes `steps[]` with per-step timing (wireframe progress UI).

### 4.3 Isolation & security

- Each scan runs in **isolated worker context** — no shared memory between tenants (FR-030).
- Scan artifacts in S3: `s3://{bucket}/{tenant_id}/{scan_id}/`.
- Target must not be third-party domain outside tenant scope (FR-029 at Phase 2 enforcement).

### 4.4 Rate limit errors

| Condition | HTTP | Code |
|---|---|---|
| Freemium monthly limit reached | 429 | `FREEMIUM_LIMIT_EXCEEDED` |
| Unverified domain (Phase 2+) | 403 | `DOMAIN_NOT_VERIFIED` |
| Invalid target | 400 | `INVALID_SCAN_TARGET` |

---

## 5. AI intelligence layer (Phase 1.4)

**Wireframe:** `04-l1-report.html` · **Stories:** US-018–020, US-055–060 · **FRs:** FR-040–047, FR-048 (gate)

### 5.1 Trigger

On L1 scan `completed`, worker invokes Claude (`claude-sonnet-4-6`) with structured scan JSON.

### 5.2 Required outputs (stored on scan record)

| Output field | Description | Freemium | Paid |
|---|---|---|---|
| `health_score` | 0–100 | Visible | Visible |
| `financial_exposure_usd` | Aggregated $ risk | Visible | Visible |
| `findings[]` | Plain-English summaries per issue | Visible | Visible |
| `remediation_scripts[]` | Copy-paste fixes | **Hidden** (FR-048) | Visible |
| `confidence_score` | Per finding (Phase 2) | — | Optional |

### 5.3 Failure behaviour

- Claude API unavailable → generate **offline fallback report** (FR-047) from rule templates; mark `ai_status: degraded`.
- Retry: exponential backoff, max 5 attempts.
- Write token usage to DynamoDB `cost_telemetry` (FR-105).

### 5.4 Cost

- Log input/output tokens per scan for admin COGS (see §7).
- Prompt caching enabled when available (FR-046).

---

## 6. Dashboard (Phase 1.5)

**Wireframe:** `02-dashboard.html` · **Stories:** US-066–071 · **FRs:** FR-090–092

### 6.1 Summary (`GET /dashboard/summary`)

Returns for current tenant (from JWT):

```json
{
  "health_score": 62,
  "financial_exposure_usd": 12400,
  "top_findings": [{ "title": "...", "impact_usd": 3200, "severity": "high" }],
  "last_scan_at": "2026-06-18T10:00:00Z",
  "scan_quota": { "used": 1, "limit": 1, "resets_at": "2026-07-01T00:00:00Z" }
}
```

### 6.2 UI rules

- Dashboard loads in **<2 s** on staging (performance target in tech stack).
- Health score dial + financial exposure prominent (conversion driver).
- Freemium CTA to upgrade when remediation scripts exist but are gated.

---

## 7. Admin telemetry (Phase 1.6)

**Wireframe:** `19-admin.html` · **FRs:** FR-098, FR-105 · **API:** `GET /admin/telemetry`

### 7.1 Function

Internal/admin role returns aggregated unit economics:

| Metric | Source |
|---|---|
| COGS per scan (last 24h / 7d) | DynamoDB `cost_telemetry` |
| Total AI spend | Anthropic token sums |
| Gross margin estimate | Revenue stub (0 at MVP) vs COGS |
| Scans by layer | MongoDB aggregation |

### 7.2 Access control

- Requires admin/internal JWT role (Phase 2 RBAC); MVP may use Cognito group `admin`.

---

## 8. API Explorer & Pass & Keys (Milestone 2.9)

**Wireframe:** `24-admin-api-explorer.html` · **Stories:** US-186–193 · **FRs:** FR-194–207 · **Guide:** [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md)

### 8.1 Functional modules

| Module | Behaviour | API |
|---|---|---|
| **Catalogue** | Sync from OpenAPI; group by tags | `GET /admin/explorer/catalog` |
| **Test runner** | Server-side proxy; resolve `{{vault}}` vars; try/catch envelope | `POST /admin/explorer/test` |
| **Vault CRUD** | Encrypted at rest (KMS); masked list | `GET/POST/DELETE /admin/vault/variables` |
| **Step-up reveal** | PIN/password → 5 min session | `POST /admin/vault/unlock`, `/reveal/{key}` |
| **Auto-save** | Map `access_token`, `tenant_id`, `scan_id` from test responses | FR-200 |

### 8.2 Security rules

- Secrets **never** logged in plaintext (FR-204 audit logs key names only).
- Proxy allowlist: internal API base URLs only (threat model T-12).
- Roles: Manager, DevOps, SysOps, VA/PT for explorer; Manager, DevOps for vault write (FR-205).

### 8.3 Done when

- [ ] Auth → scan flow runnable entirely from admin UI on staging
- [ ] Bruno `01-auth` passes using vault-stored variables
- [ ] Build order steps 1–5 in implementation guide complete

---

## 9. Threat Intel Feed Registry (Milestone 2.11)

**Wireframe:** Threat Intel tab on `24-admin-api-explorer.html` · **Stories:** US-201–208 · **FRs:** FR-216–229 · **Catalogue:** [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md)

### 9.1 Admin functions

| Function | Description | API |
|---|---|---|
| List feeds | Filter by layer, environment; show quota status | `GET /admin/ti/feeds` |
| Configure | Enable/disable, link vault key, set daily limit | `PATCH /admin/ti/feeds/{id}` |
| Test | Live connectivity + sample IOC | `POST /admin/ti/feeds/{id}/test` |
| Usage | 24h calls vs free tier | `GET /admin/ti/feeds/{id}/usage` |
| Priority | Fallback order when quota exceeded | `PUT /admin/ti/feeds/priority` |

**Rule:** Provider list is **seeded from doc 20 §5 JSON** at deploy — not hardcoded in React.

### 9.2 Runtime: ThreatIntelManager

Scanners call by **intent**, not provider URL:

| Intent | Called from | MVP providers |
|---|---|---|
| `enrich_ip` | L1 step 11, L7 alerts | AbuseIPDB, Spamhaus (local list) |
| `lookup_domain` | L1 breach check | HIBP |
| `lookup_cve` | L2 findings (Phase 2) | NVD, OSV.dev |
| `lookup_hash` | L8 malware (Phase 2) | MalwareBazaar, VirusTotal |
| `lookup_url` | L1/L2 URL checks | URLhaus |

**Caching:** DynamoDB `ti_cache` with TTL. **On feed failure:** scan continues; finding tagged `enrichment_status: partial`.

### 9.3 Correlation (FR-225–227)

After enrichment, `CorrelationEngine` clusters IOCs within 72h. Report payload includes:

```json
{
  "enrichment_summary": { "critical_iocs": [], "patterns_detected": [] }
}
```

Passed to Claude for financial narrative. Cross-tenant early warning (FR-228) is post-MVP.

### 9.4 Done when

- [ ] L1 scan enriches IP via AbuseIPDB when feed enabled on staging
- [ ] Super Admin can test/disable feeds without redeploy
- [ ] At least one correlated pattern appears when HIBP + mock L7 alert share tenant context

---

## 10. Cross-cutting non-functional (MVP)

| NFR | Requirement | Verification |
|---|---|---|
| Auth | JWT on all protected routes | Bruno negative test |
| CORS | Allowlist staging/prod app origins only | Browser preflight test |
| Tenant isolation | `tenant_id` on every query | Integration test cross-tenant read |
| Secrets | SSM Parameter Store; KMS for vault | Code scan + tracker INF row |
| CI/CD | Staging auto; prod manual | GitHub Actions log |
| Observability | CloudWatch logs + scan COGS writes | Admin telemetry spot check |

Full NFR list: [`03_REQUIREMENTS.md`](./03_REQUIREMENTS.md) §2.

---

## 11. API surface (MVP)

| Method | Path | Phase | Spec |
|---|---|---|---|
| GET | `/health` | 0 | openapi |
| POST | `/auth/signup` | 1 | openapi |
| POST | `/auth/verify-otp` | 1 | openapi |
| POST | `/auth/refresh` | 1 | openapi |
| GET | `/auth/me` | 1 | openapi |
| POST | `/scan/execute` | 1 | openapi |
| GET | `/scan/{scan_id}` | 1 | openapi |
| GET | `/scan/history` | 1 | openapi |
| GET | `/dashboard/summary` | 1 | openapi |
| GET | `/admin/telemetry` | 1 | openapi |
| GET/POST | `/admin/explorer/*`, `/admin/vault/*` | 2.9 | openapi |
| GET/PATCH/POST | `/admin/ti/feeds/*` | 2.11 | openapi |

---

## 12. Traceability index (MVP features)

| Feature | FRs | US (sample) | Wireframe | Roadmap |
|---|---|---|---|---|
| Signup/OTP | FR-001–006 | US-001–005 | 01 | 1.1 |
| L1 scan | FR-019, FR-026–031 | US-008–017 | 03, 04 | 1.2–1.3 |
| AI report | FR-040–047 | US-018–020 | 04 | 1.4 |
| Dashboard | FR-090–092 | US-066–068 | 02 | 1.5 |
| Admin COGS | FR-098, FR-105 | US-092+ | 19 | 1.6 |
| API Explorer | FR-194–207 | US-186–193 | 24 | 2.9 |
| TI feeds | FR-216–227 | US-201–208 | 24 (tab) | 2.11 |

Full matrix: [`16_TRACEABILITY_MATRIX.md`](./16_TRACEABILITY_MATRIX.md).

---

## 13. Related documents

| Doc | Use when |
|---|---|
| [`22_DATA_FLOW_DIAGRAMS.md`](./22_DATA_FLOW_DIAGRAMS.md) | Visual data flow for scan, TI, SOAR |
| [`13_TEST_STRATEGY.md`](./13_TEST_STRATEGY.md) | Test cases derived from this spec |
| [`14_THREAT_MODEL.md`](./14_THREAT_MODEL.md) | Security review |

---

*This spec is maintained alongside the blueprint. When FRs or openapi change, update §11–§12 references — do not copy provider tables or full FR text into this file.*
