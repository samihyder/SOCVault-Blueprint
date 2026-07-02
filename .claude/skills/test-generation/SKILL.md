---
name: test-generation
description: Use for new SOCVault feature code, or when asked to add coverage, run the tests/qa/ staging suite, or validate against the Bruno/Postman collections. Maps to the Test Agent (Test Generation + QA Automation) in SOCVAULT_PRODUCT_DESCRIPTION.md secs 1.6/2.6.1.
---

Trigger: new feature code lands, or a request to add/verify test coverage.

1. For generating a full test layer (new pytest suite, new Playwright flow, new Bruno collection folder), delegate to the `test-agent` subagent via the Agent tool.
2. For a test tied to a small change you're already making, write it directly:
   - Backend: pytest, targeting >80% coverage on new code, mocking only at true system boundaries.
   - Frontend: Jest alongside the component.
   - API contract change: update the matching `.bru` file in `collections/bruno/SOCVault-MVP/` to match `api/openapi.yaml`.
3. Core E2E flow to protect: login → scan → dashboard (Playwright). Don't let a partial feature ship without at least a smoke-level check of this path if it touches it.
4. Performance: k6 scenarios should validate p95 <500ms API latency and <3 minute end-to-end L1 scan time — these are the NFR targets in `docs/03_REQUIREMENTS.md`.
5. Don't write tests for behavior that doesn't exist yet, and don't pad coverage numbers with trivial getter/setter assertions.
