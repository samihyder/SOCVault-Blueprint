# SOCVault — Test Strategy
**Version 1.0 | June 2026**

---

## 1. Objectives

Validate MVP acceptance criteria (`03_REQUIREMENTS.md` §4) and regression coverage for all 8 core layers + L9 + AI Chat before each phase gate.

---

## 2. Test levels

| Level | Scope | Tools |
|---|---|---|
| Unit | Auth gating, rate limits, COGS calc, Pydantic validation | pytest, pytest-asyncio |
| Integration | Scanner drivers, Claude client, Stripe webhooks | pytest + testcontainers |
| E2E | Signup → scan → report → dashboard | Playwright |
| Security | OWASP Top 10, tenant isolation | SOCVault self-scan, manual pen test |
| Load | 50 concurrent scans, 100 RPS API | k6, Phase 4 |

---

## 3. MVP test plan (Phase 1 gate)

| # | Test case | Maps to |
|---|---|---|
| T-001 | Reject gmail.com signup | FR-002, US-002 |
| T-002 | OTP flow completes <60s | FR-004–006, US-001 |
| T-003 | Freemium: 2nd L1 scan in same month blocked | FR-026 |
| T-004 | L1 returns health score + exposure | FR-043, FR-041 |
| T-005 | Claude report valid JSON; fallback on 503 | FR-047 |
| T-006 | Remediation paywalled for Freemium | FR-048 |
| T-007 | API returns 401 without JWT | NFR-020 |
| T-008 | Scan tenant isolation (tenant A cannot read B) | FR-030, NFR-025 |
| T-009 | Admin telemetry COGS accurate ±5% | FR-098 |
| T-010 | Dashboard loads <2s (p95) | NFR-004, US-066 |

---

## 4. Phase 2 gate (cloud + SOC)

- Stripe checkout + webhook tier upgrade
- Domain verification blocks L2 until verified
- Wazuh ingest → Claude triage → approval queue
- Malware auto-remediate path (confidence >95%)
- L9 agent completes with activity log
- Sub-user RBAC enforced per role matrix

---

## 5. Phase 3 gate (launch)

- AI Chat credit purchase + deduction
- PDF executive export
- OWASP review: zero Critical/High open
- GDPR deletion endpoint completes within 30 days

---

## 6. Automated staging QA

All MVP acceptance tests run against **live staging** after every deploy.

| Asset | Location |
|---|---|
| Master runner | [`tests/qa/run-staging-qa.sh`](../tests/qa/run-staging-qa.sh) |
| Story → test map | [`tests/qa/manifest.yaml`](../tests/qa/manifest.yaml) |
| pytest suites | [`tests/qa/api/`](../tests/qa/api/) |
| Build order | [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) |
| GitHub workflow | [`templates/github/workflows/qa-staging.yml`](../templates/github/workflows/qa-staging.yml) |

### CI pipeline (staging MVP)

```
lint → unit tests → terraform plan (PR)
merge main → terraform apply staging → run-staging-qa.sh → optional Bruno
```

Per user story: `./tests/qa/run-staging-qa.sh --story US-xxx` before marking complete in Dev Tracker.

Security: Dependabot + Trivy on every PR (dogfooding).
