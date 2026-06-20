# SOCVault — Threat Model
**Version 1.1 | June 2026 | STRIDE** — aligned to ADR-006 (serverless staging MVP)

---

## 1. System boundary

**MVP (staging):**

```
[Browser] → [Amplify Hosting] → [API Gateway HTTP] → [Lambda (FastAPI/Mangum)]
                              ↘ [Atlas MongoDB / DynamoDB / S3]
                              ↘ [SQS] → [Lambda async workers]
                              ↘ [Lambda L1 scanner]
[Wazuh Agents] → [Wazuh Manager (EC2, Phase 2+)] → [SOCVault ingest webhooks]
```

**Paid tier (scale):** CloudFront · AWS WAF · isolated **Fargate/EKS** scan workers for L2+ · ElastiCache + Celery on EKS.

---

## 2. Assets

| Asset | Classification |
|---|---|
| Tenant scan results | Confidential |
| JWT / refresh tokens | Secret |
| Anthropic API keys | Secret |
| Stripe customer IDs | Confidential |
| Wazuh agent keys | Secret |
| Audit logs | Integrity-critical |
| Admin Pass & Keys vault | Secret (KMS-encrypted) |

---

## 3. Threat catalogue

| ID | Threat | STRIDE | Mitigation |
|---|---|---|---|
| T-01 | Cross-tenant data access | Spoofing / Info disclosure | `tenant_id` middleware on all DB queries; integration tests |
| T-02 | Scanning third-party domains | Elevation | FR-029 target validation; domain verification FR-010–015 |
| T-03 | SOAR auto-remediation damages production | Tampering / DoS | Human approval gate FR-079; confidence threshold 95% |
| T-04 | AI prompt injection via scan output | Tampering | Sanitise scanner output before Claude; structured JSON parsing |
| T-05 | Credential leakage in repo | Info disclosure | SSM Parameter Store (MVP) → Secrets Manager (paid); pre-commit secret scan |
| T-06 | DDoS on scan API | DoS | API Gateway throttling; AWS WAF + CloudFront (paid tier); per-tenant rate limits FR-110–120 |
| T-07 | Malicious APK upload (L3) | Tampering | Scan in isolated Lambda/Fargate/EKS task; file size/type limits |
| T-08 | Stripe webhook forgery | Spoofing | Webhook signature verification |
| T-09 | Sub-user privilege escalation | Elevation | Server-side RBAC; Cognito per-user accounts |
| T-10 | Audit log tampering | Repudiation | Append-only collection; admin actions via CloudTrail |
| T-11 | Pass & Keys vault exfiltration | Info disclosure | KMS encryption (FR-203); step-up PIN (FR-201); no plaintext in logs; reveal audit (FR-204); 5-min unlock TTL |
| T-12 | API Explorer SSRF via proxy test | Spoofing / Info disclosure | Allowlist internal base URLs only; block metadata IP ranges; Manager/DevOps RBAC (FR-205) |

---

## 4. Trust zones

| Zone | Trust level | Controls |
|---|---|---|
| Public internet | Untrusted | API Gateway throttling; WAF (paid tier); rate limits; CORS |
| Tenant dashboard | Authenticated user | Cognito JWT, RBAC |
| Scan sandbox (Lambda / Fargate / EKS) | Semi-trusted | Per-invocation isolation; no cross-tenant memory |
| Admin / internal | High trust | MFA within 24h (FR-166), internal RBAC |
| Wazuh agents | Tenant-controlled | Enrollment keys per tenant |

---

## 5. Pre-launch review

- OWASP Top 10 assessment (Roadmap 3.1.1)
- Quarterly self-scan using SOCVault L1–L2 on `app-staging.socvault.io` (MVP); `app.socvault.io` post-cutover
- Cyber Essentials Plus (Phase 4)
