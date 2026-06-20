# ADR 006: Serverless MVP on staging — tiered AWS services, IaC, EKS at paid tier

**Status:** Accepted  
**Date:** June 2026  
**Amends:** ADR-004 (environments), ADR-005 (MVP compute — ECS Fargate deferred to paid scale path)

## Context

SOCVault will be built **user story by user story**. During MVP, **staging is the only active runtime** until production is deliberately cut over. The team will **maximise AWS Free Tier** where possible; paid services (CDN, advanced security, backups, EKS, AWS-native CI/CD) activate when revenue or compliance requires them — and the plan will be updated if course changes.

Engineering happens in this repo and `socvault-app`; **all infrastructure is Terraform (IaC)**. Code pushes to **GitHub**; **GitHub Actions** runs tests and deploys to **staging**; **production** deploys only after production is activated.

## Decision

### 1. Environment model

| Environment | MVP status | Purpose |
|---|---|---|
| **Staging** | **Active** — all development, QA, demos | `api-staging.socvault.io`, `app-staging.socvault.io` |
| **Production** | **Dormant** until cutover checklist complete | Provisioned via same IaC with `count = 0` or separate workspace — no traffic until go-live |

**Rule:** Bruno, automated QA, and Super Admin default to **staging**. Production smoke tests only after activation.

### 2. MVP architecture (Free Tier–first, serverless)

```
                    STAGING (MVP — active)
┌─────────────────────────────────────────────────────────────┐
│  AWS Amplify Hosting          React SPA (serverless CDN edge) │
│  Amazon API Gateway (HTTP)    Edge API — auth, routing, throttling │
│  AWS Lambda                   Sync API handlers (FastAPI/Mangum or handlers) │
│  Amazon SQS                   Async job queue (replaces Celery for MVP) │
│  AWS Lambda (workers)         Scan orchestration, webhooks │
│  AWS Lambda (L1)              15-step recon scanner │
│  Amazon Cognito               Auth / JWT │
│  MongoDB Atlas M0 on AWS     Primary database (eu-west-2) │
│  Amazon S3                    Artifacts │
│  Amazon DynamoDB              Cost telemetry │
│  SSM Parameter Store          Secrets (Free Tier) │
│  Terraform                    All infra |
│  GitHub Actions               Lint → QA → deploy staging │
└─────────────────────────────────────────────────────────────┘

Deferred to PAID tier (see §4):
  CloudFront CDN · AWS WAF/Shield/GuardDuty · AWS Backup · ElastiCache
  ECS Fargate (optional bridge) · Amazon EKS (Kubernetes) · AWS CodePipeline
```

### 3. Service choices & recommendations

| Layer | MVP (Free Tier–first) | Recommendation |
|---|---|---|
| **Frontend** | **AWS Amplify Hosting** | Serverless; connects to staging API; replaces Vercel for AWS-native stack |
| **API edge** | **Amazon API Gateway HTTP API** | Cheaper/lighter than REST API; OpenAPI import; Cognito authorizer |
| **Sync backend** | **AWS Lambda** (Python 3.12) | FastAPI via **Mangum** adapter **or** thin handlers per route for smallest cold starts |
| **Async backend** | **SQS + Lambda** | Serverless queue; no Redis/Celery on MVP (paid: ElastiCache + workers on ECS/EKS) |
| **L1 scans** | **Lambda** (container or zip) | Already Free Tier–aligned |
| **L2+ scans** | Lambda / Fargate tasks (paid) | Ephemeral; scale on queue depth |
| **Database** | **MongoDB Atlas M0** (hosted on **AWS** `eu-west-2`) | Full MongoDB API (Motor driver); **not DocumentDB** on MVP — DocumentDB lacks full MongoDB compatibility |
| **Auth** | **Amazon Cognito** | JWT; integrates with API Gateway authorizer |
| **Secrets** | **SSM Parameter Store** | Free Tier; Secrets Manager at paid hardening |
| **IaC** | **Terraform** | Modules: `network`, `api`, `lambda`, `amplify`, `data`, `iam`; workspaces `staging` / `production` |
| **CI (MVP)** | **GitHub Actions** | Push to `main` → QA suite → Terraform apply + Lambda/Amplify deploy **staging only** |
| **CI (paid)** | **AWS CodePipeline + CodeBuild** | Orchestrates staging/production; GitHub remains source via CodeStar connection |
| **Orchestration (paid)** | **Amazon EKS (Kubernetes)** | When multi-service ops, scan isolation, or team scale exceeds Lambda/Fargate comfort |

