---
name: socvault-security-scan
description: Use on every SOCVault PR or new code, before merge — SAST, dependency, and secret scanning. Maps to the Security Agent in SOCVAULT_PRODUCT_DESCRIPTION.md sec 2.6.1. Distinct from the general-purpose "security-review" skill — this one is SOCVault-specific (tenant isolation, CORS, threat model cross-reference).
---

Trigger: any PR, or any newly written/changed code, before it's considered done.

1. For a full, standalone security pass, delegate to the `security-agent` subagent via the Agent tool — it's read-only and reports findings without touching code.
2. For a quick inline check while already working on a change, verify:
   - No secrets committed (API keys, tokens) — cross-check against `.env.example` for what real values would look like.
   - No dependency added with a known CVE at the pinned version.
   - CORS stays an explicit allowlist, never `["*"]` — this codebase has a documented prior incident of a wildcard CORS regression.
   - Every MongoDB query/API response touching tenant data is scoped by `tenant_id`.
3. Cross-reference findings against the STRIDE catalogue in `docs/14_THREAT_MODEL.md` — cite the specific threat category, don't just assert "this is insecure."
4. Report with file:line and a concrete exploit scenario. If nothing is wrong, say so — don't invent nits to seem thorough.
