# SOCVault — Financial Plan
**Version 1.0 | June 2026**

---

## 1. Financial Summary

| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| **Revenue (ARR)** | $108,000 | $540,000 | $1,800,000 |
| **COGS** | $18,700 | $48,600 | $126,000 |
| **Gross Profit** | $89,300 | $491,400 | $1,674,000 |
| **Gross Margin** | 82.7% | 91.0% | 93.0% |
| **Operating Expenses** | $251,000 | $380,000 | $720,000 |
| **EBITDA** | -$161,700 | +$111,400 | +$954,000 |
| **Paying Clients (EoY)** | 150 | 600 | 2,000 |
| **ARPU (monthly)** | $60 | $75 | $75 |

> Note: Year 1 EBITDA is negative as expected for a pre-revenue startup investing in product and go-to-market. **Cash-flow break-even is Month 28** (September 2028) per `08_THREE_YEAR_EXPENSES_LEDGER.md`. EBITDA break-even on operating expenses alone is projected earlier (~Month 18) once MRR covers monthly OPEX.

---

## 2. Unit Economics

### 2.1 Cost Per Scan (COGS Analysis)

The variable cost of executing one scan is the fundamental unit economic of SOCVault.

#### Layer 1 — Recon Scan (Lambda)

| Cost Component | Calculation | Cost |
|---|---|---|
| AWS Lambda compute | 120s × 1024MB × $0.0000166667/GB-s | $0.000002 |
| Claude AI tokens (input) | 50,000 tokens × $0.003/1K tokens | $0.15 |
| Claude AI tokens (output) | 1,500 tokens × $0.015/1K tokens | $0.0225 |
| Threat Intel lookups | 3 IPs × $0.01/lookup | $0.03 |
| **Total COGS per Recon scan** | | **$0.2025** |

> Note: Claude claude-sonnet-4-6 pricing: $3/1M input, $15/1M output. Prompt caching reduces input cost by up to 90% on repeated system prompts, bringing effective input cost to ~$0.015 for cached portion.

#### Layer 2 — Web VAPT Scan (Fargate)

| Cost Component | Calculation | Cost |
|---|---|---|
| AWS Fargate compute | 600s × 0.5 vCPU × $0.04048/vCPU-hr | $0.034 |
| AWS Fargate memory | 600s × 1GB × $0.004445/GB-hr | $0.00074 |
| Claude AI tokens (input) | 80,000 tokens × $0.003/1K (cached) | $0.24 |
| Claude AI tokens (output) | 2,000 tokens × $0.015/1K | $0.03 |
| Nuclei / tool execution | Included in Fargate compute | $0 |
| Threat Intel lookups | 5 IPs × $0.01/lookup | $0.05 |
| **Total COGS per VAPT scan** | | **$0.355** |

#### Layer 7 — SOC Incident (per alert, Claude triage)

| Cost Component | Calculation | Cost |
|---|---|---|
| Claude AI tokens (input) | 10,000 tokens × $0.003/1K (cached) | $0.03 |
| Claude AI tokens (output) | 800 tokens × $0.015/1K | $0.012 |
| AbuseIPDB lookup | 1 lookup × $0.01 | $0.01 |
| OTX lookup | 1 lookup × $0.005 | $0.005 |
| **Total COGS per SOC alert** | | **$0.057** |

#### L8 Malware Detection & Response — COGS per Incident

| Cost Component | Calculation | Cost |
|---|---|---|
| VirusTotal API hash lookup | 1 lookup × $0.01 | $0.010 |
| Claude AI tokens — analysis (input) | 8,000 tokens × $0.003/1K (cached) | $0.024 |
| Claude AI tokens — remediation (output) | 1,200 tokens × $0.015/1K | $0.018 |
| ClamAV / YARA | Open-source (free) | $0.000 |
| Post-remediation re-scan | Included in Wazuh infra | $0.000 |
| **Total COGS per malware incident** | | **$0.052** |

> Malware Detection & Response is included in the SOC Pro flat fee ($199/mo). The tooling COGS are effectively zero (ClamAV, YARA rules are open-source). VirusTotal API is the only variable cost — at ~5 detections/month per endpoint, marginal COGS = $0.26/endpoint/month, well within the flat-fee model.

