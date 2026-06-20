# SOCVault Blueprint — Gap Analysis
**Assessment date:** 18 June 2026  
**Remediation date:** 18 June 2026 (v1.17)  
**Scope:** All documents in `docs/`, `userstories-wireframes/`, `LogoAssets/`, and `BusinessProposal/`

---

## Remediation Status (v1.17 — architecture diagram suite)

| Gap | Resolution |
|---|---|
| No C4 context/container diagrams | [`diagrams/01_C4_CONTEXT_CONTAINER.md`](./diagrams/01_C4_CONTEXT_CONTAINER.md) |
| No system flow / sequence diagrams | [`diagrams/02_SYSTEM_FLOWS.md`](./diagrams/02_SYSTEM_FLOWS.md) — 10 journeys |
| DFD gaps (billing, AI chat, isolation, L2/L9) | [`diagrams/03_DATA_FLOW_EXTENDED.md`](./diagrams/03_DATA_FLOW_EXTENDED.md) |
| RBAC not visualised (3 models) | [`diagrams/04_RBAC_MAPPING.md`](./diagrams/04_RBAC_MAPPING.md) |
| No module connectivity map | [`diagrams/05_MODULE_CONNECTIVITY.md`](./diagrams/05_MODULE_CONNECTIVITY.md) |
| No L1–L9 layer reference diagrams | [`diagrams/06_SCAN_LAYERS.md`](./diagrams/06_SCAN_LAYERS.md) |
| Ops / observability not diagrammed | [`diagrams/07_OPS_AND_CICD.md`](./diagrams/07_OPS_AND_CICD.md) |
| Trust boundaries not visualised | [`diagrams/08_TRUST_AND_SECURITY.md`](./diagrams/08_TRUST_AND_SECURITY.md) |
| API surface not grouped visually | [`diagrams/09_API_SURFACE.md`](./diagrams/09_API_SURFACE.md) |
| No state machines | [`diagrams/10_STATE_MACHINES.md`](./diagrams/10_STATE_MACHINES.md) |
| Master index missing | [`diagrams/00_INDEX.md`](./diagrams/00_INDEX.md) |

**Remaining (implementation):** `socvault-app`, Terraform apply, legal counsel; render Mermaid to PNG for investor pack if needed.

---

## Remediation Status (v1.16 — investor deck re-audit)

| Gap | Resolution |
|---|---|
| Seed row ISO certified at close (P2) | **ISO in progress (cert Oct 2027)**; certification stays on M18 / Oct 2027 rows |
| `api-staging.socvault.io` absent | Ask + staging MVP success criteria cite **api-staging + app-staging** |
| 26 epics not cited | Cover strip, Ask, traction bullets → **208 stories · 26 epics** |
| Seed / Series A valuations missing | Funding table: **$750K ($3.5M pre)** · **$3M ($12M pre)** |
| Milestone table out of order | **Chronological sort** (Product Hunt before M18) |
| Month 28 without calendar date | **September 2028** on unit economics + traction timeline |
| Pre-Seed unlock 3 MSP agreements | Pre-Seed funding row + 50-client milestone criteria |

**Remaining (implementation):** `socvault-app`, Terraform apply, legal counsel; regenerate deck after blueprint changes via `update_deck.py`.

---

## Remediation Status (v1.15 — investor deck full alignment)

| Gap | Resolution |
|---|---|
| Empty “The Ask” section (§1) | **ASK_SUMMARY** paragraph + cover metrics strip (table 0) |
| USP 8 compliance body orphaned after USP 10 | Body moved under **USP 8 — Compliance as Standard** |
| Milestone table vs investor §16 drift | **Feb 2027** 50/$10K · **Aug 2027** Seed close · **M18** 323/$22K · Product Hunt · 150 clients |
| Duplicate “Seed unlock (see row above)” row | Removed |
| Revenue table missing M6/M12/M15/M18 | Snapshot rows added to Year/MRR table |
| Unit economics missing M18/M15 MRR | **MRR at M18** + **Seed close M15** rows |
| Architecture table missing MVP services | **API Gateway, SQS, DynamoDB, Atlas M0** rows |
| AWS Activate credits stale Fargate wording | **12+ months serverless MVP** |
| Executive overview milestone drift | Aligned to **Feb 2027 / M18 / M28** |

**Remaining (implementation):** `socvault-app`, Terraform apply, legal counsel; regenerate deck after blueprint changes via `update_deck.py`.

---

## Remediation Status (v1.14 — investor deck)

| Gap | Resolution |
|---|---|
| Deck “Series A deck” after Pre-Seed | **Seed deck** / **Seed round positioning** in milestones + funding rows |
| Deck production cutover wrong success criteria | **api.socvault.io + app.socvault.io** post-cutover QA |
| Deck 50 clients Dec 2026 vs investor Feb 2027 | **February 2027 (~M8)** unified with $10K MRR |
| Deck missing M18 323 / $22K | Table 25 row + break-even **EBITDA ~M18 · cash M28** |
| Deck “working product” implies built app | **Staging MVP (blueprint complete; socvault-app build next)** |
| Deck “Claude + Fargate” COGS line | **Claude + compute** |
| Deck duplicate/stale traction bullets | Removed ADR-004 “both envs live” + duplicate extension bullets |
| Deck doc 20 TI reference | **`20_FREE_EXTERNAL_APIS.md`** |
| Deck Secrets Manager / CloudFront on MVP | **SSM (MVP) · Amplify + CloudFront (paid tier)** |
| Deck Series A Month 30 drift | **Month 31 (December 2028)** aligned with investor §14.3 |

