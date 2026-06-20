# SOCVault — API Explorer & Pass & Keys: Implementation Guide
**Milestone 2.9 build order · FR-194–FR-207 · Wireframe: `24-admin-api-explorer.html`**

---

## Build order (mandatory sequence)

Implement **backend layers first**, then the React screen. Do not start the UI until steps 1–4 have passing API tests.

```
Step 1  catalog sync          GET  /admin/explorer/catalog
   │
   ▼
Step 2  proxy test runner     POST /admin/explorer/test
   │
   ▼
Step 3  encrypted vault       /admin/vault/variables + auto-save from tests
   │
   ▼
Step 4  PIN step-up           POST /admin/vault/unlock + /admin/vault/reveal/{key}
   │
   ▼
Step 5  React screen          Admin route → wireframe 24-admin-api-explorer.html
   │
   ▼
Step 6  Bruno sync (optional) Import/export vault ↔ Bruno env files
```

| Step | Roadmap ID | Delivers | Blocks |
|---|---|---|---|
| **1. Catalog sync** | 2.9.1 | OpenAPI → grouped endpoint list | Steps 2, 5 |
| **2. Proxy test runner** | 2.9.2 | Server-side HTTP proxy + try/catch envelope | Steps 3, 5 |
| **3. Encrypted vault** | 2.9.3 | KMS CRUD + `{{var}}` resolution + auto-save | Steps 4, 5 |
| **4. PIN step-up** | 2.9.4 | Unlock session + masked list + reveal/copy audit | Step 5 (secrets UX) |
| **5. React screen** | 2.9.5 | Full admin UI | — |
| **6. Bruno sync** | 2.9.6 | DevOps import/export | — |

**Prerequisites:** FastAPI app repo live, internal RBAC (FR-150–166), `api/openapi.yaml` as source of truth, KMS key `alias/socvault-mvp-vault` (see [`AWS_SETUP_README.md`](./AWS_SETUP_README.md)). Track each step in [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) § API Explorer build order.

---

## Step 1 — Catalog sync

**Endpoint:** `GET /admin/explorer/catalog`  
**FRs:** FR-194  
**OpenAPI:** [`api/openapi.yaml`](../api/openapi.yaml) → `adminExplorerCatalog`

### Backend tasks

1. On app startup (or admin “Sync OpenAPI” action), parse `openapi.yaml` from repo path or S3 artifact.
2. Build response grouped by OpenAPI `tags` → folders (`Health`, `Auth`, `Scan`, …).
3. For each operation include: `method`, `path`, `operation_id`, `summary`, request body schema ref, security requirements.
4. Store `synced_at` and `openapi_version` in response; cache in DynamoDB or in-memory 5 min (no Redis on MVP).

### Acceptance criteria

- [ ] Returns all MVP paths from `openapi.yaml` (10+ endpoints)
- [ ] Groups match Bruno folders (`00-health`, `01-auth`, …)
- [ ] 403 for non-internal roles; 401 without JWT
- [ ] Unit test: catalog count matches OpenAPI path count

### Verify (curl / Bruno)

```bash
curl -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://api-staging.socvault.io/api/v1/admin/explorer/catalog
```

---

## Step 2 — Proxy test runner

**Endpoint:** `POST /admin/explorer/test`  
**FRs:** FR-195, FR-196, FR-197, FR-198  
**Threat:** T-12 (SSRF) — enforce allowlist

### Backend tasks

1. Accept `ExplorerTestRequest`: `method`, `path`, `environment`, `headers`, `query`, `body`, `auto_save`.
2. Resolve `base_url` from environment profile (`mock` | `staging` | `production`). **Staging is primary** for all operator testing.
3. **SSRF guard:** only allow requests to configured `base_url` host; block `169.254.169.254`, `10.*`, `127.*`, private ranges. **`mock`** profile may only target `localhost:4010` (Prism).
4. Execute HTTP call with `httpx` (async); wrap in try/except → unified `ExplorerTestResult`.
5. Map outcomes:
   - 2xx → `success: true`
   - 4xx/5xx → `success: false`, `error_type: HTTP_ERROR`
   - timeout → `error_type: TIMEOUT`
   - connection error → `error_type: NETWORK`
   - invalid body JSON → `error_type: VALIDATION`
6. Log `correlation_id`; **never** log Authorization header values.

### Acceptance criteria

- [ ] `POST /auth/verify-otp` against **staging** returns 200 envelope with `latency_ms`
- [ ] Invalid token on `GET /auth/me` returns `success: false`, `status_code: 401`
- [ ] Request to `http://169.254.169.254/` rejected with 403 before egress
- [ ] `stack_trace` present only when `APP_ENV=development`

### Verify

Run Bruno `01-auth` flow via `POST /admin/explorer/test` with inline body (vault not required yet).

---

## Step 3 — Encrypted vault

**Endpoints:** `GET|POST /admin/vault/variables`, `DELETE /admin/vault/variables/{key}`  
**FRs:** FR-199, FR-200, FR-203, FR-205 (write roles)

### Backend tasks

1. DynamoDB table `socvault-vault-variables`: PK `env#key`, attributes `ciphertext`, `is_secret`, `auto_saved`, `updated_at`, `updated_by`.
2. Encrypt values with **AWS KMS** (`Encrypt`/`Decrypt`); store ciphertext only.
3. `GET` list returns `VaultVariableMeta` — `masked_preview: "••••••••"` for secrets; non-secrets (e.g. `tenant_id`) may show last 4 chars.
4. Wire test runner: resolve `{{key}}` in path, headers, body before proxy call.
5. **Auto-save** (FR-200): after successful test, if `auto_save: true`, extract default map:

   | JSON path | Vault key |
   |---|---|
   | `access_token` | `access_token` |
   | `refresh_token` | `refresh_token` |
   | `tenant_id` | `tenant_id` |
   | `scan_id` | `scan_id` |

