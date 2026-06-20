# SOCVault — Business Plan
**Version 1.0 | June 2026**

---

## 1. Company Overview

**Company Name:** SOCVault Ltd  
**Positioning:** The Unified AI-Enabled Cybersecurity Solution  
**Tagline:** One Platform. Eight Layers. AI-Enabled.  
**Sector:** B2B SaaS / Cybersecurity / AI  
**Stage:** Pre-Revenue / MVP Development  
**Headquarters:** UK (England & Wales)  
**Brand Colors:** Forest Green `#1B3D35` | Lime Green `#4CC844` | White `#FFFFFF`

---

## 2. Mission & Vision

**Positioning:** SOCVault is the unified AI-enabled cybersecurity solution for SMBs — one platform that covers the complete attack surface, replaces fragmented point solutions, and translates every finding into actionable financial risk intelligence. Where competitors offer one or two layers of protection, SOCVault unifies all eight.

**Mission:** Make enterprise-grade cybersecurity accessible to every business through unified AI-enabled automation — removing the barriers of cost, complexity, and talent that leave SMBs exposed.

**Vision:** To become the default security operations centre for the global SMB market — the single platform where any business can understand its full risk exposure, meet compliance obligations, and respond to threats automatically, without needing an in-house security team.

---

## 3. Problem Statement

### 3.1 The SMB Security Gap

SMBs represent **43% of all cyberattack targets** globally yet receive less than 15% of the cybersecurity product investment. The reasons are structural:

**Financial Barrier:** Annual penetration testing engagements cost $10,000–$50,000. A monthly retainer SOC service from a Managed Security Service Provider (MSSP) costs $3,000–$15,000/month. These are enterprise price points.

**Talent Barrier:** The global cybersecurity workforce shortage exceeds 3.4 million professionals. SMBs cannot compete with enterprise salaries for skilled analysts.

**Comprehension Barrier:** Raw scanner outputs (CVE IDs, CVSS scores, Nmap port lists) require expert interpretation. Non-technical SMB founders and finance directors cannot convert this data into business decisions.

### 3.2 The Consequence

- 60% of SMBs shut down within 6 months of a significant breach (National Cyber Security Alliance)
- Average SMB breach cost: $4.45M (IBM, 2024)
- Average time to detect a breach: 204 days
- Only 14% of SMBs rate their ability to mitigate cyber risks as "highly effective"

---

## 4. Solution

SOCVault is a **multi-tenant AI-powered security maturity platform** that:

1. **Onboards in 60 seconds** — business email + phone number, no procurement contracts
2. **Runs automated scans** — open-source security binaries (Nmap, Nuclei, Semgrep, Wazuh) orchestrated by Python
3. **Translates findings** — Claude AI converts raw CVE data into plain-English financial risk assessments
4. **Automates remediation** — SOAR playbooks execute containment automatically or route to human approval
5. **Tracks compliance** — maps findings to PCI-DSS, GDPR, ISO 27001, SOC2 controls

---

## 5. Market Analysis

### 5.1 Total Addressable Market (TAM)

| Geography | SMBs (50–500 employees) | Potential Addressable |
|---|---|---|
| United Kingdom | ~160,000 | ~48,000 |
| United States | ~1,400,000 | ~420,000 |
| Australia / NZ | ~90,000 | ~27,000 |
| EU (ex-UK) | ~850,000 | ~255,000 |
| **Global TAM** | **~8,400,000** | **~2,520,000** |

At $199/month average ARPU across the paying base: **TAM revenue potential = $500M+/year**

### 5.2 Serviceable Addressable Market (SAM)

Phase 1 focus: UK-based SMBs in regulated sectors (financial services, healthcare, e-commerce, legal).

- UK SMBs in regulated sectors: ~48,000
- Willing-to-pay (budget >£200/month for IT security): ~12,000
- **SAM at launch = ~$28.8M ARR potential**

### 5.3 Serviceable Obtainable Market (SOM)

Year 1 target: **150 paying clients** at ~$60 blended ARPU = **$108,000 ARR** (authoritative: [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) §4)  
Year 2 target: **600 paying clients** at ~$75 blended ARPU = **$540,000 ARR run rate** (M24)  
Year 3 target: **2,000 paying clients** = **$1.8M ARR** run rate (M36)

### 5.4 Market Trends Supporting SOCVault

