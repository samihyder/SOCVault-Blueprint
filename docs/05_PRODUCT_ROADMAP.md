# SOCVault — Product Roadmap
**Phases, Sprints, Milestones & Nano Steps**
**Version 1.0 | June 2026**

---

## Overview

The roadmap is structured into **5 Phases** spanning 24 months, broken into **2-week sprints**. Each sprint contains specific **nano steps** — atomic, completable tasks assignable to a single engineer for a single session.

```
Phase 0: Foundation    (Weeks 1–4)     ─ One AWS account; **staging** active; production dormant; CI/CD + Terraform
Phase 1: Cloud MVP     (Weeks 5–16)    ─ Auth + L1 + AI + dashboard on **staging**; production dormant until cutover
Phase 2: Beta & scale  (Weeks 17–24)   ─ Payments, SOAR, beta users, paid AWS upgrades
Phase 3: Launch        (Weeks 25–36)   ─ Public launch + GTM
Phase 4: Growth        (Weeks 37–52)   ─ Scaling + compliance + enterprise tier
Phase 5: Expansion     (Year 2)        ─ International + Series A + managed SOC
```

> **No local runtime.** MVP runs on **staging only**; production activates at cutover. User stories one-at-a-time per [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md). ADR-006.

---

## Phase 0: Foundation (Weeks 1–4)

**Goal:** AWS account, **staging-only** serverless stack, Terraform IaC, GitHub Actions + QA — **production dormant**.

> **MVP = staging** until production cutover (ADR-006). Pick **one user story at a time** — see [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md).

### Milestone 0.1 — AWS staging, IaC & CI/CD

**Sprint 0.1 (Week 1–2)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 0.1.1 | Create **one** AWS account + root MFA + $15–30 budget | Founder | 1h |
| 0.1.2 | IAM admin + MFA | Founder | 0.5h |
| 0.1.3 | Create GitHub org + `socvault-app` repository | Founder | 1h |
| 0.1.4 | Terraform backend (S3 state + DynamoDB lock) | Eng | 2h |
| 0.1.5 | Staging: API Gateway HTTP + Lambda skeleton + Cognito | Eng | 4h |
| 0.1.6 | Staging: S3, DynamoDB, SQS, SSM `/staging/*` | Eng | 2h |
| 0.1.7 | Atlas M0 **socvault-staging** + connection in SSM | Eng | 1h |
| 0.1.8 | Amplify **app-staging** + `api-staging` DNS → API GW | Eng | 2h |
| 0.1.9 | `ci.yml` + `deploy-staging.yml` + `qa-staging.yml` | Eng | 4h |
| 0.1.10 | `GET /health` green + `run-staging-qa.sh` pass | Eng | 2h |

**Sprint 0.2 (Week 3–4)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 0.2.1 | OpenAPI import to API Gateway; Bruno staging env | Eng | 2h |
| 0.2.2 | Lambda L1 staging function | Eng | 3h |
| 0.2.3 | Super Admin API Explorer scaffold (staging only) | Eng | 4h |
| 0.2.4 | **Production Terraform workspace** (dormant — not applied) | Eng | 2h |
| 0.2.5 | React shell on Amplify staging (brand tokens) | Eng | 3h |
| 0.2.6 | Anthropic + TI keys in SSM staging | Founder | 1h |
| 0.2.7 | Document paid-tier placeholders (CloudFront, WAF, Backup, EKS) in IaC | Eng | 2h |
| 0.2.8 | ADR-006 review + Dev Tracker US-001 queued | Founder | 1h |

### Milestone 0.2 — Brand Assets Ready

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 0.3.1 | Export SOCVault logo in SVG, PNG (512×512), and ICO formats | Designer | 1h |
| 0.3.2 | Document brand colours: `#1B3D35` (forest green), `#4CC844` (lime green), `#FFFFFF` (white) | Designer | 0.5h |
| 0.3.3 | Create Tailwind CSS theme file with SOCVault brand tokens | Eng | 1h |
| 0.3.4 | Register `socvault.io` domain (or preferred TLD) | Founder | 0.5h |

---

## Phase 1: Cloud MVP on staging (Weeks 5–16)

