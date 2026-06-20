# SOCVault — Three-Year Operating Expenses Ledger
**June 2026 – May 2029 | All figures in USD**

---

## Notes & Assumptions

- **Year 1:** June 2026 – May 2027 — Pre-revenue through first paying clients
- **Year 2:** June 2027 – May 2028 — Growth phase, hiring, Seed round deployed
- **Year 3:** June 2028 – May 2029 — Scale phase, Series A fuel
- Personnel costs shown as gross (employer cost = salary × 1.15 for employer NI/benefits)
- AWS costs scale with client count; model assumes linear growth per tier
- Claude API costs assume prompt caching from Month 3 onward (60% cost reduction on input)
- All one-time costs (legal setup, ISO audit) shown in the month incurred
- Months are numbered M1–M36

---

## Category Definitions

| Code | Category |
|---|---|
| PERS | Personnel (salaries, contractor fees, employer taxes) |
| INFRA | Cloud & infrastructure (AWS serverless MVP, MongoDB Atlas, paid-tier CDN/WAF) |
| AI | AI API costs (Anthropic Claude) |
| TI | Threat Intelligence APIs (AbuseIPDB, OTX, GreyNoise) |
| TOOLS | Development tooling (Cursor, GitHub, Sentry, monitoring) |
| LEGAL | Legal, compliance, accounting, insurance |
| MKTG | Marketing, advertising, events, PR |
| MISC | Office, travel, subscriptions, contingency |

---

## Year 1 Monthly Ledger (June 2026 – May 2027)

| Month | PERS | INFRA | AI | TI | TOOLS | LEGAL | MKTG | MISC | **TOTAL** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|
| M1 Jun 2026 | $10,350 | $100 | $80 | $0 | $60 | $8,500 | $0 | $500 | **$19,590** | $19,590 |
| M2 Jul 2026 | $10,350 | $100 | $120 | $0 | $60 | $500 | $500 | $300 | **$11,930** | $31,520 |
| M3 Aug 2026 | $10,350 | $100 | $150 | $0 | $60 | $500 | $500 | $300 | **$11,960** | $43,480 |
| M4 Sep 2026 | $10,350 | $433 | $150 | $0 | $86 | $500 | $1,000 | $500 | **$13,019** | $56,499 |
| M5 Oct 2026 | $10,350 | $433 | $200 | $20 | $86 | $1,500 | $1,000 | $500 | **$14,089** | $70,588 |
| M6 Nov 2026 | $10,350 | $433 | $250 | $20 | $86 | $500 | $1,000 | $500 | **$13,139** | $83,727 |
| M7 Dec 2026 | $10,350 | $433 | $300 | $40 | $86 | $500 | $2,000 | $700 | **$14,409** | $98,136 |
| M8 Jan 2027 | $10,350 | $600 | $400 | $40 | $86 | $500 | $1,500 | $500 | **$13,976** | $112,112 |
| M9 Feb 2027 | $10,350 | $600 | $500 | $60 | $86 | $500 | $1,500 | $500 | **$14,096** | $126,208 |
| M10 Mar 2027 | $10,350 | $800 | $600 | $80 | $86 | $1,000 | $2,000 | $700 | **$15,616** | $141,824 |
| M11 Apr 2027 | $10,350 | $800 | $700 | $80 | $86 | $500 | $2,000 | $700 | **$15,216** | $157,040 |
| M12 May 2027 | $10,350 | $800 | $800 | $100 | $86 | $500 | $2,000 | $700 | **$15,336** | $172,376 |
| **Y1 Total** | **$124,200** | **$5,632** | **$4,250** | **$440** | **$868** | **$15,500** | **$15,000** | **$6,200** | **$172,090** | |

**Year 1 Sub-totals by Category:**

| Category | Annual | % of Total |
|---|---|---|
| Personnel | $124,200 | 72.2% |
| Infrastructure | $5,632 | 3.3% |
| AI (Claude API) | $4,250 | 2.5% |
| Threat Intel | $440 | 0.3% |
| Dev Tooling | $868 | 0.5% |
| Legal / Compliance | $15,500 | 9.0% |
| Marketing | $15,000 | 8.7% |
| Misc | $6,200 | 3.6% |
| **TOTAL** | **$172,090** | **100%** |