### 2.2 Revenue vs COGS per Scan

| Tier / Product | Revenue | COGS | Gross Profit | Margin |
|---|---|---|---|---|
| Freemium Recon | $0 | $0.20 | -$0.20 | — (cost to acquire) |
| Web VAPT ($15/IP/mo) | $15.00 | $0.36 | $14.64 | **97.6%** |
| Mobile License ($20/app/mo) | $20.00 | $0.45 | $19.55 | **97.8%** |
| Cloud License ($25/env/mo) | $25.00 | $0.55 | $24.45 | **97.8%** |
| SOC Pro ($199/mo flat) | $199.00 | ~$15/mo infra | $184.00 | **92.5%** |
| SOC Enterprise ($499/mo flat) | $499.00 | ~$35/mo infra | $464.00 | **93.0%** |

### 2.3 Customer Acquisition Cost (CAC)

| Channel | Cost per Lead | Conversion Rate | CAC |
|---|---|---|---|
| Organic / SEO | $5 | 3% | $167 |
| LinkedIn content | $12 | 4% | $300 |
| Product Hunt | $2 | 6% | $33 |
| Google Ads (Year 2) | $25 | 5% | $500 |
| Partner / MSP | $0 | 8% | $0 (rev-share) |
| **Blended CAC (Year 1)** | | | **$60** |
| **Blended CAC (Year 2)** | | | **$45** |

### 2.4 Lifetime Value (LTV)

| Tier | Monthly ARPU | Avg Lifespan (months) | LTV |
|---|---|---|---|
| Transactional (VAPT) | $35 | 18 | $630 |
| SOC Pro | $199 | 24 | $4,776 |
| SOC Enterprise | $499 | 36 | $17,964 |
| **Blended LTV (Year 1)** | | | **$720** |

### 2.5 LTV:CAC Ratio

| Period | LTV | CAC | Ratio |
|---|---|---|---|
| Year 1 | $720 | $60 | **12:1** |
| Year 2 | $1,080 | $45 | **24:1** |
| Year 3 | $1,800 | $35 | **51:1** |

> A ratio above 3:1 is considered healthy. Above 5:1 is excellent. SOCVault's model shows exceptional capital efficiency due to high gross margins and low infrastructure COGS.

### 2.5a Marketing tier ↔ data model mapping

| Marketing / wireframe | MongoDB `payment_tier` | Typical price |
|---|---|---|
| Freemium (L1 only) | `FREEMIUM` | $0 |
| Pay-per-scan / Web VAPT | `STARTER` | ~$15/scan or $35/mo transactional |
| SOC Pro (L7–L9, flat) | `PRO` | $199/mo |
| SOC Enterprise / MSP white-label | `ENTERPRISE` | $499/mo+ |

Use **SOC Pro** in investor/GTM copy; persist enum values in API and Stripe metadata.

### 2.6 AI Chat Credit — Unit Economics

The AI Chat Assistant is a credit-prepay consumption product with near-zero marginal infrastructure cost beyond Claude API tokens. Unit economics are calculated per credit consumed.

#### COGS per Credit Consumed

| Cost Component | Calculation | Cost per Credit |
|---|---|---|
| Claude API (input tokens — cached) | ~4,000 cached tokens × $0.30/1M | $0.00120 |
| Claude API (input tokens — uncached) | ~1,000 uncached tokens × $3.00/1M | $0.00300 |
| Claude API (output tokens) | ~500 tokens × $15.00/1M | $0.00750 |
| Lambda invocation + DynamoDB writes | Fixed overhead, shared | $0.00030 |
| Credit ledger write (DynamoDB) | 1 write × $0.00000125 | $0.00001 |
| **Total COGS per credit** | | **~$0.012** |

> Assumes 84% prompt cache hit rate based on static system prompt reuse across tenant sessions (per session benchmarks). Claude claude-sonnet-4-6 pricing: input $3/1M uncached, $0.30/1M cached; output $15/1M.

#### Revenue vs COGS per Credit Bundle

