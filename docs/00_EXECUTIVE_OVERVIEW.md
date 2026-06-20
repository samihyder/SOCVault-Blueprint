# SOCVault — Executive Overview
**The Unified AI-Enabled Cybersecurity Solution for SMBs**

---

## The Problem

Small and Medium-Sized Businesses (SMBs) are the most targeted segment in cybersecurity yet the least protected. Three structural barriers trap them:

| Barrier | Reality |
|---|---|
| **Capital** | Traditional VAPT engagements cost $10,000–$50,000/year — inaccessible for <200-employee firms |
| **Talent** | SMBs cannot recruit or retain specialist security engineers |
| **Translation** | Raw CVE outputs and technical logs are meaningless to non-technical business owners |

The average SMB breach costs **$4.45M** (IBM Cost of a Data Breach 2024), yet 60% of SMBs close within 6 months of a major cyber incident. The market is large, underserved, and in pain.

---

## The Solution: SOCVault

SOCVault is the **unified AI-enabled cybersecurity solution** for SMBs. It consolidates the complete security maturity lifecycle — eight attack surface layers — into a single multi-tenant SaaS platform, powered by Anthropic Claude AI for detection, triage, financial risk translation, and automated response.

**Core Value Proposition:** A non-technical SMB owner logs in with a business email, enters their domain, and receives a plain-English financial risk report within minutes — with one-click remediation scripts. No security expertise required. No fragmented tools. No enterprise price tag.

**What Makes It Unified:** Every competing SMB tool covers 1–2 layers. SOCVault covers all 8 — external recon, web application security, mobile, API, compliance, cloud posture, real-time SOC, and AI-driven malware response — in one dashboard, with one AI engine, one health score, and one integrated response pipeline.

### What SOCVault Does

```
[SMB Domain / IP / Endpoint]
         │
         ▼
[Unified 8-Layer Scanning Engine]
  L1 External Recon  ·  L2 Web AppSec  ·  L3 Mobile  ·  L4 API
  L5 Compliance      ·  L6 Cloud       ·  L7 SOC/SIEM  ·  L8 Malware D&R
         │
         ▼
[Claude AI — Unified Intelligence Layer]
  · Financial risk (£/$) per finding
  · Plain-English business summaries
  · Remediation scripts
  · Automated SOAR triage & response
         │
         ├──► Executive Risk Report  (Health Score + total exposure)
         ├──► 1-Click Remediation Scripts  (per vulnerability)
         ├──► SOAR Auto-Response  (contain, quarantine, block)
         └──► Compliance Register  (PCI-DSS · GDPR · ISO 27001 · SOC2 · CE+)
```

### Scanning Layers

| Layer | Tier | Tools | What It Finds |
|---|---|---|---|
| **L1 — Recon** | **Free** | Subfinder, Naabu, httpx, sslyze, checkdmarc, crt.sh, HaveIBeenPwned | WHOIS/DNS analysis, subdomain discovery, port scanning, SSL/TLS audit, HTTP security headers, email security (SPF/DKIM/DMARC), IP/domain reputation, credential leak check, technology fingerprinting, subdomain takeover detection |
| **L2 — Web AppSec** | Paid | Nuclei, Semgrep, OWASP ZAP, Trivy | CVEs, injection flaws, outdated libraries, web shell detection |
| **L3 — Mobile** | Paid | MobSF | Android/iOS binary vulnerabilities, MASVS compliance |
| **L4 — API** | Paid | Nuclei API templates | Auth bypass, OWASP API Top 10 |
| **L5 — Compliance** | Paid | Custom rule engine, Prowler | PCI-DSS, GDPR, ISO 27001, SOC2 gap analysis |
| **L6 — Cloud** | Paid | CloudFox, Pacu, Prowler | IAM misconfigurations, privilege escalation paths |
| **L7 — SOC** | SOC Pro | Wazuh + Claude AI | Real-time threat detection, automated SOAR response |
| **L8 — Malware Detection & Response** | SOC Pro | ClamAV, YARA, Trivy, Nuclei webshell templates | Malware detection on endpoints and web servers; Claude AI determines family, severity, and generates quarantine + removal commands; auto-remediates isolated threats; human-gated for system-wide incidents |

