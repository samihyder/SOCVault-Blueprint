# SOCVault — B2B Channel Strategy
## Marketplace, Hosting Provider & Partner Distribution
**Version 1.0 | June 2026**
**Confidential — For Internal & Investor Use**

---

> *SOCVault's direct sales motion builds the product and proves the model. The channel motion — cloud marketplaces, hosting providers, MSPs, and telcos — is what turns a successful SaaS into a market-defining platform.*

---

## Table of Contents

1. [Channel Strategy Overview](#1-channel-strategy-overview)
2. [AWS Marketplace Listing](#2-aws-marketplace-listing)
3. [Azure Marketplace Listing](#3-azure-marketplace-listing)
4. [Google Cloud Marketplace](#4-google-cloud-marketplace)
5. [Hosting Provider Partnerships](#5-hosting-provider-partnerships)
6. [MSP / MSSP Channel Programme](#6-msp--mssp-channel-programme)
7. [Domain Registrar & DNS Provider Integrations](#7-domain-registrar--dns-provider-integrations)
8. [Cyber Insurance Partnerships](#8-cyber-insurance-partnerships)
9. [Telecoms / ISP Partnerships](#9-telecoms--isp-partnerships)
10. [Channel Revenue Model](#10-channel-revenue-model)
11. [Why This Is a Strong Market Fit](#11-why-this-is-a-strong-market-fit)
12. [Implementation Roadmap](#12-implementation-roadmap)

---

## 1. Channel Strategy Overview

### The Core Insight

Every SMB already has a relationship with a cloud provider, a hosting company, a domain registrar, or an ISP. These providers have three things SOCVault needs:

1. **Existing trust** — the SMB already pays them and trusts their recommendations
2. **Infrastructure context** — they can see the customer's servers, domains, and configurations
3. **Distribution at scale** — millions of SMB customers in a single channel agreement

The SOCVault direct sales motion acquires customers one at a time. The channel motion acquires thousands of customers through a single partner contract.

### Channel Tiers

```
TIER 1 — CLOUD MARKETPLACES
  AWS, Azure, Google Cloud
  → Access to enterprise procurement workflows + committed cloud spend drawdown
  → Target: mid-market and enterprise SOC Pro clients

TIER 2 — HOSTING PROVIDERS
  Fasthosts, GoDaddy, Kinsta, WP Engine, Cloudways, DigitalOcean, Linode
  → Access to millions of SMBs who already host with them
  → Target: SMB Freemium-to-VAPT conversion at massive scale

TIER 3 — MSP / MSSP PARTNERS
  Managed Service Providers who resell SOCVault to their SMB client base
  → Access to pre-built SMB relationships with monthly billing already in place
  → Target: SOC Pro white-label resale

TIER 4 — ECOSYSTEM PARTNERS
  Domain registrars, cyber insurers, telcos, accountancy platforms
  → Distribution through trusted, non-security intermediaries
  → Target: freemium acquisition at zero CAC
```

### Channel vs Direct Revenue Mix (Projected)

| Year | Direct Revenue | Channel Revenue | Channel % |
|---|---|---|---|
| 1 | $108,000 | $0 | 0% |
| 2 | $378,000 | $162,000 | 30% |
| 3 | $900,000 | $900,000 | 50% |
| 5 | $8,100,000 | $9,900,000 | 55% |

Channel revenue carries lower gross margin (~65–75% vs ~99% direct) due to partner commissions and marketplace fees, but requires zero incremental sales cost and scales without headcount.

---

## 2. AWS Marketplace Listing

### Why AWS Marketplace

AWS Marketplace is where enterprises discover and procure SaaS tools directly billed to their AWS account. It is the single highest-intent B2B procurement channel in the cloud market:

- **350,000+ active customers** buying from AWS Marketplace
- **No procurement friction:** listed tools bill directly through the AWS account — no separate vendor invoice, no AP process
- **Committed Spend drawdown:** Enterprise customers with AWS Enterprise Discount Programmes (EDPs) can apply their committed AWS spend toward Marketplace purchases — zero-cost to the customer's software budget
- **30–40% faster deal cycles:** Procurement is already approved through AWS; no new vendor onboarding required

### SOCVault Positioning on AWS Marketplace

**Listing name:** SOCVault — Unified AI-Enabled Cybersecurity for SMBs  
**Category:** Security → Vulnerability Management + SIEM/SOAR  
**Pricing model:** SaaS subscription (metered)

| Plan | Monthly Price (AWS Marketplace) | Notes |
|---|---|---|
| Web VAPT | $15/IP/month | Per-target billing via Marketplace metering API |
| SOC Pro | $199/month | Flat subscription; Wazuh agent limit = 50 |
| SOC Enterprise | $499/month | Unlimited agents, white-label, SLA |

### Technical Requirements for AWS Listing

- **SaaS listing type** (customer does not deploy to their own AWS account — SOCVault is multi-tenant SaaS)
- **AWS Marketplace Metering Service** integration for per-IP variable billing
- **AWS CloudFormation template** (optional but recommended) for customers who want to deploy Wazuh agents using IaC
- **PAYG (Pay As You Go)** model — no annual commitment required
- **1-click subscribe** flow → redirects to SOCVault onboarding with `aws_marketplace_token` in URL → auto-provisions tenant

### AWS Marketplace Go-To-Market Leverage

1. **AWS ISV Accelerate Programme:** Apply for co-sell designation — AWS field sales teams actively refer listed ISVs to enterprise customers. Accepted ISVs get introductions to AWS account teams working with matching customer profiles.
2. **AWS SMB Competency:** Achieve AWS SMB Competency designation — listed as a validated SMB security solution in the AWS Partner Network (APN) directory
3. **AWS Security Competency:** Long-term target (Year 2) — requires 3+ enterprise reference customers and technical review. Dramatically increases AWS-referred deal volume.
4. **AWS Activate sponsorship:** SOCVault can apply for AWS Activate credits ($25,000–$100,000) as an early-stage SaaS — offsetting infrastructure costs during the pre-revenue phase

### Implementation Steps

| Step | Task | Owner | Timeline |
|---|---|---|---|
| 1 | Register as AWS Marketplace seller | Founder | Week 1 |
| 2 | Complete seller tax interview and banking details | Founder | Week 1 |
| 3 | Integrate AWS Marketplace Metering Service API for per-IP billing | Eng | 2 weeks |
| 4 | Build Marketplace token → tenant provisioning flow | Eng | 1 week |
| 5 | Create product listing page (description, screenshots, pricing) | Founder | 1 week |
| 6 | Submit listing for AWS review (2–4 week review process) | Founder | Month 1 |
| 7 | Apply for ISV Accelerate co-sell programme | Founder | Month 2 |
| 8 | Apply for AWS SMB Competency | Founder | Month 6 |

---

## 3. Azure Marketplace Listing

### Why Azure Marketplace

Microsoft Azure Marketplace is the second-largest cloud procurement channel, with particular strength in enterprise and public sector. For SOCVault, the Azure channel is strategically important for three reasons:

1. **Microsoft Defender gap:** Azure customers using Microsoft Defender for Business have endpoint protection but no external VAPT, cloud posture across non-Azure clouds, or compliance reporting for non-Microsoft frameworks. SOCVault fills this gap.
2. **Azure customers pay with Azure credits:** Enterprise customers with Azure commitments can spend those credits on Marketplace listings — zero incremental budget required.
3. **UK public sector concentration:** UK government and NHS entities are heavily Azure-deployed. SOCVault's UK GDPR and Cyber Essentials compliance module is directly relevant.

### SOCVault Positioning on Azure Marketplace

**Listing name:** SOCVault — Multi-Layer Cybersecurity & Compliance Platform  
**Category:** Security → Security Operations + Compliance  
**Pricing model:** SaaS subscription (monthly)

The positioning pitch for Azure customers: *"You have Microsoft Defender protecting your devices. SOCVault scans what Defender cannot see — your web application attack surface, your non-Azure cloud infrastructure, your compliance posture across GDPR, PCI-DSS, and ISO 27001."*

### Azure co-sell and MACC (Microsoft Azure Consumption Commitment)

- **Co-sell Ready status:** Apply after listing goes live — allows Microsoft field sellers to include SOCVault in customer proposals
- **MACC eligible:** Customers with Microsoft Azure Consumption Commitments can draw down against SOCVault spend — critical for enterprise deal velocity
- **ISV Success programme:** Microsoft provides technical support, go-to-market resources, and co-marketing funds for qualifying ISVs

### Implementation Steps

| Step | Task | Owner | Timeline |
|---|---|---|---|
| 1 | Register on Microsoft Partner Centre as ISV publisher | Founder | Week 1 |
| 2 | Complete identity verification and publisher agreement | Founder | Week 2 |
| 3 | Build SaaS offer with Azure SaaS fulfillment APIs (landing page + webhook) | Eng | 2 weeks |
| 4 | Implement subscription management (activate, suspend, unsubscribe webhooks) | Eng | 1 week |
| 5 | Create offer listing (description, plans, screenshots, legal terms) | Founder | 1 week |
| 6 | Submit for Microsoft review (1–2 week review) | Founder | Month 2 |
| 7 | Apply for co-sell Ready status | Founder | Month 3 |

---

## 4. Google Cloud Marketplace

### Why Google Cloud Marketplace

Google Cloud's marketplace is smaller than AWS and Azure but strategically important for:
- Startup-heavy customer base (GCP is the preferred cloud for many tech startups)
- Google Workspace integration — SOCVault can alert to Google Workspace Gmail, Calendar, and Admin console
- Startup credits programme (Google for Startups Cloud Programme — up to $200,000 in credits)

The approach mirrors AWS and Azure but is lower priority — Phase 3 (after AWS and Azure listings are live and generating revenue).

---

## 5. Hosting Provider Partnerships

### The Hosting Provider Opportunity

Hosting providers are where the majority of SMB websites live. Every customer of GoDaddy, Kinsta, WP Engine, Fasthosts, Cloudways, or SiteGround has:
- A domain they need to protect
- A web application that is exposed to the public internet
- Zero visibility into their security posture
- A monthly billing relationship already in place

**The hosting provider's problem:** They face increasing pressure from customers who get hacked on their platform. A single high-profile breach of a customer site creates reputational damage, churn, and potential liability.

**SOCVault's solution for hosting providers:** Offer SOCVault as a value-add security layer — either bundled into hosting plans or as an add-on upsell. The provider protects their customers and their reputation; SOCVault gains distribution at scale.

### Target Hosting Partners

| Provider | Customers | SMB Focus | Integration Type | Priority |
|---|---|---|---|---|
| **GoDaddy** | 20M+ customers | High (primary SMB host) | Marketplace add-on | Tier 1 |
| **Kinsta** | 35,000 managed WP | High (WordPress SMB) | Native integration + upsell | Tier 1 |
| **WP Engine** | 150,000+ WP sites | High (premium WordPress) | Native integration | Tier 1 |
| **Cloudways** | 90,000+ customers | High (managed cloud) | Marketplace add-on | Tier 1 |
| **DigitalOcean** | 600,000+ customers | Very high (startup/SMB) | Marketplace listing | Tier 1 |
| **Fasthosts (UK)** | 170,000 UK businesses | Very high (UK SMB) | Native integration | Tier 1 (UK focus) |
| **Linode (Akamai)** | 1M+ customers | High (developer/SMB) | Marketplace listing | Tier 2 |
| **SiteGround** | 2.8M+ domains | High (SMB WordPress) | Marketplace add-on | Tier 2 |
| **Rackspace** | Enterprise/SMB | Mid-market | Managed service add-on | Tier 2 |

### DigitalOcean Marketplace — Highest Priority

DigitalOcean Marketplace already lists security tools and has a developer-friendly SMB customer base that maps directly to SOCVault's target persona. The listing process is self-serve and faster than AWS or Azure.

**Integration model:**
1. SOCVault lists on DigitalOcean Marketplace as a 1-Click Add-on
2. When a DigitalOcean customer provisions a Droplet or App Platform deployment, SOCVault appears as a recommended security add-on
3. One-click to activate → SOCVault automatically scans the customer's associated domain and IP

### GoDaddy Partnership Model

GoDaddy's 20 million customers represent the largest single SMB distribution channel in the market. The partnership model:

**Option A — Co-marketing:** SOCVault appears in GoDaddy's "Recommended Apps" or security marketplace. Revenue split: GoDaddy takes 25–30% commission.

**Option B — White-label:** GoDaddy offers "GoDaddy Security Scan" powered by SOCVault. The product carries GoDaddy branding. SOCVault receives a per-active-user fee. Higher volume, lower per-unit economics.

**Option C — API integration:** GoDaddy's DNS management dashboard shows a "Security Score" badge for each domain — powered by SOCVault L1 recon running in the background. Clicking the badge upsells to a full scan.

Option C is the most compelling for GoDaddy — it adds visible value to their existing product without requiring customers to leave the GoDaddy ecosystem.

### WordPress Hosting Partners (Kinsta / WP Engine)

WordPress powers 43% of all websites on the internet. WordPress sites are the most frequently targeted SMB web applications — SQL injection, plugin CVEs, wp-admin brute-force, and PHP web shells are daily occurrences.

**The integration pitch:** *"Every WordPress site you host gets continuous security monitoring and immediate malware alerts. When a site on your platform is compromised, you know before your customer does."*

Integration approach:
- Wazuh agent pre-installed as part of the hosting stack (server-side monitoring)
- SOCVault L2 web scan runs weekly against all WordPress installations on the platform
- Alerts sent to both the hosting provider dashboard and the end customer
- Hosting provider white-labels the alert UI with their brand

Revenue model: Per-site monthly fee ($3–$5/site/month) — hosting provider adds this to their plan pricing or as a premium tier upgrade.

**At Kinsta's 35,000 sites: $3/site/month = $105,000/month in channel revenue from a single partner.**

---

## 6. MSP / MSSP Channel Programme

### Why MSPs Are the Optimal Channel

Managed Service Providers serve 60–70% of UK SMBs. The typical MSP:
- Has 50–500 SMB clients under management
- Provides IT support, Microsoft 365 management, backup, and basic security
- Is actively looking for security products to resell to differentiate from competition and increase ARPU
- Already has monthly billing relationships with every client
- Is trusted implicitly — clients do what their MSP recommends

An MSP channel strategy means that instead of selling to individual SMBs one at a time, SOCVault sells to one MSP who brings 200 clients.

### SOCVault MSP Programme Structure

**Tier 1 — Referral Partner**
- Minimum commitment: None
- Commission: 20% recurring on referred clients
- Access: Co-branded marketing materials, partner portal, lead registration
- Training: Online self-paced certification (2 hours)

**Tier 2 — Reseller Partner**
- Minimum commitment: 10 active SOCVault clients
- Discount: 30% off list price (MSP buys at 70%, sells at 100%)
- Access: White-label option (SOCVault reports carry MSP branding), priority support, quarterly business reviews
- Training: Full SOCVault Certified Partner programme (1-day virtual training)

**Tier 3 — Strategic Partner (MSSP)**
- Minimum commitment: 50 active clients
- Discount: 40% off list price
- Access: Full white-label, API access for platform integration, co-sell support, dedicated account manager, custom playbooks, joint marketing budget
- Revenue: SOCVault provides the platform; MSSP wraps human analyst hours around it at their margin

### The White-Label Value Proposition for MSPs

The most powerful MSP offering is the **white-label SOC Pro tier**: the MSP sells "Managed Cybersecurity" to their clients at $299–$499/month, powered by SOCVault at $139/month (Tier 3 pricing) — capturing a $160–$360/client/month margin without building the platform themselves.

```
MSP Revenue Model per SOC Pro Client:

MSSP resell price:        $399/month (billed to SMB client)
SOCVault Tier 3 cost:    -$119/month (40% off $199)
MSP gross margin:         $280/month per client (70% margin)

At 50 clients:            $14,000/month MSP margin
At 200 clients:           $56,000/month MSP margin
```

The MSP's alternative: build their own SOC capability (£200,000+ per year in analyst salaries). SOCVault makes them profitable immediately with zero capex.

### Target MSP Partners

| Profile | UK Examples | Approach |
|---|---|---|
| IT MSPs serving 50–200 SMB clients | Nexus, Netify, Managed IT | Direct outreach + LinkedIn |
| Cybersecurity-focused MSSPs | CyberHive, Saepio, SRM | Co-sell partnership |
| Accountancy-adjacent IT firms | MSPs serving accountancy and legal | Sector targeting |
| Microsoft Gold Partners | Any UK Microsoft CSP reseller | Microsoft marketplace integration |

---

## 7. Domain Registrar & DNS Provider Integrations

### The Logic

Every business starts its digital life by registering a domain. The domain registrar is the first point of contact — and the most natural place to surface security awareness.

**Proposition to registrars:** Offer SOCVault's L1 free scan as a post-registration onboarding step. When a customer registers `mybusiness.co.uk`, they immediately receive: *"Your domain has been registered. Here's your first security report."*

This creates:
- Zero CAC acquisition for SOCVault (registrar bears the distribution cost)
- Immediate perceived value for the registrar's customer (security health check as a free welcome gift)
- A freemium conversion pipeline: customer sees their health score, converts to paid

### Target Registrars

| Registrar | UK Market Share | SMB Focus | Approach |
|---|---|---|---|
| **123-reg** | ~15% UK registrations | Very high | API integration — auto-run L1 on new domains |
| **GoDaddy UK** | ~25% UK registrations | Very high | Co-marketing + marketplace |
| **Fasthosts** | ~10% UK registrations | Very high | White-label security report |
| **Namecheap** | ~8% global | High | Marketplace listing |
| **Cloudflare Registrar** | Growing | Developer/SMB | API integration + dashboard widget |

### Cloudflare Integration — Highest Technical Value

Cloudflare is uniquely positioned: they provide DNS, CDN, WAF, and DDoS protection to millions of SMBs. SOCVault's L1 scan results (DNS health, HTTP headers, SSL/TLS) map directly to Cloudflare's product surface.

**Integration model:**
- SOCVault appears in the Cloudflare App Marketplace
- When an SMB's Cloudflare-protected domain has a security finding (missing HSTS, weak TLS, missing DMARC), SOCVault surfaces the alert in the Cloudflare dashboard
- One-click to run a full SOCVault scan from within Cloudflare
- Cloudflare earns per-active-user revenue; SOCVault gains zero-friction acquisition

---

## 8. Cyber Insurance Partnerships

### The Market Shift

Cyber insurance has become essential for SMBs — but insurers now require documented security posture evidence before writing policies. This creates a direct distribution channel:

**The flow:**

```
SMB applies for cyber insurance
        │
        ▼
Insurer requires: "Demonstrate your security posture"
        │
        ▼
Insurer recommends SOCVault (or requires it as a condition)
        │
        ▼
SMB signs up for SOCVault SOC Pro to satisfy insurer
        │
        ▼
SOCVault provides dated compliance reports — insurer accepts as evidence
        │
        ▼
Insurer potentially offers reduced premiums for SOCVault-verified clients
```

### Target Insurance Partners

| Company | Market | Proposition |
|---|---|---|
| **Hiscox UK** | UK SMB cyber specialist | Preferred tool for policy qualification + premium discount for SOCVault clients |
| **CFC Underwriting** | UK cyber SMB leader | Integration: SOCVault health score → automated risk scoring input |
| **Beazley** | UK/US enterprise + SMB | Co-branded marketing to policy holders |
| **Chubb** | Global SMB | Security assessment tool for policy underwriting |
| **Markel** | UK SMB specialist | Compliance report = audit evidence for claims |

### The Economics for Insurers

An SMB using SOCVault continuously monitors their security posture. Their breach probability decreases. The insurer's loss ratio improves. A 10% reduction in breach probability on a $500 premium portfolio is directly measurable — insurers can and do pay referral fees or marketing co-investment for validated risk reduction tools.

**Referral model:** Insurer recommends SOCVault. SOCVault pays a referral fee of $20–$40 per converted SOC Pro subscriber. At scale, this is the insurer's lowest-cost risk mitigation tool — they pay $40 once and get a permanently monitored, lower-risk client.

---

## 9. Telecoms / ISP Partnerships

### The Opportunity

UK SMB telecoms providers — BT, Vodafone, Virgin Media Business, Sky Business, TalkTalk Business — serve millions of SMBs with broadband, connectivity, and managed services. Security is the most requested value-add their SMB customers ask for.

**The proposition:** *"SOCVault for Business — included with your BT Business broadband. One-click to scan your website and see your security score."*

**Model:** SOCVault provides white-label freemium as a broadband bundle benefit. Upsell to paid tiers shares revenue 70/30 (SOCVault / telco).

At BT's scale (2.7M business customers), even a 1% freemium uptake = 27,000 active users — larger than SOCVault's Year 3 direct client target.

---

## 10. Channel Revenue Model

### Economics Per Channel Type

| Channel | List Price | SOCVault Net Revenue | Partner Take | Gross Margin |
|---|---|---|---|---|
| **Direct** | $199/mo | $199/mo | 0% | 99%+ |
| **AWS Marketplace** | $199/mo | $159/mo | AWS 20% | ~91% |
| **Azure Marketplace** | $199/mo | $159/mo | Microsoft 20% | ~91% |
| **MSP Referral** | $199/mo | $159/mo | 20% commission | ~87% |
| **MSP Reseller (Tier 2)** | $199/mo | $139/mo | 30% discount | ~83% |
| **MSP White-label (Tier 3)** | $199/mo | $119/mo | 40% discount | ~79% |
| **Hosting Provider** | $199/mo | $139/mo | 30% rev share | ~83% |
| **Domain Registrar** | $199/mo | $169/mo | 15% referral | ~93% |
| **Insurance Partner** | $199/mo | $179/mo | $20 one-time referral fee | ~97% |

### Channel Revenue Projections

| Year | Direct Clients | Channel Clients | Total ARR | Channel ARR |
|---|---|---|---|---|
| 1 | 150 | 0 | $108,000 | $0 |
| 2 | 400 | 200 | $540,000 | $162,000 |
| 3 | 800 | 1,200 | $1,800,000 | $900,000 |
| 4 | 1,500 | 4,500 | $5,400,000 | $3,240,000 |
| 5 | 3,000 | 12,000 | $18,000,000 | $12,600,000 |

---

## 11. Why This Is a Strong Market Fit

### Problem–Channel Alignment

The core insight driving channel fit: **the people who already have SMB trust are not security companies — they are infrastructure companies.**

A hosting provider, registrar, or ISP already has the SMB's domain, server, and payment details. They are the natural place for a security conversation to happen. When a hosting provider says *"your site needs a security scan,"* the SMB listens — because it comes bundled with the service they already pay for.

SOCVault is positioned precisely at this intersection: it scans the infrastructure those providers already host, using the domain those registrars already manage, producing results that insurers need and auditors expect.

### Market Fit Evidence

| Signal | Data Point |
|---|---|
| SMB security spending growth | 19% YoY (Gartner 2024) |
| SMBs that have been breached | 46% in 2023 (Hiscox Cyber Readiness Report) |
| SMBs with no formal security programme | 62% (UK Government Cyber Security Breaches Survey 2024) |
| Cyber insurance premium increases | +50–100% since 2021 (Marsh) |
| MSPs actively seeking security add-ons | 74% (Kaseya MSP Survey 2024) |
| AWS Marketplace SMB deal velocity | 30–40% faster than direct procurement |
| DigitalOcean SMB profile match | 600,000 developer/SMB customers in SOCVault's exact persona |

### Why Competitors Are Not in These Channels

| Competitor | Why They Can't Win in Hosting/Registrar Channel |
|---|---|
| **Tenable / Qualys** | Enterprise complexity — can't onboard in 60 seconds; requires agent deployment and security expertise |
| **Intruder.io** | No SOAR, no compliance, no malware response — insufficient value-add for hosting bundles |
| **Arctic Wolf** | $5,000+/month — incompatible with SMB hosting add-on economics |
| **Detectify** | Developer-focused — wrong persona for hosting provider customers |
| **Microsoft Defender** | Tied to Microsoft ecosystem — non-Microsoft hosting providers won't bundle a competitor's product |

**SOCVault is the only platform that:**
1. Can onboard in <60 seconds (hosting bundle UX requirement)
2. Delivers value at $0 (freemium qualifies as a free add-on)
3. Covers the full SMB attack surface (domain + web + compliance)
4. Is priced for SMB budgets ($15–$199/month — within hosting plan pricing brackets)
5. Has no conflicting allegiance to a competing cloud or technology provider

---

## 12. Implementation Roadmap

### Phase 1 — Direct Only (Months 1–12)

Prove product-market fit, build case studies, reach 150 paying clients.
No channel investment until the direct motion is proven.

### Phase 2 — Marketplace Launch (Months 13–18)

| Month | Action |
|---|---|
| 13 | Register AWS Marketplace seller account; begin listing preparation |
| 14 | Integrate AWS Metering API; build Marketplace token → tenant flow |
| 15 | Submit AWS Marketplace listing for review |
| 15 | Register Azure Partner Centre; begin Azure SaaS offer build |
| 16 | AWS Marketplace listing goes live |
| 17 | Submit Azure Marketplace listing for review |
| 17 | Begin DigitalOcean Marketplace application |
| 18 | Azure Marketplace listing goes live; DigitalOcean listing goes live |

**Month 18 target:** $10,000–$20,000 MRR from cloud marketplace channels (subset of company-wide **$22K MRR** at M18 per [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) and [`09_INVESTOR_BUSINESS_PLAN.md`](./09_INVESTOR_BUSINESS_PLAN.md) §13.1).

### Phase 3 — MSP Programme Launch (Months 18–24)

| Month | Action |
|---|---|
| 18 | Build MSP partner portal (white-label config, client management, billing view) |
| 19 | Launch MSP Referral (Tier 1) programme — outreach to 100 UK MSPs |
| 20 | Onboard first 10 MSP reseller partners (Tier 2) |
| 21 | Launch MSP white-label offering (Tier 3) — target 3 MSSP partners |
| 22 | First MSP Tier 3 partner goes live with SOCVault-powered managed security service |
| 24 | MSP channel contributes 200+ clients |

**Month 24 target:** 500+ clients through MSP channel, generating $60,000+/month MRR.

### Phase 4 — Hosting & Ecosystem Partners (Months 24–36)

| Month | Action |
|---|---|
| 24 | Approach DigitalOcean for featured marketplace placement |
| 25 | Pilot with 1 UK hosting provider (Fasthosts or Cloudways) |
| 26 | Approach Kinsta / WP Engine for WordPress security integration |
| 27 | Approach 1 cyber insurer (Hiscox or CFC) for referral partnership |
| 28 | Cloudflare App Marketplace listing |
| 30 | Expand to 3 hosting providers with live integrations |
| 33 | Approach BT Business or Vodafone Business for telco bundle pilot |
| 36 | Target: 1,200 channel clients across all partner types |

### Phase 5 — Channel at Scale (Year 3+)

By Year 3, channel revenue should equal or exceed direct revenue. The operational investment required:
- 1 dedicated Partner Success Manager (hired Month 18)
- Partner portal development (integrated into product roadmap Milestone 4.1)
- Legal: standard reseller agreement template, white-label terms, SLA addenda
- Marketing: co-branded materials, partner newsletter, annual partner summit

---

*SOCVault Ltd — Confidential | June 2026 | contact: mutexsystemsltd@gmail.com*