- **UK NCSC Active Cyber Defence** programme pushing SMBs toward automated security tools
- **GDPR enforcement** intensifying: ICO issued £1.2B in fines in 2023 alone
- **Cyber Essentials mandate** expanding across UK government supply chains (forcing SMB suppliers to comply)
- **AI-driven security tools** now viable at low cost thanks to Claude API pricing

---

## 6. Business Model

### 6.1 Revenue Streams

#### Stream 1: Freemium-to-Paid Conversion (Transaction)
- Entry point: 1 free Recon scan per month
- Conversion trigger: user receives financial risk map showing £X in potential liability
- Upgrade path: unlock remediation scripts, VAPT layers, SOAR playbooks

#### Stream 2: Pay-Per-IP/Domain Licensing (Transactional SaaS)
| Product | Price | Margin |
|---|---|---|
| Web VAPT License | $15/IP/month | ~97.6% |
| Mobile Binary License | $20/app/month | ~97.8% |
| Cloud Perimeter License | $25/env/month | ~97.8% |
| API Security License | $15/endpoint/month | ~97.6% |
| Compliance Register | $30/month/domain | ~99.7% |

#### Stream 3: SOC Pro Subscription (Recurring)
| Tier | Price | Included |
|---|---|---|
| SOC Pro | $199/month | Unlimited scans, 50 Wazuh agents, SOAR, Claude triage |
| SOC Enterprise | $499/month | Unlimited agents, white-label, API access, SLA |
| Managed SOC Add-on | $799/month | Human analyst overlay (8-hour response SLA) |

#### Stream 4: AI Chat Assistant — Credit-Based (New)

The AI Security Assistant is a conversational interface powered by Anthropic Claude, embedded directly in the SOCVault dashboard. Tenants purchase credits to query the AI, trigger scan actions, generate fix scripts, approve SOAR actions, and produce reports — all through natural language.

**Credit Bundles (prepaid, no subscription required):**

| Bundle | Credits | Price | Per-Credit Cost | Saving vs Starter |
|---|---|---|---|---|
| Starter | 50 | $5.00 | $0.100 | — |
| Standard | 200 | $15.00 | $0.075 | 25% |
| Pro | 500 | $30.00 | $0.060 | 40% |
| Enterprise | 2,000 | $99.00 | $0.050 | 50% |

**Credit Cost per Action:**

| Action | Credits | What Happens |
|---|---|---|
| Ask a security question | 1 | Claude answers using tenant's live scan context |
| Show findings / reports | 1 | Pulls live data from scan DB, formats as table |
| Generate remediation script | 2 | Claude generates copy-paste fix for a specific finding |
| Trigger L1 recon scan | 3 | Enqueues a new L1 scan and streams progress |
| Trigger L2 VAPT scan | 5 | Enqueues Fargate VAPT task, returns scan_id |
| Compliance gap analysis | 3 | Queries compliance module, maps to frameworks |
| Cloud posture check | 4 | Triggers Prowler/CloudFox, returns summary |
| Approve / reject SOAR action | 2 | Writes approval to audit log, executes or cancels |
| Generate board / exec report | 5 | Produces a formatted PDF-ready executive summary |
| Create Jira / ServiceNow ticket | 1 | Creates ticket via integration with finding context |

**Unit Economics (AI Chat):**
- Average credit bundle sold: $18 (blended)
- Claude API cost per credit consumed: ~$0.008 (with 84% prompt cache hit rate)
- Gross margin on AI Chat credits: **~87%**
- Expected credit burn per active user/month: 40–80 credits ($3–6 cost, $3.20–6.40 revenue)

#### Stream 5: Professional Services (Future — Year 2+)
- Incident response retainers
- Custom playbook development
- Compliance audit reports (ISO 27001 gap analysis)

### 6.2 Freemium Funnel Economics

```
10,000 Free Signups
     │
     ▼ (12% conversion rate — industry benchmark for DevTools SaaS)
1,200 Trial-to-Paid
     │
     ▼ ($15 avg first transaction)
$18,000 first-month revenue
     │
     ▼ (30% upgrade to subscription within 90 days)
360 SOC Pro subscribers × $199 = $71,640/month
```

**Target blended ARPU at maturity:** $150–180/month/client

---

## 7. Pricing Strategy

### 7.1 Anchoring Rationale

SOCVault pricing is anchored against MSSP alternatives:
- MSSP basic monitoring: $3,000/month → SOCVault SOC Pro = $199 (93% cheaper)
- Annual VAPT: $15,000 → SOCVault annual unlimited = $2,388 (84% cheaper)

