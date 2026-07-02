---
name: bug-detection-fixing
description: Use when a GitHub issue is labeled `bug-report`, or a PR contains code changes that might have introduced a logic bug. Maps to the Bug Fixer/Bug Analyzer Agent in SOCVAULT_PRODUCT_DESCRIPTION.md secs 1.6/2.6.1/2.6.2.
---

Trigger: a `bug-report`-labeled issue, or reviewing a PR with non-trivial logic changes.

1. Reproduce the bug before fixing it — run the code, write a small repro script, or trace the exact failing path. Don't fix from a read-through guess; that's how you fix the wrong thing.
2. For an involved investigation (unclear root cause, multiple candidate files), delegate to the `bug-fixer-agent` subagent via the Agent tool.
3. For an already-located, well-understood bug, fix it directly:
   - Minimal fix addressing the root cause — no unrelated refactoring, no speculative error handling "while you're in there."
   - Add or update a test that would have caught it.
   - Reference the originating issue number in the commit.
4. Watch for this codebase's known bug classes: off-by-one in scan rate-limit windows, missing `tenant_id` scoping, async/await mistakes in Motor queries, wrong model IDs in Claude API calls (there's a documented history of non-existent Gemini-style model IDs being used by mistake — verify against `docs/claude-api` conventions).
