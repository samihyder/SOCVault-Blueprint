# SOCVault — Automated Staging QA

Runs against **live staging API** (`api-staging.socvault.io`). Part of the MVP build loop (ADR-006, doc 23).

## Quick start

```bash
cp tests/qa/config/staging.env.example tests/qa/config/staging.env
# edit staging.env if needed

pip install -r tests/qa/requirements.txt
chmod +x tests/qa/run-staging-qa.sh
./tests/qa/run-staging-qa.sh
```

## Modes

| Command | When |
|---|---|
| `./tests/qa/run-staging-qa.sh` | Full suite after deploy |
| `./tests/qa/run-staging-qa.sh --pre-deploy` | Health only before `terraform apply` |
| `./tests/qa/run-staging-qa.sh --story US-005` | Single user story filter |
| `./tests/qa/run-staging-qa.sh --bruno` | Include Bruno CLI collection |

## Manifest

User story → test mapping: [`manifest.yaml`](./manifest.yaml)

## GitHub Actions

Copy [`templates/github/workflows/qa-staging.yml`](../templates/github/workflows/qa-staging.yml) to `socvault-app/.github/workflows/` when the app repo is created.

## Super Admin

After manual OTP verification on staging, save `access_token` to Pass & Keys → export to `STAGING_ACCESS_TOKEN` for scan QA tests.