| Bundle | Credits | Price | Revenue/Credit | COGS/Credit | Gross Profit | Margin |
|---|---|---|---|---|---|---|
| Starter (50 cr) | 50 | $5.00 | $0.100 | $0.012 | $4.40 | **88%** |
| Standard (200 cr) | 200 | $15.00 | $0.075 | $0.012 | $12.60 | **84%** |
| Pro (500 cr) | 500 | $30.00 | $0.060 | $0.012 | $24.00 | **80%** |
| Enterprise (2,000 cr) | 2,000 | $99.00 | $0.050 | $0.012 | $74.76 | **75.5%** |
| **Blended** | | **$18.00 avg** | **$0.072** | **$0.012** | **$15.60** | **~83%** |

#### Projected AI Chat Revenue Contribution

| Year | Active AI Chat Users | Avg Monthly Credit Spend | Monthly Revenue | Annual Revenue |
|---|---|---|---|---|
| Year 1 (M12) | 30 | $12 | $360 | ~$2,500 |
| Year 2 (M24) | 180 | $18 | $3,240 | ~$38,000 |
| Year 3 (M36) | 600 | $24 | $14,400 | ~$170,000 |

> Year 3 AI Chat revenue = ~9.4% of total ARR — a meaningful recurring layer on top of subscriptions, with no additional infrastructure cost per user beyond token consumption.

---

## 3. Operating Expenses

### 3.1 Infrastructure Costs

| Category | Phase 0 (Blueprint) | Phase 2a (Staging MVP — serverless) | Phase 2b (AWS Paid MVP) | Phase 3 (100+ clients) |
|---|---|---|---|---|
| Development workstation | $0 (spec only) | $0 | $0 | $0 |
| Development IDE (Cursor) | $20/mo | $20/mo | $20/mo | $40/mo |
| API Gateway + Lambda (API) | $0 | **$0–5/mo** (Free Tier) | $15/mo | $80/mo |
| Lambda (L1 + workers) | $0 | **$0–5/mo** (Free Tier) | $20/mo | $120/mo |
| AWS Amplify (frontend) | $0 | **$0** (Free Tier build mins) | $15/mo | $45/mo |
| SQS | $0 | **$0** | $5/mo | $20/mo |
| ECS Fargate / EKS | $0 | **$0** (deferred) | $45/mo (Fargate bridge) | $350/mo (EKS) |
| MongoDB Atlas M0 on AWS | $0 | **$0** | $57/mo (M10) | $190/mo (M30) |
| Wazuh Manager (EC2) | $0 | $0 (deferred) | $35/mo (t3.medium) | $120/mo (r6g.large) |
| AWS Cognito | $0 | **$0** (50k MAU free) | $0 | $25/mo |
| AWS S3 + CloudWatch | $0 | **$0–$5** | $15/mo | $60/mo |
| AWS SNS (OTP) | $0 | **$0–$5** (email-first) | $5/mo | $20/mo |
| CloudFront CDN | $0 | **$0** (paid tier) | $20/mo | $80/mo |
| WAF + GuardDuty | $0 | **$0** (paid tier) | $30/mo | $100/mo |
| AWS Backup | $0 | **$0** (paid tier) | $15/mo | $40/mo |
| Claude API (Anthropic) | $80/mo (testing) | $80/mo | $150/mo | $800/mo |
| Threat Intel APIs | $0 (mocked) | $0 (mocked) | $0 (mocked) | $150/mo |
| CodePipeline (CI/CD) | $0 | **$0** (GitHub Actions) | $10/mo | $30/mo |
| Sentry (error tracking) | $0 | $0 | $26/mo | $80/mo |
| **TOTAL INFRA** | **$100/mo** | **~$100–115/mo** | **~$433/mo** | **$2,335/mo** |

> Phase 2a = **staging-only** serverless MVP (ADR-006). Main variable cost is Anthropic API during testing. Production infra not billed until cutover.

### 3.2 Personnel Costs (Annual)

