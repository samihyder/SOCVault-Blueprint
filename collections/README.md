# SOCVault — API Collections

Runnable API collections aligned with [`api/openapi.yaml`](../api/openapi.yaml).

**Build order:** API routes first (API Gateway + Lambda), then wireframes on Amplify, linked via Super Admin. One user story at a time — [`docs/23_MVP_BUILD_ORDER_AND_QA.md`](../docs/23_MVP_BUILD_ORDER_AND_QA.md).

**Automated QA:** [`tests/qa/run-staging-qa.sh`](../tests/qa/run-staging-qa.sh) after every staging deploy.

## Bruno (recommended)

1. Install [Bruno](https://www.usebruno.com/downloads)
2. **Open Collection** → select `collections/bruno/SOCVault-MVP`
3. Choose environment:
   - **staging** — `https://api-staging.socvault.io/api/v1` (**primary** — CI/CD deploy target)
   - **production** — `https://api.socvault.io/api/v1` (smoke tests only; no destructive calls)
   - **mock** — `http://localhost:4010/api/v1` (Prism — optional offline contract check only)
   - ~~local~~ — deprecated; not used in SOCVault workflow
4. Run folders in order: `00-health` → `01-auth` → `02-scan` → `03-dashboard`

### Happy-path sequence (against staging)

```
00-health/health
01-auth/signup
01-auth/verify-otp    ← OTP from SNS/SES on staging
01-auth/me
02-scan/execute-recon
02-scan/get-scan      ← poll until COMPLETE
03-dashboard/summary
```

`verify-otp` and `execute-recon` auto-save `access_token` and `scan_id` to the Bruno environment.

## Super Admin Pass & Keys (in-app)

When the FastAPI backend and admin UI exist, the **API Explorer** (`24-admin-api-explorer.html`) replaces manual env editing for internal staff:

- Bruno/Postman variables sync with **Pass & Keys** per environment (`staging`, `production`)
- Tokens from successful test runs **auto-save** to the vault
- All secret values are **masked**; reveal/copy requires Super Admin **PIN or password**
- Use **Export to Bruno** / **Import Bruno env** for collection runs against staging

See FR-194–FR-207 and `/admin/explorer/*`, `/admin/vault/*` in OpenAPI.

## Mock server (optional — contract only)

For OpenAPI validation without AWS (not the primary dev loop):

```bash
cd api
npx @stoplight/prism-cli mock openapi.yaml -p 4010
```

Use Bruno environment **mock**.

## Postman

Import `collections/postman/SOCVault-MVP.postman_collection.json`.

Set collection variables: `base_url`, `access_token`, `scan_id`, `test_email`, `test_domain`.

## Phase 2+ stubs

Future folders (not yet in collection):

- `05-incidents/` — SOAR webhooks
- `06-malware/` — L8 MDRM
- `07-ai-chat/` — credits + chat
- `08-billing/` — Stripe

See [`docs/06_API_SPECIFICATION.md`](../docs/06_API_SPECIFICATION.md) for full catalogue.
