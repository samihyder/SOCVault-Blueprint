# SOCVault — MVP Build Order, User Stories & Automated QA
**Staging-first · API before UI · One user story at a time**  
**Version 1.0 | June 2026**

---

## 1. Principles

| Rule | Detail |
|---|---|
| **MVP = staging** | All work targets `api-staging.socvault.io` / `app-staging.socvault.io` until production cutover |
| **Free Tier first** | Use AWS Free Tier services; paid tier (CDN, WAF, backups, EKS, CodePipeline) when plan says so — update docs if course changes |
| **API before UI** | Ship API Gateway + Lambda route → Bruno/QA green → then wireframe screen |
| **One user story** | Complete QA for US-*N* before starting US-*N+1* in the build queue below |
| **Super Admin links** | API Explorer + Pass & Keys sync staging tokens; Dev Tracker marks story `verified` |
| **IaC only** | No console-only resources; Terraform modules in `socvault-app/infra/` |

Related: ADR-006 · [`19_CI_CD_AND_ENVIRONMENTS.md`](./19_CI_CD_AND_ENVIRONMENTS.md) · [`13_TEST_STRATEGY.md`](./13_TEST_STRATEGY.md) · [`../tests/qa/`](../tests/qa/)

---

## 2. Recommended AWS API stack (MVP)

| Component | Service | Why |
|---|---|---|
| Edge API | **API Gateway HTTP API** | Lower cost than REST API; OpenAPI import; native Cognito JWT authorizer |
| Sync handlers | **Lambda** (Python 3.12) | Free Tier 1M req/mo; scale to zero |
| FastAPI option | **Mangum** ASGI adapter | Single codebase; one Lambda for `/api/v1/*` |
| Async jobs | **SQS + Lambda** | Serverless queue (replaces Celery on MVP) |
| L1 scanner | **Lambda** (container image) | 15-step recon; 120s timeout |
| Frontend | **Amplify Hosting** | Serverless React build/deploy |
| Database | **MongoDB Atlas M0 on AWS** | Free; full MongoDB API (Motor). *Not DocumentDB on MVP* |
| Auth | **Cognito User Pool** | JWT for API Gateway |
| Secrets | **SSM Parameter Store** | `/socvault/staging/*` |
| IaC | **Terraform** | Workspaces: `staging` (active), `production` (dormant) |
| CI | **GitHub Actions** | PR checks + deploy staging on `main` |
| CI (paid) | **CodePipeline + CodeBuild** | AWS-managed deploy orchestration |

**Paid tier (not MVP):** CloudFront CDN · WAF/GuardDuty · AWS Backup · ElastiCache · ECS Fargate · **EKS (Kubernetes)** · CodePipeline as primary deployer.

---

## 3. Build phases

```
Phase A — Platform (INF + OpenAPI health)
Phase B — API routes per user story (Lambda + API GW)
Phase C — Automated QA green per story
Phase D — Wireframe screen + Amplify
Phase E — Super Admin wiring (Explorer / Tracker)
Phase F — Production cutover (when checklist complete)
```

---

## 4. User story build queue (pick one at a time)

Log progress in [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) as `US-xxx` + `ACT-` entries.

### Phase A — Platform

| Order | Story | API / infra | Wireframe | QA |
|---|---|---|---|---|
| A1 | — | Terraform staging: API GW, Lambda, Cognito, S3, DynamoDB, SSM | — | `T-PLAT-001` health |
| A2 | — | GitHub Actions → deploy staging | — | `T-PLAT-002` CI deploy |
| A3 | — | Amplify app-staging shell | — | `T-PLAT-003` app loads |

### Phase B–E — Product (API → QA → UI)

