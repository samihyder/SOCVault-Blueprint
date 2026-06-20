# SOCVault — Blueprint Documentation Index
**Version 1.5 | June 2026** — ADR-006 serverless staging MVP (v1.6 financial + RBAC sync)

---

## Brand

| Asset | Value |
|---|---|
| Primary (Forest Green) | `#1B3D35` |
| Accent (Lime Green) | `#4CC844` |
| Background | `#FFFFFF` |
| Logo | [`../LogoAssets/SOCVault Logo.png`](../LogoAssets/SOCVault%20Logo.png) |

---

## Documents

| # | Document | Description |
|---|---|---|
| 00 | [Executive Overview](./00_EXECUTIVE_OVERVIEW.md) | One-pager: problem, solution, market, model, ask |
| 01 | [Business Plan](./01_BUSINESS_PLAN.md) | Full GTM, competitive analysis, ops plan, risk register |
| 02 | [Technical Stack](./02_TECHNICAL_STACK.md) | Architecture, infrastructure, API design, data model |
| 03 | [Requirements](./03_REQUIREMENTS.md) | Functional/non-functional requirements, MVP criteria |
| 04 | [Financial Plan](./04_FINANCIAL_PLAN.md) | Unit economics, projections, funding, break-even analysis |
| 05 | [Product Roadmap](./05_PRODUCT_ROADMAP.md) | 5 phases, sprints, nano steps with hour estimates |
| 06 | [API Specification](./06_API_SPECIFICATION.md) | REST catalogue + [`../api/openapi.yaml`](../api/openapi.yaml) + [collections](../collections/README.md) |
| 07 | [Branded Overview (HTML)](./07_BRAND_OVERVIEW.html) | Visual one-pager — open in browser |
| 08 | [Three-Year Expenses Ledger](./08_THREE_YEAR_EXPENSES_LEDGER.md) | Monthly OPEX M1–M36, cash flow |
| 09 | [Investor Business Plan](./09_INVESTOR_BUSINESS_PLAN.md) | Complete VC-ready business plan |
| 10 | [USP & Competitive Analysis](./10_USP_COMPETITIVE_ANALYSIS.md) | 10 USPs vs SMB competitors |
| 11 | [B2B Channel Strategy](./11_B2B_CHANNEL_STRATEGY.md) | Marketplace, MSP, hosting, insurer channels |
| 12 | [Gap Analysis](./12_GAP_ANALYSIS.md) | Documentation gap assessment |
| 13 | [Test Strategy](./13_TEST_STRATEGY.md) | QA plan mapped to MVP and phase gates |
| 14 | [Threat Model](./14_THREAT_MODEL.md) | STRIDE threat catalogue |
| 15 | [Legal Templates](./15_LEGAL_TEMPLATES.md) | Privacy, ToS, DPA outlines for counsel |
| 16 | [Traceability Matrix](./16_TRACEABILITY_MATRIX.md) | US ↔ wireframe mapping |
| 17 | [**AWS Setup Guide (MVP)**](./AWS_SETUP_README.md) | **Free Tier bootstrap, service settings, free → paid migration** |
| 18 | [API Explorer Implementation](./18_API_EXPLORER_IMPLEMENTATION.md) | Milestone 2.9 build order |
| 19 | [**CI/CD & Environments**](./19_CI_CD_AND_ENVIRONMENTS.md) | **Staging-first MVP · serverless · IaC · GitHub Actions** |
| 23 | [**MVP Build Order & QA**](./23_MVP_BUILD_ORDER_AND_QA.md) | **User story queue · API-first · automated staging QA** |
| 20 | [**Free External API Registry**](./20_FREE_EXTERNAL_APIS.md) | **Per-layer threat intel, CVE, IOC feeds · Super Admin config · correlation** |
| 21 | [**MVP Functional Spec**](./21_MVP_FUNCTIONAL_SPEC.md) | **Implementation-facing MVP behaviour (Phase 0–1, 2.9, 2.11)** |
| 22 | [**Data Flow Diagrams**](./22_DATA_FLOW_DIAGRAMS.md) | **DFD Level 0/1 — auth, scan, TI, SOAR, CI/CD (Mermaid)** |
| — | [**Architecture Diagram Suite**](./diagrams/00_INDEX.md) | **C4 · system flows · RBAC · modules · layers · ops · trust · API · states** |
| — | [**Development Tracker**](../DEVELOPMENT_TRACKER.md) | Live stack status · action log |
| — | [ADRs](./adr/) | Architecture decision records |
| — | [`../BusinessProposal/`](../BusinessProposal/) | Investor deck generator (`update_deck.py`); `.docx` generated locally, not committed |

