# SOCVault — CI/CD & Environments (AWS-only)
**Staging-first MVP · Serverless · IaC · GitHub Actions → AWS staging**  
**Version 1.3 | June 2026**

---

## Strategy summary

| Principle | Detail |
|---|---|
| **MVP = staging** | Production **dormant** until cutover — all dev/QA on staging |
| **Free Tier first** | Lambda, API Gateway, Cognito, S3, DynamoDB, Amplify free tiers; plan updates if course changes |
| **Serverless MVP** | API Gateway + Lambda + Amplify + SQS (ADR-006) |
| **IaC** | **Terraform** — all infrastructure; no manual console-only resources |
| **CI (MVP)** | **GitHub Actions** — lint, QA, `terraform apply` staging |
| **CI (paid)** | **AWS CodePipeline + CodeBuild** orchestrates deploys; GitHub remains source |
| **K8s (paid)** | **Amazon EKS** — paid tier only (ADR-006 §6) |

Related: [`AWS_SETUP_README.md`](./AWS_SETUP_README.md) · ADR-004 · ADR-006 · [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md)

---

## 1. Environment model

### Staging (active — MVP)

```
AWS Account — eu-west-2 — Terraform workspace: staging
│
├── app-staging.socvault.io     →  AWS Amplify Hosting (React)
├── api-staging.socvault.io     →  API Gateway HTTP API → Lambda
├── Cognito socvault-staging-users
├── Lambda: api, workers, l1-recon
├── SQS: scan-jobs-staging
├── S3 socvault-artifacts-staging-*
├── DynamoDB socvault-staging-*
├── SSM /socvault/staging/*
└── MongoDB Atlas M0 socvault-staging (AWS eu-west-2)
```

### Production (dormant until cutover)

Same module layout with `production` workspace — **not applied or zero-traffic** until [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) §7 checklist completes.

| | **Staging** | **Production** |
|---|---|---|
| **Status (MVP)** | **Active** | **Dormant** |
| **API URL** | `https://api-staging.socvault.io/api/v1` | `https://api.socvault.io/api/v1` |
| **App URL** | `https://app-staging.socvault.io` | `https://app.socvault.io` |
| **Deploy trigger** | Push to `main` | Release tag + approval (after activation) |
| **QA** | Full automated suite | Smoke only post-cutover |

---

## 2. MVP serverless architecture

```
Engineer → GitHub (socvault-app)
              │
              ▼
       GitHub Actions
       ├── lint + pytest (unit)
       ├── tests/qa/run-staging-qa.sh
       ├── terraform plan/apply (staging)
       └── deploy Lambda + Amplify staging

Tenant browser → Amplify (app-staging) → API Gateway → Lambda (FastAPI/Mangum)
Scan request → Lambda API → SQS → Lambda worker → L1 Lambda / S3 / Atlas
Super Admin → API Explorer → staging API + Pass & Keys vault
```

### Paid tier additions (when activated)

| Capability | Service |
|---|---|
| CDN | CloudFront in front of Amplify / API |
| Security | WAF, GuardDuty, Security Hub |
| Backups | AWS Backup + Atlas M10+ continuous backup |
| Scale | ECS Fargate (ADR-005) → **EKS** (Kubernetes) |
| CI/CD | CodePipeline replaces GitHub deploy steps |

---

## 3. Repository layout (`socvault-app`)

```
socvault-app/
├── .github/workflows/
│   ├── ci.yml                 # PR: lint, unit, terraform plan
│   ├── deploy-staging.yml     # main → QA → terraform apply staging
│   ├── deploy-production.yml  # tag + approval (post-cutover)
│   └── qa-staging.yml         # callable QA workflow
├── infra/terraform/
│   ├── modules/               # api, lambda, amplify, cognito, sqs, s3, iam
│   ├── environments/
│   │   ├── staging/           # active
│   │   └── production/        # dormant
│   └── backend.tf             # S3 state + DynamoDB lock
├── apps/
│   ├── api/                   # FastAPI + Mangum handler
│   ├── web/                   # React → Amplify
│   └── workers/               # SQS Lambda handlers
├── tests/qa/                  # symlink or copy from blueprint
└── collections/bruno/         # API collection (sync with blueprint)
```

---

## 4. CI/CD pipeline

### 4.1 PR flow (`ci.yml`)

```
PR opened → lint (ruff/eslint) → pytest unit → terraform plan (staging)
         → optional: OpenAPI diff vs blueprint
```

### 4.2 Staging deploy (`deploy-staging.yml`) — primary MVP loop

| Step | Detail |
|---|---|
| 1 | OIDC assume `github-actions-socvault` role |
| 2 | `pytest tests/unit` |
| 3 | `./tests/qa/run-staging-qa.sh --pre-deploy` (health + auth smoke) |
| 4 | Build Lambda zip/container → push ECR if container image |
| 5 | `terraform apply -auto-approve` (staging workspace) |
| 6 | `./tests/qa/run-staging-qa.sh` (full suite post-deploy) |
| 7 | Optional: `bru run` Bruno collection |

### 4.3 Production deploy (`deploy-production.yml`) — after cutover

| Step | Detail |
|---|---|
| 1 | GitHub **production** environment approval |
| 2 | Full QA on staging must be green (required check) |
| 3 | `terraform apply` (production workspace) |
| 4 | Smoke `GET /health` on production API |
| 5 | ACT- log entry |

### 4.4 Paid tier — AWS CodePipeline

```
GitHub (CodeStar Connection) → CodePipeline
  → CodeBuild: test + QA + terraform
  → Deploy staging / production stages with manual approval on prod
```

GitHub Actions retained for PR validation.

---

## 5. Bootstrap order (staging only)

```
1. AWS account + MFA + $15–30 budget alert
2. Terraform backend (S3 state bucket + DynamoDB lock)
3. Staging module: VPC (minimal), API Gateway, Lambda, Cognito, S3, DynamoDB, SQS, SSM
4. MongoDB Atlas M0 socvault-staging
5. Amplify app-staging connected to GitHub branch main
6. GitHub OIDC + deploy-staging.yml
7. GET /health green on api-staging
8. tests/qa/run-staging-qa.sh green
9. (Defer) production workspace, CloudFront, WAF, Backup, EKS, CodePipeline
```

---

## 6. Cost (MVP staging — Free Tier first)

| Resource | MVP cost |
|---|---|
| API Gateway HTTP | $0–$1/mo (1M free) |
| Lambda | $0 within Free Tier |
| Amplify | $0 build minutes (free tier) |
| Cognito, S3, DynamoDB | $0 within limits |
| Atlas M0 | $0 |
| CloudFront, WAF, Backup, EKS | **$0 — not provisioned** |
| Anthropic (testing) | ~$20–80/mo |

---

*Staging is MVP. Production activates on checklist. Plan updates when paid tier services are added.*
