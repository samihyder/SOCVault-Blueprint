---
name: backend-code-generation
description: Use when a GitHub issue is labeled `backend`, or the user asks to build/modify a SOCVault FastAPI endpoint, service, or database operation. Maps to the Backend Agent (Cursor Backend Agent) in SOCVAULT_PRODUCT_DESCRIPTION.md secs 1.6/2.6.1.
---

Trigger: a `backend`-labeled issue, or any request to add/change an API endpoint, business logic, or MongoDB operation.

1. Read `api/openapi.yaml` first — it's the source of truth for the endpoint's contract. If the request conflicts with it, resolve the conflict explicitly (update the spec, don't silently diverge from it).
2. For a full new endpoint or service (routes + Pydantic schema + business logic + tests), delegate to the `backend-agent` subagent via the Agent tool.
3. For a small, targeted change (one field, one validation rule, one bug fix), apply it directly:
   - Pydantic models for request/response validation.
   - Async Motor/MongoDB queries — always scoped by `tenant_id`. This is the single most important invariant in this codebase; a missing tenant_id filter is a cross-tenant data leak, not a minor bug.
   - Correct HTTP status codes and error handling for edge cases.
   - pytest test covering the change.
   - Update `api/openapi.yaml` and the matching Bruno collection entry in `collections/bruno/SOCVault-MVP/` if the contract changed.
4. Add CloudWatch logging for anything running on Lambda (per ADR-006 serverless architecture).