> Note: Personnel cost = Founding Engineer $70K/yr + Compliance Contractor $12K/yr, shown as monthly employer cost (×1.15 for NI/benefits), prorated. Legal spike in M1 = company formation + ToS + DPA.

---

## Year 1 Infrastructure Breakdown Detail

| Month | API GW + Lambda | MongoDB Atlas | SQS | Wazuh EC2 | S3 / DynamoDB | CDN / WAF (paid) | Cognito | SNS | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| M1–M3 (staging MVP — serverless) | $5 | $0 (M0) | $0 | $0 | $10 | $0 | $0 | $0 | ~$100 (ledger incl. tooling) |
| M4–M6 (paid tier bootstrap) | $15 | $57 (M10) | $5 | $35 | $20 | $20 | $0 | $5 | ~$157 base → **$433** in ledger |
| M7–M9 (beta, 10 clients) | $25 | $57 | $5 | $35 | $25 | $20 | $5 | $10 | ~$182 base → **$600** in ledger |
| M10–M12 (50 clients) | $45 | $57 | $10 | $35 | $35 | $50 | $10 | $15 | ~$257 base → **$800** in ledger |

> MVP months use Free Tier–first serverless stack (ADR-006). Paid-tier columns (Atlas M10, Wazuh EC2, CloudFront/WAF) apply from M4 onward per Phase 2b. No Redis/Celery on MVP — async via SQS + Lambda.

---

## Year 2 Monthly Ledger (June 2027 – May 2028)

*Seed round closes Month 15 (Aug 2027). Hiring accelerates from Month 16.*

| Month | PERS | INFRA | AI | TI | TOOLS | LEGAL | MKTG | MISC | **TOTAL** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|
| M13 Jun 2027 | $12,650 | $1,100 | $1,000 | $120 | $160 | $600 | $2,500 | $800 | **$18,930** | $191,306 |
| M14 Jul 2027 | $12,650 | $1,200 | $1,200 | $150 | $160 | $600 | $3,000 | $800 | **$19,760** | $211,066 |
| M15 Aug 2027 | $12,650 | $1,400 | $1,400 | $150 | $160 | $1,500 | $3,500 | $1,000 | **$21,760** | $232,826 |
| M16 Sep 2027 | $27,600 | $1,600 | $1,600 | $150 | $200 | $600 | $4,000 | $1,200 | **$36,950** | $269,776 |
| M17 Oct 2027 | $27,600 | $1,800 | $1,800 | $150 | $200 | $600 | $4,000 | $1,200 | **$37,350** | $307,126 |
| M18 Nov 2027 | $27,600 | $2,000 | $2,000 | $200 | $200 | $1,000 | $4,500 | $1,500 | **$39,000** | $346,126 |
| M19 Dec 2027 | $27,600 | $2,200 | $2,500 | $200 | $200 | $600 | $5,000 | $1,500 | **$39,800** | $385,926 |
| M20 Jan 2028 | $35,650 | $2,500 | $3,000 | $250 | $250 | $600 | $5,500 | $1,500 | **$49,250** | $435,176 |
| M21 Feb 2028 | $35,650 | $2,800 | $3,500 | $250 | $250 | $600 | $5,500 | $1,800 | **$50,350** | $485,526 |
| M22 Mar 2028 | $35,650 | $3,000 | $4,000 | $300 | $300 | $15,000 | $6,000 | $2,000 | **$66,250** | $551,776 |
| M23 Apr 2028 | $35,650 | $3,200 | $4,500 | $300 | $300 | $1,000 | $6,000 | $2,000 | **$52,950** | $604,726 |
| M24 May 2028 | $35,650 | $3,500 | $5,000 | $350 | $300 | $1,000 | $6,000 | $2,000 | **$53,800** | $658,526 |
| **Y2 Total** | **$336,950** | **$26,300** | **$31,500** | **$2,570** | **$2,680** | **$23,700** | **$55,500** | **$17,300** | **$486,100** | |

**Year 2 Sub-totals by Category:**

