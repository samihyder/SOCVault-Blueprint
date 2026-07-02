---
name: compliance-check
description: Use for any SOCVault change touching data handling, authentication, billing, or audit logging. Maps to the Compliance Agent in SOCVAULT_PRODUCT_DESCRIPTION.md sec 2.6.1 — GDPR, PCI-DSS, SOC2.
---

Trigger: a change touches personal data, auth, billing, or audit logging.

1. For a full compliance pass, delegate to the `compliance-agent` subagent via the Agent tool — it's read-only and cites specific requirements, not general opinions.
2. GDPR: check any new field or flow that collects/stores personal data against `docs/15_LEGAL_TEMPLATES.md` for a documented legal basis.
3. Audit logging: sensitive actions (admin actions, auth events, billing changes, tenant data access) need an audit trail — cross-check against `userstories-wireframes/18-audit-log.html` and the relevant FR-### entries in `docs/03_REQUIREMENTS.md`.
4. Tenant isolation: every query/response touching tenant data must be scoped by `tenant_id` — this is SOCVault's primary compliance and security boundary as a multi-tenant SaaS, and the single most important thing to check.
5. PCI-DSS: SOCVault should never directly touch card data — Stripe handles that. Flag any code that would pull SOCVault into PCI scope.
6. SOC2: flag missing encryption at rest/in transit, missing access controls, or missing change-audit trails on infrastructure changes.
7. Always cite the specific requirement or doc section — an unsourced compliance finding is just an opinion.
