# SOCVault — Unique Selling Propositions & Competitive Analysis
**Version 2.0 | June 2026**
**Confidential — For Internal & Investor Use**

---

> *SOCVault is the unified AI-enabled cybersecurity solution. It does not compete with enterprise tools SMBs can't afford, or add to the pile of point solutions they're already drowning in. It replaces the entire fragmented stack — eight attack surface layers, one platform, AI-enabled from detection to remediation.*

---

## Table of Contents

1. [The Competitive Landscape Defined](#1-the-competitive-landscape-defined)
2. [USP 1 — AI Financial Risk Translation](#2-usp-1--ai-financial-risk-translation)
3. [USP 2 — Freemium With Real Scan Value](#3-usp-2--freemium-with-real-scan-value)
4. [USP 3 — SOAR Automation at SMB Price Points](#4-usp-3--soar-automation-at-smb-price-points)
5. [USP 4 — Full 8-Layer Attack Surface Coverage](#5-usp-4--full-8-layer-attack-surface-coverage)
6. [USP 5 — Malware Detection & Response With AI Triage](#6-usp-5--malware-detection--response-with-ai-triage)
7. [USP 6 — 60-Second Onboarding](#7-usp-6--60-second-onboarding)
8. [USP 7 — Open-Source Scanning Core](#8-usp-7--open-source-scanning-core)
9. [USP 8 — Compliance as Standard](#9-usp-8--compliance-as-standard)
10. [USP 9 — Conversational AI Security Assistant With Action Triggers](#10-usp-9--conversational-ai-security-assistant-with-action-triggers)
11. [Head-to-Head SMB Competitor Analysis](#11-head-to-head-smb-competitor-analysis)
12. [SMB Feature Matrix](#12-smb-feature-matrix)
13. [SMB Pricing Comparison](#13-smb-pricing-comparison)
14. [Market Fit Summary](#14-market-fit-summary)
15. [Moat & Defensibility](#15-moat--defensibility)

---

## 1. The Competitive Landscape Defined

### Who SOCVault Actually Competes With

SOCVault's competitive set is defined by the tools an IT manager or business owner at a 20–200 person company would realistically evaluate. Enterprise tools — Tenable, Qualys, Arctic Wolf, Rapid7, CrowdStrike — are not in scope: an SMB would never begin a procurement conversation with those vendors. Their pricing ($3,000–$50,000+/year), complexity, and enterprise sales cycles disqualify them entirely from the SMB buying motion.

The actual SMB cybersecurity market is served by a fragmented set of point solutions, each covering one or two attack surface layers:

| Competitor | Category | Price | What It Covers |
|---|---|---|---|
| **Intruder.io** | Attack surface management | $101/mo | External scanning, ports, CVEs |
| **Detectify** | Web application scanner | $89/mo | Web app vulnerabilities |
| **Guardz** | AI SMB cyber platform | ~$9/user/mo | Email threats, dark web, endpoint, identity |
| **Huntress** | MDR for SMBs (via MSP) | $125–175/agent/mo | Endpoint detection, ransomware |
| **Todyl** | Multi-module SMB platform | $12/endpoint/mo | Network, EDR, basic SIEM |
| **Malwarebytes for Teams** | Endpoint/malware | $6.67/device/mo | Malware, ransomware, endpoint only |
| **Pentest-Tools.com** | Vulnerability scanner | $79–$299/mo | Network + web scanning, no AI |
| **Sucuri** | Website security | $199–$499/yr | Website malware, WAF, CDN |
| **Microsoft Defender for Business** | Endpoint security | $3/user/mo | Windows endpoint, M365-integrated |

**The pattern:** every SMB-accessible tool covers 1–2 dimensions of the attack surface. None of them translate findings into financial risk. None include SOAR. None cover the full 8-layer attack surface in a single platform.

### The USP Framework

SOCVault's competitive advantages operate at three depths:

```
LEVEL 1 — SURFACE DIFFERENTIATION
  "We do things SMB competitors don't"
  → Freemium with real scans, 60-second onboarding, plain-English reports

LEVEL 2 — STRUCTURAL DIFFERENTIATION
  "We are built differently — competitors can't add this without rebuilding"
  → AI financial translation, 8-layer integrated coverage, automated SOAR at $199/mo

LEVEL 3 — MOAT DIFFERENTIATION
  "This advantage compounds — a competitor can copy the feature but not the lead"
  → Proprietary scan corpus, compliance history switching cost, network threat intelligence
```

---

## 2. USP 1 — AI Financial Risk Translation

### The Claim

SOCVault is the **only platform in the SMB cybersecurity market** that converts raw technical vulnerability findings into quantified, per-finding financial exposure in GBP/USD — automatically, in real time, without a consultant.

### Why This Gap Exists

Every SMB security tool outputs the same data formats designed for security engineers: CVE IDs, CVSS scores (a number from 1–10), port listings, and NVD advisory links. This output is useless to the actual decision-maker at an SMB — the CEO, CFO, or Operations Director who needs to understand **business risk**, not technical findings.

**The translation gap is not a minor UX problem. It is the primary reason SMBs don't act on security findings.**

A CVSS 9.8 finding that reads *"Unauthenticated remote code execution in OpenSSH 8.4"* requires a security engineer to understand. The same finding translated as *"An attacker can take full control of your payment server remotely. Estimated regulatory exposure: £340,000. Estimated incident response cost: £85,000. This takes under 2 minutes to exploit with publicly available tools"* — that is an immediate board-level decision.

### How SOCVault Does It

Claude AI (`claude-sonnet-4-6`) receives the raw scan output and calculates a multi-factor financial exposure estimate per finding:

| Input | Calculation | Output |
|---|---|---|
| CVE severity + affected system | Downtime hours × £500/hour operational loss rate | Operational risk (£) |
| Data exposure scope + record count | GDPR Article 83 maximum fine bracket | Regulatory exposure (£) |
| Exploit availability + attack complexity | Forensics + notification + PR cost model | Breach recovery cost (£) |
| Business sector + compliance context | Insurance void risk + premium impact | Insurance exposure (£) |
| **All combined** | | **Total financial exposure per finding** |

### Market Evidence — Zero SMB Competitors Offer This

| Competitor | Financial Risk Output? | What They Output Instead |
|---|---|---|
| **Intruder.io** | ❌ None | CVE IDs + CVSS scores |
| **Detectify** | ❌ None | Technical CVE descriptions |
| **Guardz** | ❌ None | Risk level tags (Low/Medium/High) |
| **Huntress** | ❌ None | Threat incident descriptions |
| **Todyl** | ❌ None | Alert severity labels |
| **Pentest-Tools.com** | ❌ None | Technical vulnerability reports |
| **Malwarebytes** | ❌ None | Threat name + quarantine status |
| **Sucuri** | ❌ None | Malware type + infection status |
| **SOCVault** | ✅ Yes — per finding, in £/$ | Financial exposure + remediation cost |

### Why Competitors Cannot Simply Copy This

1. **Prompt depth:** The financial translation is built on calibrated prompt engineering against real breach cost databases (IBM Cost of a Data Breach, ICO fine records, Verizon DBIR). This represents months of tuning — not a feature switch.
2. **Claude AI dependency:** The quality of multi-variable financial reasoning is a Claude-specific capability. Competitors using GPT-3.5 or rule-based ML cannot produce the same quality of contextual financial narrative.
3. **Calibration data:** As SOCVault processes scans, the AI output improves against real-world outcomes. A new entrant starts with zero calibration data.

---

## 3. USP 2 — Freemium With Real Scan Value

### The Claim

SOCVault's free tier delivers a genuine 15-step external reconnaissance report against the user's real domain — permanently, once per month. No time limit. No fake data. No feature-gated demo.

### The SMB Competitor Free Tier Reality

| Competitor | Free Tier | Quality |
|---|---|---|
| **Intruder.io** | ❌ No free tier | Trial requires signup + payment method |
| **Detectify** | ⚠️ 14-day trial only | Clock-limited; no ongoing free access |
| **Guardz** | ⚠️ Limited free trial | Restricted features; time-bounded |
| **Huntress** | ❌ No free tier | MSP channel only; per-agent billing |
| **Todyl** | ❌ No free tier | Minimum seat commitment required |
| **Pentest-Tools.com** | ⚠️ 1 free scan/24h | Feature-limited; no AI output |
| **Malwarebytes** | ⚠️ 14-day trial | Consumer-grade free version only |
| **Sucuri** | ❌ No free scan | Paid WAF subscription required |
| **SOCVault** | ✅ Real scan, free forever | 15 steps, real findings, financial exposure |

### The Conversion Mechanic

The freemium model is the primary acquisition engine, not an act of generosity:

```
Free scan produces real results on the user's actual domain:
  → Health Score: 34/100
  → Financial exposure: £182,000 across 4 critical findings
  → Remediation scripts: PAYWALLED

The £182,000 figure creates an immediate fiduciary obligation.
The user cannot look away. They convert to paid to access the fix.
```

This turns a discretionary purchase ("should I invest in security?") into an unavoidable decision ("I now know my company has a £182,000 exposure and the fix is £15/month").

### What 15 Steps Covers — vs Competitors' Free Tiers

Intruder.io's $101/month paid plan covers roughly steps 7, 8, 9, and partial 4–5 of SOCVault's free tier:

| Step | SOCVault Free | Intruder $101/mo | Detectify $89/mo | Pentest-Tools Free |
|---|---|---|---|---|
| WHOIS & registrar expiry | ✅ | ❌ | ❌ | ❌ |
| Full DNS analysis | ✅ | ⚠️ | ❌ | ❌ |
| SPF / DKIM / DMARC | ✅ | ❌ | ❌ | ❌ |
| SSL/TLS audit | ✅ | ✅ | ✅ | ⚠️ |
| HTTP security headers | ✅ | ⚠️ | ✅ | ❌ |
| Certificate transparency | ✅ | ❌ | ✅ | ❌ |
| Subdomain discovery | ✅ | ✅ | ✅ | ❌ |
| Live host validation | ✅ | ✅ | ✅ | ❌ |
| Top-100 port scan | ✅ | ✅ | ❌ | ✅ |
| Technology fingerprinting | ✅ | ⚠️ | ✅ | ❌ |
| IP reputation (AbuseIPDB) | ✅ | ❌ | ❌ | ❌ |
| Domain reputation (Safe Browsing) | ✅ | ❌ | ❌ | ❌ |
| Credential leak check (HIBP) | ✅ | ❌ | ❌ | ❌ |
| Subdomain takeover detection | ✅ | ⚠️ | ✅ | ❌ |
| Service banner analysis | ✅ | ❌ | ❌ | ⚠️ |
| **Financial risk translation** | ✅ | ❌ | ❌ | ❌ |
| **Remediation scripts** | Paywalled | Paywalled | Paywalled | ❌ |

---

## 4. USP 3 — SOAR Automation at SMB Price Points

### The Claim

SOCVault is the **only SMB-priced platform** ($199/month) that includes a fully automated Security Orchestration, Automation, and Response (SOAR) engine with AI triage and a human approval gate.

### Why No SMB Tool Has SOAR

SOAR has historically required:
- Dedicated security engineers to write and maintain playbooks
- Integration with a full enterprise SIEM stack (months of professional services)
- Analyst teams to review and approve automated actions
- Per-incident pricing or enterprise licensing ($5,000–$20,000+/month)

**None of the SMB tools in the market have solved this.** The closest offering is Todyl, which has a basic SIEM with alert correlation — but no automated response playbooks, no AI triage, and no human approval gate for high-risk actions.

### SMB Competitor SOAR Comparison

| Capability | SOCVault | Intruder | Detectify | Guardz | Huntress | Todyl | Malwarebytes | Pentest-Tools |
|---|---|---|---|---|---|---|---|---|
| Alert ingestion (Wazuh/EDR) | ✅ | ❌ | ❌ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| Threat intel enrichment (AbuseIPDB, OTX) | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ |
| AI triage (contain vs escalate) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Automated containment playbooks | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ |
| Human approval gate | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ |
| Alert-to-containment time | <60 sec | N/A | N/A | Manual | Minutes | Minutes | Manual | N/A |

### The Economics Behind SOCVault's Advantage

SOCVault can deliver SOAR at $199/month because:
1. **Wazuh is free and open-source** — zero SIEM licensing cost
2. **Claude AI triage costs $0.057/alert** — vs £35+/hour for a human analyst
3. **Pre-built playbooks** — SMBs configure on day one, no professional services
4. **SaaS delivery** — Wazuh agents deploy in minutes, no on-site installation

Huntress, the closest SMB MDR competitor, costs $125–175/agent/month and requires a minimum agent commitment. For a 10-server SMB, Huntress = $1,250–$1,750/month vs SOCVault SOC Pro at $199/month flat — with SOCVault covering 50 Wazuh agents.

---

## 5. USP 4 — Full 8-Layer Attack Surface Coverage

### The Claim

SOCVault is the **only SMB-priced platform** that covers the complete attack surface in a single product: from passive external reconnaissance to real-time malware response. Every competitor in the SMB market covers one or two layers maximum.

### Layer Coverage Comparison Against SMB Competitors

| Layer | SOCVault | Intruder | Detectify | Guardz | Huntress | Todyl | Malwarebytes | Pentest-Tools | Sucuri |
|---|---|---|---|---|---|---|---|---|---|
| **L1 External Recon** | ✅ 15 steps | ✅ Partial | ✅ Partial | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ |
| **L2 Web AppSec** | ✅ Full | ✅ Basic | ✅ Full | ❌ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ WAF only |
| **L3 Mobile** | ✅ Full | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **L4 API Security** | ✅ Full | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **L5 Compliance** | ✅ Full | ❌ | ❌ | ⚠️ Basic | ❌ | ❌ | ❌ | ❌ | ❌ |
| **L6 Cloud Posture** | ✅ Full | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **L7 SOC/SIEM** | ✅ Full | ❌ | ❌ | ⚠️ Partial | ✅ Endpoint | ✅ Basic | ✅ Endpoint | ❌ | ❌ |
| **L8 Malware D&R** | ✅ AI-driven | ❌ | ❌ | ⚠️ Partial | ⚠️ Partial | ⚠️ Basic | ✅ Endpoint only | ❌ | ✅ Website only |
| **Layers covered** | **8/8** | 2/8 | 2/8 | 2/8 | 2/8 | 2/8 | 1/8 | 1/8 | 1/8 |

**The gap is not marginal. The best-covered SMB competitor covers 2 out of 8 layers.**

### Why Single-Platform Coverage Matters for SMBs

An SMB that patches together point solutions faces:

- **No correlation:** An Intruder.io finding about an exposed subdomain and a Malwarebytes malware detection on an endpoint are never connected — a human has to spot the link
- **No unified risk score:** Five different dashboards produce five different risk ratings with no common baseline
- **No orchestrated response:** When Guardz detects a phishing email and Huntress detects a process anomaly on an endpoint simultaneously, no tool knows to correlate them as a single attack chain
- **Compounding bills:** Intruder ($101) + Guardz (~$108 for 12 users) + Huntress (~$375 for 3 agents) + Malwarebytes ($67 for 10 devices) + Sucuri ($199/yr) = **$700+/month for fragmented partial coverage**

SOCVault replaces all of this with a single platform at $199/month.

---

## 6. USP 5 — Malware Detection & Response With AI Triage

### The Claim

SOCVault's L8 MDRM (Malware Detection & Response Manager) is the **only SMB solution** that combines multi-source malware detection with AI-generated family identification, severity scoring, autonomous remediation for isolated threats, and a human approval gate for system-wide threats — all within a single $199/month subscription.

### What SMB Competitors Actually Deliver

| Capability | SOCVault L8 | Malwarebytes Teams | Huntress | Guardz | Sucuri | Todyl |
|---|---|---|---|---|---|---|
| Detection source | ClamAV + YARA + Trivy + Nuclei + VirusTotal | Signature + ML | Process + memory | Email + endpoint | File scan | EDR signatures |
| Coverage | Endpoint + web server + containers | Endpoint only | Endpoint only | Endpoint + email | Website only | Endpoint only |
| AI family identification | ✅ Claude AI | ❌ Signature name | ❌ Threat name | ❌ Category label | ❌ Malware type | ❌ Alert label |
| Financial risk context | ✅ Per-incident £/$ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Auto-remediation | ✅ Confidence-gated | ✅ Quarantine | ⚠️ Via MSP | ❌ Alert only | ✅ Malware removal | ⚠️ Basic |
| Human approval gate | ✅ For system-wide threats | ❌ | ⚠️ MSP decides | ❌ | ❌ | ❌ |
| Post-remediation verification | ✅ Automated re-scan | ❌ | ❌ | ❌ | ✅ | ❌ |
| Incident report | ✅ AI-generated | ❌ | ⚠️ Manual | ❌ | ✅ Basic | ❌ |
| Price | $199/mo flat | $6.67/device/mo | $125–175/agent/mo | ~$9/user/mo | $199–$499/yr | $12/endpoint/mo |

### The Confidence-Gated Autonomy Difference

Malwarebytes quarantines everything it detects automatically — sometimes correctly, sometimes not, with no context about whether the "malicious" file is a production binary or a test script. Huntress routes findings to an MSP analyst who decides — adding human delay and cost.

SOCVault's MDRM applies a confidence threshold:

```
Confidence >95% AND isolated file/process
  → Auto-quarantine, process kill, blocklist update in <60 seconds
  → No human delay, no production risk

Confidence <95% OR system-wide impact (core services, databases)
  → Human approval gate: analyst sees full threat context,
    proposed commands, and business impact warning
  → Approves → Execute immediately
  → Rejects → Escalate with full audit trail
```

This is the design pattern that enterprise MDR teams use internally. SOCVault delivers it as a self-service SMB feature at $199/month.

---

## 7. USP 6 — 60-Second Onboarding

### The Claim

A new SOCVault user goes from first visit to first L1 scan result in under 5 minutes. No credit card for freemium. Domain ownership verified before paid scans. No agent installation for L1–L6. No sales call.

### SMB Competitor Onboarding Reality

| Product | Time to First Scan Result | Friction Points |
|---|---|---|
| **SOCVault** | 3–5 minutes | Business email + phone OTP only |
| **Intruder.io** | 20–40 minutes | Signup → domain verification → target config → scan queue |
| **Detectify** | 30–60 minutes | Signup → DNS TXT record → scan config → 14-day clock starts |
| **Guardz** | 15–30 minutes | Signup → Google Workspace/M365 OAuth → configuration |
| **Huntress** | Days–weeks | MSP must enrol → agent deployed on endpoint → scan runs |
| **Todyl** | 30–60 minutes | Signup → network agent deployment → configuration |
| **Pentest-Tools.com** | 10–20 minutes | Signup → target verification → scan config |
| **Malwarebytes** | 30–60 minutes | Account → agent deployed on device → scan |
| **Sucuri** | 30–60 minutes | Signup → DNS CNAME change (for WAF) → propagation wait |

### Why SOCVault Can Achieve This

- **No credit card required** — freemium removes the financial commitment barrier entirely
- **Fast freemium L1** — passive external recon runs immediately; domain ownership verification (DNS TXT or email) required before paid scans and active testing
- **No agent installation for L1–L6** — L1 runs entirely from AWS Lambda against publicly accessible infrastructure
- **No sales cycle** — product-led growth; the scan result IS the sales pitch
- **No configuration** — sensible defaults applied; user sees results before they've finished reading the UI

This onboarding model is why freemium conversion works. A user who reaches their first result in 3 minutes is a user who has already experienced the core value proposition before being asked to pay for anything.

---

## 8. USP 7 — Open-Source Scanning Core

### The Claim

SOCVault's detection engine is built entirely on production-grade open-source tooling — Wazuh, Nuclei, Semgrep, MobSF, CloudFox, Subfinder, httpx, Naabu. This eliminates scanner licence costs, ensures daily vulnerability template updates from the security community, and creates zero vendor lock-in at the tooling layer.

### The Commercial Advantage Over SMB Competitors

| Dimension | SOCVault (Open-Source Core) | Guardz | Huntress | Todyl | Pentest-Tools |
|---|---|---|---|---|---|
| Scanner licence cost | $0 | Proprietary | Proprietary | Proprietary | Proprietary |
| Vulnerability template updates | Community-driven (daily) | Vendor cycle | Vendor cycle | Vendor cycle | Vendor cycle |
| Template count (Nuclei) | 60,000+ | Vendor's own | N/A | N/A | Vendor's own |
| Audit transparency | Source-inspectable | Black box | Black box | Black box | Black box |
| Lock-in risk | None | High | High | High | High |

SOCVault's proprietary value is not in the scanners — it is in the **AI translation layer, the SOAR orchestration, the financial risk model, and the multi-tenant architecture** that sits above those tools. Any competitor acquiring SOCVault acquires a clean, licence-free tooling stack that can be extended without proprietary dependencies.

---

## 9. USP 8 — Compliance as Standard

### The Claim

SOCVault includes automated gap analysis against **PCI-DSS 4.0, UK GDPR, ISO 27001:2022, SOC 2 Type II, and Cyber Essentials Plus** as a standard feature of the paid tier. No add-on. No enterprise upsell. Every SMB-sized competitor either omits compliance entirely or covers it only at a surface level.

### Why Compliance Coverage Is Non-Negotiable for UK SMBs

- **UK Cyber Security and Resilience Bill (2026):** Mandatory incident reporting + minimum security standards for thousands of additional SMBs
- **PCI-DSS 4.0:** In force since March 2024 — mandatory for any business accepting card payments
- **UK GDPR / ICO:** £1.2B in fines issued in 2023; SMBs supplying public sector clients must demonstrate Cyber Essentials compliance
- **Cyber insurance underwriting:** 67% of UK insurers now require documented security posture evidence before writing policies

### SMB Competitor Compliance Coverage

| Framework | SOCVault | Intruder | Detectify | Guardz | Huntress | Todyl | Malwarebytes | Pentest-Tools | Sucuri |
|---|---|---|---|---|---|---|---|---|---|
| PCI-DSS 4.0 | ✅ Included | ❌ None | ❌ None | ⚠️ Limited | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |
| UK GDPR | ✅ Included | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |
| ISO 27001:2022 | ✅ Included | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |
| SOC 2 Type II | ✅ Included | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |
| Cyber Essentials Plus | ✅ Included | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None | ❌ None |

**No SMB-priced security scanner or endpoint tool provides compliance gap analysis against any of these frameworks as a standard feature.**

The only SMB-accessible compliance platforms are tools like Vanta and Drata — but these are **compliance evidence collection tools**, not security scanners. They collect questionnaire evidence and integrate with cloud providers to check configurations, but do not perform VAPT, SOAR, or malware detection. At $1,000+/month, they serve a different buyer (Series A+ startups preparing for SOC 2 audits). SOCVault produces compliance evidence as a byproduct of the security work itself.

### The Compliance Switching Cost

Every SOCVault scan creates a dated compliance artifact. After 18 months of scans, a customer has:
- A complete timestamped history of PCI-DSS gap findings and remediations
- Audit evidence accepted by insurers, auditors, and enterprise procurement teams
- A compliance posture trend that shows improvement over time

This data is stored in SOCVault's data model and cannot be migrated to a competing tool. Switching means starting the compliance history at zero — a cost that grows every month and becomes decisive by Year 2.

---

## 10. USP 9 — Conversational AI Security Assistant With Action Triggers

### The Claim

SOCVault includes a **conversational AI security assistant** powered by Anthropic Claude, embedded directly in the tenant dashboard. Tenants can ask natural-language security questions, receive Claude-reasoned responses with full extended thinking transparency, and — critically — **trigger live platform actions from within the chat interface**: launching scans, generating remediation scripts, approving SOAR playbooks, and creating compliance reports.

No competitor in the SMB security market offers this capability.

### What the Feature Does

```
Tenant: "Why is my security score 68? What's the most urgent thing to fix?"

Claude: [Reasoning — 8 seconds, extended thinking]
        "Your score is 68/100 primarily because of 3 critical findings:
         1. SQL injection in /api/v1/checkout — £18,400 financial exposure
         2. Exposed .git directory on prod.domain.com — £9,200 exposure
         3. RDP port 3389 open to internet — £6,500 exposure
         
         I recommend starting with the SQL injection — it's the highest
         financial risk and I can generate the fix now."

[Action Card] → Show all 12 findings | 1 credit
[Action Card] → Generate SQLi fix script | 2 credits
[Action Card] → Trigger L2 VAPT scan | 5 credits
[Action Card] → Generate board report | 5 credits
```

The entire interaction — from question to finding to fix — happens without leaving the chat window. Action results appear inline in the conversation as data tables, code blocks, or scan summaries.

### Competitor Landscape

| Product | Natural Language Security Q&A | Action Triggers from Chat | Live Scan Data Context | Credit-Based Consumption |
|---|---|---|---|---|
| **SOCVault** | ✅ Claude — extended thinking | ✅ 10 action types | ✅ Real-time tenant findings | ✅ Prepaid bundles |
| **Intruder.io** | ❌ | ❌ | ❌ | ❌ |
| **Detectify** | ❌ | ❌ | ❌ | ❌ |
| **Guardz** | ⚠️ Basic AI alerts only | ❌ | ❌ | ❌ |
| **Huntress** | ⚠️ Human analyst response (hours) | ❌ | ❌ | ❌ (flat fee) |
| **Todyl** | ❌ | ❌ | ❌ | ❌ |
| **Microsoft Copilot for Security** | ✅ | ⚠️ Limited to M365 actions | ⚠️ M365 only | ❌ ($4/hour, enterprise only) |

Microsoft Copilot for Security is the only comparable product — but it costs $4/hour, targets enterprise buyers, and is limited to the Microsoft stack. An SMB using AWS and non-Microsoft infrastructure gets nothing from it.

### Why This Is a Defensible USP

**Technical depth:** The AI assistant has access to the tenant's live scan database as grounding context. Claude's response is not generic security advice — it references the specific findings, scores, domains, and financial exposures from that tenant's actual scans. Building this requires deep integration with the scan data model, not just an LLM API call.

**Extended thinking:** Claude is called with `thinking.type = "enabled"` and `budget_tokens = 8192` for security questions. The reasoning chain is surfaced to the user as a collapsible "Reasoning" block — showing the inference steps that led to the recommendation. No SMB security tool exposes AI reasoning to end users. This builds trust with technical buyers.

**Action dispatch architecture:** The action trigger system routes from the chat interface to the same scan execution pipeline that runs scheduled scans — it is not a separate system. When a tenant clicks "Trigger L2 VAPT scan", it enqueues the same Fargate task that the automated scheduler would enqueue. This means the AI chat surface inherits all the concurrency, rate-limiting, and tenant-isolation guarantees of the core scan architecture.

**Credit mechanics create a flywheel:** Tenants who buy credits to ask questions discover action triggers. Tenants who trigger scans generate new findings. New findings generate new questions. Each completed AI session ends with unspent credits and a reason to return — driving repeat credit purchases and increasing LTV without any subscription upsell required.

### The Business Model Angle

The AI Chat feature is the only revenue stream where **higher usage = higher revenue with no incremental service delivery cost** (beyond Claude API token cost, which is bounded by 84% cache hit rate). Every other SOCVault revenue stream has a scan execution cost floor. AI Chat does not — a 5-message question-and-answer session costs SOCVault ~$0.05 in Claude tokens and generates $1–5 in credit revenue.

This creates an asymmetric marginal economics profile that makes AI Chat the highest-quality revenue layer in the portfolio.

---

## 11. Head-to-Head SMB Competitor Analysis  

### Intruder.io

**What they do:** External attack surface management — network scanning, port discovery, vulnerability detection. One of the most polished SMB-focused scanners in the market. $101/month (Essential plan). Raised $11M Series A in 2023.

**Where they are strong:** Clean UI, reliable scanning cadence, good subdomain and port coverage, emerging attack surface management features, solid CVE library. A genuine product that SMBs can use.

**Where SOCVault wins:**

| Dimension | Intruder.io $101/mo | SOCVault |
|---|---|---|
| Freemium tier | ❌ No free scan | ✅ Real 15-step scan, free forever |
| Financial risk translation | ❌ CVE IDs + CVSS scores | ✅ £/$ exposure per finding |
| Plain-English business summaries | ❌ Technical descriptions | ✅ Non-technical narrative |
| 1-click remediation scripts | ❌ Links to NVD advisories | ✅ Copy-pasteable bash commands |
| Email security (SPF/DKIM/DMARC) | ❌ Not covered | ✅ Step 3 of L1 Recon |
| Credential leak check (HIBP) | ❌ Not covered | ✅ Step 13 of L1 Recon |
| SOAR / automated response | ❌ None | ✅ Wazuh + Claude AI pipeline |
| Continuous SOC monitoring | ❌ None | ✅ Wazuh agents real-time |
| Compliance reporting | ❌ None | ✅ PCI, GDPR, ISO, SOC2 included |
| Malware detection & response | ❌ None | ✅ L8 MDRM (AI-driven) |
| Mobile app security | ❌ None | ✅ MobSF (Android + iOS) |
| API security (OWASP API Top 10) | ❌ None | ✅ Included |
| Cloud posture (AWS/Azure/GCP) | ❌ None | ✅ CloudFox/Pacu included |
| Onboarding time | ~20–40 min | ✅ <5 minutes |

**Verdict:** Intruder.io is what SOCVault's L1 + partial L2 layers would be if sold as a standalone product — without AI translation, SOAR, SOC, compliance, or malware response. At $101/month, it answers the question *"what's exposed on my network?"* but not *"what does that exposure cost my business?"* or *"what happens when something is actually compromised?"*

---

### Detectify

**What they do:** Continuous web application security scanner built for developers and dev-security teams. $89/month (Starter). Strong focus on DAST, with a Crowdsource researcher community for new vulnerability discovery.

**Where they are strong:** Deep web application coverage, continuous scanning (not one-off), solid developer integrations (Jira, Slack, GitHub), Crowdsource model keeps templates fresh.

**Where SOCVault wins:**

| Dimension | Detectify $89/mo | SOCVault |
|---|---|---|
| Target buyer | Developers / DevSec | SMB IT manager / business owner |
| Financial risk translation | ❌ Technical CVE output | ✅ Plain-English + £/$ exposure |
| Onboarding | ~30–60 min (DNS verification) | ✅ <5 minutes |
| Freemium | ⚠️ 14-day trial only | ✅ Free forever (1 scan/month) |
| External recon (WHOIS, IP rep, HIBP) | ❌ Web-focused only | ✅ Full 15-step recon |
| SOAR automation | ❌ None | ✅ Full pipeline |
| Continuous SOC monitoring | ❌ None | ✅ Real-time Wazuh |
| Compliance gap analysis | ❌ None | ✅ Full framework coverage |
| Malware detection | ❌ None | ✅ L8 MDRM |
| Mobile / API / Cloud layers | ❌ None | ✅ L3 / L4 / L6 included |

**Verdict:** Detectify and SOCVault serve adjacent but distinct buyers. Detectify serves a technical team that understands CVEs and wants continuous web scanning integrated into a CI/CD pipeline. SOCVault serves the IT manager or business owner who needs to understand financial risk and have threats responded to — not just listed. Where they overlap, SOCVault wins on breadth, AI translation, and the freemium conversion hook.

---

### Guardz

**What they do:** AI-powered SMB cybersecurity platform covering the user-centric attack surface — phishing emails, dark web credential exposure, Google Workspace/Microsoft 365 security, endpoint protection, and basic compliance posture. ~$9/user/month. One of the most direct conceptual competitors to SOCVault at the SMB tier.

**Where they are strong:** Strong email and identity threat coverage, good Google Workspace and M365 integration, MSP-friendly distribution, genuine AI-assisted alert prioritisation, easy onboarding for Microsoft/Google shops.

**Where SOCVault wins:**

| Dimension | Guardz ~$9/user/mo | SOCVault |
|---|---|---|
| External VAPT (scanning attack surface) | ❌ No scanning | ✅ L1–L6 full active scanning |
| Web application security testing | ❌ None | ✅ L2 DAST + SAST |
| Network port / service discovery | ❌ None | ✅ L1 Recon (Naabu top-100 ports) |
| Financial risk quantification | ❌ Risk level tags only | ✅ Per-finding £/$ exposure |
| SOAR automation with playbooks | ❌ Alert-only | ✅ Full Wazuh SOAR pipeline |
| Human approval gate for containment | ❌ None | ✅ Integrated |
| Mobile binary security (L3) | ❌ None | ✅ MobSF included |
| Cloud posture (L6) | ❌ None | ✅ CloudFox/Pacu included |
| PCI-DSS / ISO 27001 compliance | ⚠️ Basic posture only | ✅ Full gap analysis per framework |
| Malware remediation (AI-driven) | ⚠️ Alert + basic quarantine | ✅ L8 MDRM with confidence-gated auto-remediation |
| Freemium tier | ⚠️ Limited trial | ✅ Real free scan |

**Verdict:** Guardz protects the *user layer* — email, identity, credentials, SaaS apps. SOCVault protects the *infrastructure layer* — the domain, web application, servers, endpoints, cloud. These are genuinely complementary, but an SMB that chooses Guardz has no visibility into their external attack surface, web application vulnerabilities, cloud misconfigurations, or mobile app security. Guardz answers *"are my users being targeted?"* SOCVault answers *"where are the holes in my infrastructure?"* — and then responds to threats across all of them.

---

### Huntress

**What they do:** Managed Detection & Response (MDR) purpose-built for SMBs, sold exclusively through MSP partners. Covers endpoint process detection, ransomware canaries, managed antivirus, and security awareness training. $125–175/agent/month.

**Where they are strong:** Excellent endpoint threat hunting, human analyst review team (24/7), strong ransomware canary detection, deeply MSP-integrated, trusted by the MSP community.

**Where SOCVault wins:**

| Dimension | Huntress $125–175/agent/mo | SOCVault $199/mo flat |
|---|---|---|
| Self-service access | ❌ MSP-only; can't buy direct | ✅ Direct signup in <5 minutes |
| External attack surface | ❌ Endpoint-only | ✅ L1–L6 external + web + cloud |
| Financial risk translation | ❌ Threat descriptions | ✅ Per-finding £/$ exposure |
| Compliance reporting | ❌ None | ✅ PCI, GDPR, ISO, SOC2 |
| SOAR automation playbooks | ⚠️ Human-mediated via MSP | ✅ Automated + human gate |
| Cost for 10-server SMB | $1,250–$1,750/month | ✅ $199/month (50-agent flat) |
| Freemium entry | ❌ None | ✅ Real free scan |
| Web application security | ❌ None | ✅ L2 DAST/SAST |
| Cloud posture | ❌ None | ✅ L6 included |

**Verdict:** Huntress is an excellent endpoint MDR — but it requires an MSP intermediary, costs 6–9× more for a typical SMB deployment, and covers only the endpoint layer. SOCVault includes equivalent continuous endpoint monitoring via Wazuh (which Huntress's architecture mirrors) at $199/month flat — while also covering external recon, web apps, compliance, cloud, and malware AI triage that Huntress doesn't touch.

**Where Huntress beats SOCVault:** Huntress has 24/7 human analysts reviewing endpoint findings. Their human-backed threat hunting catches subtle process-level anomalies that automated AI may miss. For endpoint-heavy SMBs with a high threat profile, Huntress + SOCVault (for external surface coverage) is the ideal combination — not a substitution.

---

### Todyl

**What they do:** Multi-module SMB security platform covering SASE (network security), EDR, SIEM, and basic SOAR. $12/endpoint/month. Targets IT-managed SMBs and MSPs.

**Where they are strong:** Multi-module architecture (most SMB tools are single-layer), network-level security (ZTNA/SASE), basic SIEM log aggregation, growing MSP traction.

**Where SOCVault wins:**

| Dimension | Todyl $12/endpoint/mo | SOCVault $199/mo flat |
|---|---|---|
| External VAPT (active scanning) | ❌ None | ✅ L1–L6 |
| AI financial risk translation | ❌ Alert labels only | ✅ Per-finding £/$ exposure |
| Automated SOAR playbooks | ❌ Basic alert routing only | ✅ Full playbooks + human gate |
| Compliance gap analysis | ❌ None | ✅ PCI, GDPR, ISO, SOC2 |
| Malware AI triage + auto-remediation | ❌ Signature detection only | ✅ L8 MDRM |
| Freemium entry | ❌ None | ✅ Real free scan |
| Cost for 20-device SMB | $240/month | ✅ $199/month (all features) |

**Verdict:** Todyl is network and endpoint protection with basic SIEM. It doesn't scan or test anything — it monitors. SOCVault actively probes the attack surface to find vulnerabilities before attackers do, then monitors and responds in real time. The scanning + monitoring combination is what SMBs need; Todyl only offers half of it.

---

### Malwarebytes for Teams

**What they do:** Endpoint security and malware protection for small businesses. $6.67/device/month ($80/device/year). The SMB evolution of the consumer Malwarebytes product.

**Where they are strong:** Effective endpoint malware detection, familiar brand, lightweight agent, ransomware rollback capability, very affordable per-device pricing.

**Where SOCVault wins:**

| Dimension | Malwarebytes $6.67/device/mo | SOCVault |
|---|---|---|
| External attack surface visibility | ❌ None — endpoint only | ✅ L1–L6 full external coverage |
| Web application security | ❌ None | ✅ L2 AppSec |
| Financial risk translation | ❌ Threat name + quarantine status | ✅ Per-finding £/$ exposure |
| SOAR automation | ❌ None | ✅ Full pipeline |
| Compliance reporting | ❌ None | ✅ Full framework coverage |
| Malware AI analysis (family ID, severity) | ❌ Signature match only | ✅ Claude AI analysis |
| Human approval gate | ❌ None | ✅ For system-wide threats |
| Cost for 20-device SMB | $134/month (endpoint only) | ✅ $199/month (all 8 layers) |

**The key distinction:** Malwarebytes detects and removes malware after it has arrived on an endpoint. SOCVault's L1–L6 scanning finds the vulnerabilities that allow malware to arrive in the first place. Malwarebytes is the ambulance; SOCVault is the guard at the gate plus the ambulance (L8 MDRM).

**Where Malwarebytes beats SOCVault:** Per-device endpoint detection at $6.67/device is very cost-efficient for endpoint-only protection. For an SMB that only wants basic malware protection and has no compliance obligation or external infrastructure to protect, Malwarebytes is adequate. SOCVault is for SMBs that need to understand and manage their full security posture.

---

### Pentest-Tools.com

**What they do:** Cloud-based vulnerability scanner targeting security professionals and SMBs with technical IT teams. $79–$299/month depending on plan. Covers network scanning, web app scanning, and basic reporting.

**Where they are strong:** Wide vulnerability coverage, on-demand testing, affordable for technical teams, useful for spot-check assessments.

**Where SOCVault wins:**

| Dimension | Pentest-Tools.com $79–$299/mo | SOCVault |
|---|---|---|
| Target buyer | Technical security professionals | SMB IT managers + business owners |
| Financial risk translation | ❌ Technical reports | ✅ Plain-English + £/$ exposure |
| AI-powered analysis | ❌ None | ✅ Claude AI per finding |
| Continuous monitoring | ❌ On-demand only | ✅ Real-time Wazuh |
| SOAR automation | ❌ None | ✅ Full pipeline |
| Compliance reporting | ❌ None | ✅ Full framework coverage |
| Malware detection & response | ❌ None | ✅ L8 MDRM |
| Freemium | ⚠️ 1 free scan/24h (feature-limited) | ✅ Full 15-step scan, free forever |
| Onboarding | 10–20 min | ✅ <5 minutes |

**Verdict:** Pentest-Tools.com is a professional scanning toolkit — it produces raw vulnerability data for a technically-skilled operator to interpret. SOCVault is a complete security platform that translates, responds to, and reports on the same data for a non-security audience. Different tool for a different buyer.

---

### Sucuri

**What they do:** Website security platform covering web application firewall (WAF), website malware scanning, DDoS protection, and CDN. $199–$499/year. Focused entirely on website and web server protection.

**Where they are strong:** Strong WAF protection, effective website malware detection and removal, CDN included, good performance history for WordPress/CMS sites, reasonable pricing.

**Where SOCVault wins:**

| Dimension | Sucuri $199–$499/yr | SOCVault |
|---|---|---|
| External attack surface beyond web | ❌ Website only | ✅ Subdomains, ports, services, DNS |
| Network / server scanning | ❌ None | ✅ L1–L2 |
| Financial risk translation | ❌ Malware type + clean status | ✅ Per-finding £/$ exposure |
| SOAR automation | ❌ None | ✅ Full pipeline |
| Compliance reporting | ❌ None | ✅ Full framework coverage |
| Continuous endpoint monitoring | ❌ None | ✅ Wazuh agents |
| AI malware analysis | ❌ Signature-based | ✅ Claude AI family identification |
| Freemium | ❌ None | ✅ Real free scan |
| Mobile / API / Cloud | ❌ None | ✅ L3 / L4 / L6 |

**The complementary case:** Sucuri's WAF is a legitimate layer of defence for website-only protection and is not directly substituted by SOCVault (SOCVault does not deploy a WAF). For SMBs that want both a WAF and full attack surface visibility, Sucuri + SOCVault is a reasonable combination. However, SOCVault's L2 AppSec scanning and L8 MDRM replaces much of Sucuri's malware detection value at a lower total cost.

---

## 12. SMB Feature Matrix

Full capability comparison across the actual SMB security market:

| Feature | SOCVault | Intruder | Detectify | Guardz | Huntress | Todyl | Malwarebytes | Pentest-Tools | Sucuri | Defender Biz |
|---|---|---|---|---|---|---|---|---|---|---|
| **DISCOVERY & RECON** | | | | | | | | | | |
| WHOIS + registrar expiry | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Full DNS analysis | ✅ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| SPF / DKIM / DMARC | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| SSL/TLS audit | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| HTTP security headers | ✅ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Certificate transparency | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Subdomain discovery | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| Live host validation | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| Port / service discovery | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Technology fingerprinting | ✅ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| IP reputation (AbuseIPDB) | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Credential leak (HIBP) | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Subdomain takeover | ✅ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **WEB APPLICATION** | | | | | | | | | | |
| DAST (active web scanning) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ WAF | ❌ |
| SAST (static code analysis) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Web shell detection | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **MOBILE** | | | | | | | | | | |
| Android APK analysis | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| iOS IPA analysis | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **API SECURITY** | | | | | | | | | | |
| OWASP API Top 10 | ✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| **COMPLIANCE** | | | | | | | | | | |
| PCI-DSS 4.0 | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| UK GDPR | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| ISO 27001:2022 | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| SOC 2 Type II | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cyber Essentials Plus | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **CLOUD SECURITY** | | | | | | | | | | |
| AWS posture (IAM, S3, EC2) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Azure posture | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| GCP posture | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **SOC & RESPONSE** | | | | | | | | | | |
| Real-time endpoint monitoring | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| SOAR automation playbooks | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| AI alert triage | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Malware detection | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| AI malware family identification | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Confidence-gated auto-remediation | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| Human approval gate | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **AI & REPORTING** | | | | | | | | | | |
| Financial risk (£/$) per finding | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Plain-English AI summaries | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 1-click remediation scripts | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Workspace Health Score | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **BUSINESS MODEL** | | | | | | | | | | |
| Freemium (real scans, free forever) | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ |
| Self-serve (<5 min to first scan) | ✅ | ⚠️ | ⚠️ | ✅ | ❌ | ⚠️ | ✅ | ⚠️ | ⚠️ | ✅ |
| Under $200/mo for full SOC coverage | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legend:** ✅ Full native support | ⚠️ Partial / limited / add-on | ❌ Not available

---

## 13. SMB Pricing Comparison

### Monthly Cost for Realistic SMB Coverage

Scenario: A 30-person UK business with one web application, 10 servers, and a cloud presence on AWS. They process card payments (PCI-DSS) and hold UK customer data (GDPR).

**Patching together SMB point solutions:**

| Coverage Layer | Best SMB Tool | Monthly Cost |
|---|---|---|
| External recon + CVE scanning | Intruder.io Essential | $101 |
| Web application scanning | Detectify Starter | $89 |
| Email + dark web + identity monitoring | Guardz (30 users) | $270 |
| Endpoint malware + ransomware | Malwarebytes Teams (10 devices) | $67 |
| Endpoint MDR (10 servers) | Huntress (10 agents) | $1,500 |
| Website malware + WAF | Sucuri Pro | $50 |
| Compliance evidence collection | Vanta Starter (minimum) | $833 |
| **Total — fragmented stack** | | **$2,910/month** |
| **Coverage gaps remaining** | | Mobile, API, cloud posture, SOAR, AI translation |

**SOCVault SOC Pro:** **$199/month** — covers all 8 layers including the gaps not addressed by the fragmented stack.

**SOCVault is 93% cheaper than the equivalent SMB point-solution stack — and still more comprehensive.**

### Price-Per-Layer Comparison

| Platform | Monthly Price | Layers Covered | Cost per Layer |
|---|---|---|---|
| **SOCVault SOC Pro** | **$199** | **8** | **$24.88/layer** |
| Intruder.io Essential | $101 | 2 | $50.50/layer |
| Detectify Starter | $89 | 2 | $44.50/layer |
| Guardz (10 users) | $90 | 2 | $45.00/layer |
| Huntress (5 agents) | $750 | 2 | $375.00/layer |
| Todyl (10 endpoints) | $120 | 2 | $60.00/layer |
| Malwarebytes (10 devices) | $67 | 1 | $67.00/layer |
| Pentest-Tools.com | $79–$299 | 1–2 | $79–$149/layer |
| Sucuri | $17–$41/mo | 1 | $17–$41/layer |

### The Freemium Value Gap

SOCVault's free tier provides more external attack surface intelligence than several paid SMB plans:

| Product | Price | External Recon Steps Covered |
|---|---|---|
| **SOCVault Free** | **$0** | **15 steps (WHOIS, DNS, SPF/DKIM/DMARC, SSL, headers, CT, subdomains, live hosts, ports, fingerprinting, IP rep, domain rep, HIBP, takeover, banners)** |
| Intruder.io Essential | $101/mo | ~5 steps (subdomains, live hosts, ports, partial SSL, partial headers) |
| Detectify Starter | $89/mo | ~6 steps (subdomains, live hosts, headers, SSL, CT, takeover) |
| Pentest-Tools.com | $79/mo | ~4 steps (ports, basic web, partial DNS) |

---

## 14. Market Fit Summary

### Why SOCVault Has Strong Market Fit

**1. The problem is real and growing.** 46% of UK SMBs were breached in 2023 (Hiscox). 62% have no formal security programme (UK Government Cyber Breaches Survey 2024). Regulatory pressure (PCI-DSS 4.0, UK Cyber Resilience Bill) is converting passive SMBs into active buyers.

**2. Every existing SMB tool is a point solution.** The market is fragmented. Intruder scans the perimeter. Guardz watches the user. Huntress monitors the endpoint. Malwarebytes catches malware. No SMB tool connects these layers, translates them into financial risk, and responds automatically. SOCVault is the first integrated platform.

**3. Price is not the barrier — translation is.** SMBs don't buy security because they don't understand the risk in terms they can act on. SOCVault's financial risk translation converts a technical finding into a business decision. This is the conversion mechanism that all point solutions lack.

**4. The freemium strategy creates organic acquisition.** No SMB competitor offers a real free scan. SOCVault's freemium tier is the product-led growth engine that fills the top of the funnel with zero CAC — users arrive because they want to know their Health Score, and they convert because they can't ignore their financial exposure figure.

**5. The compliance mandate is creating non-discretionary spend.** Every UK SMB that processes cards (PCI-DSS) or holds personal data (GDPR) now faces mandatory compliance requirements. SOCVault turns compliance from a scary audit into an automated dashboard. No SMB competitor provides this.

**6. The SOAR gap is a genuine white space.** Zero SMB-priced tools offer automated incident response. Huntress gets close but requires an MSP intermediary and costs $1,250+/month for 10 agents. SOCVault's SOAR is native, automated, and included at $199/month. This is a genuine capability gap in the market that SOCVault occupies alone.

### The Ideal SOCVault Customer Profile vs Competitor Profiles

| Customer Type | Best Fit |
|---|---|
| SMB IT manager who wants to see full attack surface + respond to threats + meet compliance | **SOCVault** — only product that covers all three |
| Developer who wants continuous web app scanning integrated into CI/CD | Detectify |
| SMB that only wants external network scanning, no AI needed | Intruder.io |
| SMB deep in Microsoft 365 / Google Workspace who wants user/email/identity protection | Guardz (complementary to SOCVault) |
| MSP managing SMB endpoints who needs deep process-level threat hunting | Huntress (complementary to SOCVault) |
| SMB that only wants endpoint malware protection at minimum cost | Malwarebytes |
| SMB with a WordPress site that just needs website malware removal | Sucuri |

**The key insight:** Guardz, Huntress, and Malwarebytes are **complementary** to SOCVault, not competitive substitutes. SOCVault's L1–L6 external scanning and L7–L8 SOC/malware response covers the infrastructure layer that those tools don't touch. The ideal SMB security stack for a regulated UK business is SOCVault ($199/mo) + optionally Guardz ($90/mo for user/email layer) — total $289/month for comprehensive coverage across all vectors.

---

## 15. Moat & Defensibility

### How Each USP Resists Imitation

| USP | Time for SMB Competitor to Copy | Barrier |
|---|---|---|
| AI financial translation | 12–18 months | Prompt calibration depth, Claude-specific reasoning quality, real-world data flywheel |
| Freemium with real scan value | 6–12 months | Requires high margin to fund free infrastructure; SMB competitors with lower margins can't absorb the cost |
| SOAR at $199/mo | 18–24 months | Requires full SIEM + orchestration rebuild; scanning tools (Intruder, Detectify) aren't architected for this |
| 8-layer integrated coverage | 24–36 months | Each layer requires separate deep integration expertise; most competitors are 1–2 layer specialists |
| Malware AI triage | 12–18 months | MDRM confidence-gating design is novel; endpoint-only tools (Malwarebytes, Huntress) would need to expand architecture |
| 60-second onboarding | 6–12 months | Requires PLG rethink; MSP-channelled tools (Huntress) structurally cannot do self-serve |
| Compliance as standard | 12–18 months | Framework mapping is labour-intensive; scanning tools haven't built this (Intruder, Detectify) |
| Compliance history moat | Permanent (per-customer) | Dated artifacts accumulate in SOCVault — switching costs grow every month; can't be migrated |
| Conversational AI with action triggers | 18–24 months | Requires deep scan data model integration, extended thinking prompt design, credit system, action dispatch — not just an LLM API wrapper; context richness improves with tenure |

### The Compounding Data Moat

As SOCVault processes scans at scale:
- **Scan corpus → better AI prompts:** Financial risk calibration improves against real breach costs
- **Cross-tenant threat intelligence:** Threats detected across all tenants create a shared early-warning signal unavailable to single-tenant tools
- **Compliance benchmarking:** *"Your PCI-DSS score is 71/100 — the UK e-commerce median is 58/100"* — only possible with dataset scale

None of this data is available to a new entrant or to a point solution that only covers one layer.

---

*SOCVault Ltd — Confidential | June 2026 | contact: mutexsystemsltd@gmail.com*
