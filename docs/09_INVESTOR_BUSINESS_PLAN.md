# SOCVault
## Investor Business Plan
### The Unified AI-Enabled Cybersecurity Solution

**Confidential — June 2026**
**Prepared for: Investor / VC Review**
**Contact:** mutexsystemsltd@gmail.com

---

> *"60% of small businesses close within 6 months of a cyber attack. SOCVault ensures they never have to."*

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Company Overview](#2-company-overview)
3. [The Problem](#3-the-problem)
4. [The Solution](#4-the-solution)
5. [Product Deep Dive](#5-product-deep-dive)
6. [Market Opportunity](#6-market-opportunity)
7. [Business Model](#7-business-model)
8. [Go-To-Market Strategy](#8-go-to-market-strategy)
9. [Competitive Analysis](#9-competitive-analysis)
10. [Technology & Architecture](#10-technology--architecture)
11. [Team](#11-team)
12. [Traction & Validation](#12-traction--validation)
13. [Financial Projections](#13-financial-projections)
14. [Funding Ask & Use of Proceeds](#14-funding-ask--use-of-proceeds)
15. [Risk Analysis & Mitigation](#15-risk-analysis--mitigation)
16. [Product Roadmap](#16-product-roadmap)
17. [Exit Strategy](#17-exit-strategy)
18. [Appendices](#18-appendices)

---

## 1. Executive Summary

### The Opportunity

The global SMB cybersecurity market is a $67.4 billion opportunity growing at 15.2% CAGR. Yet 43% of all cyber attacks target small businesses, while less than 14% of SMBs feel confident in their ability to defend themselves. The tools that exist are either too expensive ($10,000–$50,000/year for enterprise), too complex (requiring specialist security engineers), or too limited (point solutions that don't cover the full attack surface).

**This is not a niche gap. This is a structural market failure.**

### The Product

SOCVault is the **unified AI-enabled cybersecurity solution** purpose-built for SMBs. It is the only platform that consolidates the full security maturity lifecycle — external reconnaissance, vulnerability assessment, compliance gap analysis, real-time SOC monitoring, SOAR automation, and AI-driven malware response — into a single product, and translates every finding into plain-English business risk with quantified financial exposure. One platform replaces what would otherwise require eight separate point solutions costing $35,000+/year.

A non-technical business owner can sign up with their work email, enter their domain, and receive a boardroom-ready financial risk report within 3 minutes. No security expertise required. No procurement process. No enterprise sales cycle.

### The Business Model

- **Freemium:** 1 free scan per month drives organic acquisition and demonstrates value
- **Pay-per-target:** $15–$25/IP or domain/month for advanced scanning layers
- **SOC Pro subscription:** $199/month flat for continuous monitoring, 50 Wazuh agents, and automated SOAR playbooks

Gross margin per paid scan: **97.6%**. Cost to serve one SOC Pro client: ~$15/month. Revenue: $199/month.

### The Ask

We are raising **$251,000 (Pre-Seed)** on a SAFE note at a $2M cap to fund 12 months of development, reach 50 paying clients, achieve $10K MRR, and position for a $750K Seed round at Month 15.

### Three-Year Targets

| Year | Clients | ARR | Gross Margin |
|---|---|---|---|
| 1 | 150 | $108,000 | 82.7% |
| 2 | 600 | $540,000 | 91.0% |
| 3 | 2,000 | $1,800,000 | 93.0% |

---

## 2. Company Overview

| | |
|---|---|
| **Company Name** | SOCVault Ltd |
| **Incorporated** | UK (England & Wales) |
| **Sector** | B2B SaaS / Cybersecurity / AI |
| **Stage** | Pre-Revenue / MVP Development |
| **Founded** | 2026 |
| **Headquarters** | United Kingdom |
| **Target Launch** | Q4 2026 |
| **Website** | socvault.io |

**Positioning:** The unified AI-enabled cybersecurity solution — one platform covering all eight attack surface layers, replacing fragmented point solutions at a fraction of the cost.

**Mission:** Make enterprise-grade cybersecurity accessible to every business, regardless of size or in-house security expertise, through unified AI-enabled automation.

**Vision:** To become the default security operations centre for the global SMB market — the single platform where any business owner can understand their full risk exposure, meet compliance obligations, and respond to threats automatically, without hiring a security team.

**Core Principles:**
- **Accessibility:** No security knowledge required to use the platform
- **Transparency:** Every risk expressed in financial terms any business owner understands
- **Automation:** Remediation should be executable in one click, not a 6-week project
- **Affordability:** World-class protection at SMB-accessible pricing

---

## 3. The Problem

### 3.1 SMBs Are the Biggest Cyber Target

Small and medium-sized businesses face the full spectrum of cyber threats that enterprises face, but with none of the defensive infrastructure:

- **43%** of all cyber attacks globally target SMBs (Verizon DBIR 2024)
- **60%** of breached SMBs close within 6 months (National Cyber Security Alliance)
- Average cost of an SMB breach: **$4.45 million** (IBM Cost of a Data Breach 2024)
- Average detection time: **204 days** — most SMBs don't know they've been breached

### 3.2 The Three Structural Barriers

**Barrier 1 — Capital:** Traditional Vulnerability Assessment and Penetration Testing (VAPT) costs $10,000–$50,000 per engagement annually. A monthly Managed Security Service Provider (MSSP) retainer runs $3,000–$15,000/month. These are enterprise price points inaccessible to the 99.9% of businesses that employ fewer than 250 people.

**Barrier 2 — Talent:** The global cybersecurity workforce shortage exceeds 3.4 million professionals (ISC² 2024). SMBs cannot hire and retain specialist security analysts who command £60,000–£120,000 salaries. Even when they can, those analysts are overwhelmed by alert volume, spending 70% of their time on false positives.

**Barrier 3 — Translation:** Standard security scanners output raw CVE IDs, CVSS scores, and Nmap port listings. This data is meaningless to the vast majority of SMB decision-makers — the CEO, CFO, or Operations Director — who need to understand *business* risk, not *technical* risk. There is currently no product on the market that bridges this gap for SMBs at an affordable price.

### 3.3 The Regulatory Pressure Is Intensifying

- **UK GDPR:** ICO issued £1.2B in fines in 2023. SMBs supplying public sector clients must meet Cyber Essentials requirements
- **PCI-DSS 4.0:** Mandatory for any business accepting card payments — stricter requirements came into force March 2024
- **NIS2 Directive (EU):** Extends cybersecurity obligations to thousands of additional SMB-scale entities from October 2024
- **Cyber insurance:** Premiums have risen 50–100% since 2021; insurers now require security posture evidence before writing policies

This regulatory environment is creating urgent demand from previously passive SMBs. They now *must* demonstrate a security programme — but have no affordable, accessible way to do so.

---

## 4. The Solution

### 4.1 SOCVault Platform Overview

SOCVault is a **multi-tenant, cloud-native SaaS platform** that delivers the full stack of a corporate security operations centre in a self-service format:

```
[Business Owner enters domain] ──► [Automated 8-Layer Scan] ──► [Claude AI Translates]
                                                                        │
                              ┌─────────────────────────────────────────┤
                              ▼                                         ▼
                    [Financial Risk Report]              [1-Click Remediation Scripts]
                    "Your data is at £45,000           "Run this command to fix
                    risk due to this exposure"          the Redis configuration"
                              │
                              ▼
                    [Continuous SOC Monitoring]
                    Wazuh agents + Claude AI triage
                    + automated SOAR playbooks
```

### 4.2 The Core User Journey

**Step 1 — Onboarding (60 seconds):** User enters their business email and phone number. The platform extracts and validates their domain, sends an OTP, and provisions a private workspace. No credit card, no procurement, no configuration.

**Step 2 — First Scan (3 minutes):** User enters their domain and clicks "Scan". SOCVault runs Layer 1 Recon — subdomain discovery, port scanning, service fingerprinting, DNS analysis, brand leak detection — in the background.

**Step 3 — AI Report:** Claude AI translates raw scan findings into a Workspace Health Score (0–100) and a total financial exposure figure. Each vulnerability is explained in plain business language with a projected remediation cost and a one-click patch script.

**Step 4 — Upgrade Trigger:** The financial exposure figure and health score create an immediate conversion motivation. Remediation scripts are paywalled — unlocked only with a paid plan. The user upgrades to access them.

**Step 5 — Continuous Protection:** SOC Pro clients deploy Wazuh agents across their servers. SOCVault monitors real-time alerts, enriches them with threat intelligence, routes them through Claude AI triage, and either contains threats automatically or surfaces them to a human approval dashboard.

### 4.3 Why This Works Now

Three forces have converged to make SOCVault viable today:

1. **AI reasoning quality:** Claude claude-sonnet-4-6 can reliably translate raw security data into accurate financial risk narratives. This capability did not exist at commercial scale 18 months ago.
2. **AI cost efficiency:** Fully-loaded VAPT COGS is ~$0.36 (Claude + compute with prompt caching — **Lambda for L1**, **Fargate/EKS for L2+**) — **97.6% gross margin** at $15/scan.
3. **Open-source security tooling:** Production-grade tools (Nuclei, Wazuh, Semgrep, MobSF) are now mature, well-documented, and free to operate.

---

## 5. Product Deep Dive

### 5.1 Scanning Layer Architecture

SOCVault's platform is structured as eight scanning layers, each targeting a different attack surface dimension:

| Layer | Name | Tools | What It Detects | Tier |
|---|---|---|---|---|
| **L1** | External Recon | python-whois, dnspython, checkdmarc, sslyze, crt.sh, Subfinder, httpx, Naabu, Wappalyzer, AbuseIPDB, HIBP | WHOIS/expiry, full DNS analysis, SPF/DKIM/DMARC, SSL/TLS audit, HTTP security headers, certificate transparency, subdomain discovery, live host validation, top-100 port scan, technology fingerprinting, IP/domain reputation, credential leak check, subdomain takeover, service banners | Free |
| **L2** | Web AppSec | Nuclei, OWASP ZAP, Semgrep, Trivy | CVEs, OWASP Top 10, injection flaws, outdated libraries, authentication bypass, web shell detection | Paid |
| **L3** | Mobile Binary | MobSF, Frida, APKTool | Android APK / iOS IPA vulnerabilities, OWASP MASVS compliance, hardcoded secrets | Paid |
| **L4** | API Security | Nuclei API templates, ZAP API scan | OWASP API Top 10, broken object-level auth, excessive data exposure, rate limit bypass | Paid |
| **L5** | Compliance | Custom rule engine, Prowler | PCI-DSS, GDPR, ISO 27001, SOC2, Cyber Essentials control gap analysis | Paid |
| **L6** | Cloud | CloudFox, Pacu, Prowler, Steampipe | AWS/Azure/GCP IAM misconfigurations, privilege escalation paths, exposed buckets | Paid |
| **L7** | SOC/SIEM | Wazuh 4.7, Claude AI, AbuseIPDB, OTX | Real-time endpoint threats, network anomalies, brute force, malware, ransomware | SOC Pro |
| **L8** | Malware Detection & Response | ClamAV, YARA, Trivy, Nuclei webshell templates, VirusTotal | Malware detection on endpoints and web servers; Claude AI determines family, severity, and generates quarantine + removal commands; auto-remediates isolated threats; human-gated for system-wide incidents | SOC Pro |

#### L1 Freemium Recon — Complete 15-Step Process

The free tier executes a full passive reconnaissance pipeline against the user's registered domain. All 15 steps run in parallel within a single AWS Lambda invocation and complete in under 90 seconds:

| Step | Check | Tool | What It Flags |
|---|---|---|---|
| 1 | WHOIS & Registrar | python-whois | Registrar, creation/expiry dates; flags if expiry <30 days |
| 2 | DNS Record Analysis | dnspython | A, AAAA, MX, NS, TXT, CNAME, SOA — missing or misconfigured records |
| 3 | Email Security | checkdmarc | Missing/broken SPF, DKIM, DMARC — phishing risk |
| 4 | SSL/TLS Audit | sslyze | Expired certs, weak ciphers (RC4, DES), TLS 1.0/1.1, missing HSTS |
| 5 | HTTP Security Headers | httpx | Missing CSP, X-Frame-Options, HSTS, X-Content-Type-Options |
| 6 | Certificate Transparency | crt.sh API | All certificates ever issued — shadow subdomains |
| 7 | Subdomain Discovery | Subfinder (passive) | Subdomains from DNS, CT logs, public sources |
| 8 | Live Host Validation | httpx | Which subdomains are live and responding |
| 9 | Port Discovery | Naabu (top 100 ports) | Open ports, unexpected exposed services |
| 10 | Technology Fingerprinting | Wappalyzer headless | CMS, framework, server, CDN, analytics stack |
| 11 | IP Reputation | AbuseIPDB API | Abuse confidence score for all resolved IPs |
| 12 | Domain Reputation | Google Safe Browsing + URLhaus | Phishing/malware blacklist status |
| 13 | Credential Leak Check | HaveIBeenPwned domain API | How many accounts from this domain appear in breach databases |
| 14 | Subdomain Takeover | CNAME dangling checker | CNAMEs pointing to deprovisioned cloud services (S3, Heroku, Azure) |
| 15 | Service Banner Analysis | Nmap -sV (version scan) | Exposed service versions and EOL software detection |

### 5.2 AI Intelligence Engine

Every scan finding passes through the Claude AI intelligence layer, which performs three operations:

**Financial Risk Quantification:** Each vulnerability is assigned a projected financial exposure in USD/GBP, calculated from:
- Estimated downtime hours × average SMB operational loss rate ($500/hour)
- Regulatory penalty risk (GDPR Article 83 maximum: 4% of global turnover)
- Data breach recovery cost (forensics, notification, credit monitoring, PR)

**Plain-Language Translation:** Technical CVE descriptions are rewritten as business-level narratives. A CVE for an unauthenticated Redis exposure becomes: *"Your database server is publicly accessible without a password. An attacker could download your entire customer database in under 10 minutes."*

**Remediation Script Generation:** Claude generates copy-pasteable bash commands, configuration file patches, and step-by-step developer instructions to remediate each finding. These are paywalled for Freemium users — the most powerful conversion lever in the product.

### 5.3 SOAR Automation Engine

SOCVault's Layer 7 SOC product includes a Security Orchestration, Automation, and Response (SOAR) engine powered by Wazuh and Claude AI:

**Real-time Alert Pipeline:**
```
Wazuh Agent (client server)
      │ alert triggered
      ▼
SOCVault SOAR API
      │
      ├─► Threat Intel Enrichment (AbuseIPDB + OTX + GreyNoise)
      │
      ├─► Claude AI Triage
      │       │ Is it a true positive?
      │       │ What's the business impact?
      │       │ Contain automatically or escalate?
      │       ▼
      ├─► CONTAIN: Execute Wazuh Active Response automatically
      │       (firewall-drop IP, kill process, isolate host)
      │
      └─► ESCALATE: Human approval queue
              (analyst sees full context, approves/rejects)
```

**Automated Playbooks:**
- PB-101: Active Ransomware & Cryptojacking Mitigation
- PB-102: Network Attack & IP Block Containment
- PB-103: Phishing Campaign Containment & Mail Purge
- PB-104: Lateral Movement Detection & Isolation
- PB-105: Privileged Account Compromise Response

### 5.2 Threat Intelligence & Correlation

External enrichment is configured in **Super Admin → Threat Intel Feeds** (Pass & Keys vault for API keys). **32 free/freemium providers** mapped per layer (CVE/NVD, AbuseIPDB, OTX, HIBP, VirusTotal, URLhaus, MalwareBazaar, CISA KEV, etc.) with cross-layer correlation for reporting and SOAR. Authoritative catalogue: [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) — not duplicated in this document.

**Human-in-the-Loop Gate:** All high-risk automated actions (blocking user accounts, restarting production services, isolating entire subnets) are routed to a human approval dashboard before execution. Claude provides the full decision context: threat summary, confidence score, proposed action, and business impact warning.

### 5.4 Malware Detection & Response Engine (L8 — SOC Pro)

Layer 8 is triggered continuously via Wazuh on enrolled SOC Pro endpoints, and on-demand by L2 web application scans. It is the only layer that can take autonomous remediation action against an active threat — all other layers produce reports.

**Detection Sources:**

```
┌──────────────────────────────────────────────────────────────┐
│               L8 DETECTION SOURCES                          │
├─────────────────────┬────────────────────────────────────────┤
│  Wazuh ClamAV       │  Continuous AV scan on all enrolled    │
│  (Continuous)       │  endpoints; detects known malware sigs │
├─────────────────────┼────────────────────────────────────────┤
│  Wazuh FIM          │  File Integrity Monitoring — new or     │
│  (Continuous)       │  modified executables trigger alert     │
├─────────────────────┼────────────────────────────────────────┤
│  L2 Nuclei          │  Web shell detection templates;         │
│  (On-Demand)        │  triggers when AppSec scan runs         │
├─────────────────────┼────────────────────────────────────────┤
│  Trivy              │  Container image malicious layer        │
│  (On-Demand)        │  detection during L2 scan               │
└─────────────────────┴────────────────────────────────────────┘
```

**Analysis & Response Pipeline:**

```
Detection Event (ClamAV/FIM/Nuclei/Trivy)
      │
      ▼
MDRM Microservice (Malware Detection & Response Manager)
      │
      ├─► Hash lookup: VirusTotal API (confidence + family)
      ├─► YARA rule match (local rules: ransomware, RATs, cryptominers)
      │
      ▼
Claude AI Analysis (claude-sonnet-4-6)
      │  Input: file hash, file path, process name, YARA match, VT result, host context
      │
      ├─► Output: malware family, severity score (1–10)
      ├─► Output: lateral movement risk + data exfiltration likelihood
      ├─► Output: quarantine command, removal command, persistence cleanup steps
      ├─► Output: IOC list (hashes, file paths, network indicators)
      └─► Output: post-remediation verification command
      │
      ▼
Decision Gate:
      │
      ├─► CONFIDENCE >95% + ISOLATED FILE/PROCESS
      │       → AUTO-REMEDIATE:
      │         1. Move file → /var/ossec/quarantine/
      │         2. Kill process (if active)
      │         3. Update Wazuh blocklist
      │         4. Log action with hash + actor + timestamp
      │
      └─► SYSTEM-WIDE THREAT / CONFIDENCE <95%
              → HUMAN APPROVAL GATE:
                Analyst receives: threat summary, affected hosts,
                proposed commands, business impact warning
                → Approves → Execute
                → Rejects → Escalate to SOC team
      │
      ▼
Post-Remediation:
      ├─► Automated re-scan to confirm removal
      ├─► Malware Incident Report generated (family, files, actions, clean status)
      ├─► Workspace Health Score updated
      └─► Slack + email + dashboard notification
```

**Key Differentiator:** SOCVault's L8 engine is the only component in the SMB market that combines autonomous AI-driven malware analysis with a human-in-the-loop gate — providing the speed of automation without the risk of unchecked autonomous action on production systems.

### 5.5 Compliance Module

The compliance layer maps scan findings to specific control requirements across major frameworks:

| Framework | Controls Mapped | Automated Checks |
|---|---|---|
| PCI-DSS 4.0 | 12 requirements, 60+ controls | Port exposure, TLS config, patch levels, segmentation |
| UK GDPR | Articles 5, 25, 32 | Data encryption, access controls, breach detection capability |
| ISO 27001:2022 | Annex A controls | 93 controls across 4 themes |
| SOC 2 Type II | Trust Service Criteria | CC6–CC9 (security, availability, confidentiality) |
| Cyber Essentials Plus | 5 technical controls | Firewall, secure config, access control, malware, patch management |

Each compliance report generates a gap register — a prioritised list of control failures with remediation actions, ownership assignments, and risk ratings. This is the core deliverable for any SMB preparing for regulatory audit or cyber insurance underwriting.

### 5.6 Multi-Tenant Architecture

Every customer operates in a completely isolated workspace:

- **Authentication:** One **Cognito User Pool per environment** (staging / production); custom `tenant_id` attribute on every user and JWT — not one pool per tenant (ADR-003)
- **Data isolation:** All MongoDB documents partitioned by `tenant_id`; row-level security enforced at API middleware layer
- **Scan isolation:** L1 runs in **AWS Lambda**; L2+ scans run in ephemeral **Fargate/EKS** tasks — no shared memory, no persistent state between tenants
- **Storage isolation:** S3 artifacts stored under `s3://socvault-artifacts/{tenant_id}/{scan_id}/` — no cross-tenant read access possible
- **Audit trail:** Every action logged with actor, tenant, timestamp, and resource — immutable for 12 months

---

## 6. Market Opportunity

### 6.1 Total Addressable Market

The global cybersecurity market was valued at **$214 billion in 2024** and is projected to reach **$424 billion by 2030** (MarketsandMarkets). The SMB-specific segment represents approximately 31% of this market.

**SMB Cybersecurity Market:**
- Global (2024): $67.4 billion
- Global (2030): $156.2 billion
- CAGR: 15.2%

| Geography | Total SMBs | Addressable (50–500 employees) | Willing-to-Pay (>$100/mo security budget) |
|---|---|---|---|
| United Kingdom | 5.6M businesses | ~160,000 | ~48,000 |
| United States | 33.2M businesses | ~1,400,000 | ~420,000 |
| Australia / NZ | 2.5M businesses | ~90,000 | ~27,000 |
| EU (ex-UK) | 25M businesses | ~850,000 | ~255,000 |
| **Global TAM** | **~66M businesses** | **~8,400,000** | **~2,520,000** |

At $150/month blended ARPU: **Global TAM = $4.5B ARR**

### 6.2 Serviceable Addressable Market (SAM)

Phase 1 focus: UK-based SMBs in regulated sectors with active cyber compliance obligations.

**Target sectors (UK):**
- Financial services and fintech: ~28,000 firms
- E-commerce and retail: ~45,000 firms
- Healthcare and life sciences: ~22,000 firms
- Legal and professional services: ~38,000 firms
- Technology / SaaS companies: ~35,000 firms

**Total UK SAM: ~168,000 companies** — of which approximately 48,000 have the budget and the regulatory pressure to pay for automated cybersecurity tooling.

**SAM revenue at $150/month ARPU: $86.4M ARR**

### 6.3 Serviceable Obtainable Market (SOM)

| Year | Target Clients | Market Share of UK SAM | ARR |
|---|---|---|---|
| 1 | 150 | 0.3% | $108,000 |
| 2 | 600 | 1.3% | $540,000 |
| 3 | 2,000 | 4.2% | $1,800,000 |
| 5 | 10,000 | 20.8% | $18,000,000 |

**Year 5 with US expansion:** 30,000+ clients → $54M ARR

### 6.4 Market Tailwinds

**Regulatory pressure:** The UK Cyber Security and Resilience Bill (2024) will impose mandatory incident reporting and minimum security standards on thousands of additional SMBs. NIS2 in the EU extends similar obligations. This creates non-discretionary spending.

**Cyber insurance:** Insurers now require security posture assessments before writing policies. Platforms like SOCVault become table stakes for any SMB seeking coverage.

**Supply chain security:** Large enterprises increasingly mandate that suppliers meet minimum security standards (ISO 27001, Cyber Essentials Plus). SMBs must comply or lose contracts. SOCVault provides the compliance evidence they need.

**AI cost deflation:** Claude API pricing has fallen significantly and continues to decline. The economics that make SOCVault's 97%+ gross margin possible will only improve over time.

**Talent shortage:** The 3.4 million cybersecurity professional shortage drives demand for automation. SOCVault replaces the need for in-house expertise — a $70,000+ annual hire — at $199/month.

### 6.5 Customer Profile

**Primary Persona: "The Worried IT Manager"**
- Role: IT Manager or Head of Technology at a 30–200 person business
- Pain: Knows the risks, overwhelmed by alert volume, no budget for an MSSP
- Trigger: Recent breach news in their sector, upcoming compliance audit, insurance renewal
- Decision power: Can approve tools up to £500/month; presents larger spends to CFO
- Current tools: Antivirus, basic firewalls, perhaps Microsoft Defender

**Secondary Persona: "The Compliance-Pressured Founder"**
- Role: Founder/CEO of a 10–50 person SaaS company
- Pain: Client requiring ISO 27001 or SOC 2 compliance before signing contract
- Trigger: Enterprise customer request, funding due diligence, insurance requirement
- Decision power: Full autonomy over tool spend
- Current tools: Nothing formal — this is their first structured security investment

**Tertiary Persona: "The MSP Owner"**
- Role: Managed Service Provider serving 20–100 SMB clients
- Pain: Can't profitably offer security services at SMB price points
- Trigger: Client asking for security reporting, compliance evidence, SOAR
- Decision power: Full autonomy; can white-label SOCVault to their clients
- Current tools: RMM, patch management, basic SIEM

---

## 7. Business Model

### 7.1 Revenue Architecture

SOCVault operates four distinct but complementary revenue streams, engineered to maximise both conversion rate and lifetime value:

#### Stream 1 — Freemium Acquisition (L1 Recon)

Free users receive one complete Recon scan per month against their primary domain. The scan runs in minutes using serverless Lambda functions with zero Claude API cost (structured data only, no AI translation required at this tier).

**What's included free:** Domain mapping, open port identification, service fingerprinting, subdomain enumeration, DNS structure, threat reputation check.

**What's excluded (conversion gate):** Financial risk translation, remediation scripts, compliance status, vulnerability severity ratings.

**The conversion mechanic:** Users see a "Workspace Health Score" and a total "Estimated Financial Exposure" figure with the specific breakdowns blurred and paywalled. The psychological impact of seeing "£47,200 at risk" drives upgrade intent. Free trial converts at 12% to a paid plan within 30 days.

#### Stream 2 — Pay-Per-Target Licensing (L2–L6)

Advanced scanning layers are licensed per IP address, domain, application binary, or cloud environment:

| Product | Price | COGS | Gross Margin |
|---|---|---|---|
| Web VAPT License (L2) | $15/IP/month | $0.36 | 97.6% |
| Mobile Binary License (L3) | $20/app/month | $0.45 | 97.8% |
| Cloud Perimeter License (L6) | $25/env/month | $0.55 | 97.8% |
| API Security License (L4) | $15/endpoint/month | $0.36 | 97.6% |
| Compliance Register (L5) | $30/domain/month | $0.08 | 99.7% |

This pay-per-target model aligns pricing with customer value and removes barriers for entry. A startup with one domain pays $15/month; a company with 20 domains and a cloud environment pays $345/month — scaling linearly with their attack surface.

#### Stream 3 — SOC Pro Subscription (L7 Continuous Monitoring)

| Tier | Price | Included |
|---|---|---|
| **SOC Pro** | $199/month | Unlimited scans; 50 Wazuh agents; SOAR playbooks; Claude AI triage; Slack + email alerts; compliance dashboard |
| **SOC Enterprise** | $499/month | All Pro features; unlimited agents; white-label; SAML SSO; API access; SLA guarantee; custom playbooks |
| **Managed SOC Add-on** | $799/month | SOC Enterprise + human analyst overlay; 4-hour response SLA (Year 2) |

Monthly recurring infrastructure cost to serve one SOC Pro client: ~$15. Net margin per client: **$184/month (92.5%)**.

#### Stream 4 — AI Chat Assistant Credits (New Revenue Layer)

The AI Security Assistant is the most differentiated product feature in SOCVault's portfolio. No SMB security competitor offers conversational AI security analysis with real-time action triggers backed by live scan data.

Tenants pre-purchase credit bundles through Stripe. Each interaction with the AI — a question, a triggered scan, a generated remediation script — deducts credits from the balance. Credits never expire. There is no subscription required to buy credits, creating a low-friction entry point for non-subscribers.

**Credit Bundles:**

| Bundle | Credits | Price | Margin |
|---|---|---|---|
| Starter | 50 | $5.00 | 88% |
| Standard | 200 | $15.00 | 84% |
| Pro | 500 | $30.00 | 80% |
| Enterprise | 2,000 | $99.00 | 75.5% |

**Why this is a high-quality revenue stream for investors:**

1. **Prepaid = zero receivables risk.** Tenants buy before they consume. Revenue is recognised on purchase, not delivery.
2. **Consumption compounds.** Active users who discover the value of Claude-generated remediation scripts become habitual credit buyers — a recurring revenue behaviour with no churn signal.
3. **Cross-stream multiplier.** A credit-triggered L1 scan converts a credit buyer into a scan result viewer — driving subscription upsell from within the AI session.
4. **Gross margin of 80–88%.** Claude API cost per credit is ~$0.012 with 84% prompt cache hit rate. Revenue per credit is $0.050–$0.100. No meaningful infrastructure overhead.
5. **Net Revenue Retention booster.** Credits are consumed, not cancelled. A tenant who runs out of credits and tops up registers as expansion MRR, lifting NRR above 100% without any upsell effort.

**Projected AI Chat Revenue:**

| Year | Active Users | Avg Monthly Spend | Annual Revenue |
|---|---|---|---|
| Year 1 | 30 | $12 | ~$2,500 |
| Year 2 | 180 | $18 | ~$38,000 |
| Year 3 | 600 | $24 | ~$170,000 |

#### Stream 5 — Professional Services (Year 2+)

- ISO 27001 gap analysis report: $2,500/engagement
- Custom SOAR playbook development: $1,500/playbook
- Incident response retainer: $3,000/month
- Security training workshop: $1,200/session

### 7.2 Freemium Conversion Funnel

```
10,000 Free Signups
  ↓ 12% conversion within 30 days
1,200 First Purchase (~$35 average)
  ↓ 30% upgrade to subscription within 90 days
360 SOC Pro Subscribers × $199 = $71,640 MRR
  ↓ 25% expand to Enterprise within 12 months
90 Enterprise × $499 = $44,910 MRR
─────────────────────────────────────────
Total MRR at this funnel scale: ~$116,550
```

### 7.3 Unit Economics

| Metric | Value |
|---|---|
| Blended CAC (Year 1) | $60 |
| Blended LTV (Year 1) | $720 (24-month retention × $30 net revenue) |
| LTV:CAC Ratio | **12:1** |
| Payback Period | 2.0 months |
| Gross Margin (blended) | 91–97% |
| Net Revenue Retention (target Year 2) | >110% (expansion revenue from upsell) |
| Monthly Churn Target | <5% |

### 7.4 Pricing Psychology & Anchoring

SOCVault anchors its pricing against two widely understood reference points:

**vs. MSSP:** "A traditional SOC retainer costs £3,000–£15,000/month. SOCVault SOC Pro costs £169/month — 93% cheaper, with equivalent threat detection powered by the same technology used by enterprise security teams."

**vs. the cost of a breach:** "The average SMB data breach costs £3.2 million. SOCVault for a full year at SOC Pro costs £2,028. That's 0.06% of your breach risk covered for the price of a monthly software subscription."

---

## 8. Go-To-Market Strategy

### 8.1 Phase 1 GTM — Organic & Community (Months 1–6)

**Objective:** 2,000 free signups, 50 paying clients, first $7,500 MRR

**Primary Channel: Content Marketing**

The most cost-effective SMB security buyer acquisition channel is organic content that demonstrates expertise and creates trust before the sales conversation:

- **LinkedIn:** Weekly posts framing security risks in business terms ("Your competitor's data breach cost them £3.4M — here's what they missed"). Target IT Manager and Founder personas.
- **"We scanned the [industry] sector":** Monthly research posts scanning publicly-accessible domains of well-known SMBs (with legal review) to demonstrate real risks. High-sharing content.
- **"SMB Breach Debrief" newsletter:** Weekly analysis of a recent SMB breach. What happened. What it cost. What would have caught it. Drives consistent organic traffic.
- **Free Domain Risk Score tool:** No-signup public tool at socvault.io/scan that gives any domain a quick reputation check and partial health score. Generates leads, demonstrates product, creates sharing incentive.

**Product Hunt Launch:** Scheduled for Month 4 (October 2026). Target top 5 of the day. Drives initial backlink profile, developer community awareness, and international traffic.

**Hacker News "Show HN":** Post when live free tier is available. The security and developer community on HN are exactly the "Worried IT Manager" persona.

**NCSC Partnership:** Register as a recommended tool for businesses working toward Cyber Essentials certification. The NCSC's active promotion of SMB tools provides credibility and inbound referrals.

### 8.2 Phase 2 GTM — Channel & Partner (Months 6–12)

**Objective:** **150 paying clients** and **$9K MRR** by Month 12 (Year 1 end); MSP partner foundation for Year 2 scale — see §8.4 Marketing KPIs and [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md)

**MSP White-Label Channel:**
Managed Service Providers already have relationships with the SMB clients we want to reach. SOCVault's white-label tier allows MSPs to brand and resell the platform:
- MSP pricing: 30% discount on SOC Enterprise ($349/month)
- MSP sells to their clients at £299–£399/month
- Target: 10 MSP partners × average 15 sub-clients each = 150 clients through channel
- Revenue per MSP relationship: $5,235/month at $349 × 15 clients

**Accountancy Firm Partnerships:**
UK accountancy firms are increasingly advising SMB clients on regulatory compliance. GDPR, cyber insurance, and investor due diligence have made cybersecurity a finance-adjacent conversation. Partnering with top 50 regional accountancy firms positions SOCVault as the tool they recommend to any client facing these pressures.

**Cyber Insurance Broker Integration:**
Several major cyber insurance brokers (Markel, AXA XL, Tokio Marine) now require security posture assessments before writing policies. SOCVault's compliance reports serve as this evidence. Establishing partnerships where brokers recommend SOCVault to prospective clients creates a strong inbound lead flow with high purchase intent.

**Law Firm Referral Network:**
Data protection solicitors and law firms advising SMBs on GDPR compliance are another natural referral source. An SMB that just received an ICO inquiry needs a security posture tool immediately — this is the highest-intent moment in the sales funnel.

### 8.3 Phase 3 GTM — Paid Acquisition (Year 2)

**Objective:** 600+ paying clients, $45K MRR, 3 geographic markets

**Google Ads:** Target high purchase-intent keywords:
- "cyber security for small business UK" (1,300 searches/month, $8.50 CPC)
- "SMB penetration testing" (720 searches/month, $12.00 CPC)
- "GDPR security compliance tool" (880 searches/month, $9.50 CPC)
- Target CAC: $80 on paid search, LTV:CAC still >9:1

**LinkedIn Ads:** Job-title targeting of IT Managers, Operations Directors, CTOs, and Finance Directors at 20–500 person UK businesses. Used for retargeting free-tier users who haven't upgraded within 14 days.

**Affiliate Programme:** Security bloggers, CISO coaches, and IT consultant community. 15% of first 12 months' revenue per referred paying client.

### 8.4 Marketing KPIs

| KPI | Month 3 | Month 6 | Month 12 | Year 2 |
|---|---|---|---|---|
| Monthly website visitors | 2,000 | 8,000 | 25,000 | 80,000 |
| Free signups / month | 80 | 300 | 800 | 2,500 |
| Free-to-paid conversion rate | 8% | 10% | 12% | 14% |
| Paying clients (cumulative) | 8 | 30 | 150 | 600 |
| MRR | $400 | $2,000 | $9,000 | $45,000 |
| Organic traffic share | 90% | 85% | 75% | 55% |

---

## 9. Competitive Analysis

### 9.1 Direct Competitor Landscape (SMB Market)

SOCVault competes in the SMB cybersecurity market — tools accessible to businesses with 10–200 employees at price points SMBs can actually pay. Enterprise tools (Tenable, Qualys, Arctic Wolf, Rapid7) are not in scope: their pricing, complexity, and sales cycles exclude them from the SMB buying decision entirely.

| Company | Positioning | Price | Layers Covered | AI Translation | SOAR | Compliance |
|---|---|---|---|---|---|---|
| **Intruder.io** | Attack surface scanner | $101/mo | 2/8 | None | None | None |
| **Detectify** | Web app scanner | $89/mo | 2/8 | None | None | None |
| **Guardz** | AI SMB cyber (user layer) | ~$9/user/mo | 2/8 | ⚠️ Labels only | None | ⚠️ Basic |
| **Huntress** | SMB MDR via MSP | $125–175/agent/mo | 2/8 | None | ⚠️ Via MSP | None |
| **Todyl** | Multi-module SMB | $12/endpoint/mo | 2/8 | None | ⚠️ Basic | None |
| **Malwarebytes Teams** | Endpoint malware | $6.67/device/mo | 1/8 | None | None | None |
| **Pentest-Tools.com** | Vuln scanner | $79–$299/mo | 1–2/8 | None | None | None |
| **Sucuri** | Website security | $199–$499/yr | 1/8 | None | None | None |
| **Microsoft Defender Biz** | Endpoint security | $3/user/mo | 1/8 | None | ⚠️ Limited | None |
| **SOCVault** | Full-stack SMB SOC | $0–$199/mo | **8/8** | **Yes (Claude AI)** | **Yes (Wazuh)** | **Yes (5 frameworks)** |

### 9.2 SOCVault's Defensible Advantages

**1. AI-Powered Financial Translation (Unique across entire SMB market):** Zero SMB competitors translate security findings into dollar-denominated business risk. Every tool outputs CVE IDs, CVSS scores, or threat level tags — meaningless to the SMB decision-maker. SOCVault converts each finding into a plain-English financial exposure figure: *"This vulnerability puts £47,200 of your revenue at immediate risk."* That turns a discretionary purchase into a fiduciary obligation.

**2. Only Integrated 8-Layer Platform at SMB Price:** Every SMB competitor covers 1–2 attack surface layers. An SMB patching together point solutions (Intruder + Guardz + Huntress + Malwarebytes) pays $2,900+/month with coverage gaps remaining. SOCVault covers all 8 layers for $199/month — 93% cheaper, more comprehensive.

**3. Integrated SOAR — A Genuine White Space:** No SMB-priced tool offers automated incident response with AI triage and a human approval gate. Huntress comes closest but requires an MSP intermediary and costs $1,250+/month for 10 agents. SOCVault's SOAR is native, self-serve, and included at $199/month flat.

**4. Freemium With Real Scan Value:** No SMB competitor offers a meaningful free tier. Intruder, Detectify, Guardz, Huntress, Todyl, Malwarebytes, Sucuri — none offer a real free scan. SOCVault's 15-step freemium recon runs against the user's actual domain, produces real findings with financial exposure figures, and converts to paid when the user can't ignore their Health Score.

**5. Compliance as Standard — Another White Space:** No SMB security scanner provides PCI-DSS, UK GDPR, ISO 27001, SOC 2, or Cyber Essentials gap analysis as a standard feature. Every UK SMB under regulatory pressure (card processing, public sector contracts, cyber insurance) must produce compliance evidence — but has no affordable tool to do so. SOCVault fills this gap.

### 9.3 Competitive Moat Development

| Timeframe | Moat Layer |
|---|---|
| Launch | AI financial translation (prompt engineering, Claude-specific optimisation) |
| Month 6 | Proprietary scan dataset (scan result corpus → better AI prompts) |
| Month 12 | Compliance automation depth (mapped control libraries) |
| Year 2 | Network effect: threat intelligence pool across all SOCVault tenants |
| Year 3 | Switching cost: compliance history, asset inventory, incident records — years of data that can't be migrated |

---

## 10. Technology & Architecture

### 10.1 System Architecture (MVP = staging, serverless)

```
┌─────────────────────────────────────────────────────────────┐
│              AWS eu-west-2 — STAGING (MVP active)            │
│                                                             │
│  ┌──────────────┐   ┌──────────────────┐   ┌─────────────┐ │
│  │  React/TS    │   │  API Gateway      │   │  Lambda L1  │ │
│  │  (Amplify)   │──►│  HTTP → Lambda    │──►│  + workers  │ │
│  └──────────────┘   └────────┬─────────┘   └─────────────┘ │
│                              │         SQS async queue       │
│                    ┌─────────▼────────┐                    │
│                    │ MongoDB Atlas M0 │◄── AWS Cognito     │
│                    │ (on AWS)         │                    │
│                    └─────────┬────────┘                    │
│              S3 · DynamoDB · Claude API                     │
└─────────────────────────────────────────────────────────────┘

Paid tier: CloudFront CDN · WAF · Backup · EKS · CodePipeline
Production: dormant until cutover (ADR-006)
```

### 10.2 Core Technology Stack

| Layer | Technology | Why |
|---|---|---|
| **Backend API** | FastAPI on AWS Lambda (Mangum) | Serverless; API Gateway edge |
| **Frontend** | React 18 + TypeScript on **Amplify** | AWS-native serverless hosting |
| **Database** | MongoDB Atlas M0 on AWS | Full MongoDB API; upgrade to M10 at paid tier |
| **Async queue (MVP)** | Amazon SQS + Lambda | Scan jobs; no Redis on MVP |
| **AI Reasoning** | Anthropic Claude claude-sonnet-4-6 | JSON adherence, prompt caching |
| **Authentication** | AWS Cognito + API Gateway authorizer | Multi-tenant JWT |
| **Scan Runtime** | Lambda (L1) → Fargate/EKS (L2+) | Per-invocation isolation |
| **File Storage** | AWS S3 | Tenant-partitioned artifacts |
| **SIEM (paid)** | Wazuh on EC2 | SOC Pro layer |
| **CDN / WAF (paid)** | CloudFront + AWS WAF | Not on Free Tier MVP |
| **IaC** | Terraform | All environments |
| **CI/CD (MVP)** | GitHub Actions | QA + deploy staging |
| **CI/CD (paid)** | AWS CodePipeline | Production orchestration |
| **Scale (paid)** | Amazon EKS (Kubernetes) | Full platform orchestration |

### 10.3 Security-by-Design

SOCVault applies enterprise security principles to its own platform — it is both a security product and a security-grade product:

- All data in transit: TLS 1.3 enforced; HSTS headers
- All data at rest: AES-256 encryption (MongoDB Atlas, S3, DynamoDB)
- Authentication: **Cognito-issued** JWT + refresh tokens (pool TTLs); MFA required for admin (ADR-003)
- CORS: Strict origin allowlist — never open wildcard
- Input validation: Pydantic v2 strict models on all API boundaries
- Scan isolation: Lambda/Fargate per job; tenant_id on all MongoDB queries
- Secrets: SSM Parameter Store (MVP) → Secrets Manager (paid)
- Dependency scanning: Trivy + Dependabot in CI/CD (dogfooding the platform)
- Pen testing: Quarterly self-scan using SOCVault's own tools
- Audit logging: AWS CloudTrail for all infrastructure events; immutable 12-month retention

### 10.4 Scalability Profile

| Scale | Architecture | Monthly Infrastructure Cost |
|---|---|---|
| MVP (staging) | API GW + Lambda + Amplify + Atlas M0 | ~$100–115 (incl. Anthropic testing) |
| 0–50 clients | + CloudFront, WAF, M10 Atlas, Wazuh EC2 | ~$433 |
| 50–200 clients | + EKS or Fargate scale, larger Wazuh | ~$900 |
| 200–500 clients | EKS HPA, M20 Atlas | ~$2,200 |
| 500+ clients | Multi-AZ EKS, M30+ Atlas | ~$4,500+ |

Serverless MVP minimises idle spend; paid tier adds CDN, security, backups, and Kubernetes.

---

## 11. Team

### 11.1 Founding Team

*[To be completed with actual team bios — placeholder structure below]*

**[Founder Name] — CEO & Co-Founder**
- Background: [X years in cybersecurity / SaaS / entrepreneurship]
- Previous: [Relevant prior experience]
- Strength: Vision, product strategy, customer development

**[Technical Co-Founder] — CTO**
- Background: [Python, DevSecOps, cloud architecture]
- Previous: [Relevant technical experience]
- Strength: Architecture, engineering velocity, security tool expertise

### 11.2 Advisors Needed (To Be Recruited)

| Role | Why Critical |
|---|---|
| CISO Advisor | Industry credibility, enterprise intro network |
| Compliance/Legal Advisor | GDPR, ISO 27001, FCA regulatory navigation |
| SaaS GTM Advisor | Freemium-to-paid optimisation, channel partnerships |
| Cybersecurity VC LP | Signal to market, warm intros to investors |

### 11.3 Hiring Plan

| Role | Quarter | Salary | Priority |
|---|---|---|---|
| AI / ML Engineer | Q3 Year 1 (Seed) | $75,000 | High — prompt optimisation, scan intelligence |
| Frontend Engineer | Q4 Year 1 (Seed) | $65,000 | High — dashboard, UX, conversion funnel |
| Sales / GTM Lead | Q4 Year 1 (Seed) | $60K + commission | High — channel partnerships, MSP |
| Head of Customer Success | Q2 Year 2 | $65,000 | Medium — churn reduction, expansion revenue |
| SOC Analyst | Q3 Year 2 (Series A) | $55,000 | Medium — Managed SOC tier |
| DevOps Engineer | Q3 Year 2 (Series A) | $80,000 | Medium — infrastructure at scale |

---

## 12. Traction & Validation

### 12.1 Product Development Status

| Component | Status | Notes |
|---|---|---|
| Core API (FastAPI + MongoDB on Lambda) | Blueprint complete | OpenAPI + FRs defined; **`socvault-app` not started** |
| AI financial translation (Claude) | Blueprint complete | Model IDs, prompts, FRs in requirements; no runtime yet |
| SOAR engine (Wazuh + Claude) | Blueprint complete | Wireframes + FRs; live Wazuh testing after AWS provision |
| React TypeScript dashboard | Blueprint complete | 25 HTML wireframes; Amplify app not started |
| AWS staging MVP (serverless) | Documented | Staging-only; API GW + Lambda + Amplify; production dormant (ADR-006) |
| AWS Terraform infrastructure | Blueprint complete | IaC spec: **API Gateway, Lambda, Cognito, SQS, Amplify, DynamoDB, S3** — ECS/EKS paid tier only (ADR-006) |
| Stripe payment integration | Planned | Phase 2 — Month 8 target |
| Scanning binaries (real, not mock) | Blueprint complete | Tooling + roadmap nano steps; integration in `socvault-app` TBD |
| Threat Intel Feed Registry | Spec complete | 32 APIs · Super Admin UI · correlation engine — [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) |
| OpenAPI + 208 user stories | Complete | Includes `/admin/ti/feeds` · US-201–208 |

> **Blueprint vs runtime:** This repository is product documentation only. Status **“Blueprint complete”** = specified here; **“Complete”** = artefact exists in-repo (OpenAPI, xlsx). Application code lives in future **`socvault-app`** repo.

### 12.2 Market Validation

- **Primary research:** 12 structured interviews with UK IT Managers and CTOs at 20–200 person companies
  - 11/12 confirmed they have no formal security scanning in place
  - 9/12 said they would pay £50–£200/month for an automated solution
  - 8/12 said the "financial risk in £" framing was the feature that most resonated
  - Average stated willingness to pay: £87/month

- **Regulatory signal:** UK NCSC's "Cyber Essentials" mandatory requirement for government supply chains has created 60,000+ SMBs actively seeking certification tools in 2024 alone

- **Analogous market evidence:** Intruder.io (direct comparator) raised $11M Series A in 2023 — validating investor appetite for SMB security SaaS. Intruder lacks AI translation, SOAR, and compliance modules.

### 12.3 Letters of Intent / Pilot Commitments

*[To be completed — target 5 LOIs from qualified SMB prospects before Pre-Seed close]*

---

## 13. Financial Projections

### 13.1 Revenue Projections

| Month | Free Users | Paying Clients | MRR | ARR Run Rate |
|---|---|---|---|---|
| M6 (Nov 2026) | 1,200 | 20 | $1,100 | $13,200 |
| M9 (Feb 2027) | 3,500 | 65 | $3,900 | $46,800 |
| M12 (May 2027) | 9,000 | 150 | $9,000 | $108,000 |
| M18 (Nov 2027) | 22,000 | 323 | $22,000 | $264,000 |
| M24 (May 2028) | 38,000 | 600 | $45,000 | $540,000 |
| M30 (Nov 2028) | 65,000 | 1,200 | $90,000 | $1,080,000 |
| M36 (May 2029) | 100,000 | 2,000 | $150,000 | $1,800,000 |

> **M18 vs M28:** M18 targets **323 clients / $22K MRR** (post-Seed operating milestone; **EBITDA positive ~M18**). **Seed close** is **M15 (Aug 2027)** at ~200 clients / ~$16K MRR. **Cash-flow break-even** (fixed opex covered) is **M28** — see §13.6 and [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) §6.

### 13.2 Three-Year Profit & Loss

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| **Revenue** | $108,000 | $540,000 | $1,800,000 |
| Cost of Goods Sold | $18,700 | $48,600 | $126,000 |
| **Gross Profit** | **$89,300** | **$491,400** | **$1,674,000** |
| **Gross Margin** | **82.7%** | **91.0%** | **93.0%** |
| Personnel | $124,200 | $336,950 | $633,650 |
| Infrastructure (excl. COGS) | $2,332 | $8,400 | $22,500 |
| AI API (excl. COGS) | $4,250 | $31,500 | $138,000 |
| Threat Intelligence | $440 | $2,570 | $9,450 |
| Marketing | $15,000 | $55,500 | $140,000 |
| Legal / Compliance | $15,500 | $23,700 | $20,000 |
| Tooling | $868 | $2,680 | $6,900 |
| Misc / G&A | $6,200 | $17,300 | $46,500 |
| **Total Operating Expenses** | **$168,790** | **$478,600** | **$1,017,000** |
| **EBITDA** | **-$79,490** | **+$12,800** | **+$657,000** |
| EBITDA Margin | -73.6% | +2.4% | +36.5% |

### 13.3 Cash Flow Projection

| Period | Opening Cash | Funding In | Revenue | OpEx | **Closing Cash** |
|---|---|---|---|---|---|
| Y1 (pre-seed) | $0 | $251,000 | $32,230 | $172,090 | **$111,140** |
| Y2 (seed + ops) | $111,140 | $750,000 | $396,500 | $486,100 | **$771,540** |
| Y3 (series A) | $771,540 | $3,000,000 | $1,620,000 | $1,075,500 | **$4,316,040** |

### 13.4 Unit Economics Deep Dive

**Customer Acquisition Cost (CAC)**

| Channel | Cost per Lead | Lead-to-Trial Rate | Trial-to-Paid Rate | CAC |
|---|---|---|---|---|
| Organic / SEO | $5 | 15% | 12% | $28 |
| LinkedIn content | $12 | 10% | 12% | $100 |
| Product Hunt | $2 | 20% | 12% | $8 |
| MSP / Channel | $0 | N/A | 100% (pre-qualified) | $0 |
| Google Ads (Y2) | $25 | 8% | 10% | $313 |
| **Blended (Y1)** | | | | **$60** |
| **Blended (Y2)** | | | | **$45** |

**Lifetime Value (LTV)**

| Tier | Monthly Net Revenue | Average Lifespan | LTV |
|---|---|---|---|
| Transactional only | $30 | 18 months | $540 |
| SOC Pro | $184 | 28 months | $5,152 |
| SOC Enterprise | $460 | 36 months | $16,560 |
| **Blended (Y1)** | | | **$720** |

**LTV:CAC Ratios**

| Year | LTV | CAC | Ratio | Payback Period |
|---|---|---|---|---|
| 1 | $720 | $60 | **12:1** | 2 months |
| 2 | $1,080 | $45 | **24:1** | 1.5 months |
| 3 | $1,800 | $35 | **51:1** | 1 month |

### 13.5 Gross Margin Analysis

SOCVault operates an exceptionally high gross margin business because:

1. **Variable cost per scan is tiny.** Claude API tokens (~$0.27 with prompt caching) plus compute (~$0.009 Lambda for L1 freemium; ~$0.035 Fargate for L2+ VAPT) total **~$0.36 COGS** per paid Web VAPT scan against **$15.00 revenue (97.6% gross margin)**.

2. **The freemium tier costs us almost nothing.** L1 Recon scans run in Lambda at $0.000002 per execution. There is no Claude API cost for free scans (the health score is computed from structured scan data without AI translation).

3. **SOC Pro infrastructure is shared efficiently.** The Wazuh Manager and Claude triage layer serve all SOC Pro clients from a single persistent installation. At 200 SOC Pro clients, infrastructure cost is ~$15/client/month against $199 revenue.

4. **Margins improve with scale.** Reserved instances on EC2 (Wazuh) save 40% vs. on-demand. MongoDB Atlas reserved instances save 35%. At Year 3 scale, infrastructure unit costs continue to decline as fixed infrastructure costs are amortised across more clients.

### 13.6 Break-Even Analysis

| Variable | Value |
|---|---|
| Monthly fixed operating cost (Year 2, 3-person team) | $22,000 |
| Blended gross margin at Year 2 | 91% |
| Clients needed to cover fixed costs | 22,000 / (75 × 0.91) = **323 clients** |
| Projected month of break-even | **Month 28 (September 2028)** — cash-flow positive |
| EBITDA positive (operating) | **~Month 18 (November 2027)** — see Year 2 P&L |
| MRR at cash-flow break-even | **~$24,225** |
| MRR at M18 (323 clients) | **$22,000** — post-Seed operating milestone; aligns with client count for EBITDA positive |

---

## 14. Funding Ask & Use of Proceeds

### 14.1 Pre-Seed Round

| Detail | |
|---|---|
| **Amount** | $251,000 |
| **Instrument** | SAFE Note |
| **Valuation Cap** | $2,000,000 |
| **Discount** | 20% on next priced round |
| **Pro-rata rights** | Yes |
| **Use of proceeds** | 12-month runway to 50 paying clients and $10K MRR |

**Detailed Use of Funds:**

| Category | Amount | % | Notes |
|---|---|---|---|
| Founding Engineer salary (12 mo) | $70,000 | 27.9% | Primary technical build |
| Founder living allowance (12 mo) | $60,000 | 23.9% | CEO/Founder |
| AWS infrastructure | $24,000 | 9.6% | $2,000/month average |
| Claude API budget | $12,000 | 4.8% | $1,000/month for testing + production |
| Security tooling licences | $12,000 | 4.8% | AbuseIPDB, OTX, monitoring tools |
| Compliance contractor | $12,000 | 4.8% | GDPR, DPA, ISO 27001 prep |
| Legal (company, contracts, ToS) | $8,000 | 3.2% | One-time setup |
| Marketing & content | $20,000 | 8.0% | Content, design, Product Hunt |
| ISO 27001 audit preparation | $10,000 | 4.0% | Stage 1 readiness |
| Contingency (10%) | $23,000 | 9.2% | Buffer for overruns |
| **Total** | **$251,000** | **100%** | |

**Pre-Seed Milestones (12 months):**
- [ ] Staging MVP live at `app-staging.socvault.io` (production per cutover checklist)
- [ ] 10 beta clients onboarded (Month 6)
- [ ] First paid conversion (Month 7)
- [ ] **50 paying clients + $10K MRR** (Month 8 — Seed unlock criteria; see §16 milestones)
- [ ] **150 paying clients** (Month 12 — Year 1 end per §13.1)
- [ ] ISO 27001 certification in progress
- [ ] 3 MSP/channel partner agreements signed

### 14.2 Seed Round (Projected Month 15 — August 2027)

| Detail | |
|---|---|
| **Amount** | $750,000 |
| **Structure** | Priced equity (Series Seed) |
| **Valuation** | $3.5M pre-money |
| **Dilution** | ~21.4% |
| **Lead investor type** | UK cybersecurity/SaaS specialist VC or angel syndicate |

**Seed Use of Funds:**
- AI/ML Engineer hire: $75,000
- Frontend Engineer hire: $65,000
- Sales/GTM Lead hire: $60,000 + commission
- Marketing acceleration: $150,000 (paid acquisition, events)
- ISO 27001 final audit: $15,000
- SOC 2 preparation: $20,000
- AWS infrastructure scale-up: $80,000
- Operating reserve: $285,000

**Post-Seed operating targets (Month 18 / Nov 2027):**
- **323 paying clients** and **$22K MRR** (EBITDA / OPEX break-even per §13.6)
- ISO 27001 certified
- 10 MSP partner agreements
- US market launch (beta)

> **Note:** Seed **closes Month 15 (Aug 2027)** once unlock criteria are met (50+ clients, $10K+ MRR — typically by Month 8). Month-18 targets are **use-of-proceeds outcomes**, not closing conditions.

### 14.3 Series A (Projected Month 31 — December 2028)

| Detail | |
|---|---|
| **Amount** | $3,000,000 |
| **Structure** | Priced equity |
| **Valuation** | $12M pre-money (8× forward ARR multiple) |
| **Lead investor type** | Tier 1 cybersecurity VC (Accel, Notion Capital, Balderton, Paladin Capital) |

**Series A Use of Funds:**
- Engineering team: 4 additional engineers ($320,000)
- Sales team: 3 sales engineers + 1 VP Sales ($400,000)
- Marketing: Content, paid, events, PR ($500,000)
- Managed SOC team (2 analysts): $110,000
- US market infrastructure (AWS us-east-1): $120,000
- SOC 2 Type II audit: $20,000
- International legal and compliance: $80,000
- Reserve: $1,450,000

---

## 15. Risk Analysis & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Users scan unauthorised targets (legal/reputational)** | Medium | Very High | Domain ownership verification before any active scan; explicit consent checkbox with IP logged; clear ToS; indemnification clause |
| **Claude API cost overrun on high scan volume** | Medium | High | Per-tenant daily cost caps; prompt caching (60–90% cost reduction); Haiku model for simple enrichments; admin budget alerts at $50/day |
| **Major competitor adds AI translation features** | High | Medium | First-mover advantage in SMB AI security; deepen SOAR moat; compliance depth; switching cost from data history |
| **Breach of SOCVault platform itself** | Low | Very High | Security-by-design; quarterly self-scans; bug bounty from Year 2; ISO 27001; pen testing by external firm; cyber insurance |
| **High false positive rate causing client anxiety** | High | Medium | Confidence scoring on all AI findings; human review gate for critical claims; "explain this finding" feature; accuracy feedback loop |
| **Regulatory classification as offensive security tool** | Medium | High | Legal review of ToS and consent flow; NCSC alignment; restrict active scanning to verified domain owners only; clear responsible use policy |
| **Anthropic API downtime or price increase** | Low | Medium | Graceful degradation with cached offline reports; pricing insulated by high gross margins (97%) even at 3× current API price |
| **Key technical founder departure** | Medium | Very High | Comprehensive documentation from Day 1; IP assignment agreements; 4-year vesting with 1-year cliff; knowledge sharing culture |
| **Slow enterprise adoption of SOAR tier** | Medium | Medium | Focus on SMB Pro tier first; SOAR as upsell not requirement; testimonials from beta clients |
| **Economic downturn reducing SMB IT spend** | Medium | Medium | Security spend is increasingly non-discretionary (compliance-driven); price point low enough to survive budget cuts; annual plan incentives |

---

## 16. Product Roadmap

### Phase Summary

| Phase | Timeline | Goal |
|---|---|---|
| **Phase 0: Foundation** | Jun–Jul 2026 | AWS account, CI/CD pipeline, brand, OpenAPI contract |
| **Phase 1: Cloud MVP on staging** | Jul–Sep 2026 | Auth + L1 + Claude on `api-staging.socvault.io`; Bruno collection green (matches [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) Phase 1) |
| **Phase 2: Beta & scale** | Oct–Nov 2026 | Production cutover (checklist), Stripe, SOAR beta, 10 beta clients (matches [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) Phase 2) |
| **Phase 3: Public Launch** | Dec 2026–Feb 2027 | 50 paying clients, $10K MRR, all 8 core layers (L1–L8); L9 agent scan in parallel track |
| **Phase 4: Growth** | Mar–Jun 2027 | **150 clients** (Year 1 end), MSP channel, ISO 27001 Stage 1 |
| **Phase 5: Expansion** | Jul 2027–Year 2 | Seed close (Month 15), scale to **323 clients / $22K MRR** (M18), $50K MRR, Series A prep |

### Key Product Milestones

| Milestone | Date | Metric |
|---|---|---|
| AWS staging MVP complete (scanners + AI) | August 2026 | Full E2E journey on staging with CI/CD |
| First beta client onboarded | October 2026 | 1 paying client |
| Staging platform serving beta clients (`app-staging.socvault.io`) | November 2026 | 99.5% uptime; production cutover when checklist complete |
| 10 paying beta clients | November 2026 | $1,000 MRR |
| First paid conversion (cold) | November 2026 | Organic signup → paid |
| Product Hunt launch | December 2026 | Top 5 of the day |
| 50 paying clients | February 2027 | $10K MRR |
| ISO 27001 Stage 1 audit | March 2027 | Zero critical findings |
| SOAR playbooks live (full) | March 2027 | 5 automated playbooks |
| Seed round close | August 2027 | $750K raised (~200 clients · ~$16K MRR at close) |
| **323 paying clients (EBITDA milestone)** | **November 2027 (M18)** | **$22K MRR** |
| ISO 27001 certified | October 2027 | Certificate issued |
| MSP white-label channel live | November 2027 | 3 MSP partners |
| US market beta | January 2028 | 20 US clients |
| 600 paying clients | May 2028 | $45K MRR |
| Break-even | September 2028 | Positive monthly cash flow |
| 2,000 paying clients | May 2029 | $150K MRR |
| Series A close | December 2028 | $3M raised |

### Feature Roadmap (Next 18 Months)

**Months 1–6 (MVP Core):**
- Email + phone onboarding with OTP verification
- L1 Recon scanning (Subfinder, Naabu, httpx)
- Claude AI financial risk translation
- React dashboard with health score and exposure figure
- Freemium gate (1 scan/month)
- Admin COGS telemetry

**Months 7–12 (Full Product):**
- L2 Web AppSec (Nuclei, OWASP ZAP, Semgrep)
- L3 Mobile binary analysis (MobSF)
- L6 Cloud penetration (CloudFox, Pacu)
- Wazuh SOC deployment + SOAR playbooks
- Stripe payment integration
- PDF export of executive reports
- Slack + email incident notifications
- Compliance dashboard (PCI-DSS, GDPR)

**Months 13–18 (Growth Features):**
- White-label MSP portal
- SAML SSO (Okta, Azure AD, Google Workspace)
- Custom SOAR playbook builder
- Asset inventory (auto-discovered domains, IPs)
- API access for Enterprise tier
- Multi-region support (UK + US)
- Managed SOC tier (human analyst overlay)

---

## 17. Exit Strategy

### 17.1 Strategic Rationale for Acquirers

SOCVault's architecture, customer base, and compliance certifications make it an attractive acquisition target for several categories of buyer:

**Large Cybersecurity Vendors** seeking SMB market penetration: Rapid7, Tenable, Qualys, Sophos, Palo Alto Networks, Darktrace — all have enterprise-focused products and have explicitly stated SMB expansion as a strategic priority. SOCVault provides instant go-to-market with a proven SMB-native product.

**MSSP / MDR Providers** seeking product-led growth capability: Arctic Wolf, Expel, eSentire — all operate high-touch, high-cost models. SOCVault's self-service platform enables them to serve the sub-$3,000/month segment they currently cannot profitably address.

**Insurance and Risk Management Platforms:** Cyber insurers (AXA XL, Markel, Beazley) are actively acquiring security posture assessment tools to integrate into their underwriting process. SOCVault's compliance reports become a natural insurance pre-qualification layer.

**Private Equity Roll-ups:** The SMB cybersecurity space is actively consolidating. A PE firm building a platform in this space would acquire SOCVault as an anchor asset.

### 17.2 Exit Timeline & Valuation

| Scenario | Timeline | ARR | Multiple | Valuation |
|---|---|---|---|---|
| Early strategic acquisition | Year 3–4 | $3M ARR | 10× | $30M |
| Growth-stage strategic acquisition | Year 4–5 | $8M ARR | 10× | $80M |
| PE / roll-up | Year 4–5 | $8M ARR | 8× | $64M |
| IPO | Year 6–7 | $25M ARR | 12× | $300M |

**Target exit:** Strategic acquisition at Year 4–5 at **$60–$100M** valuation, returning 24–40× on Pre-Seed capital.

---

## 18. Appendices

### Appendix A — Sample AI Report Output

```json
{
  "workspace_health_score": 58,
  "total_projected_financial_exposure": 73400.00,
  "issues": [
    {
      "id": "SV-THREAT-01",
      "cve": "CVE-2023-38646",
      "risk_type": "Database Exfiltration Risk",
      "summary": "Your database server is accessible from the public internet without a password. An attacker can connect in seconds and download your entire customer database, including payment records and personal data.",
      "projected_damage_usd": 45000.00,
      "downtime_hours": 12,
      "remediation_action": "Add the following two lines to your database configuration file and restart the service:\n\nbind 127.0.0.1\nprotected-mode yes"
    },
    {
      "id": "SV-THREAT-02",
      "cve": "CVE-2022-44228",
      "risk_type": "Business Interruption Risk",
      "summary": "Your public website runs an outdated web server framework with a known vulnerability. Attackers can use this to take your website offline, redirect your customers to a fake site, or intercept sensitive form submissions.",
      "projected_damage_usd": 28400.00,
      "downtime_hours": 18,
      "remediation_action": "sudo apt-get update && sudo apt-get install --only-upgrade apache2 -y"
    }
  ]
}
```

### Appendix B — SMB Pricing Comparison

**Scenario:** 30-person UK business, one web app, 10 servers, AWS cloud, PCI-DSS + GDPR obligations.

**Fragmented SMB point-solution stack (best available):**

| Layer | Best SMB Tool | Annual Cost | Gaps Remaining |
|---|---|---|---|
| External recon + CVE scanning | Intruder.io Essential | $1,212 | No AI, no SOAR, no compliance |
| Web application scanning | Detectify Starter | $1,068 | No AI, no SOAR |
| Email + dark web + identity | Guardz (30 users) | $3,240 | No VAPT, no compliance |
| Endpoint malware (10 devices) | Malwarebytes Teams | $800 | No scanning, no SOAR |
| Endpoint MDR (10 agents) | Huntress | $18,000 | No VAPT, no compliance, MSP required |
| Website malware + WAF | Sucuri Pro | $600 | Website only |
| Compliance evidence | Vanta Starter | $10,000 | No scanning, no SOAR |
| **Total fragmented stack** | | **$34,920/year** | **Mobile, API, cloud, SOAR, AI still missing** |

**SOCVault SOC Pro:** $2,388/year — covers all 8 layers including every gap above.

**SOCVault saves the equivalent SMB $32,532/year (93% cost reduction) while delivering more comprehensive coverage.**

| Product | Annual Cost | Layers | AI Translation | SOAR | Compliance |
|---|---|---|---|---|---|
| **SOCVault SOC Pro** | **$2,388** | **8/8** | **✅ Financial £/$** | **✅ Automated** | **✅ 5 frameworks** |
| Intruder.io Essential | $1,212 | 2/8 | ❌ | ❌ | ❌ |
| Detectify Starter | $1,068 | 2/8 | ❌ | ❌ | ❌ |
| Guardz (30 users) | $3,240 | 2/8 | ⚠️ Labels only | ❌ | ⚠️ Basic |
| Huntress (10 agents) | $18,000 | 2/8 | ❌ | ⚠️ Via MSP | ❌ |
| Malwarebytes (10 devices) | $800 | 1/8 | ❌ | ❌ | ❌ |
| Todyl (10 endpoints) | $1,440 | 2/8 | ❌ | ⚠️ Basic | ❌ |

### Appendix C — Technology Dependencies

**Open-Source Tools (Zero Licensing Cost):**
- Subfinder, Naabu, httpx (ProjectDiscovery) — Apache 2.0
- Nuclei (ProjectDiscovery) — MIT License
- Semgrep (Semgrep Inc.) — LGPL
- OWASP ZAP — Apache 2.0
- MobSF (OpenSecurity) — GPL v3
- Wazuh (Wazuh Inc.) — GPL v2
- CloudFox — MIT License
- Prowler — Apache 2.0

**Paid APIs:**
- Anthropic Claude API — Pay per token (no minimum)
- AbuseIPDB — Free to 1,000 checks/day; $20/month beyond
- AlienVault OTX — Community tier free; enterprise $150/month
- GreyNoise — Free 100 queries/day; $99/month beyond

**Paid Infrastructure (MVP staging serverless + paid-tier scale):**
- AWS (API Gateway, Lambda, Amplify, SQS, Cognito, S3, DynamoDB, SNS) — Pay as you go; Free Tier covers early staging
- MongoDB Atlas — M0 free on AWS; from $57/month (M10 cluster) at paid tier
- CloudFront + AWS WAF — Paid tier (replaces third-party CDN/WAF on AWS-native stack)
- ECS Fargate / Amazon EKS — Paid tier scan workers and Celery at scale
- Stripe — 1.4% + 20p per transaction (Stripe Radar included)

### Appendix D — Regulatory Framework Coverage

| Regulation | Who It Affects in UK | SOCVault Coverage |
|---|---|---|
| UK GDPR | All businesses processing personal data | Article 32 security measures, breach detection capability |
| PCI-DSS 4.0 | Any business accepting card payments | All 12 requirements mapped; L2 scanning covers critical controls |
| Cyber Essentials | Gov supply chain; many enterprise suppliers | All 5 technical controls verified by L1+L2 scanning |
| ISO 27001:2022 | Businesses selling to enterprise/public sector | 93 Annex A controls mapped; gap register with remediation |
| NIS2 (EU) | UK businesses with EU operations | Incident detection + reporting capability via SOC Pro |
| FCA Operational Resilience | Financial services firms | Threat detection, SOAR response, audit trail |

### Appendix E — Founding Assumptions & Sensitivity

**Key assumptions underlying the financial model:**
1. 12% freemium-to-paid conversion rate (industry benchmark: 5–15%)
2. 5% monthly churn on paying clients (industry: 3–8%)
3. $75 blended ARPU at Year 2 (conservative — SOC Pro alone is $199)
4. 91% gross margin at Year 2 (achievable with prompt caching and scale)
5. $45 blended CAC at Year 2 (organic-heavy mix; conservative)
6. 24-month average customer lifespan (sticky due to compliance history and data)
7. Claude API pricing held flat — any price reduction improves margins further

**Key risks to the financial model:**
- If conversion rate drops to 6% → Year 2 ARR = $270,000 (still positive EBITDA from M20)
- If churn rises to 8% → Year 2 ARR = $340,000 (profitable from M24)
- If Claude API costs 3× → gross margin falls to 93% (still excellent)
- If CAC rises to $120 → LTV:CAC falls to 6:1 (still strong, payback ~4 months)

---

*This document contains forward-looking statements based on current assumptions and market conditions. Actual results may differ materially. This plan is confidential and intended solely for qualified investors.*

*© 2026 SOCVault Ltd. All rights reserved.*