### 4. Paid-tier activation (plan — update when course changes)

| Capability | Paid AWS service | Trigger |
|---|---|---|
| **CDN** | **Amazon CloudFront** in front of Amplify/API | Custom domain performance, global edge, cache static assets |
| **Security** | **AWS WAF**, **GuardDuty**, **Security Hub**, **Shield Standard** | Beta customers, compliance questionnaire |
| **Backups** | **AWS Backup** (S3, DynamoDB), **Atlas continuous backup** (M10+) | Production active; RPO/RTO commitments |
| **Redis / Celery** | **ElastiCache** + ECS workers | High async volume; long-running Celery tasks |
| **Scale compute** | **ECS Fargate** auto-scaling | Sustained load beyond Lambda limits |
| **Kubernetes** | **Amazon EKS** | Paid plan — full platform on K8s; migrate from Lambda/Fargate with IaC |
| **CI/CD** | **AWS CodePipeline** | Paid plan — AWS-managed pipelines; GitHub Actions retained for PR checks |

### 5. Build order (mandatory)

1. **API collection first** — implement routes on API Gateway + Lambda aligned to [`api/openapi.yaml`](../api/openapi.yaml); validate with Bruno/Postman against **staging**.
2. **Automated QA** — [`tests/qa/`](../tests/qa/) runs on every staging deploy (see [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md)).
3. **Frontend screens** — one wireframe at a time; Amplify deploy to staging.
4. **Super Admin panel** — API Explorer + Pass & Keys links frontend env vars to live staging API; Development Tracker records user-story completion.
5. **User stories** — pick **one US-* at a time** from [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md); do not start next until QA green for current story.

### 6. Kubernetes (EKS) — paid plan only

- **Not used during MVP** (staging serverless stack).
- **EKS cluster** provisioned via Terraform when entering paid infrastructure phase.
- Workloads migrate: API (Deployment + HPA), workers (Deployment + KEDA), scan jobs (Jobs / Fargate on EKS).
- Helm charts or Kustomize overlays per environment; same GitHub → CodePipeline promotion path.

### 7. CI/CD flow

```
PR  → GitHub Actions: lint, unit tests, terraform plan, qa-staging (optional mock)
merge main → GitHub Actions: full QA → terraform apply (staging) → lambda/amplify deploy
production cutover → manual checklist → terraform apply (production workspace) → smoke QA
paid tier → CodePipeline triggers on GitHub tag; CodeBuild runs QA + deploy both envs
```

## Consequences

- MVP monthly AWS cost target: **~$0–30** infra (Free Tier Lambda, API Gateway, Cognito, S3, DynamoDB) + Anthropic testing.
- No production resources billed until production workspace activated.
- Celery/Redis removed from MVP path — SQS/Lambda async pattern required in application code.
- DocumentDB deferred; Atlas M0 is external but runs on AWS region.
- ADR-005 ECS Fargate auto-scaling remains valid as **paid-tier scale path before or alongside EKS**.

## Alternatives rejected (MVP)

| Alternative | Why rejected for MVP |
|---|---|
| Vercel frontend | User requirement: serverless on AWS |
| EC2 Docker Compose | No Free Tier autoscale; superseded |
| DocumentDB | MongoDB API gaps vs Motor/Pydantic models |
| EKS on day one | Cost and ops overhead before product validation |
| Production + staging both live from week 1 | User: MVP is staging until production active |

## References

- [`19_CI_CD_AND_ENVIRONMENTS.md`](../19_CI_CD_AND_ENVIRONMENTS.md)
- [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md)
- [`AWS_SETUP_README.md`](../AWS_SETUP_README.md)
