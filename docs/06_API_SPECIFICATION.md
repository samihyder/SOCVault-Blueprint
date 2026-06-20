# SOCVault — API Specification
**Version 1.0 | June 2026**

Machine-readable OpenAPI 3.1 definition: [`../api/openapi.yaml`](../api/openapi.yaml)

Runnable collections: [`../collections/README.md`](../collections/README.md)

---

## 1. Overview

| Property | Value |
|---|---|
| Base URL (staging — **MVP active**) | `https://api-staging.socvault.io/api/v1` |
| Base URL (production — dormant until cutover) | `https://api.socvault.io/api/v1` |
| Auth | Bearer JWT (**Cognito** via API Gateway authorizer) |
| Content-Type | `application/json` |
| Rate limit | Per-tenant + per-IP (see FR-110–FR-120); state in **DynamoDB** on MVP |

---

## 2. Endpoint catalogue

### Authentication

| Method | Path | Description | Phase |
|---|---|---|---|
| POST | `/auth/signup` | Business email + phone | 1 |
| POST | `/auth/verify-otp` | OTP verification → tokens | 1 |
| POST | `/auth/refresh` | Refresh access token | 1 |
| GET | `/auth/me` | Current tenant profile | 1 |
| POST | `/auth/domain/verify` | Start DNS/meta verification | 2 |
| GET | `/auth/domain/status` | Poll verification status | 2 |

### Scans

| Method | Path | Description | Phase |
|---|---|---|---|
| POST | `/scan/execute` | Trigger scan `{layer, target, consent}` | 1 |
| GET | `/scan/{scan_id}` | Poll status + results | 1 |
| GET | `/scan/history` | Tenant scan history | 1 |
| POST | `/scan/mobile` | Upload APK/IPA (L3) | 3 |
| POST | `/scan/l9/execute` | Start L9 AI agent scan | 2 |
| GET | `/scan/l9/{scan_id}/log` | Live agent activity log | 2 |
| POST | `/scan/l9/{scan_id}/stop` | Cancel running L9 scan | 2 |

### Dashboard

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/dashboard/summary` | Health score, exposure, top risks | 1 |
| GET | `/dashboard/compliance` | Framework pass/fail map | 2 |
| GET | `/dashboard/benchmark` | Industry benchmark (opt-in) | 3 |

### Incidents & SOAR

| Method | Path | Description | Phase |
|---|---|---|---|
| POST | `/incidents/ingest` | Wazuh webhook | 2 |
| GET | `/incidents` | Incident feed | 2 |
| POST | `/incidents/{id}/approve` | Approve playbook | 2 |
| POST | `/incidents/{id}/reject` | Reject playbook | 2 |
| POST | `/incidents/{id}/false-positive` | Mark false positive | 2 |

### Malware (L8)

| Method | Path | Description | Phase |
|---|---|---|---|
| POST | `/malware/ingest` | Wazuh ClamAV/FIM webhook | 2 |
| GET | `/malware/incidents` | Malware incident list | 2 |
| POST | `/malware/{id}/approve` | Approve remediation | 2 |
| POST | `/malware/{id}/reject` | Reject remediation | 2 |

### AI Chat

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/credits/balance` | Credit balance + reserved | 3 |
| POST | `/credits/purchase` | Stripe checkout session | 3 |
| POST | `/ai/chat` | Send message (streaming) | 3 |
| POST | `/ai/action` | Execute action from chat | 3 |
| GET | `/ai/action/{id}/result` | Poll action result | 3 |

### Billing

| Method | Path | Description | Phase |
|---|---|---|---|
| POST | `/billing/subscribe` | Stripe subscription | 2 |
| POST | `/billing/portal` | Customer portal URL | 2 |