| Category | Annual | % of Total |
|---|---|---|
| Personnel | $336,950 | 69.3% |
| Infrastructure | $26,300 | 5.4% |
| AI (Claude API) | $31,500 | 6.5% |
| Threat Intel | $2,570 | 0.5% |
| Dev Tooling | $2,680 | 0.6% |
| Legal / Compliance | $23,700 | 4.9% |
| Marketing | $55,500 | 11.4% |
| Misc | $17,300 | 3.6% |
| **TOTAL** | **$486,100** | **100%** |

**Year 2 Headcount (from M16):**

| Role | Gross Salary | Monthly Employer Cost |
|---|---|---|
| Founding Engineer | $80,000 | $7,667 |
| AI / ML Engineer (new M16) | $75,000 | $7,188 |
| Frontend Engineer (new M20) | $65,000 | $6,229 |
| Sales / GTM Lead (new M20) | $60,000 + commission | $5,750 |
| Compliance Contractor | $18,000/yr | $1,500/mo |
| **Total Monthly (M20+)** | | **$28,334** |

> Note: M22 legal spike = ISO 27001 stage 1+2 audit fees (~$15,000 total). Personnel jumps at M16 (AI Engineer hired) and M20 (Frontend + Sales hired).

---

## Year 2 Infrastructure Breakdown Detail

| Month | Lambda + workers | MongoDB | SQS / async | Wazuh | S3 / DynamoDB | CDN / WAF | Cognito | SNS | Claude API | TI APIs | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M13–M15 (~200 clients) | $80 | $190 | $15 | $85 | $60 | $200 | $25 | $20 | $1,200 | $120 | ~$1,995 |
| M16–M18 (~350 clients) | $120 | $190 | $20 | $85 | $80 | $200 | $40 | $30 | $2,000 | $150 | ~$2,915 |
| M19–M21 (~500 clients) | $180 | $190 | $25 | $120 | $100 | $200 | $55 | $40 | $3,200 | $200 | ~$4,110 |
| M22–M24 (~600 clients) | $250 | $350 | $30 | $120 | $120 | $200 | $70 | $50 | $4,500 | $300 | ~$5,990 |

> “Lambda + workers” = API Gateway + Lambda (MVP) scaling to Fargate/EKS scan workers at paid tier. ElastiCache/Celery costs roll in with EKS (Phase 3+).

---

## Year 3 Monthly Ledger (June 2028 – May 2029)

*Series A closes Month 31 (Dec 2028). Scale hiring Q3/Q4.*

| Month | PERS | INFRA | AI | TI | TOOLS | LEGAL | MKTG | MISC | **TOTAL** | Cumulative |
|---|---|---|---|---|---|---|---|---|---|---|
| M25 Jun 2028 | $38,525 | $4,000 | $6,000 | $400 | $400 | $1,200 | $8,000 | $2,500 | **$61,025** | $719,551 |
| M26 Jul 2028 | $38,525 | $4,500 | $7,000 | $450 | $400 | $1,200 | $8,000 | $2,500 | **$62,575** | $782,126 |
| M27 Aug 2028 | $38,525 | $5,000 | $8,000 | $500 | $400 | $1,200 | $9,000 | $3,000 | **$65,625** | $847,751 |
| M28 Sep 2028 | $38,525 | $5,500 | $9,000 | $500 | $500 | $1,200 | $9,000 | $3,000 | **$67,225** | $914,976 |
| M29 Oct 2028 | $38,525 | $6,000 | $10,000 | $600 | $500 | $1,200 | $10,000 | $3,500 | **$70,325** | $985,301 |
| M30 Nov 2028 | $38,525 | $6,500 | $11,000 | $700 | $500 | $1,500 | $10,000 | $3,500 | **$72,225** | $1,057,526 |
| M31 Dec 2028 | $57,500 | $7,000 | $12,000 | $800 | $600 | $5,000 | $12,000 | $4,000 | **$98,900** | $1,156,426 |
| M32 Jan 2029 | $68,800 | $7,500 | $13,000 | $900 | $700 | $1,500 | $14,000 | $4,500 | **$110,900** | $1,267,326 |
| M33 Feb 2029 | $68,800 | $8,000 | $14,000 | $1,000 | $700 | $1,500 | $14,000 | $4,500 | **$112,500** | $1,379,826 |
| M34 Mar 2029 | $68,800 | $8,500 | $15,000 | $1,100 | $800 | $2,000 | $15,000 | $5,000 | **$116,200** | $1,496,026 |
| M35 Apr 2029 | $68,800 | $9,000 | $16,000 | $1,200 | $800 | $1,500 | $15,000 | $5,000 | **$117,300** | $1,613,326 |
| M36 May 2029 | $68,800 | $9,500 | $17,000 | $1,300 | $800 | $1,500 | $16,000 | $5,500 | **$120,400** | $1,733,726 |
| **Y3 Total** | **$633,650** | **$81,000** | **$138,000** | **$9,450** | **$6,900** | **$20,000** | **$140,000** | **$46,500** | **$1,075,500** | |