| Order | Story | Title | API routes (OpenAPI) | Wireframe | QA tests |
|---|---|---|---|---|---|
| 1 | US-001 | Signup with business email | `POST /auth/signup` | `01-onboarding.html` | `T-001`, `T-002` |
| 2 | US-002 | Block freemail domains | `POST /auth/signup` (400) | `01-onboarding.html` | `T-001` |
| 3 | US-003 | Domain extraction | signup response | `01-onboarding.html` | `T-002` |
| 4 | US-004 | OTP via SNS | `POST /auth/signup` | `01-onboarding.html` | `T-002` |
| 5 | US-005 | Verify OTP | `POST /auth/verify-otp` | `01-onboarding.html` | `T-002`, `T-007` |
| 6 | US-006 | Session refresh | `POST /auth/refresh` | `01-onboarding.html` | `T-007` |
| 7 | US-007 | Profile / me | `GET /auth/me` | `01-onboarding.html` | `T-007` |
| 8 | US-008 | Start L1 scan | `POST /scan/execute` | `03-l1-recon.html` | `T-003`, `T-004` |
| 9 | US-009 | Scan status polling | `GET /scan/{id}` | `03-l1-recon.html` | `T-004` |
| 10 | US-010 | Freemium rate limit (1/calendar month) | `POST /scan/execute` (429) | `03-l1-recon.html` | `T-003` |
| 11 | US-011 | L1 step — WHOIS | scan pipeline | `03-l1-recon.html` | `T-004` |
| 12 | US-012 | L1 step — DNS | scan pipeline | `03-l1-recon.html` | `T-004` |
| 13 | US-013 | L1 step — SSL/TLS | scan pipeline | `03-l1-recon.html` | `T-004` |
| 14 | US-014 | L1 step — HTTP headers | scan pipeline | `03-l1-recon.html` | `T-004` |
| 15 | US-015 | L1 step — Subdomains | scan pipeline | `03-l1-recon.html` | `T-004` |
| 16 | US-016 | L1 step — Port scan | scan pipeline | `03-l1-recon.html` | `T-004` |
| 17 | US-017 | L1 step — Tech stack | scan pipeline | `03-l1-recon.html` | `T-004` |
| 18 | US-018 | L1 report — score | `GET /scan/{id}` report | `04-l1-report.html` | `T-004`, `T-008` |
| 19 | US-019 | L1 report — findings list | report routes | `04-l1-report.html` | `T-008` |
| 20 | US-020 | L1 report — export PDF | report routes | `04-l1-report.html` | `T-008` |
| 21 | US-021+ | Claude AI report | report generation | `05-ai-report.html` | `T-005` |
| 22 | US-066+ | Dashboard summary | `GET /dashboard/summary` | `06-dashboard.html` | `T-010` |
| 23 | US-186–193 | API Explorer | `/admin/explorer/*` | `24-admin-api-explorer.html` | `T-ADM-001` |
| 24 | US-201–208 | Threat Intel feeds | `/admin/ti/feeds/*` | `24-admin-api-explorer.html` | `T-ADM-002` |
| 25 | US-194–200 | Dev Tracker (FR-208–215) | `/admin/development-tracker` | `25-admin-dev-tracker.html` | `T-ADM-003` |

> Full US ↔ FR ↔ wireframe map: [`16_TRACEABILITY_MATRIX.md`](./16_TRACEABILITY_MATRIX.md). Extend this table as stories enter MVP scope.

### Definition of done (per user story)

- [ ] Terraform/IaC updated if new AWS resource needed
- [ ] OpenAPI + Bruno collection updated
- [ ] Lambda + API Gateway route deployed to **staging**
- [ ] QA scripts in [`tests/qa/`](../tests/qa/) pass (`run-staging-qa.sh --story US-xxx`)
- [ ] Wireframe screen live on Amplify staging (if UI story)
- [ ] Super Admin panel reflects route in Explorer catalog (admin stories)
- [ ] `DEVELOPMENT_TRACKER.md` action log entry

---

## 5. Super Admin integration flow

```
1. Engineer implements API route on staging
2. Super Admin → API Explorer → test route → token saved to Pass & Keys (staging)
3. Export env → Bruno / frontend `.env.staging`
4. Frontend screen calls staging API with vault token
5. Dev Tracker → mark US-xxx verified
```

See [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md).

---

## 6. Automated QA (staging)

### 6.1 Tooling

| Tool | Role |
|---|---|
| [`tests/qa/run-staging-qa.sh`](../tests/qa/run-staging-qa.sh) | Master runner — all suites or `--story US-xxx` |
| [`tests/qa/manifest.yaml`](../tests/qa/manifest.yaml) | Maps user stories → test IDs → scripts |
| `tests/qa/api/*.py` | pytest + httpx against live staging API |
| Bruno CLI | Optional: `bru run collections/bruno/SOCVault-MVP --env staging` |
| GitHub Actions | `.github/workflows/qa-staging.yml` (template in [`templates/`](../templates/github/workflows/)) |

### 6.2 When QA runs

| Trigger | Scope |
|---|---|
| Every push to `main` | Full staging QA suite |
| PR to `main` | Unit tests + terraform plan + optional mock OpenAPI |
| Manual | `./tests/qa/run-staging-qa.sh --story US-005` |
| Pre-production cutover | Full suite + Bruno + smoke on production (once active) |

### 6.3 Required secrets (GitHub Actions)

| Secret | Purpose |
|---|---|
| `STAGING_API_URL` | `https://api-staging.socvault.io/api/v1` |
| `STAGING_TEST_EMAIL` | Business email for signup tests |
| `STAGING_TEST_PHONE` | E.164 phone for OTP tests |
| `AWS_ROLE_ARN` | OIDC deploy role (separate workflow) |

---

## 7. Production cutover checklist

Production remains **dormant** until all items complete:

- [ ] MVP user stories through Phase 1 gate verified on staging
- [ ] Terraform `production` workspace applied
- [ ] Production secrets in SSM `/socvault/production/*` (not copies of staging)
- [ ] Paid tier decisions documented (CDN, WAF, Backup) if required
- [ ] GitHub production environment approval configured
- [ ] Smoke QA on `api.socvault.io`
- [ ] ACT- log entry

---

*Pick the next `US-*` from §4. Do not parallelise across stories until QA is green.*