**Remaining (implementation):** `socvault-app`, Terraform apply, legal counsel; deck regenerated via `update_deck.py`.

---

## Remediation Status (v1.12)

| Gap | Resolution |
|---|---|
| Investor §12.1 “Prototype complete” with no app repo | **Blueprint complete** labels + footnote: docs-only repo; runtime in `socvault-app` TBD |
| Investor §12.1 Terraform “VPC, ECS, Cognito” | **Serverless IaC spec**: API GW, Lambda, Cognito, SQS, Amplify, DynamoDB, S3 (ADR-006) |
| Gap analysis §10 “post v1.6” header | Updated to **post v1.10 — doc-sync complete** |

**Remaining (implementation):** `socvault-app`, Terraform apply, legal counsel sign-off; regenerate investor `.docx` when needed.

---

## Remediation Status (v1.10)

| Gap | Resolution |
|---|---|
| Onboarding wireframe L1 “~8 min” vs NFR-002/002a | **`<90 sec pipeline · <3 min to report`** in `01-onboarding.html` |
| Brand break-even card “Mo 18” ambiguous | **EBITDA Mo 18 · Cash Mo 28** + 323 clients subtext |
| Brand badge “$10K MRR in 18mo” | **`~M8`** (Feb 2027 milestone; M18 = $22K) |
| Investor §14.2 “Seed Milestones” at M18 | Renamed **Post-Seed operating targets (M18)** |
| Investor Phase 3 “all 8 layers” without L9 | **8 core layers (L1–L8) + L9 parallel track** |
| README / gap analysis deck `.docx` assumed in repo | Documented: **`update_deck.py` generates locally**; not committed |
| Threat model self-scan prod-only URL | **`app-staging`** until cutover |

**Remaining (implementation):** `socvault-app`, Terraform, legal counsel sign-off; regenerate investor `.docx` when needed.

---

## Remediation Status (v1.8)

| Gap | Resolution |
|---|---|
| Investor §13.1 revenue table broken by mid-table footnote | Footnote moved below full M6–M36 table |
| M18 labeled “Seed milestone” | **Seed close = M15**; **M18 = post-Seed / EBITDA milestone** in investor §13.1 + §13.6 |
| Roadmap Milestone 2 “Platform live at app.socvault.io” | Staging primary; production after cutover checklist |
| Investor “AWS platform live” ambiguous | **Staging serving beta clients** + cutover note |
| Brand Phase 3 “7 scan layers” | **8 core layers (L1–L8)** + L9 parallel track |
| Brand Phase 2 “Cloud MVP + Beta” | **Beta & scale** aligned with roadmap |
| Executive overview “Series A deck” after pre-seed | **Seed deck ready** |
| Observatory wireframe CORS missing staging | **`app-staging` + `api-staging`**; removed localhost (ADR-006) |
| MVP spec vs roadmap L9/Observatory scope | Cross-ref note: Phase 2 milestones 2.6–2.8 outside Phase 1 spec |
| Gap analysis v1.5 FR-117/119 “remaining” | Marked resolved (v1.6 roadmap 2.8.6–2.8.7) |

**Remaining (implementation):** `socvault-app`, Terraform, legal counsel sign-off.

---

## Remediation Status (v1.6)

| Gap | Resolution |
|---|---|
| Client/MRR contradictions (150 vs 200 vs 323) | **`04_FINANCIAL_PLAN.md` authoritative**; aligned `01_BUSINESS_PLAN`, investor §8/§14/§16, roadmap Phase 4 KPIs |
| Seed close M15 vs milestones 200/$22K | Seed unlock 50/$10K ~M8; close M15; **M18 = 323/$22K** post-Seed outcomes |
| OpenAPI JWT 15-min expiry | Cognito-issued JWT + pool TTLs in `openapi.yaml` |
| Roadmap Phase 0/2 success metrics | Phase 0 = Terraform/QA; Phase 2 = Beta & scale |
| RBAC Admin/Analyst/Read-only vs 3-slot | Roadmap 4.2.2 → FR-141–150; **`02_TECHNICAL_STACK.md` §2.7** |
| Observatory vs Grafana | **`02_TECHNICAL_STACK.md` §2.8** + roadmap 4.4.1 cross-ref |
| Wireframe L1 duration 8m vs NFR-002a | Admin/observatory: **72s L1 pipeline**; 8m = L2+ |
| FR-117 / FR-119 nano steps | Roadmap 2.8.6–2.8.7 |
| Pricing tier naming drift | **`04_FINANCIAL_PLAN.md` §2.5a** mapping table |
| Phase 3 / 2.5 schedule overlap | Parallel-track note in roadmap Phase 3 |
| Deck “dual-env single account” | staging active · production dormant |

**Remaining (implementation):** `socvault-app`, Terraform, legal counsel sign-off.

---

## Remediation Status (v1.5)

