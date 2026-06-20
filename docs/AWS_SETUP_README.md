# SOCVault — AWS Setup Guide (MVP)
**Staging-first · Serverless · Free Tier–first · Terraform IaC**  
**Version 1.1 | June 2026 | Region: `eu-west-2` (London)**

---

## How to use this document

| Document | Role |
|---|---|
| [`adr/006-serverless-mvp-staging-first-iac.md`](./adr/006-serverless-mvp-staging-first-iac.md) | **Authoritative MVP architecture** |
| [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) | User story build order + QA |
| [`19_CI_CD_AND_ENVIRONMENTS.md`](./19_CI_CD_AND_ENVIRONMENTS.md) | GitHub Actions + paid CodePipeline |
| [`02_TECHNICAL_STACK.md`](./02_TECHNICAL_STACK.md) | Full stack + EKS paid path |

**Strategy:** **MVP = staging only.** **Free Tier** where possible; **CDN, WAF, Backup, EKS, CodePipeline** on **paid tier** — update plan if course changes. **No local runtime.** All infra via **Terraform**.

**Progress:** [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md)

---

## 1. MVP architecture — staging (active)

```
STAGING (Free Tier–first)
├── app-staging.socvault.io     AWS Amplify Hosting (React)
├── api-staging.socvault.io     API Gateway HTTP API → Lambda
├── Lambda: api (Mangum/FastAPI), workers, l1-recon
├── SQS: scan-jobs-staging
├── Cognito · S3 · DynamoDB · SSM /staging/*
└── MongoDB Atlas M0 on AWS eu-west-2

PRODUCTION — dormant (Terraform workspace exists; not applied until cutover)

PAID TIER (not MVP): CloudFront · WAF · GuardDuty · AWS Backup · EKS · CodePipeline
```

See ADR-006 for service recommendations and paid-tier triggers.

---

## 2. Account bootstrap

| Setting | Value |
|---|---|
| Accounts | One AWS account |
| Region | `eu-west-2` |
| Budget | **$15–30/mo** alert (Free Tier MVP) |
| IaC state | S3 + DynamoDB lock table |

### Naming

```
Project     = socvault
Environment = staging | production
```

Prefix: `socvault-staging-*` (production modules dormant until cutover).

---

## 3. Service checklist (staging)

Work in order; check off in Dev Tracker.

### 3.1 Terraform backend

| Resource | Purpose |
|---|---|
| S3 bucket | Remote state |
| DynamoDB table | State locking |

### 3.2 API Gateway HTTP API

| Setting | Value |
|---|---|
| Protocol | HTTP API (not REST — lower cost) |
| Integration | Lambda (proxy) |
| Authorizer | Cognito JWT (when auth live) |
| Custom domain | `api-staging.socvault.io` + ACM |

**Recommendation:** Import routes from [`api/openapi.yaml`](../api/openapi.yaml) incrementally per user story.

### 3.3 Lambda

| Function | Role |
|---|---|
| `socvault-staging-api` | FastAPI via Mangum or route handlers |
| `socvault-staging-worker` | SQS consumer — scan orchestration |
| `socvault-staging-l1` | 15-step recon |

Free Tier: 1M requests/mo + 400k GB-seconds.

### 3.4 Amplify Hosting

Connect `socvault-app` GitHub repo, branch `main`, build `apps/web`. Custom domain `app-staging.socvault.io`.

### 3.5 MongoDB on AWS

**Recommendation:** **MongoDB Atlas M0** in **AWS eu-west-2** (free). Full MongoDB compatibility for Motor/Pydantic.

**Not MVP:** Amazon DocumentDB (MongoDB-compatible but API gaps). Re-evaluate at paid tier if AWS-native DB required.

### 3.6 SQS

Queue `socvault-staging-scan-jobs` — replaces Celery/Redis on serverless MVP.

### 3.7–3.15

Cognito, S3, DynamoDB, SNS, SSM, IAM, CloudWatch — same patterns as prior guide; scope to **staging** only until cutover.

---

## 4. Deployment sequence

```
1. Account + MFA + budget
2. Terraform backend
3. Staging: API GW + Lambda health route
4. Staging: Cognito, S3, DynamoDB, SQS, SSM
5. Atlas M0 socvault-staging
6. Amplify app-staging
7. GitHub OIDC + deploy-staging.yml + qa-staging.yml
8. ./tests/qa/run-staging-qa.sh green
9. Begin US-001 (see doc 23)
10. (Defer) production workspace, CloudFront, WAF, Backup, EKS, CodePipeline
```

---

## 5. Paid tier migration

| Phase | Add |
|---|---|
| Hardening | Atlas M10, Secrets Manager, CloudTrail |
| CDN + Security | CloudFront, WAF, GuardDuty |
| Backups | AWS Backup, Atlas continuous backup |
| Scale | ECS Fargate (ADR-005) or **EKS** (ADR-006) |
| CI/CD | AWS CodePipeline + CodeBuild |

---

## 6. Verification

- [ ] `GET https://api-staging.socvault.io/api/v1/health` → 200
- [ ] `./tests/qa/run-staging-qa.sh` → pass
- [ ] Amplify app-staging loads
- [ ] Budget alert configured
- [ ] No production resources billing (unless cutover started)

---

*Full legacy EC2/ECS sections removed — see ADR-005/006 and git history if needed.*
