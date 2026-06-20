# SOCVault — Legal & Compliance Templates
**Version 1.0 | June 2026 — OUTLINE FOR COUNSEL REVIEW**

> These are structural outlines. Engage qualified legal counsel before publication.

---

## 1. Privacy Policy (outline)

**Data controller:** SOCVault Ltd (UK)  
**Data processed:** Business email, phone, scan results, billing metadata  
**Lawful basis:** Contract (Art 6(1)(b)), Legitimate interest (security scanning)  
**Retention:** Scan results 24 months; audit logs 12 months; billing 7 years  
**Sub-processors:** AWS (eu-west-2), Anthropic, Stripe, MongoDB Atlas  
**Rights:** Access, erasure (`DELETE /api/v1/account`), portability, objection  
**Contact:** privacy@socvault.io  
**ICO registration:** Required before UK launch (Roadmap 4.3.6)

---

## 2. Terms of Service (outline)

- Service description: passive and active security scanning SaaS
- **Scan authorisation:** User warrants authority to scan registered domains
- Acceptable use: no scanning of third-party targets; no abuse of rate limits
- Tier limits per `03_REQUIREMENTS.md` rate limit table
- Liability cap: fees paid in prior 12 months (subject to counsel)
- Governing law: England and Wales
- SOC Pro SLA: 99.9% uptime (Enterprise); support response times per tier

---

## 3. Data Processing Agreement (B2B outline)

- **Roles:** Customer = Controller; SOCVault = Processor
- **Subject matter:** Security scanning and reporting
- **Duration:** Term of subscription
- **Security measures:** Reference `14_THREAT_MODEL.md` and ISO 27001 roadmap
- **Sub-processor list:** AWS, Anthropic, Stripe, MongoDB Atlas (with 30-day change notice)
- **Data location:** UK/EU (eu-west-2) unless US region opted in (Phase 5)
- **Breach notification:** Within 72 hours of awareness
- **Deletion:** On termination + erasure API

---

## 4. Scan authorisation consent (UI copy)

> I confirm that I am authorised to perform security scans against the domain(s) and IP addresses registered in my SOCVault workspace. I understand that active scans may interact with live systems.

Stored: `consent_timestamp`, `user_id`, `target`, `layer`, `ip_address`

---

## 5. Benchmark opt-in consent (US-111)

> I agree to contribute anonymised health scores to industry benchmarks. No domain names or company names will be shared.

Default: **off**. Stored on tenant record.