| Gap | Resolution |
|---|---|
| FR-006 custom JWT issuance | Cognito-issued tokens + API Gateway authorizer (ADR-003) |
| Investor/deck “per-tenant user pools” | **One User Pool per environment** + `tenant_id` attribute |
| Executive overview Week 12 production | **Week 17+ cutover checklist** (Milestone 2.1) |
| Investor Phase 2 “Production + Beta” | **Beta & scale** aligned with roadmap |
| Explorer vault Redis session on MVP | **DynamoDB TTL** session (no Redis) |
| `06-l3-mobile.html` prod curl / wrong path | `api-staging.socvault.io/api/v1/...` |
| `19-admin.html` Redis without paid-tier label | ElastiCache labeled paid tier; MVP = DynamoDB |
| NFR-002 “2 min vs 3 min” ambiguity | Tech stack labels requirement vs stretch at scale |
| Gap analysis §5.1 / §6.3 / appendices stale | Refreshed below |
| B2B M18 channel MRR vs company M18 | Cross-linked to $22K company-wide MRR |

**Remaining (implementation):** `socvault-app` repo, Terraform, legal counsel sign-off. *(FR-117/119 resolved in v1.6 — roadmap 2.8.6–2.8.7.)*

---

## Remediation Status (v1.4)

| Gap | Resolution |
|---|---|
| Roadmap Phase 1 “promote to production” + custom JWT nano steps | **Cognito from day one** (ADR-003); staging-only until cutover; Milestone 2.2 = hardening |
| `.env.example` Redis + `DEPLOY_TARGET=ec2-docker` | Serverless vars: SQS, DynamoDB, `DEPLOY_TARGET=serverless` |
| `06_API_SPECIFICATION.md` prod-only base URL | **Staging primary**; production marked dormant |
| Investor deck Cloudflare WAF row | **`update_deck.py`** → CloudFront + AWS WAF (paid tier); docx regenerated |
| `18_API_EXPLORER_IMPLEMENTATION.md` prod curl | **`api-staging.socvault.io`** |
| Investor COGS “Fargate for all VAPT” | L1 Lambda vs L2+ Fargate/EKS clarified |
| M18 $22K MRR vs M28 cash-flow break-even | Cross-linked in investor §13.1 / §13.6 + financial plan |
| Phase naming drift (investor vs roadmap) | Unified → **Phase 1: Cloud MVP on staging** |
| Gap analysis §1.1 / §10 stale open items | Refreshed below; P1 doc-sync items closed |

**Remaining (implementation):** `socvault-app` repo, Terraform, legal counsel sign-off.

---

## Remediation Status (v1.3)

| Gap | Resolution |
|---|---|
| Build queue US-208–215 (FR/US collision) | Fixed → **US-194–200** (Dev Tracker); US-201–208 = Threat Intel |
| FR-208 + wireframe 25 old env matrix | **Blueprint \| Staging \| Production dormant**; API GW + Lambda; SQS |
| FR-120 / FR-170 / FR-174 / FR-176 Redis-on-MVP | DynamoDB + SQS on MVP; ElastiCache/Fargate paid tier |
| FR-206 / Explorer `local` profile | **`mock` \| `staging` \| `production`**; OpenAPI + wireframe 24 updated |
| Break-even Month 18 vs 28 | `04_FINANCIAL_PLAN.md` §6 labels **EBITDA M18** vs **cash-flow M28** |
| L1 duration 90s vs 3 min | **NFR-002** (user journey) + **NFR-002a** (pipeline <90s) |
| Tracker Phase 1/2 duplicate “Cloud MVP” | Phase 2 → **Beta & scale**; roadmap Phase 0 single-account wording |
| Investor appendix Cloudflare/Fargate-first | **CloudFront + AWS WAF**; serverless MVP listed first |
| Gap analysis §2.2/2.3 stale orphans | Marked resolved (dashboard tags, AI Chat FRs exist) |
| Postman default localhost | Default → **api-staging** |
| Metrics observatory US/FR subtitles | Aligned (US+4 → FR pattern); Claude card FR-172 |

**Remaining (implementation):** `socvault-app` repo, Terraform, legal counsel sign-off.

---

## Remediation Status (v1.2)

The following gaps from v1.0/v1.1 have been **addressed** (see also v1.1 table below):

| Gap | Resolution |
|---|---|
| Stale architecture (ALB, Celery/Redis, EC2 Docker, Vercel) | **ADR-006** serverless staging MVP synced across docs, deck, wireframes, threat model |
| Threat model boundary outdated | `14_THREAT_MODEL.md` v1.1 — API GW + Lambda + SQS + Atlas |
| Expense ledger “local dev” / Fargate-first costs | `08_THREE_YEAR_EXPENSES_LEDGER.md` — serverless M1–M3, paid tier from M4 |
| Business plan §10 Docker Compose | Updated to serverless MVP + paid-tier path |
| User story count drift (194 vs 208) | Tracker + index + deck aligned to **208** |
| Freemium gate “30 days” in roadmap | **1 calendar month** (FR-026) in roadmap + build queue |
| Build queue US-009–020 collapsed | `23_MVP_BUILD_ORDER_AND_QA.md` — individual rows |
| API README localhost-only | Staging URL primary; localhost optional |
| Investor deck Celery + Redis row | `update_deck.py` + regenerated docx |
| Metrics index “Fargate compute” | Updated to Lambda compute (observatory shows paid-tier workers at scale) |

**Remaining (implementation repo / counsel):** Production OpenAPI completion, legal text sign-off, application source code, Terraform modules.

---

## Remediation Status (v1.1)

The following P0/P1 gaps from the initial assessment have been **addressed**:

| Gap | Resolution |
|---|---|
| User story spreadsheet ends at US-120 | Extended to **US-208** (208 stories, 26 epics) in xlsx |
| AI Chat missing FRs | Added FR-183–193 in `03_REQUIREMENTS.md` |
| Duplicate FR-080/081 | Dashboard renumbered to FR-090–099 |
| L1 rate limit conflict | Freemium = 1/month (FR-026); paid L1 = 2/week (FR-110) |
| Financial contradictions | Executive/README aligned to 97.6% margin, $0.36 COGS |
| Missing docs 06, 13–16 | API spec, test strategy, threat model, legal, traceability added |
| Missing ADRs, README, CONTRIBUTING | Added at repo root and `docs/adr/` |
| Wireframes without story refs | Dashboard, AI Chat, orphans patched; 0 unwired stories |
| Roadmap missing L9/teams/observatory | Milestones 2.6–2.8 added |
| Tech stack outdated | L8/L9, APIs, data models, DynamoDB credits updated |
| No AWS bootstrap / Free Tier guide | **`docs/AWS_SETUP_README.md`** + `02_TECHNICAL_STACK.md` §6.1; roadmap 2.1 split Free Tier / paid |
| No live product/infra status tracker | **`DEVELOPMENT_TRACKER.md`** |
| AWS-only staging + production CI/CD | **`19_CI_CD_AND_ENVIRONMENTS.md`** + ADR-004 (one Free Tier account) |
| Investor deck aligned to blueprint | **`BusinessProposal/update_deck.py`** → generates `SOCVault-Investor-Partner-Deck.docx` locally (not committed); 97.6% margin, AWS-only milestones, Threat Intel registry |
| Threat intel API registry | **`docs/20_FREE_EXTERNAL_APIS.md`** + FR-216–229 + US-201–208 + OpenAPI `/admin/ti/feeds` |
| MVP functional spec + DFDs | **`docs/21_MVP_FUNCTIONAL_SPEC.md`** + **`docs/22_DATA_FLOW_DIAGRAMS.md`** |
| Serverless staging-first architecture | **ADR-006** + **`docs/23_MVP_BUILD_ORDER_AND_QA.md`** + automated QA (`tests/qa/`) |
| Architecture doc sync (June 2026) | ADR-004/005 amended; tech stack, roadmap, investor plan, financial plan aligned |

**Remaining (implementation repo / counsel):** Production OpenAPI completion, legal text sign-off, application source code, Terraform modules.

---

## Executive Summary (current — June 2026)

SOCVault-Blueprint is investor-ready: **208 user stories**, **25 wireframes**, OpenAPI MVP, serverless staging architecture (ADR-006), automated QA scripts, and aligned financial/investor materials.

| Area | Status |
|---|---|
| Core business & investor narrative | Strong |
| L1–L9 scanning specification | Strong |
| User story spreadsheet (`US-001`–`US-208`) | Complete |
| Threat intel feed registry | **Added** — [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md), FR-216–229, US-201–208 |
| Wireframes (25 pages) + Super Admin tools | Present |
| Requirements ↔ wireframes ↔ xlsx alignment | **Reconciled** (v1.1+) |
| Architecture (MVP serverless staging) | **ADR-006** synced (v1.6) |
| Cross-document financial & product facts | **Aligned** — 97.6% VAPT margin, $0.36 COGS |
| Engineering artefacts (API spec, ADRs, tests, legal) | **Added** (MVP OpenAPI, ADRs 001–006, QA in `tests/qa/`) |

**Bottom line:** Remaining work is **application implementation** (`socvault-app`), Terraform provisioning, and legal counsel sign-off.

---

## Executive Summary (original assessment — historical)

SOCVault-Blueprint is a strong foundation: business narrative, technical direction, 120 structured user stories, 23 HTML wireframes, and financial/channel planning are largely in place *(historical baseline — now **208 stories / 25 wireframes**)*. The main gaps are **synchronisation** and **coverage of newer features** added after the original 120-story baseline.

| Area | Status |
|---|---|
| Core business & investor narrative | Strong |
| L1–L8 scanning specification | Strong |
| User story spreadsheet (`US-001`–`US-208`) | Complete |
| Threat intel feed registry | **Added** — [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md), FR-216–229, US-201–208 |
| Wireframes for L9, AI Chat, Teams, Metrics Observatory, Admin tools | Present |
| Requirements ↔ wireframes ↔ xlsx alignment | **Reconciled** (v1.1) |
| Product roadmap for new features (L9, teams, observatory) | **Added** (Milestones 2.6–2.10) |
| Cross-document financial & product facts | **Aligned** — 97.6% VAPT margin, $0.36 COGS |
| Engineering artefacts (API spec, ADRs, tests, legal) | **Added** (MVP OpenAPI, ADRs, outlines) |

**Bottom line:** The blueprint is investor-ready and aligned across docs, wireframes, and the investor deck. Remaining work is application implementation and legal counsel sign-off.

---

## 1. Documentation Inventory Gaps

### 1.1 Missing or placeholder artefacts — **largely resolved (v1.4)**