**Goal:** Build the core product loop on **staging** (auth → L1 → Claude → dashboard). Production stays **dormant** until cutover checklist ([`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) §7). Validate with Bruno against `api-staging.socvault.io`.

> **Auth (ADR-003):** Cognito from day one — no custom JWT library phase.

### Milestone 1.1 — Authentication & Onboarding (Cognito)

**Sprint 1.1 (Weeks 5–6)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.1.1 | Write `POST /api/v1/auth/signup` Lambda with Pydantic model (email + phone) | Eng | 2h |
| 1.1.2 | Implement `is_valid_business_domain()` with comprehensive blocklist (20+ freemail domains) | Eng | 1h |
| 1.1.3 | Implement domain extraction from email and store as `workspace_domain` | Eng | 0.5h |
| 1.1.4 | Generate UUID v4 `tenant_id`; provision tenant document in MongoDB | Eng | 1h |
| 1.1.5 | Generate 6-digit OTP; deliver via SNS (staging) / SES | Eng | 1h |
| 1.1.6 | Write `POST /api/v1/auth/verify-otp` Lambda | Eng | 1h |
| 1.1.7 | Configure **Cognito User Pool** + custom `tenant_id` attribute; pre-signup Lambda blocks freemail (ADR-003) | Eng | 2h |
| 1.1.8 | On OTP success, create/link Cognito user; return **Cognito JWT** access + refresh tokens | Eng | 2h |
| 1.1.9 | Write `GET /api/v1/auth/me` — validate Cognito JWT; return tenant profile | Eng | 0.5h |
| 1.1.10 | Protect routes via **API Gateway Cognito authorizer** + Lambda `tenant_id` middleware | Eng | 1.5h |
| 1.1.11 | Write unit + integration tests for auth (pytest + staging Cognito) | Eng | 2h |
| 1.1.12 | Set CORS to staging + production app origins only (never `*`) | Eng | 0.5h |

**Frontend Sprint 1.1 (parallel)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.1.13 | Build onboarding screen: email + phone form with SOCVault brand colours | Eng | 2h |
| 1.1.14 | Build OTP verification screen | Eng | 1h |
| 1.1.15 | Wire **Amplify Auth** to Cognito User Pool (session via Cognito SDK — not raw tokens in localStorage) | Eng | 1h |
| 1.1.16 | Add redirect to dashboard on successful login | Eng | 0.5h |
| 1.1.17 | Add error states for invalid domain, already registered | Eng | 1h |

### Milestone 1.2 — Scanning Engine (Mock → Real)

**Sprint 1.2 (Weeks 7–8)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.2.1 | Write `ScannerDrivers` class with `execute_recon()` returning mock port data | Eng | 1h |
| 1.2.2 | Write `execute_appsec()` returning mock CVE data | Eng | 1h |
| 1.2.3 | Write `POST /api/v1/scan/execute` endpoint accepting `{tenant_id, target, layer}` | Eng | 2h |
| 1.2.4 | Implement Freemium gate: check calendar month, reject if L1 already run this month (FR-026) | Eng | 1.5h |
| 1.2.5 | Add scan authorisation consent field to scan request model | Eng | 0.5h |
| 1.2.6 | Add target validation: target must match `workspace_domain` or a licensed IP | Eng | 1.5h |
| 1.2.7 | Implement `GET /api/v1/scan/{scan_id}` polling endpoint | Eng | 1h |
| 1.2.8 | Store scan record in MongoDB with status: QUEUED → RUNNING → COMPLETE | Eng | 1.5h |
| 1.2.9 | Write unit tests for scan gating logic | Eng | 1.5h |

**Sprint 1.3 (Weeks 9–10) — Real Scanner Integration**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.3.1 | Implement Step 1: WHOIS lookup using `python-whois`; extract registrar, expiry, flag if <30 days | Eng | 1h |
| 1.3.2 | Implement Step 2: DNS record analysis (A, AAAA, MX, NS, TXT, CNAME, SOA) using `dnspython` | Eng | 1.5h |
| 1.3.3 | Implement Step 3: Email security check (SPF/DKIM/DMARC) using `checkdmarc` library | Eng | 1.5h |
| 1.3.4 | Implement Step 4: SSL/TLS audit using `sslyze`; flag expired certs, TLS 1.0/1.1, weak ciphers | Eng | 2h |
| 1.3.5 | Implement Step 5: HTTP security headers check using `python-requests`; flag missing CSP/HSTS | Eng | 1h |
| 1.3.6 | Implement Step 6: Certificate transparency lookup via `crt.sh` REST API | Eng | 1h |
| 1.3.7 | Implement Step 7: Subdomain discovery using `subfinder` (passive only in free tier) | Eng | 2h |
| 1.3.8 | Implement Step 8: Live host validation using `httpx`; extract HTTP titles, redirects, server headers | Eng | 1.5h |
| 1.3.9 | Implement Step 9: Port discovery using `naabu` (top 100 TCP ports); flag high-risk ports | Eng | 2h |
| 1.3.10 | Implement Step 10: Technology fingerprinting using `httpx` + Wappalyzer signature matching | Eng | 1.5h |
| 1.3.11 | Implement Step 11: IP reputation check using AbuseIPDB API | Eng | 1h |
| 1.3.12 | Implement Step 12: Domain reputation check using Google Safe Browsing + URLhaus APIs | Eng | 1h |
| 1.3.13 | Implement Step 13: Credential leak check using HaveIBeenPwned domain search API | Eng | 1h |
| 1.3.14 | Implement Step 14: Subdomain takeover detection (check CNAMEs against unclaimed cloud services) | Eng | 2h |
| 1.3.15 | Implement Step 15: Service banner analysis (Naabu + Nmap banner grab on open ports) | Eng | 1.5h |
| 1.3.16 | Aggregate all 15 step outputs into unified `raw_findings` JSON schema | Eng | 2h |
| 1.3.17 | Run all 15 steps in parallel using `asyncio.gather()` (target: <90 second total time) | Eng | 2h |
| 1.3.18 | Add timeout handling per step (30 seconds max per step; continue on timeout) | Eng | 1h |
| 1.3.19 | Add error handling: step failure → mark as "unavailable", do not fail whole scan | Eng | 1h |
| 1.3.20 | Enqueue scan to **SQS**; API returns **202 + scan_id** immediately (async pattern) | Eng | 3h |
| 1.3.21 | **Lambda worker** consumes SQS → invokes L1 Lambda; update scan status in MongoDB | Eng | 2h |
| 1.3.22 | Test full 15-step Recon scan against `scanme.nmap.org` (authorised target) | Eng | 1h |

### Milestone 1.3 — AI Intelligence Layer

**Sprint 1.4 (Weeks 11–12)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.4.1 | Create `AnthropicClient` class using official `anthropic` Python SDK | Eng | 1h |
| 1.4.2 | Replace ALL Gemini API references with Anthropic API calls | Eng | 2h |
| 1.4.3 | Replace incorrect model IDs with `claude-sonnet-4-6` throughout codebase | Eng | 0.5h |
| 1.4.4 | Write financial risk translation system prompt (vCISO persona) | Eng | 2h |
| 1.4.5 | Implement `analyze_financially()` method sending raw scan JSON to Claude | Eng | 2h |
| 1.4.6 | Implement JSON response parsing with markdown code block stripping | Eng | 1h |
| 1.4.7 | Implement exponential backoff (5 retries, 1s initial delay) for API calls | Eng | 1h |
| 1.4.8 | Implement offline fallback: return pre-defined mock report if API unavailable | Eng | 1h |
| 1.4.9 | Enable Anthropic prompt caching for system prompts (reduce token costs) | Eng | 1.5h |
| 1.4.10 | Calculate and store per-scan token counts in `cogs` subdocument | Eng | 1h |
| 1.4.11 | Write integration test: send mock scan data → receive valid JSON report | Eng | 1h |
| 1.4.12 | Validate Claude output matches expected JSON schema with Pydantic | Eng | 1.5h |

### Milestone 1.4 — Dashboard (Frontend)

**Sprint 1.5 (Weeks 13–14)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.5.1 | Build dashboard layout: sidebar nav + main content area | Eng | 2h |
| 1.5.2 | Apply SOCVault brand colours (#1B3D35, #4CC844) to Tailwind config | Eng | 0.5h |
| 1.5.3 | Build Health Score widget (circular gauge, 0–100) | Eng | 2h |
| 1.5.4 | Build Financial Exposure widget (large $ figure, red/amber/green colouring) | Eng | 1.5h |
| 1.5.5 | Build scan target input + layer selector (RECON, APPSEC, CLOUD) | Eng | 1.5h |
| 1.5.6 | Build loading state with animated scan progress indicator | Eng | 1h |
| 1.5.7 | Build findings list: card per vulnerability with risk type, summary, damage | Eng | 2h |
| 1.5.8 | Build paywall gate on remediation scripts (Freemium sees blur + upgrade CTA) | Eng | 2h |
| 1.5.9 | Integrate polling: GET /scan/{id} every 3 seconds until COMPLETE | Eng | 1.5h |
| 1.5.10 | Build admin telemetry panel (COGS per scan, total cost) | Eng | 1.5h |
| 1.5.11 | Add SOCVault logo to navbar and favicon | Eng | 0.5h |

**Sprint 1.6 (Weeks 15–16) — Polish & Internal Testing**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 1.6.1 | E2E on **staging**: sign up → OTP → scan → report (`run-staging-qa.sh` + manual OTP) | Founder | 2h |
| 1.6.2 | Fix all bugs found in E2E test | Eng | 4h |
| 1.6.3 | Add rate limiting (API Gateway usage plans + per-tenant check in Lambda) | Eng | 1.5h |
| 1.6.4 | Add input validation for all endpoints (reject oversized payloads) | Eng | 1h |
| 1.6.5 | Remove all hardcoded credentials and API keys from source code | Eng | 1h |
| 1.6.6 | Test Freemium gate: verify second scan within same **calendar month** is rejected (FR-026) | Eng | 0.5h |
| 1.6.7 | Write `GET /api/v1/admin/telemetry` endpoint with COGS aggregation | Eng | 1.5h |
| 1.6.8 | Internal demo to 3 friendly SMB contacts for feedback | Founder | 3h |
| 1.6.9 | Document all API endpoints in Postman collection | Eng | 2h |

**Milestone 1 Completion Criteria:**
- [ ] Full user journey on **staging**: signup → OTP → scan → AI report → dashboard
- [ ] `./tests/qa/run-staging-qa.sh` green for Phase 1 user stories
- [ ] Freemium gate enforced (1 scan/calendar month — FR-026)
- [ ] Claude AI integration with `claude-sonnet-4-6`
- [ ] No hardcoded secrets; SSM only
- [ ] Super Admin API Explorer can test staging routes (Milestone 2.9 partial)

---

## Phase 2: Beta & scale (Weeks 17–24)

**Goal:** Production cutover (when ready), Stripe, SOAR beta, 10 paying clients. **Infra bootstrap is Phase 0** — do not duplicate here.

### Milestone 2.1 — Paid-tier infrastructure hardening

**Strategy:** Staging MVP already live (ADR-006). This milestone adds **paid-tier** services when triggered: CloudFront, WAF, Backup, Atlas M10, Wazuh EC2, optional ECS Fargate bridge, **EKS** prep, **CodePipeline**.

**Sprint 2.1 (Weeks 17–18)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.1.1 | Production cutover checklist ([`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) §7) | Founder | 2h |
| 2.1.2 | Terraform apply **production** workspace (post-approval) | Eng | 4h |
| 2.1.3 | Atlas **M0 → M10** + VPC peering | Eng | 2h |
| 2.1.4 | **CloudFront** CDN in front of Amplify + API (paid tier) | Eng | 2h |
| 2.1.5 | **AWS WAF** + GuardDuty on API Gateway (paid tier) | Eng | 2h |
| 2.1.6 | **AWS Backup** for S3/DynamoDB; Atlas continuous backup | Eng | 2h |
| 2.1.7 | **CodePipeline** + CodeBuild (replace GitHub deploy for prod) | Eng | 4h |
| 2.1.8 | Wazuh EC2 t3.medium when L7 beta starts | Eng | 2h |
| 2.1.9 | EKS cluster Terraform module (paid — activate when scale requires) | Eng | 6h |
| 2.1.10 | Bruno + QA smoke on production post-cutover | Eng | 1h |