**Year 3 Sub-totals by Category:**

| Category | Annual | % of Total |
|---|---|---|
| Personnel | $633,650 | 58.9% |
| Infrastructure | $81,000 | 7.5% |
| AI (Claude API) | $138,000 | 12.8% |
| Threat Intel | $9,450 | 0.9% |
| Dev Tooling | $6,900 | 0.6% |
| Legal / Compliance | $20,000 | 1.9% |
| Marketing | $140,000 | 13.0% |
| Misc | $46,500 | 4.3% |
| **TOTAL** | **$1,075,500** | **100%** |

**Year 3 Headcount (from M32 post-Series A):**

| Role | Gross Salary | Monthly Employer Cost |
|---|---|---|
| Founding Engineer | $90,000 | $8,625 |
| AI / ML Engineer | $85,000 | $8,146 |
| Frontend Engineer | $75,000 | $7,188 |
| Sales / GTM Lead | $70,000 + commission | $6,708 |
| SOC Analyst #1 (new M31) | $55,000 | $5,271 |
| Sales Engineer (new M32) | $80,000 | $7,667 |
| Marketing Manager (new M32) | $65,000 | $6,229 |
| DevOps Engineer (new M32) | $80,000 | $7,667 |
| Compliance Contractor | $24,000/yr | $2,000/mo |
| **Total Monthly (M32+)** | | **$59,501** |

---

## Three-Year Summary

| Period | Personnel | Infrastructure | AI API | Threat Intel | Tooling | Legal | Marketing | Misc | **Total OpEx** |
|---|---|---|---|---|---|---|---|---|---|
| **Year 1** | $124,200 | $5,632 | $4,250 | $440 | $868 | $15,500 | $15,000 | $6,200 | **$172,090** |
| **Year 2** | $336,950 | $26,300 | $31,500 | $2,570 | $2,680 | $23,700 | $55,500 | $17,300 | **$486,100** |
| **Year 3** | $633,650 | $81,000 | $138,000 | $9,450 | $6,900 | $20,000 | $140,000 | $46,500 | **$1,075,500** |
| **3-Year Total** | **$1,094,800** | **$112,932** | **$173,750** | **$12,460** | **$10,448** | **$59,200** | **$210,500** | **$70,000** | **$1,733,690** |
| **% of Total** | **63.1%** | **6.5%** | **10.0%** | **0.7%** | **0.6%** | **3.4%** | **12.1%** | **4.0%** | **100%** |

---

## Revenue vs. Expenses (Cash Flow Summary)

| Period | Revenue | OpEx | **Net Cash Flow** | **Cumulative P&L** |
|---|---|---|---|---|
| Y1 Q1 (M1–M3) | $0 | $43,480 | -$43,480 | -$43,480 |
| Y1 Q2 (M4–M6) | $1,160 | $40,247 | -$39,087 | -$82,567 |
| Y1 Q3 (M7–M9) | $6,250 | $42,481 | -$36,231 | -$118,798 |
| Y1 Q4 (M10–M12) | $24,820 | $46,168 | -$21,348 | -$140,146 |
| **Y1 Full Year** | **$32,230** | **$172,376** | **-$140,146** | **-$140,146** |
| Y2 Q1 (M13–M15) | $60,500 | $60,450 | +$50 | -$140,096 |
| Y2 Q2 (M16–M18) | $82,500 | $113,300 | -$30,800 | -$170,896 |
| Y2 Q3 (M19–M21) | $108,000 | $139,400 | -$31,400 | -$202,296 |
| Y2 Q4 (M22–M24) | $145,500 | $173,000 | -$27,500 | -$229,796 |
| **Y2 Full Year** | **$396,500** | **$486,150** | **-$89,650** | **-$229,796** |
| Y3 Q1 (M25–M27) | $270,000 | $189,225 | +$80,775 | -$149,021 |
| Y3 Q2 (M28–M30) | $360,000 | $209,775 | +$150,225 | +$1,204 |
| Y3 Q3 (M31–M33) | $450,000 | $322,300 | +$127,700 | +$128,904 |
| Y3 Q4 (M34–M36) | $540,000 | $353,900 | +$186,100 | +$315,004 |
| **Y3 Full Year** | **$1,620,000** | **$1,075,200** | **+$544,800** | **+$315,004** |