---

## Market Opportunity

| Segment | Size |
|---|---|
| Global SMB Cybersecurity Market (2024) | $67.4B |
| Projected (2030) | $156.2B |
| CAGR | ~15.2% |
| Target addressable SMBs (UK + US + AU) | ~8.4 million businesses |
| Willing-to-pay segment (50–500 employees) | ~2.1 million |

**Immediate TAM:** UK-first launch targeting 450,000 SMBs in financial services, e-commerce, healthcare, and professional services — all under active regulatory pressure (GDPR, FCA, NHS Digital).

---

## Business Model

```
FREEMIUM  ──►  PAY-PER-SCAN  ──►  SOC SUBSCRIPTION
(Acquire)       (Monetise)          (Retain)
```

| Tier | Price | What's Included |
|---|---|---|
| **Free** | $0 | 1 Recon scan/month, 1 domain, financial risk map |
| **Web VAPT** | $15/IP/month | Full SAST/DAST, CVE remediation scripts |
| **Mobile** | $20/app/month | MobSF binary analysis, MASVS report |
| **Cloud** | $25/env/month | CloudFox/Pacu audit, IAM risk map |
| **SOC Pro** | $199/month flat | Unlimited scans, 50 Wazuh agents, SOAR playbooks, live Claude triage |

**Gross margin per paid VAPT scan: ~97.6%** (COGS ≈ $0.36 per scan; revenue = $15.00)

**Platform layers:** 8 core scanning layers (L1–L8) plus **L9 AI Agent Scan** (SOC Pro). See `03_REQUIREMENTS.md`.

---

## Competitive Landscape

| Competitor | Price | SMB Focus | AI Translation | Auto-Remediation |
|---|---|---|---|---|
| Tenable.io | $3,000+/yr | Partial | None | None |
| Qualys | $2,500+/yr | No | None | None |
| Detectify | $89/mo | Partial | None | None |
| Intruder.io | $101/mo | Yes | None | None |
| **SOCVault** | **$0–$199/mo** | **Yes** | **Yes (Claude AI)** | **Yes (SOAR)** |

SOCVault's unique moat: **AI-powered financial risk translation** that turns raw CVEs into dollar-denominated business risk, plus **automated SOAR playbooks** at a price point accessible to any SMB.

---

## Traction & Milestones

| Milestone | Target Date |
|---|---|
| AWS staging MVP (CI/CD + auth + L1 + Claude) | Week 8 (August 2026) |
| Production cutover live (`api.socvault.io`) | Week 17+ (when cutover checklist complete — Milestone 2.1) |
| 10 beta clients onboarded | Week 16 (October 2026) |
| First paid conversion | Week 18 (November 2026) |
| 50 paying clients | February 2027 (~M8) |
| $10K MRR | February 2027 (~M8) — Seed unlock with 50 clients |
| 323 clients · $22K MRR (M18) | November 2027 — EBITDA milestone |
| Cash-flow break-even | September 2028 (Month 28) |
| Seed deck ready | Pre-Seed outcome; Seed close Month 15 (Aug 2027) |

---

## Team Capability Requirements

| Role | Status | When Needed |
|---|---|---|
| Founding Engineer (Python/DevSecOps) | [TBD] | Immediate |
| AI/ML Engineer | [TBD] | Phase 2 |
| Frontend Engineer (React/TS) | [TBD] | Phase 2 |
| Sales / GTM Lead | [TBD] | Phase 3 |
| Compliance Advisor (GDPR/ISO27001) | Contractor | Phase 2 |

---

## Funding Ask (Pre-Seed)

| Item | Amount |
|---|---|
| 12-month runway (lean team of 3) | $180,000 |
| AWS infrastructure (12 months) | $24,000 |
| Security tooling licences | $12,000 |
| Legal / compliance | $15,000 |
| Marketing & GTM | $20,000 |
| **Total Ask** | **$251,000** |

Expected outcome: 50 paying clients, $10K MRR, product-market-fit validation, Seed deck ready.