### Milestone 2.2 — Cognito Hardening & Session UX

**Sprint 2.2 (Weeks 19–20)** — Cognito bootstrap is in Phase 1 (Milestone 1.1); this milestone hardens auth for beta.

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.2.1 | Pre-token-generation Lambda: inject `tenant_id` claim into Cognito JWT | Eng | 2h |
| 2.2.2 | Implement `POST /api/v1/auth/refresh` against Cognito refresh token flow | Eng | 1.5h |
| 2.2.3 | Optional TOTP MFA for tenant admin roles | Eng | 2h |
| 2.2.4 | Account recovery / password reset flows via Cognito | Eng | 2h |
| 2.2.5 | API Gateway usage-plan rate limits on auth routes | Eng | 1h |
| 2.2.6 | Audit: no custom JWT signing libraries in codebase (ADR-003 compliance) | Eng | 1h |
| 2.2.7 | Auth E2E in `tests/qa/` green on staging | Eng | 1h |

### Milestone 2.3 — Stripe Payment Integration

**Sprint 2.3 (Weeks 21–22)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.3.1 | Create Stripe account and configure SOCVault products/prices | Founder | 2h |
| 2.3.2 | Install `stripe` Python library and configure webhook endpoint | Eng | 1h |
| 2.3.3 | Write `POST /api/v1/billing/subscribe` endpoint | Eng | 2h |
| 2.3.4 | Store `stripe_customer_id` on tenant document after checkout | Eng | 0.5h |
| 2.3.5 | Handle `customer.subscription.created` webhook → upgrade tenant tier | Eng | 2h |
| 2.3.6 | Handle `customer.subscription.deleted` webhook → downgrade to FREEMIUM | Eng | 1.5h |
| 2.3.7 | Handle `invoice.payment_failed` webhook → send warning email, 7-day grace | Eng | 1.5h |
| 2.3.8 | Write `POST /api/v1/billing/portal` endpoint (Stripe portal redirect) | Eng | 1h |
| 2.3.9 | Add upgrade CTA on all paywall gates in the frontend | Eng | 1.5h |
| 2.3.10 | Test end-to-end checkout flow with Stripe test cards | Eng | 1h |
| 2.3.11 | Enable Stripe Radar for fraud detection | Founder | 0.5h |

