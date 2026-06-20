# SOCVault API — MVP Contract

OpenAPI 3.1 contract and Bruno collection for Phase 1 MVP.

## Files

| File | Purpose |
|---|---|
| [`openapi.yaml`](./openapi.yaml) | Source of truth — schemas, examples, error responses |
| [`../collections/bruno/SOCVault-MVP/`](../collections/bruno/SOCVault-MVP/) | Runnable Bruno collection |
| [`../collections/postman/SOCVault-MVP.postman_collection.json`](../collections/postman/SOCVault-MVP.postman_collection.json) | Postman import (optional) |

## MVP endpoints (10)

| Method | Path | Auth |
|---|---|---|
| GET | `/health` | No |
| POST | `/auth/signup` | No |
| POST | `/auth/verify-otp` | No |
| POST | `/auth/refresh` | No |
| GET | `/auth/me` | Bearer |
| POST | `/scan/execute` | Bearer |
| GET | `/scan/{scan_id}` | Bearer |
| GET | `/scan/history` | Bearer |
| GET | `/dashboard/summary` | Bearer |
| GET | `/admin/telemetry` | Bearer |

## Mock server (Prism)

```bash
cd api
npx --yes @stoplight/prism-cli@5 mock openapi.yaml -p 4010
```

Select Bruno environment **mock** (`base_url: http://localhost:4010/api/v1`) and run the collection.

## Validate OpenAPI

```bash
npx --yes @redocly/cli@1 lint openapi.yaml
```

## Implement with FastAPI (Lambda / Mangum)

When the app repo exists, validate the deployed staging API against this contract:

```bash
# Against staging (authoritative)
curl -s https://api-staging.socvault.io/openapi.json | npx openapi-diff openapi.yaml -

# Optional: local dev server
curl -s http://localhost:8000/openapi.json | npx openapi-diff openapi.yaml -
```

FastAPI on Lambda (Mangum) should expose matching paths under `/api/v1` and return schemas defined here.

## Auth flow (collection)

1. **Signup** → saves `tenant_id`
2. **Verify OTP** → saves `access_token`, `refresh_token`
3. All protected requests use `Authorization: Bearer {{access_token}}`
4. **Execute scan** → saves `scan_id`
5. **Get scan** → poll until `COMPLETE`

Run folders in order: `00-health` → `01-auth` → `02-scan` → `03-dashboard`.
