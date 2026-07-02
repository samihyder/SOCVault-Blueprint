---
name: infrastructure-deployment
description: Use for a GitHub issue labeled `infrastructure`, a deployment request, or any change to Terraform, AWS resources, IAM, or CI/CD pipelines for SOCVault. Maps to the DevOps Sub-Agent in SOCVAULT_PRODUCT_DESCRIPTION.md secs 1.6/2.6.1.
---

Trigger: an `infrastructure`-labeled issue, a deployment request, or a Terraform/CI/CD/AWS change.

1. Scope constraint first: SOCVault is staging-first, serverless, single AWS account per ADR-006 (`docs/adr/006-serverless-mvp-staging-first-iac.md`) — API Gateway + Lambda + Amplify + SQS, MongoDB Atlas M0, `eu-west-2`. Production is dormant until explicit cutover; don't provision it and don't reach for ECS/Fargate (a superseded ADR) unless explicitly asked.
2. For a full infrastructure change (new Terraform module, new pipeline stage), delegate to the `devops-agent` subagent via the Agent tool.
3. Generating/validating Terraform and opening a PR with the diff does not need confirmation. Actually running `terraform apply` or deploying real AWS resources does — always confirm with the user first, since infrastructure changes cost money and are hard to reverse.
4. Secrets belong in AWS Secrets Manager under `/socvault/staging/*` or `/socvault/production/*` (see `.env.example`) — never hardcoded.
5. After any deployment, verify via CloudWatch that it's actually healthy before reporting success — don't just report "deployed" because `terraform apply` exited 0.