| Expected artefact | Referenced in | Status |
|---|---|---|
| `docs/06_API_SPECIFICATION.md` | Doc index | **Added** — staging base URL primary |
| Root `README.md` | Standard repo convention | Missing — only `docs/README.md` exists (blueprint repo) |
| Architecture Decision Records (ADRs) | `05_PRODUCT_ROADMAP.md` Phase 0 | **Added** — `docs/adr/001`–`006` |
| `CONTRIBUTING.md`, `.env.example` | Roadmap Phase 0 | **Added** at repo root (serverless template; no runtime secrets) |
| OpenAPI / API contract (beyond endpoint list) | `02_TECHNICAL_STACK.md` | **Added** — `api/openapi.yaml` + Bruno/Postman |
| Privacy Policy, Terms of Service, DPA | Roadmap Milestone 3.1 | Outline in `15_LEGAL_TEMPLATES.md`; counsel sign-off pending |
| Test strategy / QA plan | MVP acceptance criteria | **Added** — `13_TEST_STRATEGY.md` + `tests/qa/` |
| Threat model / security architecture doc | NFR-029 OWASP review | **Added** — `14_THREAT_MODEL.md` v1.1 (ADR-006) |
| Traceability matrix (FR ↔ US ↔ wireframe) | Implied by structure | **Added** — `16_TRACEABILITY_MATRIX.md` |

### 1.2 Undocumented in index

| Asset | Location | Gap |
|---|---|---|
| Investor deck (`.docx`) | `BusinessProposal/update_deck.py` | **Resolved (v1.10)** — `.docx` generated locally; script committed; output not in git |
| Wireframes `20`–`25` | `userstories-wireframes/` | **Resolved (v1.1+)** — listed in `00-index.html` and `docs/README.md` |
| Logo asset path | `docs/README.md` references `../SOCVault Logo.png` | File lives in `LogoAssets/SOCVault Logo.png` — broken relative path from `docs/` |

### 1.3 Index metadata — **resolved (v1.1)**

`userstories-wireframes/00-index.html` now states **25 wireframes covering 208 user stories** across 26 epics, matching `SOCVault-User-Stories.xlsx` and [`16_TRACEABILITY_MATRIX.md`](./16_TRACEABILITY_MATRIX.md).

---

## 2. User Story & Wireframe Gaps

### 2.1 Spreadsheet vs wireframe drift — **resolved (v1.1)**

Spreadsheet and wireframes both cover **US-001 … US-208**. See [`16_TRACEABILITY_MATRIX.md`](./16_TRACEABILITY_MATRIX.md) for the authoritative map.

<details>
<summary>Original finding (June 2026 — superseded)</summary>

```
Spreadsheet (SOCVault-User-Stories.xlsx)     Wireframes (HTML)
────────────────────────────────────────     ───────────────────
US-001 … US-120  (120 stories, 18 epics)     US-130 … US-180 referenced
                                             but NOT in spreadsheet
```
</details>

### 2.2 Stories in spreadsheet without wireframe tags — **resolved (v1.1)**

Dashboard and related wireframes now include `story-ref` tags (e.g. `02-dashboard.html`: US-066–071, 111, 119). Re-run traceability before each sprint for new stories.

<details>
<summary>Original finding (June 2026 — superseded)</summary>

| Story ID | Epic | Gap |
|---|---|---|
| US-060 | AI Risk Translation | No wireframe `story-ref` |
| US-066 | Dashboard & Reporting | No wireframe `story-ref` |
| … | … | … |

`02-dashboard.html` — the natural home for US-066/068/069/070/071/111 — contained **zero** `story-ref` tags.
</details>

### 2.3 Features with wireframes but no user stories — **resolved (v1.1)**

AI Chat: **FR-183–193**, **US-121–129**, wireframe `12-ai-chat.html`. Credit ledger covered in billing FRs + roadmap 3.4.

<details>
<summary>Original finding (June 2026 — superseded)</summary>

| Feature | Wireframe | FR coverage | US coverage |
|---|---|---|---|
| **AI Chat Assistant** | `12-ai-chat.html` | **None** | **None** |
</details>

### 2.4 Epics missing from spreadsheet — **resolved (v1.1)**

L9, AI Chat, tenant teams, internal RBAC, Metrics Observatory, Threat Intel, and Super Admin epics are in xlsx through **US-208**.

### 2.5 Wireframe numbering inconsistencies

`00-index.html` card labels do not match filenames:

| Card label | Actual file |
|---|---|
| "12 — SOAR & Playbooks" | `13-soar.html` |
| "13 — Billing" | `14-billing.html` |
| "14 — MSP Portal" | `15-msp-portal.html` |
| "15 — Notifications" | `16-notifications.html` |
| "16 — Settings" | `17-settings.html` |
| "17 — Audit Log" | `18-audit-log.html` |

Files `20`–`23` are in the sidebar and grid but were added after the original numbering scheme — contributing to index confusion.

### 2.6 US/FR ID cross-reference in wireframes — **resolved (v1.3)**

Metrics Observatory cards use **US-166…185** mapped to **FR-170…182** (consistent +4 offset). Dev Tracker uses **US-194–200** ↔ **FR-208–215**. Build queue must not conflate FR IDs with US IDs (see v1.3 remediation).

---

## 3. Requirements Specification Gaps

### 3.1 Structural issues in `03_REQUIREMENTS.md`