This creates an instant "why wouldn't I switch" value proposition for budget-conscious SMB decision-makers.

### 7.2 Geographic Pricing

| Region | SOC Pro | Web VAPT |
|---|---|---|
| USA / Canada | $199/mo | $15/IP/mo |
| UK / EU | £169/mo | £12/IP/mo |
| Australia | A$299/mo | A$22/IP/mo |
| India / SE Asia | $79/mo | $6/IP/mo |

---

## 8. Go-To-Market Strategy

### 8.1 Phase 1 GTM — Content & Community (Months 1–6)

**Target persona:** IT Manager or Technical Founder at a 20–200 person UK business

**Channels:**
- **LinkedIn content** — weekly posts showing "your domain has X exposed ports and here's the financial cost" using real public scans (with permission) as social proof
- **Hacker News / Reddit r/netsec** — launch post + "Show HN" with working free tier
- **Product Hunt launch** — Day 1 press, aim for Top 5 of the day
- **NCSC Cyber Essentials partner ecosystem** — register as a preferred tool for SMBs pursuing certification

**Content strategy:**
- Free Domain Risk Score tool (no signup) — traffic magnet that converts on report delivery
- "We scanned the FTSE 350 supply chain" — PR/media hook to national press
- Weekly "SMB Breach Debrief" newsletter

### 8.2 Phase 2 GTM — Partner & Channel (Months 6–12)

- **MSP/MSSP white-label channel** — reseller program at 30% margin share
- **Accountancy firm partnerships** — target top 50 UK accounting firms to recommend to SMB clients (compliance angle)
- **Insurance broker partnerships** — cyber insurance underwriters recommend SOCVault as pre-qualification tool
- **Legal & HR software integrations** — bundle with existing SMB software stacks

### 8.3 Phase 3 GTM — Paid Acquisition (Year 2)

- Google Ads: "cyber security for small business UK" — high purchase intent keywords
- LinkedIn Ads: job-title targeting (IT Manager, CTO, Operations Director, Finance Director)
- Retargeting: free-tier users who haven't upgraded within 14 days

### 8.4 Key Performance Indicators (KPIs)

| Metric | Month 3 | Month 6 | Month 12 | Year 2 |
|---|---|---|---|---|
| Free signups | 500 | 2,000 | 8,000 | 40,000 |
| Paying clients | 10 | 50 | 200 | 800 |
| MRR | $1,500 | $7,500 | $30,000 | $120,000 |
| Churn rate | <10% | <8% | <6% | <5% |
| CAC | $80 | $60 | $45 | $35 |
| LTV | $480 | $720 | $1,080 | $1,800 |
| LTV:CAC ratio | 6:1 | 12:1 | 24:1 | 51:1 |

---

## 9. Competitive Analysis

### 9.1 Direct SMB Competitors

SOCVault competes in the SMB cybersecurity market — tools accessible to businesses with 10–200 employees. Enterprise platforms (Tenable, Qualys, Arctic Wolf, Rapid7) are excluded from this analysis: their pricing ($3,000–$50,000+/year) and enterprise sales cycles place them entirely outside the SMB buying consideration.

| Product | Positioning | Price | Layers Covered | Key Weakness vs SOCVault |
|---|---|---|---|---|
| **Intruder.io** | Attack surface scanner | $101/mo | 2/8 | No AI translation, no SOAR, no compliance, no SOC |
| **Detectify** | Web app scanner | $89/mo | 2/8 | Developer-focused, no financial risk, no SOAR |
| **Guardz** | AI SMB platform (user layer) | ~$9/user/mo | 2/8 | No external VAPT, no SOAR, no compliance frameworks |
| **Huntress** | SMB MDR (via MSP) | $125–175/agent/mo | 2/8 | MSP-only, no scanning, 6–9× more expensive |
| **Todyl** | Multi-module SMB | $12/endpoint/mo | 2/8 | No scanning, no compliance, basic SOAR only |
| **Malwarebytes Teams** | Endpoint malware | $6.67/device/mo | 1/8 | Endpoint only, no scanning, no SOAR |
| **Pentest-Tools.com** | Vuln scanner | $79–$299/mo | 1–2/8 | Technical tool, no AI, no SOAR, no compliance |
| **Sucuri** | Website security | $199–$499/yr | 1/8 | Website only, no VAPT, no SOAR |
| **Microsoft Defender Biz** | Endpoint security | $3/user/mo | 1/8 | Endpoint + M365 only, no external VAPT |