### Milestone 2.4 — SOAR Engine (Cloud)

**Sprint 2.4 (Weeks 23–24)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.4.1 | Deploy Wazuh agents to 3 test servers | Eng | 2h |
| 2.4.2 | Configure Wazuh Manager to forward alerts to SOCVault API | Eng | 1.5h |
| 2.4.3 | Write `POST /api/v1/incidents/ingest` webhook for Wazuh alerts | Eng | 2h |
| 2.4.4 | Implement `ThreatIntelManager.enrich_ip()` with real AbuseIPDB API | Eng | 1.5h |
| 2.4.5 | Implement OTX enrichment with real API key | Eng | 1h |
| 2.4.6 | Fix model reference in `SOAROrchestrator.consult_claude_soar()` to use `claude-sonnet-4-6` | Eng | 0.5h |
| 2.4.7 | Implement human approval queue: store incidents with status AWAITING_APPROVAL | Eng | 1.5h |
| 2.4.8 | Write `POST /api/v1/incidents/{id}/approve` and `/reject` endpoints | Eng | 1h |
| 2.4.9 | Build incident feed UI in React dashboard | Eng | 2.5h |
| 2.4.10 | Build human approval modal (show alert context + AI analysis + approve/reject buttons) | Eng | 2h |
| 2.4.11 | Implement Slack webhook notification on new incident | Eng | 1h |
| 2.4.12 | Test full SOAR loop: Wazuh alert → enrichment → Claude triage → human gate | Eng | 2h |

### Milestone 2.5 — Malware Detection & Response Engine (L8)

**Sprint 2.5 (Weeks 25–26)**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.5.1 | Configure Wazuh ClamAV integration on all enrolled SOC Pro test endpoints | Eng | 2h |
| 2.5.2 | Configure Wazuh FIM rules to alert on new/modified executables in `/bin`, `/usr/bin`, `/tmp`, `/var/www` | Eng | 2h |
| 2.5.3 | Create MDRM (Malware Detection & Response Manager) microservice skeleton in FastAPI | Eng | 2h |
| 2.5.4 | Write `POST /api/v1/malware/ingest` webhook to receive Wazuh ClamAV and FIM detection events | Eng | 1.5h |
| 2.5.5 | Integrate VirusTotal API: hash lookup with confidence score and malware family retrieval | Eng | 2h |
| 2.5.6 | Implement local YARA rule engine with initial ruleset (ransomware, RATs, cryptominers, web shells) | Eng | 3h |
| 2.5.7 | Build MDRM Claude AI analysis function: send detection event + VT result + YARA match to `claude-sonnet-4-6` | Eng | 2h |
| 2.5.8 | Parse Claude AI response: extract malware family, severity (1–10), lateral movement risk, exfiltration likelihood | Eng | 1.5h |
| 2.5.9 | Parse Claude AI response: extract quarantine command, removal command, persistence cleanup steps, IOC list, verification command | Eng | 1.5h |
| 2.5.10 | Implement AUTO-REMEDIATE path: confidence >95% + isolated threat → quarantine file to `/var/ossec/quarantine/`, kill process, update blocklist | Eng | 3h |
| 2.5.11 | Implement HUMAN GATE path: route to approval queue with full threat context for system-wide or low-confidence threats | Eng | 2h |
| 2.5.12 | Add malware approval/reject endpoints (`POST /api/v1/malware/{id}/approve` and `/reject`) | Eng | 1h |
| 2.5.13 | Send Slack + email + dashboard notification immediately on every malware detection event | Eng | 1.5h |
| 2.5.14 | Implement post-remediation re-scan: trigger ClamAV rescan on affected directory and confirm clean | Eng | 2h |
| 2.5.15 | Generate malware incident report: malware family, affected files, actions taken, clean bill of health — store in MongoDB | Eng | 2h |
| 2.5.16 | Update Workspace Health Score after confirmed remediation | Eng | 0.5h |
| 2.5.17 | Maintain full audit log of quarantine/removal actions (actor, timestamp, file hash, action taken) in MongoDB | Eng | 1h |
| 2.5.18 | Wire L2 Nuclei webshell detection results to MDRM webhook (on-demand trigger via AppSec scan) | Eng | 1.5h |
| 2.5.19 | Build Malware Detection dashboard tab: incident list, severity badge, status (auto-remediated / pending / approved) | Eng | 4h |
| 2.5.20 | Gate all MDRM endpoints behind SOC Pro tier check — return 402 for Freemium/Pay-per-IP tenants | Eng | 0.5h |
| 2.5.21 | Write YARA rule update script to pull latest community rules from YARA-Rules GitHub repo | Eng | 1h |
| 2.5.22 | End-to-end test: simulate ClamAV detection → MDRM ingestion → Claude analysis → auto-quarantine → re-scan clean | Eng | 3h |