| Issue | Detail |
|---|---|
| **Section order** | Sections numbered 1.7 (L8) before 1.5 (Dashboard) and 1.6 (Billing) |
| **Duplicate FR IDs** | `FR-080`/`FR-081` used for both L8 malware notifications **and** dashboard display |
| **Duplicate L2 requirement** | `FR-020` and `FR-021` are near-identical Web AppSec entries |
| **FR numbering collision** | Rate-limiting block uses `FR-110`–`FR-120`; billing already uses `FR-100`–`FR-106`; L9 uses `FR-125`–`FR-135`; teams use `FR-140`–`FR-166`; observatory uses `FR-170`–`FR-182` — gaps and overlaps make traceability fragile |

### 3.2 Missing requirement sections

| Capability | Documented elsewhere | In `03_REQUIREMENTS.md`? |
|---|---|---|
| AI Chat Assistant (credits, actions, streaming) | Roadmap 3.4, financial plan, wireframe | **No** |
| Domain verification (DNS TXT / meta tag) | US-003, onboarding wireframe | Only `FR-010` (high level); no step-by-step FRs |
| Wazuh agent deployment UX | US-041+, L7 wireframe | No dedicated FRs for agent install/onboarding |
| PDF executive report export | FR-085, wireframe | Requirement exists; no format/schema spec |
| White-label / MSP branding | FR-087, MSP wireframe | Minimal — no data model for brand overrides |
| WebSocket real-time updates | `02_TECHNICAL_STACK.md` async flow | Mentioned once; no FR/NFR |
| OpenAPI spec upload (L4) | `07-l4-api.html` wireframe | No FR for spec ingestion/parsing |
| CI/CD mobile scan trigger | US-116 wireframe | No FR |
| Azure/GCP cloud tabs | US-112 wireframe tab | L6 FR-025 is AWS-focused; multi-cloud not specified |
| False-positive management | US-109, L7 wireframe | No FR |
| Data residency selector | US-120, settings wireframe | NFR-041 (London only); no multi-region FR |

### 3.3 Conflicting rate limits — **resolved (v1.1)**

Authoritative rule: **1 L1 Recon scan per calendar month** for freemium (`FR-026`). Paid L1 uses rolling limits in `FR-110`+. Roadmap step 1.6.6 and MVP checklist aligned.

### 3.4 Layer count inconsistency (8 vs 9)

| Document | Layers described |
|---|---|
| `00_EXECUTIVE_OVERVIEW.md`, `10_USP_COMPETITIVE_ANALYSIS.md`, `docs/README.md` | **8 layers** (L1–L8) |
| `03_REQUIREMENTS.md` section 1.9 | **L9** AI Agent Scan added |
| Wireframes | L1–L9 present |
| `05_PRODUCT_ROADMAP.md` Phase 3 completion | "All **8** scanning layers functional" |
| `02_TECHNICAL_STACK.md` architecture diagram | "L1–L7 Scanners" only |
| MongoDB `scans.layer` enum in tech stack | `RECON…SOC` — **no L8, L9, MALWARE** |

---

## 4. Technical Architecture Gaps

### 4.1 `02_TECHNICAL_STACK.md` — **resolved for MVP (v1.3+); scale items remain**

| Topic | Status |
|---|---|
| Architecture diagram | **Updated** — L8/L9, API GW + Lambda, SQS |
| API endpoints | MVP + admin stubs in OpenAPI; post-MVP routes documented in FRs |
| Data model | Core collections documented; credits/teams in FRs + roadmap milestones |
| DynamoDB usage | Cost telemetry + rate limits on MVP; credits at paid tier |
| Auth model | Cognito + RBAC in ADR-003 and requirements |
| Celery vs SQS | **Resolved** — SQS + Lambda (ADR-006); Celery on EKS at paid tier |

<details>
<summary>Original gap list (June 2026 — historical)</summary>

| Topic | Gap |
|---|---|
| Architecture diagram | Shows L1–L7 only; omits L8 MDRM and L9 |
| API endpoints | Missing: `/malware/*`, `/ai/chat`, … |
| … | … |

</details>

### 4.2 Tooling inconsistencies

| Tool | Listed in | Missing from |
|---|---|---|
| Spiderfoot | `00_EXECUTIVE_OVERVIEW.md` L1 tools | L1 15-step table in tech stack and requirements |
| GreyNoise, Shodan | Tech stack threat intel | Requirements FR-061 (only AbuseIPDB, OTX) |
| `claude-opus-4-8` | L9 FR-129 | Tech stack model IDs (only sonnet + haiku) |
| Step Functions | Infrastructure section | Roadmap scan orchestration (SQS + Lambda on MVP; Step Functions optional at scale) |

### 4.3 Performance target conflicts

| Metric | `03_REQUIREMENTS.md` | `02_TECHNICAL_STACK.md` / Roadmap |
|---|---|---|
| L1 recon duration | **< 90s pipeline** (NFR-002a); **< 3 min user journey** (NFR-002) | **Resolved** — both documented |
| Freemium gate period | 1 month (FR-026) | **Resolved** — calendar month everywhere |

---

## 5. Product Roadmap Gaps

### 5.1 Roadmap coverage — **resolved for major features (v1.5)**

| Feature | Roadmap | Notes |
|---|---|---|
| L9 AI Agent Scan | Milestone **2.6** (Weeks 27–28) | Wireframe `20`, FR-129+ |
| Tenant sub-user management | Milestone **2.7** | Wireframe `21`, FR-141+ |
| Internal 12-role RBAC | Milestone **2.8** | Wireframe `22` |
| Metrics Observatory | Milestone **2.8** | Wireframe `23`, FR-170–182 |
| Rate-limit countdown UI (FR-117) | Milestone **2.8.6** | FR + wireframe |
| Superadmin rate-limit override (FR-119) | Milestone **2.8.7** | FR + audit log |