### 9.2 Complementary Tools (Not Direct Competitors)

- **Guardz** — covers the user/email/identity layer; SOCVault covers the infrastructure layer. Complementary, not substitutable.
- **Huntress** — deep endpoint process hunting via MSPs; SOCVault covers the external attack surface Huntress doesn't touch.
- **Microsoft Defender for Business** — Windows endpoint protection; SOCVault scans what Defender cannot see (web app, subdomains, cloud, compliance).

### 9.3 SOCVault Differentiation

| Factor | SOCVault | Best SMB Alternative |
|---|---|---|
| Financial risk translation (£/$) | ✅ Native, per finding | ❌ None offer this |
| Full 8-layer attack surface | ✅ L1–L8 in one platform | ❌ Maximum 2 layers per competitor |
| Freemium with real scan data | ✅ 15-step scan, free forever | ❌ None offer real free scan |
| Automated SOAR playbooks | ✅ Wazuh + Claude AI | ❌ None at SMB price |
| 60-second self-serve onboarding | ✅ Business email only | ⚠️ 15 min–days for others |
| SMB-priced full SOC | ✅ $199/mo flat (50 agents) | ❌ Huntress = $1,250+/mo for 10 agents |
| Multi-framework compliance | ✅ PCI, GDPR, ISO, SOC2, CE+ | ❌ None include this |
| Malware Detection & Response (AI) | ✅ L8 confidence-gated | ⚠️ Endpoint-only, no AI triage |
| Cost for equivalent coverage | ✅ $199/mo | ❌ $2,900+/mo (fragmented stack) |

---

## 10. Operations Plan

### 10.1 Technology Operations

- **Development:** Engineer workstations; optional local FastAPI unit tests (Docker not required for MVP deploy)
- **Cloud (MVP — staging):** AWS serverless in `eu-west-2` — API Gateway, Lambda, Amplify, SQS, Cognito, S3, DynamoDB, SSM, CloudWatch (ADR-006)
- **Cloud (paid tier):** CloudFront CDN, AWS WAF, AWS Backup, Atlas M10+, ECS Fargate bridge, **Amazon EKS**, CodePipeline
- **Scanning runtime:** L1 on Lambda; L2+ in isolated scan workers (Fargate/EKS at paid tier) — no cross-tenant contamination
- **Database:** MongoDB Atlas M0 on AWS (MVP); not DocumentDB on bootstrap
- **AI API:** Anthropic Claude API (primary), with prompt caching enabled to reduce costs

### 10.2 Customer Support

- Phase 1: Async email support (Intercom / Crisp) — founder-led
- Phase 2: In-app chat, knowledge base, self-serve docs
- Phase 3: Tiered SLA (SOC Enterprise: 4-hour response)

### 10.3 Legal & Compliance

- **Data residency:** UK/EU customer data stored in AWS eu-west-2 (London)
- **GDPR:** DPA registered, Privacy Policy, Data Processing Agreement for B2B
- **Security testing terms:** Clear ToS requiring customers to authorise their own scans
- **Penetration testing authorisation:** Documented consent flow before any active scan
- **ISO 27001:** Target certification by Month 18 (strong trust signal for enterprise sales)

---

## 11. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Customer scans unauthorised targets | Medium | Very High | Consent gating, domain ownership verification, ToS enforcement |
| Claude API cost overrun on high scan volume | Medium | High | Per-tenant cost caps, prompt caching, budget alerts |
| Competitor adds AI features | High | Medium | Move faster, deeper SOAR differentiation, compliance moat |
| Breach of SOCVault itself | Low | Very High | Security-by-design, regular self-scans, bug bounty |
| False positives causing client panic | High | Medium | Confidence scoring, human review gate for critical findings |
| Regulatory classification as security tool | Medium | Medium | Legal review, ToS clarity, NCSC alignment |
| Key talent departure | Medium | High | Documentation, equity incentives |

---

## 12. Exit Strategy

Primary exit paths (5–7 year horizon):

1. **Strategic acquisition** by large MSSP or security vendor (Darktrace, Sophos, Palo Alto Networks, Rapid7) seeking SMB market entry
2. **Private equity roll-up** as anchor platform in SMB security portfolio
3. **IPO** if ARR exceeds £20M+ with strong unit economics

Expected valuation at acquisition readiness: **8–12x ARR** (SaaS security sector benchmark), targeting £40–80M exit at £5M+ ARR.