**Milestone 2 Completion Criteria:**
- [ ] Platform live on **staging** (`app-staging.socvault.io`); **production** (`app.socvault.io`) after cutover checklist (Milestone 2.1)
- [ ] Cognito auth working end-to-end
- [ ] Stripe checkout and webhook handling complete
- [ ] SOAR pipeline live with real Wazuh alerts
- [ ] Malware Detection & Response Engine live (L8)
- [ ] L9 AI Agent Scan live with activity log
- [ ] Tenant sub-users and internal RBAC provisioned
- [ ] Metrics Observatory v1 (cost + API perf panels)
- [ ] Auto-remediation and human approval gate both tested end-to-end
- [ ] 10 beta clients onboarded manually
- [ ] First paid conversion

### Milestone 2.6 — L9 AI Agent Scan (Weeks 27–28)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.6.1 | Build `POST /api/v1/scan/l9/execute` with scope + depth params | Eng | 4h |
| 2.6.2 | Integrate Claude Opus 4.8 agent loop with THINK/TOOL/FIND/DONE events | Eng | 8h |
| 2.6.3 | Build live activity log WebSocket/poll endpoint | Eng | 3h |
| 2.6.4 | Wire L9 findings to unified report schema | Eng | 3h |
| 2.6.5 | Enforce 1 scan / 7 days rate limit (FR-115) | Eng | 2h |
| 2.6.6 | Build frontend per wireframe `20-l9-ai-scan.html` | Frontend | 8h |

### Milestone 2.7 — Tenant Teams & Internal RBAC (Weeks 27–28)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.7.1 | Build sub-user invite/accept/revoke API (FR-140–149) | Eng | 6h |
| 2.7.2 | Cognito sub-user accounts linked to tenant_id | Eng | 4h |
| 2.7.3 | Build `21-tenant-teams.html` frontend | Frontend | 6h |
| 2.7.4 | Build internal team + 12-role RBAC (FR-150–166) | Eng | 8h |
| 2.7.5 | Build `22-socvault-team-admin.html` frontend | Frontend | 6h |

### Milestone 2.8 — Metrics Observatory v1 (Weeks 29–30)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.8.1 | Integrate AWS Cost Explorer API feed | Eng | 4h |
| 2.8.2 | Build Claude token usage aggregation endpoint | Eng | 3h |
| 2.8.3 | Build API latency metrics from CloudWatch | Eng | 3h |
| 2.8.4 | Build `23-metrics-observatory.html` with 30s auto-refresh | Frontend | 10h |
| 2.8.5 | RBAC-gate Observatory panels per internal role | Eng | 4h |
| 2.8.6 | Build rate-limit countdown UI on scan modules (FR-117) | Frontend | 3h |
| 2.8.7 | Superadmin rate-limit override API + audit log (FR-119) | Eng | 2h |

### Milestone 2.9 — API Explorer & Pass & Keys (Week 31)

**Build order (do not reorder):** catalog sync → proxy test runner → encrypted vault → PIN step-up → React screen → Bruno sync.

Full step-by-step guide: [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md).

| # | Nano Step | Owner | Hours | Step |
|---|---|---|---|---|
| 2.9.1 | OpenAPI sync → `GET /admin/explorer/catalog` | Eng | 3h | **1** |
| 2.9.2 | Server-side proxy test runner + try/catch result envelope (SSRF allowlist) | Eng | 6h | **2** |
| 2.9.3 | KMS-encrypted vault CRUD + `{{var}}` resolution + auto-save from test responses | Eng | 6h | **3** |
| 2.9.4 | Step-up PIN unlock session (5 min TTL) + reveal/copy audit | Eng | 4h | **4** |
| 2.9.5 | React screen from `24-admin-api-explorer.html` (catalog + tester + Pass & Keys + PIN modal) | Frontend | 8h | **5** |
| 2.9.6 | Bruno import/export for vault variables | Eng | 3h | **6** |

**Milestone 2.9 done when:**

- [ ] Steps 1–5 shipped; auth → scan flow runnable entirely from admin UI
- [ ] Vault secrets masked until PIN unlock; audit log has no plaintext values
- [ ] Bruno `01-auth` passes using explorer-stored variables

### Milestone 2.10 — Development Tracker UI (Week 32)