### Team & settings

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/team/members` | Sub-user slots | 2 |
| POST | `/team/invite` | Invite sub-user | 2 |
| DELETE | `/team/members/{id}` | Revoke sub-user | 2 |
| GET | `/settings/assets` | Registered domains/IPs | 2 |
| POST | `/settings/api-keys` | Generate API key (Enterprise) | 3 |
| DELETE | `/account` | GDPR erasure request | 3 |

### Admin (internal RBAC)

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/admin/telemetry` | COGS + margin | 1 |
| GET | `/admin/tenants` | Tenant list | 2 |
| PATCH | `/admin/tenants/{id}/limits` | Rate limit / cost cap override | 2 |
| GET | `/admin/metrics/*` | Metrics Observatory data feeds | 2 |
| POST | `/admin/teams` | Create internal team | 2 |

### Admin API Explorer & Pass & Keys (Phase 2)

Internal-only. See wireframe `24-admin-api-explorer.html`, FR-194–FR-207, and implementation guide [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md).

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/admin/explorer/catalog` | OpenAPI-derived endpoint list (tags, methods, schemas) | 2 |
| POST | `/admin/explorer/test` | Proxy test request; returns success/failure envelope | 2 |
| GET | `/admin/vault/variables` | List variable names + masked preview (no plaintext secrets) | 2 |
| POST | `/admin/vault/variables` | Create/update variable (encrypted at rest) | 2 |
| DELETE | `/admin/vault/variables/{key}` | Delete variable | 2 |
| POST | `/admin/vault/unlock` | Step-up PIN/password → short-lived reveal session | 2 |
| POST | `/admin/vault/reveal/{key}` | Return decrypted value (requires active unlock session) | 2 |

**Test result envelope (`POST /admin/explorer/test`):**

```json
{
  "success": true,
  "status_code": 200,
  "latency_ms": 142,
  "response_headers": {},
  "response_body": {},
  "auto_saved_keys": ["access_token", "refresh_token"],
  "error_type": null,
  "message": null
}
```

On failure: `success: false`, `error_type` ∈ `HTTP_ERROR | TIMEOUT | VALIDATION | NETWORK`, non-null `message`.

### Admin Threat Intel Feeds (Phase 2)

Wireframe: Threat Intel tab on `24-admin-api-explorer.html` (US-201–208). **Feed catalogue (providers, layers, correlation):** [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) — do not duplicate in code or UI strings.

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/admin/ti/feeds` | List feed registry (filter by layer, environment) | 2 |
| GET | `/admin/ti/feeds/{feed_id}` | Single feed config + status | 2 |
| PATCH | `/admin/ti/feeds/{feed_id}` | Enable/disable, daily limit, vault key link | 2 |
| POST | `/admin/ti/feeds/{feed_id}/test` | Test API key + optional sample IOC | 2 |
| GET | `/admin/ti/feeds/{feed_id}/usage` | 24h quota usage + cache hits | 2 |
| PUT | `/admin/ti/feeds/priority` | Set global fallback order | 2 |

Runtime enrichment (not admin UI): `ThreatIntelManager` — see doc 20 §3–6.

### Admin Development Tracker (Phase 2)

Wireframe `25-admin-dev-tracker.html`, FR-208–FR-215. Syncs with [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md).

| Method | Path | Description | Phase |
|---|---|---|---|
| GET | `/admin/tracker/summary` | Phase progress, stack matrix, next action | 2 |
| GET | `/admin/tracker/items` | List INF/DEV/API/EXT checklist items (filter by type) | 2 |
| PATCH | `/admin/tracker/items/{id}` | Update status, notes, verified date | 2 |
| GET | `/admin/tracker/actions` | Action log (paginated, filterable) | 2 |
| POST | `/admin/tracker/actions` | Log new action (auto ACT- ID) | 2 |
| POST | `/admin/tracker/export` | Export markdown for git commit | 2 |
| POST | `/admin/tracker/probes/run` | Run stack health probes (optional) | 2 |

---

## 3. Common response codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 401 | Missing/invalid JWT |
| 402 | Payment required / tier gate |
| 403 | RBAC denied |
| 429 | Rate limit exceeded |
| 503 | AI provider unavailable (fallback served where applicable) |

---

## 4. Webhooks (inbound)

| Source | Path | Purpose |
|---|---|---|
| Stripe | `/webhooks/stripe` | Subscription + credit top-up |
| Wazuh | `/incidents/ingest`, `/malware/ingest` | SOC + malware events |