<details>
<summary>Original finding (June 2026 — superseded)</summary>

These had wireframes + FRs but zero roadmap entries — fixed in v1.1 Milestones 2.6–2.8.

</details>

### 5.2 Timeline overlaps — **acknowledged (v1.6)**

Milestone **2.5 (L8, Weeks 25–26)** overlaps Phase **3** launch prep (Weeks 25–28). Roadmap Phase 3 intro documents **parallel engineering + GTM tracks** — not a doc error; staffing must cover both.

### 5.3 Observability split — **resolved (v1.6)**

See [`02_TECHNICAL_STACK.md`](./02_TECHNICAL_STACK.md) §2.8: **Metrics Observatory** (product UI, Milestone 2.8) vs **Grafana** (SRE/on-call, Milestone 4.4).

### 5.4 Enterprise RBAC duplication — **resolved (v1.6)**

See [`02_TECHNICAL_STACK.md`](./02_TECHNICAL_STACK.md) §2.7: tenant 3-slot sub-users, 12 internal roles, Enterprise SAML — three scopes; roadmap 4.2.2 aligned to FR-141–150.

<details>
<summary>Original §5.2–5.4 findings (June 2026 — historical)</summary>

- L8 vs launch prep double-booked
- Observatory vs Grafana unexplained
- Three RBAC models without design doc

</details>

---

## 6. Business & Financial Gaps

### 6.1 Unit economics (resolved)

| Metric | Authoritative value | Notes |
|---|---|---|
| VAPT scan COGS | **~$0.36** | Claude ~$0.27 + compute (~$0.009 Lambda L1 / ~$0.035 Fargate L2+) — `04_FINANCIAL_PLAN.md` |
| Gross margin (VAPT) | **97.6%** | $15.00 revenue − $0.36 COGS |
| L1 Recon COGS | **~$0.20** | Includes Claude report generation |
| Malware incident COGS | **~$0.052** | L8 only — not VAPT |
| Break-even (cash-flow) | **Month 28** | Cumulative cash-flow per `08_THREE_YEAR_EXPENSES_LEDGER.md` |
| EBITDA positive | **~Month 18** | Operating P&L; cross-linked in investor §13.6 |
| Year 1 paying clients | **150** | EoY target per `04_FINANCIAL_PLAN.md` |

Investor deck (`.docx`), executive overview, README, and financial plan are now aligned.

### 6.2 Pricing tier naming — **mapped (v1.6)**

See [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) §2.5a — marketing names (SOC Pro, etc.) ↔ MongoDB `payment_tier` enum.

<details>
<summary>Original drift table (June 2026 — historical)</summary>

| Concept | Variants used across docs |
|---|---|
| Paid scan tiers | "Web VAPT", "STARTER", … |
| Top tier | "SOC Pro" ($199), "ENTERPRISE" ($499) |

</details>

### 6.3 AI Chat — **FRs added (v1.1); scheduling gap remains**

AI Chat credits have unit economics in `04_FINANCIAL_PLAN.md` and **FR-183–193** in `03_REQUIREMENTS.md` (wireframe `12-ai-chat.html`, US-121–129).

| Item | Status |
|---|---|
| Functional requirements | **Added** — FR-183–193 |
| Wireframe + user stories | US-121–129 in xlsx |
| Roadmap nano steps | Phase 3+ (post-MVP launch features) |
| Sprint plan in xlsx | May need explicit AI Chat rows before Phase 3 |

<details>
<summary>Original finding (June 2026 — superseded)</summary>

Previously no FRs for metering, purchase, or action flows — addressed in v1.1.

</details>

---

## 7. Go-to-Market & Channel Gaps

`11_B2B_CHANNEL_STRATEGY.md` is detailed but disconnected from product readiness:

| Channel promise | Product gap |
|---|---|
| AWS/Azure/GCP Marketplace metering | No FRs for marketplace billing integration |
| Hosting provider plugins (GoDaddy, Fasthosts, etc.) | No integration specs or wireframes |
| MSP revenue share reporting | Wireframe exists; no API/data model for rev-share |
| Cyber insurance partnerships | Strategy only — no data exchange format |
| Domain registrar one-click scan | US-003 domain verify exists; no registrar API spec |

Channel revenue projections (50% by Year 3) assume capabilities with no engineering backlog items.

---

## 8. Compliance & Legal Gaps

| Item | Status |
|---|---|
| UK GDPR DPA template | Referenced; not in repo |
| ICO registration | Roadmap task only |
| ISO 27001 ISMS docs | Roadmap Phase 4.3; not started |
| Scan authorisation legal text | FR-028/FR-045; no copy in wireframes |
| Cyber Essentials Plus | Roadmap mention only |
| Right to erasure | FR in roadmap; no UX wireframe |
| Audit log tamper-evidence | US-089–091; no technical design (hash chain, WORM storage, etc.) |
| 12-month audit retention | NFR-043; conflicts with GDPR erasure — no retention policy doc |

---

## 9. MVP Definition Gaps — **partially addressed**