**Build order:** seed INF/DEV/API items from blueprint → MongoDB CRUD → action log → React screen → markdown export → optional health probes.

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.10.1 | Seed tracker items from `DEVELOPMENT_TRACKER.md` / roadmap IDs | Eng | 2h |
| 2.10.2 | `GET/PATCH /admin/tracker/items` + `POST/GET /admin/tracker/actions` | Eng | 5h |
| 2.10.3 | `POST /admin/tracker/export` → markdown for git | Eng | 2h |
| 2.10.4 | Build `25-admin-dev-tracker.html` React screen (tabs, log form, filters) | Frontend | 8h |
| 2.10.5 | Stack health probe job (optional) updating live status cells | Eng | 3h |
| 2.10.6 | RBAC + audit log for tracker mutations (FR-215) | Eng | 2h |

### Milestone 2.11 — Threat Intel Feed Registry (Week 33)

**Prerequisite:** Milestone 2.9 (Pass & Keys vault). **Catalogue:** [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) only — seed feeds from JSON, do not hardcode provider lists in React.

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 2.11.1 | Seed feed registry from doc 20 §5 → MongoDB `ti_feeds` | Eng | 2h |
| 2.11.2 | `ThreatIntelManager` + provider adapters (AbuseIPDB, OTX, HIBP, NVD, URLhaus) | Eng | 10h |
| 2.11.3 | DynamoDB `ti_cache` + rate limiter + quota counters | Eng | 4h |
| 2.11.4 | OpenAPI `/admin/ti/feeds/*` routes + FR-216–226 | Eng | 5h |
| 2.11.5 | Threat Intel tab on API Explorer wireframe (US-201–205) | Frontend | 6h |
| 2.11.6 | CorrelationEngine async + `enrichment_summary` in reports (FR-225–227) | Eng | 8h |
| 2.11.7 | S3 daily snapshot job for keyless feeds (CISA KEV, Spamhaus, Feodo) — FR-229 | Eng | 3h |

**Milestone 2.11 done when:**

- [ ] L1 scan enriches IP via AbuseIPDB when feed enabled
- [ ] Super Admin can test feed, view quota, enable/disable without redeploy
- [ ] Report shows at least one correlated pattern when HIBP + L7 alert overlap

---

## Phase 3: Public Launch (Weeks 25–36)

> **Scheduling note:** Milestone **2.5 (L8 MDRM, Weeks 25–26)** overlaps Phase 3 kickoff — run as a **parallel engineering track** while GTM launch prep (Milestone 3.1) proceeds on founder/marketing capacity.

**Goal:** Public launch, 50 paying clients, $10K MRR.

### Milestone 3.1 — Launch Preparation (Weeks 25–28)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 3.1.1 | Run full OWASP Top 10 security review against SOCVault platform | Eng | 8h |
| 3.1.2 | Fix all Critical and High severity findings from security review | Eng | 8h |
| 3.1.3 | Implement Content Security Policy (CSP) headers on frontend | Eng | 1.5h |
| 3.1.4 | Enable **AWS WAF** on API Gateway (paid tier) | Eng | 1h |
| 3.1.5 | Add Sentry error tracking to frontend and backend | Eng | 1.5h |
| 3.1.6 | Write Privacy Policy, Terms of Service, and Data Processing Agreement | Founder/Legal | 6h |
| 3.1.7 | Implement scan authorisation consent flow (checkbox + timestamp stored) | Eng | 1.5h |
| 3.1.8 | Implement GDPR data deletion endpoint (`DELETE /api/v1/account`) | Eng | 2h |
| 3.1.9 | Build marketing landing page with waitlist form | Designer/Eng | 8h |
| 3.1.10 | Set up Intercom for in-app support chat | Founder | 1h |
| 3.1.11 | Write 5 LinkedIn launch posts scheduled over 2 weeks | Founder | 3h |
| 3.1.12 | Submit to Product Hunt (schedule launch day) | Founder | 2h |

### Milestone 3.2 — Advanced Scanning Layers (Weeks 29–32)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 3.2.1 | Integrate OWASP ZAP for DAST scanning (Layer 2 enhancement) | Eng | 4h |
| 3.2.2 | Integrate Semgrep for SAST scanning (Layer 2 enhancement) | Eng | 3h |
| 3.2.3 | Build MobSF container image for mobile scanning (Layer 3) | Eng | 4h |
| 3.2.4 | Write mobile binary upload endpoint (`POST /api/v1/scan/mobile`) | Eng | 2h |
| 3.2.5 | Integrate CloudFox for AWS cloud posture analysis (Layer 6) | Eng | 4h |
| 3.2.6 | Build compliance gap analysis engine (PCI-DSS, GDPR controls) | Eng | 8h |
| 3.2.7 | Build compliance dashboard view with control pass/fail status | Eng | 4h |

### Milestone 3.3 — Integrations & Notifications (Weeks 33–36)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 3.3.1 | Build Slack integration: send incident alerts and scan completions | Eng | 3h |
| 3.3.2 | Build email notification system (SendGrid/SES) for scan results | Eng | 2h |
| 3.3.3 | Build PDF export for executive scan reports | Eng | 4h |
| 3.3.4 | Build API key generation for SOC Enterprise tier (programmatic access) | Eng | 3h |
| 3.3.5 | Build Zapier/Make webhook endpoint for report delivery | Eng | 2h |
| 3.3.6 | Build custom playbook builder UI (drag-and-drop steps) | Eng | 8h |

### Milestone 3.4 — AI Chat Assistant (Weeks 33–36, parallel to 3.3)

The AI Chat Assistant is a conversational interface powered by Anthropic Claude, embedded in the tenant dashboard. Tenants pre-purchase credits and use them to query the AI, trigger scan actions, generate fix scripts, and produce reports through natural language. This is a paid feature — tenants must hold a credit balance to interact.

