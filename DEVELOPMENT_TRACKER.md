# SOCVault — Product Development Tracker
**Live stack status · infrastructure · application · action log**

| Field | Value |
|---|---|
| **Last updated** | 2026-07-03 |
| **Current phase** | Phase 0 — AWS account + CI/CD (blueprint complete; not provisioned) |
| **Development model** | **AWS-only** — **staging = MVP**; production dormant; serverless + IaC (ADR-006) |
| **Next recommended action** | `0.1.1` Create AWS account → Terraform staging → `US-001` |
| **Application repo** | [`socvault-io/socvault-app`](https://github.com/socvault-io/socvault-app) |
| **GitHub Project** | [SOCVault App — Build](https://github.com/orgs/socvault-io/projects/1) (issues live in app repo) |
| **AWS region** | `eu-west-2` (single account) |

> **Note:** This file remains for blueprint history. **Live execution tracking** is in [`socvault-app/DEVELOPMENT_TRACKER.md`](https://github.com/socvault-io/socvault-app/blob/main/DEVELOPMENT_TRACKER.md).

> **Rule:** Every completed task, deployment, config change, or doc update **must** add a row to the [Action Log](#action-log). Update [Stack Live Status](#stack-live-status) and the relevant checklist in the same commit/PR.

**Super Admin UI:** When the app is built, the same data is managed in the admin panel at `/admin/development-tracker` (wireframe `25-admin-dev-tracker.html`, FR-208–FR-215). The markdown file remains the git-exportable source; MongoDB is the runtime store.

Related: [`docs/19_CI_CD_AND_ENVIRONMENTS.md`](docs/19_CI_CD_AND_ENVIRONMENTS.md) · [`docs/05_PRODUCT_ROADMAP.md`](docs/05_PRODUCT_ROADMAP.md) · [`docs/AWS_SETUP_README.md`](docs/AWS_SETUP_README.md)

---

## Status legend

| Symbol | Meaning |
|---|---|
| 🟢 | **Live** — running and verified |
| 🟡 | **In progress** — work started, not verified |
| 🔴 | **Not started** — no implementation |
| ⏸ | **Blocked** — waiting on dependency |
| 📋 | **Spec only** — documented in blueprint; no runtime yet |

---

## Stack live status

Snapshot of what is **actually running** right now (not planned).

### Summary dashboard

| Layer | Staging | Production | Notes |
|---|---|---|---|
| **Frontend (Amplify)** | 🔴 | ⏸ dormant | Serverless; CDN paid tier |
| **API (API GW + Lambda)** | 🔴 | ⏸ dormant | Staging only until cutover |
| **MongoDB Atlas M0** | 🔴 | ⏸ dormant | On AWS eu-west-2 |
| **Async (SQS + Lambda)** | 🔴 | ⏸ dormant | Replaces Celery on MVP |
| **L1 scan (Lambda)** | 🔴 | 🔴 | Per account |
| **Cognito** | 🔴 | 🔴 | Separate user pools |
| **S3 / DynamoDB** | 🔴 | 🔴 | Per account |
| **CI/CD (GitHub Actions)** | 🔴 | 🔴 | staging auto; prod approval |
| **Cloudflare DNS** | — | — | Optional; CDN/WAF on **paid tier** (CloudFront + AWS WAF) |
| **Automated QA (staging)** | 📋 | — | `tests/qa/run-staging-qa.sh` |

### Target URLs

| Service | Staging | Production |
|---|---|---|
| Frontend | `https://app-staging.socvault.io` | `https://app.socvault.io` |
| API | `https://api-staging.socvault.io/api/v1` | `https://api.socvault.io/api/v1` |
| Health | `GET /health` | `GET /health` |
| Admin API Explorer | `/admin/api-explorer` | `/admin/api-explorer` |
| Admin Dev Tracker | `/admin/development-tracker` | read-only for most roles |

### Blueprint repo (this repository)

| Artefact | Status | Location |
|---|---|---|
| OpenAPI MVP (10 endpoints + admin explorer stubs) | 🟢 | `api/openapi.yaml` |
| Bruno collection | 🟢 | `collections/bruno/SOCVault-MVP/` |
| Postman collection | 🟢 | `collections/postman/` |
| User stories (208) | 🟢 | `userstories-wireframes/SOCVault-User-Stories.xlsx` |
| Wireframes (25 pages) | 🟢 | `userstories-wireframes/*.html` |
| Dev Tracker admin UI | 📋 | `25-admin-dev-tracker.html` |
| AWS setup guide | 🟢 | `docs/AWS_SETUP_README.md` |
| API Explorer impl guide | 🟢 | `docs/18_API_EXPLORER_IMPLEMENTATION.md` |
| Automated QA scripts | 🟢 | `tests/qa/` |
| Application source code | 🔴 | [`socvault-io/socvault-app`](https://github.com/socvault-io/socvault-app) — repo created; code not started |

---

## Phase & milestone progress

| Phase | Goal | Status | % (estimate) |
|---|---|---|---|
| **0** Foundation | AWS staging + IaC + QA | 🟡 Blueprint done; staging not live | 45% |
| **1** Cloud MVP (staging) | Auth + L1 + AI on staging | 🔴 | 0% |
| **2** Beta & scale | Stripe, SOAR, paid AWS upgrades | 🔴 | 0% |
| **3** Launch | Public launch + SOAR | 🔴 | 0% |
| **4** Growth | Scale + enterprise | 🔴 | 0% |
| **5** Expansion | International + Series A | 🔴 | 0% |

| Milestone | Name | Status |
|---|---|---|
| 0.1 | Development environment ready | 🔴 |
| 0.2 | Brand assets ready | 🟡 (colours documented; domain TBD) |
| 1.1 | Authentication & onboarding | 🔴 |
| 1.2 | Scanning engine | 🔴 |
| 1.3 | Claude AI integration | 🔴 |
| 1.4 | Dashboard | 🔴 |
| 2.1a | AWS Free Tier MVP | 🔴 |
| 2.1b | AWS paid upgrade | 🔴 |
| 2.2 | Cognito auth | 🔴 |
| 2.9 | API Explorer & Pass & Keys | 📋 spec (steps 1–6 documented) |
| 2.10 | Development Tracker UI | 📋 wireframe (`25-admin-dev-tracker.html`) |

---

## Account & shared infra (`INF-001`)

| ID | Action | Roadmap | Status | Notes |
|---|---|---|---|---|
| INF-001 | One AWS Free Tier account + MFA + $15 budget | 0.1.1 | 🔴 | |
| INF-002 | IAM admin + MFA | 0.1.2 | 🔴 | |
| INF-003 | Terraform staging: API GW + Lambda + Amplify | 0.1.4–0.1.8 | 🔴 | ADR-006 |
| INF-004 | CloudWatch + GitHub OIDC (+ ECR for Lambda container images only) | 0.1.5 | 🔴 | Single account role; no ECS on MVP |

## Staging environment (`INF-S-*`) — same account

| ID | Action | Roadmap | Status | Notes |
|---|---|---|---|---|
| INF-S-001 | S3, DynamoDB, SSM `/staging/*`, Cognito staging | 0.1.6 | 🔴 | |
| INF-S-002 | Atlas M0 socvault-staging | 0.1.7 | 🔴 | |
| INF-S-003 | API Gateway + Lambda staging + app-staging DNS | 0.1.7–0.1.8 | 🔴 | |
| INF-S-004 | deploy-staging.yml green | 0.1.9 | 🔴 | |
| INF-S-005 | Lambda L1 staging | 0.2.8 | 🔴 | |
| INF-S-006 | Bruno green on api-staging | 0.2.6 | 🔴 | |

## Production environment (`INF-P-*`) — same account

| ID | Action | Roadmap | Status | Notes |
|---|---|---|---|---|
| INF-P-001 | Production Terraform workspace (dormant) | 0.2.4 | 🔴 | Not applied until cutover |
| INF-P-002 | Atlas production cluster | — | ⏸ | Deferred |
| INF-P-003 | Production API + app DNS | — | ⏸ | Cutover checklist |
| INF-P-004 | deploy-production.yml | — | ⏸ | Post-cutover |
| INF-P-005 | Lambda L1 production | — | ⏸ | Post-cutover |

## CI/CD tracker (`CICD-*`)

| ID | Action | Roadmap | Status | Notes |
|---|---|---|---|---|
| CICD-001 | `socvault-app` repo + branch protection | 0.1.4 | 🔴 | |
| CICD-002 | `ci.yml` lint + unit tests | 0.1.11 | 🔴 | Runs on GitHub runners |
| CICD-003 | `deploy-staging.yml` → Terraform + Lambda/Amplify | 0.1.9 | 🔴 | Trigger: push `main` |
| CICD-006 | `qa-staging.yml` → run-staging-qa.sh | 0.1.9 | 🔴 | Blocks deploy on fail |
| CICD-004 | `deploy-production.yml` + approval | 0.2.4 | 🔴 | Trigger: tag / manual |
| CICD-005 | Post-deploy Bruno smoke (staging) | 0.1.12 | 🔴 | |

## Infrastructure tracker (legacy IDs — superseded)

<details>
<summary>Previous single-account INF-001–024 (reference only)</summary>

| ID | Action | Status |
|---|---|---|
| INF-001–024 | See `AWS_SETUP_README.md` | Use INF-S / INF-P instead |

</details>

## Local development stack tracker

**Not used.** SOCVault follows AWS-only development (ADR-004). The rows below are **N/A**.

| ID | Component | Status | Notes |
|---|---|---|---|
| DEV-* | Local Docker / localhost | ⛔ N/A | Use staging workspace |

---

## Application feature tracker (MVP API)

Implementation status vs [`api/openapi.yaml`](api/openapi.yaml). Update when app repo endpoints ship.

| ID | Endpoint | Milestone | Backend | Frontend | Bruno test |
|---|---|---|---|---|---|
| API-001 | `GET /health` | 1.1 | 🔴 | — | 📋 collection ready |
| API-002 | `POST /auth/signup` | 1.1 | 🔴 | 🔴 | 📋 |
| API-003 | `POST /auth/verify-otp` | 1.1 | 🔴 | 🔴 | 📋 |
| API-004 | `POST /auth/refresh` | 1.1 | 🔴 | — | 📋 |
| API-005 | `GET /auth/me` | 1.1 | 🔴 | — | 📋 |
| API-006 | `POST /scan/execute` | 1.2 | 🔴 | 🔴 | 📋 |
| API-007 | `GET /scan/{scan_id}` | 1.2 | 🔴 | 🔴 | 📋 |
| API-008 | `GET /scan/history` | 1.2 | 🔴 | 🔴 | 📋 |
| API-009 | `GET /dashboard/summary` | 1.4 | 🔴 | 🔴 | 📋 |
| API-010 | `GET /admin/telemetry` | 1.4 | 🔴 | 🔴 | 📋 |
| API-011 | `GET /admin/explorer/catalog` | 2.9.1 | 📋 | 📋 | — |
| API-012 | `POST /admin/explorer/test` | 2.9.2 | 📋 | 📋 | — |
| API-013 | `/admin/vault/*` | 2.9.3–2.9.4 | 📋 | 📋 | — |
| API-014 | `/admin/ti/feeds/*` | 2.11.4 | 📋 | 📋 | — |

---

## API Explorer build order (Milestone 2.9)

| Step | Task | Roadmap | Status | Blocked by |
|---|---|---|---|---|
| 2.9.1 | Catalog sync | 2.9.1 | 🔴 | App repo, RBAC |
| 2.9.2 | Proxy test runner | 2.9.2 | 🔴 | 2.9.1 |
| 2.9.3 | Encrypted vault + auto-save | 2.9.3 | 🔴 | 2.9.2, INF-018 |
| 2.9.4 | PIN step-up + audit | 2.9.4 | 🔴 | 2.9.3 |
| 2.9.5 | React screen | 2.9.5 | 🔴 | 2.9.1–2.9.4 |
| 2.9.6 | Bruno import/export | 2.9.6 | 🔴 | 2.9.3 |

---

## External accounts & keys

| ID | Service | Purpose | Status | Stored in |
|---|---|---|---|---|
| EXT-001 | AWS | Infrastructure | 🔴 | — |
| EXT-002 | Anthropic | Claude API | 🔴 | SSM `/socvault/mvp/anthropic/api_key` |
| EXT-003 | MongoDB Atlas | Database | 🔴 | SSM `/socvault/mvp/mongodb/uri` |
| EXT-004 | Route 53 / ACM | DNS + TLS for staging | 🔴 | api-staging / app-staging |
| EXT-005 | AWS Amplify | Frontend host (serverless) | 🔴 | Replaces Vercel |
| EXT-006 | GitHub | Code + Actions | 🟡 | Org/repo TBD for app |
| EXT-007 | AbuseIPDB | Threat intel (see registry) | 🔴 | Pass & Keys `ti_abuseipdb_*` |
| EXT-008 | AlienVault OTX | Threat intel (see registry) | 🔴 | Pass & Keys `ti_otx_*` |
| EXT-009 | Stripe | Billing (Phase 2) | 🔴 | — |
| EXT-010 | Domain `socvault.io` | Brand | 🔴 | 0.3.4 |
| EXT-011–032 | Other TI feeds | Per [`docs/20_FREE_EXTERNAL_APIS.md`](docs/20_FREE_EXTERNAL_APIS.md) §5 | 🔴 | Admin TI registry + vault |

---

## How to record an action

When you complete **any** work (infra, code, docs, test, deploy):

1. Add a row to **Action Log** (newest first).
2. Update the matching row in **Infrastructure**, **DEV**, or **API** tracker.
3. Update **Stack live status** if something became live.
4. Set **Last updated** date at top of this file.

**Action log fields:**

| Column | Required | Example |
|---|---|---|
| `ACT-###` | Yes | `ACT-042` |
| Date | Yes | `2026-06-18` |
| Category | Yes | `infra` · `dev` · `api` · `frontend` · `docs` · `test` · `deploy` |
| Ref ID | Yes | `INF-012`, `2.9.1`, `FR-194`, `US-186` |
| Summary | Yes | One line describing what was done |
| Result | Yes | `verified` · `partial` · `blocked` |
| By | Optional | Name or role |

---

## Action log

Newest entries at the top.

| ID | Date | Cat | Ref | Summary | Result | By |
|---|---|---|---|---|---|---|
| ACT-044 | 2026-06-18 | docs | diagrams | Architecture diagram suite v1.0: C4, system flows, extended DFD, RBAC (3 models), module connectivity, L1–L9, ops/CI/CD, trust boundaries, API surface, state machines — `docs/diagrams/` | verified | — |
| ACT-043 | 2026-06-18 | docs | deck | Investor deck v1.16: Seed ISO timing, api-staging URL, 26 epics, round valuations, milestone chronology, Sep 2028 break-even, 3 MSP unlock; docx regenerated | verified | — |
| ACT-042 | 2026-06-18 | docs | deck | Investor deck v1.15 full alignment: Ask section, USP 8, milestones §16, M6–M18 revenue, architecture rows, exec overview sync; docx regenerated | verified | — |
| ACT-041 | 2026-06-18 | docs | deck | Investor deck v1.14: Seed deck wording, milestones M8/M18, cutover criteria, traction dedup, SSM/Amplify labels; `update_deck.py` + docx regenerated | verified | — |
| ACT-040 | 2026-06-18 | docs | — | Full-repo gap fix v1.12: investor §12.1 blueprint status labels, serverless Terraform IaC wording, gap analysis §10 header | verified | — |
| ACT-039 | 2026-06-18 | docs | — | Full-repo gap fix v1.10: onboarding L1 duration, brand break-even/badge, investor M18 header + Phase 3 L9, deck README note, threat model staging, gap analysis | verified | — |
| ACT-038 | 2026-06-18 | docs | — | Full-repo gap fix v1.8: investor table/M18 labels, staging cutover wording, brand phases, exec Seed deck, observatory CORS, MVP spec cross-ref, gap analysis | verified | — |
| ACT-037 | 2026-06-18 | docs | — | Full-repo gap fix v1.6: financial timeline, OpenAPI Cognito JWT, RBAC/observatory design, wireframes NFR, tier mapping | verified | — |
| ACT-036 | 2026-06-18 | docs | ADR-003 | Full-repo gap fix v1.5: FR-006 Cognito, pool model, exec overview cutover, explorer DynamoDB, wireframes, gap analysis refresh | verified | — |
| ACT-035 | 2026-06-18 | docs | ADR-006 | Full-repo gap fix v1.4: roadmap Cognito/staging, .env serverless, API spec staging URL, deck WAF, investor COGS/M18, gap analysis refresh | verified | — |
| ACT-034 | 2026-06-18 | docs | ADR-006 | Full-repo gap fix v1.3: US/FR IDs, Dev Tracker matrix, Redis→DynamoDB, mock/staging envs, break-even labels | verified | — |
| ACT-033 | 2026-06-18 | docs | ADR-006 | Final architecture sync: threat model, expense ledger, gap analysis v1.2, deck Celery row, build queue | verified | — |
| ACT-032 | 2026-06-18 | docs | ADR-006 | Full architecture sync: serverless staging MVP across all docs + investor deck | verified | — |
| ACT-030 | 2026-06-18 | docs | ADR-005 | Auto-scaling ECS Fargate (paid path; MVP superseded by ADR-006) | verified | — |
| ACT-028 | 2026-06-18 | docs | FR-216–229 | Threat Intel Feed Registry: doc 20, OpenAPI `/admin/ti/feeds`, wireframe tab, US-201–208 | verified | — |
| ACT-027 | 2026-06-18 | docs | ADR-004 | Amended: **one** Free Tier AWS account; staging + prod environments (superseded by ADR-006 serverless) | verified | — |
| ACT-026 | 2026-06-18 | docs | ADR-004 | AWS-only strategy (initial two-account draft — superseded by ACT-027) | verified | — |
| ACT-025 | 2026-06-18 | docs | 2.10 | Wireframe `25-admin-dev-tracker.html` + FR-208–215 Super Admin Development Tracker UI | verified | — |
| ACT-024 | 2026-06-18 | docs | Milestone 2.9 | Created `18_API_EXPLORER_IMPLEMENTATION.md` with build order catalog → proxy → vault → PIN → React | verified | — |
| ACT-023 | 2026-06-18 | docs | AWS | Created `AWS_SETUP_README.md` Free Tier MVP guide + root pointer; updated `02_TECHNICAL_STACK` §6.1 | verified | — |
| ACT-022 | 2026-06-18 | docs | 2.9 | Milestone 2.9 API Explorer & Pass & Keys added to roadmap | verified | — |
| ACT-021 | 2026-06-18 | docs | FR-194–207 | Requirements §1.14 Super Admin API Explorer & Pass & Keys vault | verified | — |
| ACT-020 | 2026-06-18 | docs | openapi | Extended `openapi.yaml` with `/admin/explorer/*` and `/admin/vault/*` schemas | verified | — |
| ACT-019 | 2026-06-18 | docs | US-186–193 | User stories + wireframe `24-admin-api-explorer.html` for API Explorer | verified | — |
| ACT-018 | 2026-06-18 | docs | collections | Updated `collections/README.md` with Pass & Keys / Bruno sync notes | verified | — |
| ACT-017 | 2026-06-18 | docs | T-11,T-12 | Threat model updated for vault exfiltration and API Explorer SSRF | verified | — |
| ACT-016 | 2026-06-18 | docs | Phase 2a | Financial plan split Phase 2a Free Tier vs 2b paid (~$100 vs ~$433) | verified | — |
| ACT-015 | 2026-06-18 | docs | 2.1 | Roadmap Milestone 2.1 split into 2.1a Free Tier + 2.1b paid upgrade | verified | — |
| ACT-014 | 2026-06-18 | api | openapi | MVP OpenAPI contract 10 endpoints; Redocly lint (pre-existing warnings) | verified | — |
| ACT-013 | 2026-06-18 | api | collections | Bruno + Postman MVP collections aligned to OpenAPI | verified | — |
| ACT-012 | 2026-06-18 | docs | 12 | Gap analysis v1.1 remediation documented | verified | — |
| ACT-011 | 2026-06-18 | docs | US-121–208 | User story spreadsheet extended to 208 stories (incl. observatory, AI chat, admin) | verified | — |
| ACT-010 | 2026-06-18 | docs | wireframes | 25 HTML wireframes; orphan story refs patched | verified | — |
| ACT-009 | 2026-06-18 | docs | 03 | Requirements v1.1: FR dedup, AI Chat FRs, L1 rate limits fixed | verified | — |
| ACT-008 | 2026-06-18 | docs | 06,13–16 | Added API spec, test strategy, threat model, legal templates, traceability | verified | — |
| ACT-007 | 2026-06-18 | docs | adr | ADRs 001–003: MongoDB, Anthropic, Cognito | verified | — |
| ACT-006 | 2026-06-18 | docs | root | Root README, CONTRIBUTING, `.env.example` | verified | — |
| ACT-005 | 2026-06-18 | docs | 12 | Initial gap analysis created | verified | — |
| ACT-004 | 2026-06-18 | docs | — | SOCVault-Blueprint repo established as product doc source of truth | verified | — |
| ACT-003 | 2026-06-18 | docs | tracker | **Created `DEVELOPMENT_TRACKER.md`** — live stack + infra + action log | verified | — |

<!-- Template — copy when logging:
| ACT-XXX | YYYY-MM-DD | infra/dev/api/frontend/docs/test/deploy | INF-012 / 1.1.1 / FR-xxx | Description of action | verified/partial/blocked | Name |
-->

---

## Weekly review checklist

- [ ] Stack live status matches reality (curl health checks)
- [ ] All completed roadmap nano steps have ACT- log entries
- [ ] Infrastructure table matches AWS console / Atlas dashboard
- [ ] No 🔴 EXT accounts marked 🟢 without secrets in SSM
- [ ] Bruno **staging** env run against live API when API exists
- [ ] Phase % updated

---

*This file is the single product development tracker for SOCVault. Do not duplicate status elsewhere without linking back here.*
