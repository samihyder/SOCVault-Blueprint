# ADR 004: AWS-only development — staging-first MVP

**Status:** Accepted (amended)  
**Date:** June 2026  
**MVP compute:** ADR-006 (serverless). **Paid scale:** ADR-005 (ECS Fargate) → EKS.

## Context

SOCVault will not use a local Docker development loop. All build, test, and runtime environments live on **one AWS account** (`eu-west-2`), maximising **Free Tier** during MVP. **Staging is the only active environment** until production cutover.

## Decision

1. **One AWS account** — single account for all SOCVault infrastructure.

2. **Staging = MVP** — all development, QA, demos, and Bruno tests target **staging** only until the production cutover checklist ([`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md) §7) completes.

3. **Production dormant** — Terraform `production` workspace exists but is **not applied** (or receives no traffic) until cutover. Separate naming when active:
   - `socvault-staging-*` vs `socvault-production-*`
   - SSM `/socvault/staging/*` vs `/socvault/production/*`
   - Separate S3, DynamoDB, Cognito, Lambda, Atlas clusters

4. **Serverless MVP (ADR-006)** — **API Gateway HTTP API → Lambda**, **Amplify Hosting** (React), **SQS + Lambda** async workers, **Lambda L1**. No Vercel, no Celery/Redis, no ALB on MVP.

5. **No local runtime** — engineers use Git + GitHub Actions only.

6. **CI/CD** — GitHub Actions: lint → QA → Terraform apply → deploy **staging** on `main`. Production deploy only after activation (+ GitHub approval). **AWS CodePipeline** at paid tier.

7. **Region** — `eu-west-2` (London) for UK/EU data residency (NFR-041).

8. **Frontend** — **AWS Amplify Hosting** (`app-staging.socvault.io`). CloudFront CDN at paid tier.

9. **Secrets** — SSM Parameter Store (MVP); never shared between environments.

10. **IaC** — all infrastructure via **Terraform**; no console-only resources.

## Consequences

- MVP AWS infra target **~$0–30/mo** (Free Tier Lambda, API GW, Cognito, S3) + Anthropic testing.
- Production not billed until cutover.
- Bruno and automated QA default to **api-staging.socvault.io**.
- Single GitHub OIDC role; production gated in GitHub Environments.

## Alternatives rejected

| Alternative | Why rejected |
|---|---|
| Local Docker Compose | Explicit product decision |
| Vercel frontend | User requirement: AWS serverless |
| ECS Fargate on MVP | Superseded by ADR-006; valid at paid tier (ADR-005) |
| Production live from week 1 | MVP is staging until cutover |

## Future migration

Paid tier: CloudFront · WAF · AWS Backup · ECS Fargate · **Amazon EKS** · CodePipeline. Optional: move production to second AWS account when compliance requires.