**Backend:**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 3.4.1 | Create `credits` DynamoDB table (`tenant_id`, `balance`, `reserved`, `last_topup`) | Eng | 1.5h |
| 3.4.2 | Create `credit_transactions` table (ledger: action_type, credits_deducted, timestamp) | Eng | 1h |
| 3.4.3 | Build `GET /api/v1/credits/balance` — returns current balance and reserved credits | Eng | 1h |
| 3.4.4 | Build `POST /api/v1/credits/purchase` — Stripe checkout session creation | Eng | 2h |
| 3.4.5 | Build Stripe webhook handler for `checkout.session.completed` → credit top-up | Eng | 2h |
| 3.4.6 | Build credit deduction middleware: reserve credits before action, release/confirm after | Eng | 2h |
| 3.4.7 | Build `POST /api/v1/ai/chat` endpoint: accepts `{query, context_type, domain}` | Eng | 2h |
| 3.4.8 | Implement Claude API call with system prompt (tenant context: findings, scores, domain) | Eng | 3h |
| 3.4.9 | Implement Claude extended thinking mode for security questions (budget_tokens: 8000) | Eng | 2h |
| 3.4.10 | Parse Claude response for embedded `[ACTION:type]` markers; return structured action list | Eng | 2h |
| 3.4.11 | Build `POST /api/v1/ai/action` — accepts `{action_type, params}`, deducts credits, enqueues task | Eng | 3h |
| 3.4.12 | Build action dispatcher: routes actions to L1 scan queue, L2 scan queue, compliance engine, SOAR | Eng | 3h |
| 3.4.13 | Build `GET /api/v1/ai/action/{action_id}/result` — polls for and returns action result | Eng | 1.5h |
| 3.4.14 | Build conversation history store (last 20 messages per tenant, TTL 30 days, DynamoDB) | Eng | 1.5h |
| 3.4.15 | Build rate limiter: max 10 AI queries/minute/tenant regardless of credit balance | Eng | 1h |
| 3.4.16 | Write unit tests for credit deduction, Stripe webhook, action dispatch | Eng | 3h |

**Frontend (Wireframe: `12-ai-chat.html`):**

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 3.4.17 | Build three-panel chat layout (conversation sidebar, chat area, right credit panel) | Frontend | 5h |
| 3.4.18 | Build chat message component: user bubble (right), Claude bubble (left) with avatar | Frontend | 3h |
| 3.4.19 | Build collapsible reasoning block within Claude messages | Frontend | 2h |
| 3.4.20 | Build action card component: title, credit cost badge, Run button, status (⏳→✅) | Frontend | 3h |
| 3.4.21 | Build inline result component: data table or code block with copy button | Frontend | 3h |
| 3.4.22 | Build credit balance widget (right panel): balance, progress bar, Buy More button | Frontend | 2h |
| 3.4.23 | Build Buy Credits modal: 4 bundle options, Stripe redirect on selection | Frontend | 2h |
| 3.4.24 | Build chat input area: textarea, context chips, suggestion chips, credit indicator | Frontend | 2h |
| 3.4.25 | Build conversation thread sidebar with search and new chat button | Frontend | 2h |
| 3.4.26 | Add chat FAB widget to dashboard (`02-dashboard.html`): floating button, preview panel | Frontend | 1.5h |
| 3.4.27 | Wire frontend to `/api/v1/ai/chat` — streaming response with token-by-token rendering | Frontend | 4h |
| 3.4.28 | Wire action Run button to `/api/v1/ai/action`, poll result, render inline | Frontend | 3h |
| 3.4.29 | Wire credit balance to live API with auto-refresh after each action | Frontend | 1h |

**Credit Pricing:**

| Action Type | Credits Deducted |
|---|---|
| Ask a security question | 1 |
| Show findings / reports | 1 |
| Generate remediation script | 2 |
| Approve / reject SOAR action | 2 |
| Compliance gap analysis | 3 |
| Trigger L1 recon scan | 3 |
| Cloud posture check | 4 |
| Trigger L2 VAPT scan | 5 |
| Generate board / exec report | 5 |
| Create Jira / ServiceNow ticket | 1 |

**Milestone 3 Completion Criteria:**
- [ ] 50 paying clients
- [ ] $10K MRR
- [ ] All 8 core scanning layers + L9 AI Agent functional (including L8 Malware D&R)
- [ ] Slack + email notifications live
- [ ] PDF export available
- [ ] OWASP review passed
- [ ] AI Chat Assistant live with credit purchase flow (Stripe) and action triggers

---

## Phase 4: Growth & Enterprise (Weeks 37–52)

**Goal:** **150 paying clients** (Year 1 end), ISO 27001 Stage 1, MSP channel live. Seed round closes **Month 15 (Aug 2027)** per [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) §5.2 — not a Phase 4 gate.

### Milestone 4.1 — MSP / Partner Channel (Weeks 37–40)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 4.1.1 | Build white-label dashboard (custom logo, colour overrides per tenant) | Eng | 8h |
| 4.1.2 | Build MSP reseller portal (manage multiple sub-tenants) | Eng | 12h |
| 4.1.3 | Build revenue share reporting for MSP partners | Eng | 4h |
| 4.1.4 | Onboard 3 MSP partners with signed reseller agreements | Founder | 20h |

### Milestone 4.2 — Enterprise Features (Weeks 41–44)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 4.2.1 | Implement SAML 2.0 SSO (Okta, Azure AD, Google Workspace) | Eng | 8h |
| 4.2.2 | Implement tenant sub-user RBAC — **3 fixed slots** (Support, Viewer, Manager) per FR-141–150 / wireframe `21` — not generic Admin/Analyst/Read-only | Eng | 6h |
| 4.2.3 | Build SLA monitoring and uptime reporting dashboard | Eng | 4h |
| 4.2.4 | Implement asset inventory (auto-discovered domains, IPs, cloud resources) | Eng | 8h |
| 4.2.5 | Build SOC Enterprise tier with unlimited Wazuh agents | Eng | 4h |