---

## UI Wireframes & User Stories

Located in [`../userstories-wireframes/`](../userstories-wireframes/)

| File | Page | User Stories |
|---|---|---|
| `SOCVault-User-Stories.xlsx` | Backlog | **208 stories**, 26 epics, sprint plan |
| `00-index.html` | Wireframe Index | Navigation hub |
| `01-onboarding.html` | Onboarding | US-001–007 |
| `02-dashboard.html` | Main Dashboard | US-066–071, 111, 119 |
| `03-l1-recon.html` | L1 Recon | US-008–017, 099, 113, 119 |
| `04-l1-report.html` | L1 Report | US-018–020, 055–059, 060, 067, 114 |
| `05-l2-web.html` | L2 Web AppSec | US-021–026, 103 |
| `06-l3-mobile.html` | L3 Mobile | US-027–029, 116 |
| `07-l4-api.html` | L4 API Security | US-030–032 |
| `08-l5-compliance.html` | L5 Compliance | US-033–036, 105, 115 |
| `09-l6-cloud.html` | L6 Cloud | US-037–040, 112 |
| `10-l7-soc.html` | L7 SOC/SIEM | US-041–045, 109 |
| `11-l8-malware.html` | L8 Malware D&R | US-046–054, 106 |
| `12-ai-chat.html` | AI Chat Assistant | US-121–129 |
| `13-soar.html` | SOAR Engine | US-061–065, 098, 101, 108, 118 |
| `14-billing.html` | Billing | US-072–076, 100 |
| `15-msp-portal.html` | MSP Portal | US-077–080, 102, 107 |
| `16-notifications.html` | Notifications | US-081–084, 098 |
| `17-settings.html` | Settings | US-085–088, 097, 104, 120 |
| `18-audit-log.html` | Audit Log | US-089–091 |
| `19-admin.html` | Admin Console | US-092–096, 110, 117 |
| `20-l9-ai-scan.html` | L9 AI Agent Scan | US-130–140 |
| `21-tenant-teams.html` | Tenant Teams | US-141–150 |
| `22-socvault-team-admin.html` | Internal Team Admin | US-151–165 |
| `23-metrics-observatory.html` | Metrics Observatory | US-166–185 |
| `24-admin-api-explorer.html` | API Explorer, Pass & Keys & TI Feeds | US-186–208 |
| `25-admin-dev-tracker.html` | Development Tracker | US-194–200 |

---

## Quick Reference

**Key numbers (authoritative: `04_FINANCIAL_PLAN.md`):**
- COGS per VAPT scan: ~**$0.36** (with prompt caching)
- Revenue per VAPT scan: $15.00
- Gross margin (VAPT): **97.6%**
- Cash-flow break-even: **Month 28** (three-year ledger)
- LTV:CAC Year 1: **12:1**

**AI provider:** Anthropic Claude — `claude-sonnet-4-6` (reasoning), `claude-haiku-4-5-20251001` (triage), `claude-opus-4-8` (L9 agent). Prompt caching on all system prompts.

**Scanning layers:** **8 core layers** (L1–L8) + **L9 AI Agent Scan** (SOC Pro). L1 = 15-step passive recon in <90s (Lambda). L8 = Wazuh ClamAV/FIM + L2 webshell triggers.