6. Return `auto_saved_keys[]` in `ExplorerTestResult`.

### Acceptance criteria

- [ ] Create/update variable; GET never returns plaintext
- [ ] Test with `Authorization: Bearer {{access_token}}` resolves from vault
- [ ] verify-otp test auto-saves tokens when toggle on
- [ ] Delete audited; write denied for SOC L1 role

---

## Step 4 — PIN step-up

**Endpoints:** `POST /admin/vault/unlock`, `POST /admin/vault/reveal/{key}`  
**FRs:** FR-201, FR-202, FR-204

### Backend tasks

1. Store Super Admin PIN hash (bcrypt) or verify against Cognito step-up — **never** store plaintext PIN.
2. `POST /admin/vault/unlock` with `{ credential }` → issue short-lived unlock session in **DynamoDB** (TTL **5 min**, refresh on reveal) or signed JWT — no Redis on MVP.
3. `POST /admin/vault/reveal/{key}` requires valid unlock session → KMS decrypt → return `{ key, value }` once.
4. Audit log collection: `VAULT_REVEAL`, `VAULT_COPY`, `VAULT_CREATE`, `VAULT_UPDATE`, `VAULT_DELETE` — actor, key name, timestamp; **no value**.
5. Copy endpoint optional: same unlock gate; audit as `VAULT_COPY`.

### Acceptance criteria

- [ ] List shows masked values without unlock
- [ ] Reveal without unlock → 403 `unlock_session_expired`
- [ ] After unlock, reveal works; expires after 5 min idle
- [ ] Audit row created for each reveal; value absent from logs

---

## Step 5 — React screen

**Wireframe:** [`24-admin-api-explorer.html`](../userstories-wireframes/24-admin-api-explorer.html)  
**User stories:** US-186–US-193  
**FRs:** all explorer + vault UX

### Frontend tasks

1. Route: `/admin/api-explorer` (internal layout, same sidebar as Admin Console).
2. **Left panel:** catalog from Step 1; filter; click loads endpoint into builder.
3. **Center:** tabs Body / Headers / Auth / Variables; **Send Test Request** → Step 2; success/failure panels (green/red) per wireframe.
4. **Right panel:** Pass & Keys list from Step 3; Reveal/Copy → PIN modal (Step 4).
5. Environment selector: `mock` | `staging` | `production` (default **staging**).
6. Auto-save toggle; toast when `auto_saved_keys` returned.
7. Recent test history (client-side last 20, or server persist optional).

### Acceptance criteria

- [ ] Matches wireframe layout (3-column + unlock modal)
- [ ] Full auth flow runnable without Bruno: signup → verify-otp → me → scan
- [ ] Secrets never rendered in DOM until unlock succeeds
- [ ] Story refs US-186–US-208 traceable in QA

### Threat Intel Feeds tab (Milestone 2.11)

Separate tab on same page — not a duplicate admin screen. Feed catalogue seeded from [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md) §5; UI calls `/admin/ti/feeds/*` only. See roadmap 2.11.

### Suggested component tree

```
AdminApiExplorerPage
├── MainTabs                     → API Explorer | Threat Intel Feeds
├── EnvironmentToolbar
├── ApiCatalogSidebar          → GET /admin/explorer/catalog
├── RequestBuilderPanel        → POST /admin/explorer/test
│   ├── TestResultSuccess
│   └── TestResultFailure
├── ThreatIntelFeedsPanel      → GET /admin/ti/feeds, POST .../test (Milestone 2.11)
├── PassKeysVaultPanel         → GET /admin/vault/variables
│   └── UnlockPinModal         → POST /admin/vault/unlock, /reveal/{key}
└── TestHistoryList
```

---

## Step 6 — Bruno sync (optional polish)

**FR:** FR-206 (partial)  
**Roadmap:** 2.9.6

1. **Export:** generate `.bru` environment file from vault keys for selected environment.
2. **Import:** parse Bruno env → upsert vault variables (secrets flagged `is_secret: true`).
3. Document in [`collections/README.md`](../collections/README.md).

---

## Milestone 2.9 completion checklist

- [ ] Steps 1–5 complete with pytest + one E2E Playwright path
- [ ] Bruno `01-auth` green using variables stored via explorer (not manual env edit)
- [ ] Threat T-11/T-12 mitigations verified (KMS, SSRF allowlist)
- [ ] Wireframe `24-admin-api-explorer.html` linked from `19-admin.html` (already done in blueprint)

---

## Suggested FastAPI module layout

```
app/
├── admin/
│   ├── explorer/
│   │   ├── catalog.py      # Step 1
│   │   ├── test_runner.py  # Step 2
│   │   └── openapi_sync.py
│   └── vault/
│       ├── crud.py         # Step 3
│       ├── crypto.py       # KMS wrap/unwrap
│       ├── unlock.py       # Step 4
│       └── audit.py
└── routers/admin_explorer.py
```

---

## Related documents

| Doc | Link |
|---|---|
| Requirements FR-194–207 | [`03_REQUIREMENTS.md`](./03_REQUIREMENTS.md) §1.14 |
| API paths & schemas | [`06_API_SPECIFICATION.md`](./06_API_SPECIFICATION.md), [`api/openapi.yaml`](../api/openapi.yaml) |
| Roadmap nano steps | [`05_PRODUCT_ROADMAP.md`](./05_PRODUCT_ROADMAP.md) Milestone 2.9 |
| Threat model | [`14_THREAT_MODEL.md`](./14_THREAT_MODEL.md) T-11, T-12 |
| Bruno collections | [`collections/README.md`](../collections/README.md) |