`03_REQUIREMENTS.md` MVP checklist covers Phase 1; post-MVP boundaries are in roadmap Phase 2+ and [`21_MVP_FUNCTIONAL_SPEC.md`](./21_MVP_FUNCTIONAL_SPEC.md).

| Item | Status |
|---|---|
| Domain ownership verification | Phase 1.2 in MVP spec; wireframe present |
| Stripe / paid tier gating | Phase 2 roadmap |
| SOAR / L7 / L8 | Phase 2+ (documented as post-MVP) |
| L9, AI Chat, teams, observatory | Phase 2 milestones 2.6–2.10 |
| Rate limit countdown UI | FR + wireframe; build in Phase 2 |
| Multi-user tenant access | FR + wireframe 21; Phase 2 |

<details>
<summary>Original open checklist (June 2026 — historical)</summary>

- [ ] Domain ownership verification …
- [ ] Stripe / paid tier gating …
- …

</details>

---

## 10. Recommended Remediation (Priority Order)

> **Doc-sync status (v1.12):** Cross-document architecture, financial, and product facts are **aligned**. Remaining work is **implementation and counsel**, not blueprint reconciliation.

### Open items (post v1.10 — implementation only)

1. **Legal templates** — counsel sign-off on `15_LEGAL_TEMPLATES.md`.
2. **Application implementation** — `socvault-app`, Terraform modules, staging provisioning.
3. **B2B channel engineering** — marketplace/MSP integration FRs (strategy-only until Phase 3+).

### Completed (historical P0/P1 — do not re-open)

<details>
<summary>P0/P1 items resolved in v1.1–v1.6</summary>

1. ~~Reconcile L1 freemium rate limit~~ → FR-026 calendar month.
2. ~~Fix duplicate FR IDs FR-080/081~~ → renumbered.
3. ~~Extend user story spreadsheet~~ → US-208.
4. ~~Add AI Chat FRs~~ → FR-183–193.
5. ~~Align financial figures~~ → 97.6% / $0.36 / break-even labels.
6. ~~Roadmap custom JWT / promote-to-prod wording~~ → Cognito day one; staging until cutover (v1.4).
7. ~~`.env.example` Redis/EC2~~ → serverless template (v1.4).
8. ~~API spec staging URL~~ → `06_API_SPECIFICATION.md` (v1.4).
9. ~~Investor deck Cloudflare WAF~~ → CloudFront + AWS WAF (v1.4).
10. ~~FR-006 / Cognito pool model / exec overview production date~~ → v1.5.
11. ~~Explorer vault Redis~~ → DynamoDB TTL (v1.5).
12. ~~Wireframe prod URLs / admin Redis labels~~ → v1.5.
13. ~~Client count / Seed / M18 financial drift~~ → v1.6 (`04_FINANCIAL_PLAN` canonical).
14. ~~OpenAPI JWT expiry~~ → Cognito (v1.6).
15. ~~RBAC / Observatory / FR-117/119 / tier naming~~ → v1.6.
16. ~~Update roadmap nano steps for L9, teams, observatory~~ → Milestones 2.6–2.10 (v1.1).
17. ~~Tech stack L8/L9, APIs, data models~~ → synced (v1.2–v1.3).
18. ~~Wireframe story-ref tags~~ → patched ACT-010.
19. ~~Traceability matrix~~ → `16_TRACEABILITY_MATRIX.md`.

</details>

### P2 — Needed before launch

11. Privacy Policy, Terms of Service, DPA templates (counsel).
12. Production OpenAPI completion beyond MVP stubs.
13. Threat model review at SOAR auto-remediation go-live.
14. Resolve Metrics Observatory vs Grafana scope (product decision).

### P3 — Channel & scale

17. Marketplace metering FRs and integration spikes.
18. MSP rev-share data model and API.
19. Multi-cloud L6 requirements (Azure/GCP) beyond wireframe tabs.

---

## Appendix A — Document Coverage Matrix (June 2026 — post v1.5)

| Area | Executive | Business | Tech | Requirements | Roadmap | Financial | Wireframe | Xlsx |
|---|---|---|---|---|---|---|---|---|
| Onboarding | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| L1 Recon | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| L2–L6 scans | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| L7 SOC | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| L8 Malware | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| L9 AI Agent | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| AI Chat | ✅ | ✅ | ✅ | ✅ | ⚠️ Phase 3+ | ✅ | ✅ | ✅ |
| Tenant teams | — | — | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| Internal RBAC | — | — | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| Metrics Observatory | — | — | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| MSP portal | ✅ | ✅ | — | ⚠️ | ✅ | — | ✅ | ✅ |
| B2B channels | — | ✅ | — | ⚠️ | ⚠️ | ✅ | — | — |

Legend: ✅ documented · ⚠️ partial / post-MVP scheduling · — not primary for that doc type

---

## Appendix B — Story ID hygiene

**Authoritative map:** [`16_TRACEABILITY_MATRIX.md`](./16_TRACEABILITY_MATRIX.md) — run before each sprint.

**Historical orphan list (pre v1.1):** US-060, 066, 068–071, 105, 111, 113, 114 — patched in ACT-010; re-verify via traceability matrix.

**Build queue ID rule:** Dev Tracker = **US-194–200** (not US-208–215); Threat Intel = **US-201–208**.

---

*This gap analysis should be re-run after each major blueprint revision. Recommended owner: Product/Founder, with engineering review of P0 technical conflicts.*