> Cash flow turns positive in **Y3 Q2 (Month 28 — approximately September 2028)**, aligned with break-even projection of ~323 paying clients.

---

## Key Financial Ratios

| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Revenue | $32,230 | $396,500 | $1,620,000 |
| Gross Profit | $26,650 | $360,500 | $1,507,800 |
| Gross Margin | 82.7% | 90.9% | 93.1% |
| OpEx | $172,090 | $486,100 | $1,075,500 |
| EBITDA | -$145,440 | -$125,600 | +$432,300 |
| Personnel as % of OpEx | 72.2% | 69.3% | 58.9% |
| Infrastructure as % of Revenue | 17.5% | 6.6% | 5.0% |
| AI API as % of Revenue | 13.2% | 7.9% | 8.5% |
| Marketing as % of Revenue | 46.5% | 14.0% | 8.6% |

---

## One-Time Capital Events (Not in Monthly Ledger)

| Event | Month | Amount | Type |
|---|---|---|---|
| Pre-Seed raise (SAFE) | M1 (Jun 2026) | +$251,000 | Funding In |
| Company formation & bank account | M1 (Jun 2026) | -$2,500 | One-time |
| Trademark registration (SOCVault) | M2 (Jul 2026) | -$800 | One-time |
| Domain + SSL (3-year) | M1 (Jun 2026) | -$300 | One-time |
| Cyber insurance (annual) | M4 (Sep 2026) | -$4,000 | Annual |
| ISO 27001 certification | M22 (Mar 2028) | -$15,000 | One-time |
| SOC 2 Type I audit | M28 (Sep 2028) | -$18,000 | One-time |
| Seed round close | M15 (Aug 2027) | +$750,000 | Funding In |
| Series A close | M31 (Dec 2028) | +$3,000,000 | Funding In |

---

## Infrastructure Scaling Assumptions

| Client Count | Recommended AWS Config | Estimated Monthly Infra |
|---|---|---|
| 0–50 clients | Serverless MVP (API GW + Lambda + Amplify + SQS) + optional Wazuh t3.medium + Atlas M0/M10 | ~$100–433/mo |
| 50–200 clients | Serverless API + Fargate scan bridge + t3.large Wazuh + M10 Atlas + CloudFront/WAF | ~$900/mo |
| 200–500 clients | Lambda API + Fargate workers + r6g.large Wazuh + M20 Atlas | ~$2,200/mo |
| 500–1,000 clients | Fargate/EKS hybrid + r6g.xlarge Wazuh + M30 Atlas | ~$4,500/mo |
| 1,000–2,000 clients | **Amazon EKS** (API + Celery workers) + r6g.2xlarge Wazuh + M40 Atlas | ~$8,000/mo |

## AI API Cost Scaling Assumptions

| Client Count | Scans/Month | Claude Cost/Month (cached) | Claude Cost/Month (no cache) |
|---|---|---|---|
| 50 | ~200 | $40 | $160 |
| 200 | ~900 | $180 | $720 |
| 500 | ~2,500 | $520 | $2,080 |
| 1,000 | ~5,500 | $1,150 | $4,600 |
| 2,000 | ~12,000 | $2,500 | $10,000 |

> Prompt caching is the most impactful cost lever — enabling it from Month 3 reduces Claude API input costs by ~60-90%, keeping AI costs manageable even at scale.
