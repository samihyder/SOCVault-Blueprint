---
name: frontend-code-generation
description: Use when a GitHub issue is labeled `frontend`, or the user asks to build/modify a SOCVault dashboard widget, page, or UI component. Maps to the Claude UI Agent in SOCVAULT_PRODUCT_DESCRIPTION.md secs 1.6/2.6.1.
---

Trigger: a `frontend`-labeled issue, or any request to build/style/wire up a React/TypeScript UI piece for SOCVault.

1. Read the linked issue or user story fully before writing code — don't infer scope from the title alone.
2. Check `src/components/sections/` and `src/components/ui/` for an existing pattern before inventing a new one.
3. For substantial, self-contained component work (a full new page, widget, or multi-file feature), delegate to the `frontend-ui-agent` subagent via the Agent tool rather than doing it inline — it carries the full styling/testing checklist and can run in the background.
4. For a small, targeted edit (one prop, one style fix, one bug), apply it directly:
   - Tailwind CSS with `sv-*` brand tokens (`#1B3D35` forest green, `#4CC844` lime green).
   - Zustand for state, Axios + React Query against `api/openapi.yaml` for data.
   - Jest test alongside any new component logic.
   - WCAG 2.1 AA sanity check (labels, contrast, keyboard nav) before calling it done.
5. Never fabricate product screenshots or claim a UI "works" without actually running the dev server and looking at it (see the project's UI-testing convention).