| Role | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Founding Engineer (Python/DevSecOps) | $70,000 | $80,000 | $90,000 |
| AI/ML Engineer | — | $75,000 | $85,000 |
| Frontend Engineer | — | $65,000 | $75,000 |
| Sales / GTM Lead | — | $60,000 + 10% commission | $70,000 + commission |
| Compliance Advisor (contractor) | $12,000 | $18,000 | $24,000 |
| **TOTAL PERSONNEL** | **$82,000** | **$298,000** | **$344,000** |

### 3.3 Non-Personnel Operating Expenses (Annual)

| Category | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Legal (company formation, contracts, ToS) | $8,000 | $5,000 | $8,000 |
| Accounting / bookkeeping | $3,000 | $5,000 | $8,000 |
| Marketing & advertising | $10,000 | $40,000 | $120,000 |
| Security tooling licences | $12,000 | $15,000 | $20,000 |
| Office / co-working | $0 | $6,000 | $18,000 |
| ISO 27001 certification | $0 | $15,000 | $3,000 (renewal) |
| Domain, trademark, brand | $2,000 | $1,000 | $1,000 |
| Insurance (Cyber, PI) | $4,000 | $6,000 | $9,000 |
| Conferences / events | $2,000 | $8,000 | $15,000 |
| **TOTAL NON-PERSONNEL** | **$41,000** | **$101,000** | **$202,000** |

---

## 4. Revenue Model & Projections

### 4.1 Monthly Revenue Build (Year 1)

| Month | Free Users | Paying Clients | ARPU | MRR |
|---|---|---|---|---|
| 1 | 50 | 0 | — | $0 |
| 2 | 150 | 2 | $35 | $70 |
| 3 | 300 | 5 | $40 | $200 |
| 4 | 500 | 8 | $45 | $360 |
| 5 | 800 | 12 | $50 | $600 |
| 6 | 1,200 | 20 | $55 | $1,100 |
| 7 | 1,800 | 30 | $55 | $1,650 |
| 8 | 2,500 | 45 | $60 | $2,700 |
| 9 | 3,500 | 65 | $60 | $3,900 |
| 10 | 5,000 | 90 | $65 | $5,850 |
| 11 | 7,000 | 120 | $65 | $7,800 |
| 12 | 9,000 | 150 | $60 | $9,000 |
| **Year 1 Total** | | | | **$33,230 ARR equivalent** |

> Note: ARR run-rate at end of Year 1 = 150 clients × $60 ARPU × 12 = **$108,000**

### 4.2 Three-Year Revenue Projection

| Period | Clients | ARPU | MRR | ARR |
|---|---|---|---|---|
| Year 1 End | 150 | $60 | $9,000 | $108,000 |
| Year 2 End | 600 | $75 | $45,000 | $540,000 |
| Year 3 End | 2,000 | $75 | $150,000 | $1,800,000 |

### 4.3 Revenue Mix Assumption

| Stream | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Pay-per-scan (transactional) | 58% | 42% | 32% |
| SOC Pro subscription | 35% | 44% | 48% |
| SOC Enterprise / Managed | 5% | 9% | 13% |
| AI Chat Credits | 2% | 5% | 7% |

> AI Chat Credits are a pure add-on revenue layer — no additional subscription seats required. Users who exhaust credits and re-purchase have no churn risk (they are already active subscribers). Average re-purchase interval: 3–4 weeks for Standard/Pro bundle buyers.

---

## 5. Funding Requirements

### 5.1 Pre-Seed Round

**Amount:** $251,000  
**Structure:** SAFE note (20% discount, $2M cap)  
**Purpose:** 12 months of lean operations to product-market fit

| Use of Funds | Amount | % |
|---|---|---|
| Founding engineer salary (12 months) | $70,000 | 27.9% |
| Compliance advisor (contract) | $12,000 | 4.8% |
| AWS infrastructure (12 months) | $24,000 | 9.6% |
| Claude API budget | $12,000 | 4.8% |
| Security tooling licences | $12,000 | 4.8% |
| Legal (formation, contracts, DPA) | $8,000 | 3.2% |
| Marketing & GTM | $20,000 | 8.0% |
| ISO 27001 audit preparation | $10,000 | 4.0% |
| Founder living allowance | $60,000 | 23.9% |
| Reserve / contingency (10%) | $23,000 | 9.2% |
| **Total** | **$251,000** | **100%** |

