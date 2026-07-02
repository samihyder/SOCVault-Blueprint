---
name: performance-analysis
description: Use after a SOCVault staging deployment, or when asked to investigate latency, throughput, or AWS/Claude API cost. Maps to the Perf Agent in SOCVAULT_PRODUCT_DESCRIPTION.md sec 2.6.1.
---

Trigger: a staging deployment just happened, or a request to investigate slowness/cost.

1. For a full analysis pass, delegate to the `perf-agent` subagent via the Agent tool — it's read-only and reports findings/recommendations.
2. Check against the concrete NFR targets in `docs/03_REQUIREMENTS.md`: API p95 <500ms, L1 scan end-to-end <3 minutes.
3. Common serverless pitfalls to check first: Lambda cold starts, unindexed or unscoped MongoDB queries, N+1 patterns, missing Claude prompt caching.
4. Prompt caching is not just a latency concern here — per `docs/04_FINANCIAL_PLAN.md`, it's load-bearing for the ~97.6% gross margin assumption on VAPT scans. A caching regression is a cost regression; report it as both.
5. State claims with numbers. If you haven't actually measured something (CloudWatch metrics, a k6 run), say what you'd need to measure it instead of guessing "this could be slow."
