---
name: socvault-code-review
description: Use when a SOCVault PR is ready for review. Maps to the Code Review Agent in SOCVAULT_PRODUCT_DESCRIPTION.md sec 2.6.1. Distinct from the general-purpose "code-review" skill — this one checks conformance to SOCVault's specific architecture and conventions.
---

Trigger: a PR is opened or marked ready for review.

1. For a full review pass, delegate to the `code-review-agent` subagent via the Agent tool — it's read-only and reports findings, ranked most-severe first.
2. Check architecture conformance against `docs/02_TECHNICAL_STACK.md`: FastAPI/Python backend, React/TypeScript frontend, MongoDB Atlas via Motor, AWS Lambda serverless per ADR-006 (not ECS/Fargate — that ADR was superseded).
3. Flag anti-patterns specific to this codebase: missing tenant-scoping, premature abstraction, defensive code for scenarios that can't happen, PR descriptions that oversell what the diff actually does.
4. Separate must-fix correctness issues from nice-to-have style suggestions — don't bury a real bug under nits.
5. If the general "code-review" skill has already run on this diff, don't duplicate its output — focus on SOCVault-specific conformance it wouldn't know to check.