**Milestones to unlock Seed round:**
- 50 paying clients
- $10K MRR
- ISO 27001 in progress
- 3 MSP/channel partner agreements signed

> Typically met by **Month 8** (see investor §16 milestones). Round **closes Month 15 (Aug 2027)**; Month-18 targets (323 clients / $22K MRR) are post-Seed operating outcomes per §6.

### 5.2 Seed Round (Projected — Month 15)

**Amount:** $750,000  
**Valuation:** $3.5M pre-money  
**Structure:** Priced equity (Series Seed)  
**Purpose:** 18 months to $50K MRR, hiring GTM and additional engineers

### 5.3 Series A (Projected — Month 30)

**Amount:** $3,000,000  
**Valuation:** $12M pre-money  
**Purpose:** International expansion, enterprise product, 50-person team

---

## 6. Break-Even Analysis

> **Two metrics:** **EBITDA / OPEX break-even** ≈ Month 18 when MRR covers monthly operating expenses. **Cumulative cash-flow break-even** ≈ Month 28 per `08_THREE_YEAR_EXPENSES_LEDGER.md` (includes prior-year investment). Both use ~323 paying clients at blended ARPU.

**Monthly fixed costs:** ~$22,000 (at 3-person team, Phase 2 infrastructure)  
**Gross margin at break-even client base:** 91%  
**Clients needed to break even:** 22,000 / (75 × 0.91) ≈ **323 clients**  
**Projected EBITDA / OPEX break-even:** Month 18 (Q4 2027)  
**Projected cumulative cash-flow break-even:** Month 28 (September 2028)

---

## 7. Sensitivity Analysis

### 7.1 Claude API Cost Sensitivity

| Scenario | Claude Cost per Scan | Impact on Margin |
|---|---|---|
| Base case (cached prompts) | $0.20 | 97.6% margin |
| No prompt caching | $0.42 | 97.2% margin |
| 3× more tokens (complex scans) | $0.60 | 96.0% margin |
| Anthropic price increase 50% | $0.30 | 98.0% margin (still excellent) |

### 7.2 Churn Sensitivity

| Churn Rate | Year 2 Clients | Year 2 ARR |
|---|---|---|
| 3%/month (bad) | 380 | $342,000 |
| 5%/month (base) | 600 | $540,000 |
| 8%/month (worst) | 850 | $765,000 |

> Note: Higher churn scenarios still show growth because new client acquisition outpaces churn at these volume levels.

### 7.3 Conversion Rate Sensitivity

| Freemium-to-Paid Rate | Year 1 Clients | Year 1 ARR |
|---|---|---|
| 5% | 75 | $54,000 |
| 12% (base) | 150 | $108,000 |
| 20% | 250 | $180,000 |

---

## 8. Financial Controls & Governance

### 8.1 AI API Cost Controls

- Per-tenant daily AI API budget cap ($10/day default, configurable)
- Real-time cost dashboard showing COGS vs. revenue per client
- Automated alert when daily AI spend exceeds $50
- Prompt caching enabled by default (reduces costs 60–90%)
- Admin-level override for COGS thresholds

### 8.2 AWS Cost Controls

- **Free Tier MVP:** $10/month AWS Budget with alerts at 50%, 80%, 100% ([`AWS_SETUP_README.md`](./AWS_SETUP_README.md))
- Weekly review: AWS Billing → Free Tier usage page
- AWS Budget alerts at 80% and 100% of monthly budget (raise to $50/$100 when on paid stack)
- Auto-scaling policies with maximum task count limits
- Reserved instances for persistent Wazuh EC2 nodes (40% saving vs on-demand)
- S3 lifecycle policies (move scan artifacts to Glacier after 90 days)
- CloudWatch billing alarm: alert if daily spend >$50

### 8.3 Revenue Recognition

- Subscription revenue recognised monthly (not annually upfront)
- Pay-per-scan recognised at point of scan completion
- Refund policy: prorated refunds within 14 days for unused subscription periods
