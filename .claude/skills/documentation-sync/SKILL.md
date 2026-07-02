---
name: documentation-sync
description: Use whenever a SOCVault endpoint, component, or architecture decision changes and the docs need to catch up. Maps to the Doc Agent in SOCVAULT_PRODUCT_DESCRIPTION.md sec 2.6.1.
---

Trigger: any change to an API endpoint, a significant architecture decision, or a new wireframe/user story.

1. For a broad doc sync across multiple files, delegate to the `doc-agent` subagent via the Agent tool.
2. For a targeted update tied to the change you're already making, apply directly:
   - Endpoint changed → update `api/openapi.yaml` and `docs/06_API_SPECIFICATION.md`.
   - New FR/US pair → add a row to `docs/16_TRACEABILITY_MATRIX.md` (per the `CONTRIBUTING.md` checklist).
   - New wireframe → update `userstories-wireframes/00-index.html` and `docs/README.md`'s index table.
   - Significant architecture decision → new ADR in `docs/adr/`, following the existing numbered format.
   - Any meaningful change → add an Action Log row to `DEVELOPMENT_TRACKER.md` per its stated mandatory rule.
3. Status accuracy matters more than completeness: mark features 📋 (spec-only) not 🟢 (live) unless they're actually running and verified — this repo's tracker legend exists specifically to prevent aspirational status claims.