### Milestone 4.3 — Compliance & Certification (Weeks 45–48)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 4.3.1 | Engage ISO 27001 certification body (ISOQAR, BSI, Bureau Veritas) | Founder | 4h |
| 4.3.2 | Complete ISMS documentation (policies, risk register, controls) | Founder/Compliance | 40h |
| 4.3.3 | Complete ISO 27001 stage 1 audit | All | 8h |
| 4.3.4 | Remediate stage 1 findings | Eng/Founder | 16h |
| 4.3.5 | Complete ISO 27001 stage 2 audit | All | 8h |
| 4.3.6 | Register with ICO as data controller | Founder | 1h |
| 4.3.7 | Complete Cyber Essentials Plus certification | Eng | 8h |

### Milestone 4.4 — Observability & SRE (Weeks 49–52)

| # | Nano Step | Owner | Hours |
|---|---|---|---|
| 4.4.1 | Build **Grafana** dashboards for SRE/on-call (API latency, scan throughput, errors) — complements **Metrics Observatory** product UI (FR-170–182, Milestone 2.8); Grafana = infra ops back-end | Eng | 4h |
| 4.4.2 | Implement PagerDuty on-call rotation for production alerts | Eng | 2h |
| 4.4.3 | Build chaos engineering test suite (scan failure, API outage simulation) | Eng | 4h |
| 4.4.4 | Implement database connection pooling and query optimisation | Eng | 3h |
| 4.4.5 | Implement multi-region S3 replication for disaster recovery | Eng | 2h |
| 4.4.6 | Conduct 24-hour load test at 500 concurrent scan tasks | Eng | 8h |

---

## Phase 5: Expansion (Year 2)

**Goal:** Series A readiness, international expansion, $50K MRR, managed SOC launch.

### Milestone 5.1 — International Expansion (Q1 Year 2)

| Nano Step | Notes |
|---|---|
| Launch US region (AWS us-east-1 data residency) | Required for US customers |
| Achieve SOC 2 Type I compliance | Required for US enterprise sales |
| HIPAA-compliant scan reporting (healthcare vertical) | High-value US niche |
| Localise pricing for USD, AUD, CAD | Currency alignment |
| Partner with US cyber insurance broker network | GTM channel |

### Milestone 5.2 — Managed SOC Service (Q2 Year 2)

| Nano Step | Notes |
|---|---|
| Hire first human SOC analyst | $55K/year, EU-based |
| Build analyst dashboard (internal SOC tooling) | Separate from client dashboard |
| Define SLA tiers: 1-hour, 4-hour, 8-hour response | Premium feature |
| Launch "Managed SOC Add-on" at $799/month | Highest-margin product |
| Build automated shift handover report (Claude-generated) | Analyst productivity tool |

### Milestone 5.3 — Series A Preparation (Q3–Q4 Year 2)

| Nano Step | Notes |
|---|---|
| Reach $50K MRR milestone | Fundraising trigger |
| Compile 24-month cohort retention data | Investor metric |
| Build financial model deck (5-year projections) | Board-ready |
| Engage 3 Series A investors (Tier 1 UK/US cybersecurity VCs) | Notion Capital, Accel, Balderton |
| Prepare Series A data room (metrics, financials, cap table, contracts) | Legal + finance |

---

## Sprint Calendar Summary

| Sprint | Weeks | Phase | Key Deliverable |
|---|---|---|---|
| S0.1 | 1–2 | 0 | Terraform staging + automated QA scaffold |
| S0.2 | 3–4 | 0 | Brand assets + tooling + AWS account |
| S1.1 | 5–6 | 1 | Cognito auth API + Amplify onboarding |
| S1.2 | 7–8 | 1 | Scan execute endpoint + mock results |
| S1.3 | 9–10 | 1 | Real scanner binaries + SQS/Lambda queue |
| S1.4 | 11–12 | 1 | Claude AI integration + financial reports |
| S1.5 | 13–14 | 1 | React dashboard UI |
| S1.6 | 15–16 | 1 | E2E testing + polish + internal demo |
| S2.1 | 17–18 | 2 | Paid-tier hardening: CloudFront, WAF, EKS prep |
| S2.2 | 19–20 | 2 | Cognito hardening + auth QA |
| S2.3 | 21–22 | 2 | Stripe payments + billing portal |
| S2.4 | 23–24 | 2 | SOAR live + beta clients onboarded |
| S3.1 | 25–28 | 3 | Security review + launch prep |
| S3.2 | 29–32 | 3 | Advanced scan layers (DAST, mobile, cloud) |
| S3.3 | 33–36 | 3 | Integrations + PDF + notifications |
| S4.1 | 37–40 | 4 | MSP channel + white-label |
| S4.2 | 41–44 | 4 | Enterprise features (SSO, RBAC, assets) |
| S4.3 | 45–48 | 4 | ISO 27001 certification |
| S4.4 | 49–52 | 4 | Observability + load testing + SRE |

---

## Key Success Metrics Per Phase

| Phase | Primary KPI | Secondary KPI |
|---|---|---|
| 0 — Foundation | Terraform staging applied | `./tests/qa/` scaffold green on staging |
| 1 — AWS Staging MVP | Full E2E scan on staging with CI/CD | Claude AI returns valid JSON |
| 2 — Beta & scale | First paying client | Platform uptime >99% |
| 3 — Launch | 50 paying clients | $10K MRR |
| 4 — Growth | 150 paying clients (Year 1 end) | ISO 27001 Stage 1 complete |
| 5 — Expansion | 323 clients / $22K MRR (M18) | Series A term sheet |
