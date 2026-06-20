# AWS Setup — start here

The full SOCVault AWS setup guide lives in:

**[`docs/AWS_SETUP_README.md`](docs/AWS_SETUP_README.md)**

Track provisioning in **[`DEVELOPMENT_TRACKER.md`](DEVELOPMENT_TRACKER.md)** (`INF-S-*` staging active; `INF-P-*` dormant until cutover).

**Architecture (MVP):** **Staging-only** serverless stack — **API Gateway + Lambda + Amplify + SQS**, **MongoDB Atlas M0 on AWS**, Terraform IaC, GitHub Actions CI/CD. See **ADR-006**.

That document covers:

- Free Tier–first serverless MVP (no Vercel, no ECS on bootstrap)
- Step-by-step staging configuration for `eu-west-2`
- Paid-tier path: CloudFront, WAF, Backup, EKS, CodePipeline
- Automated QA on staging (`tests/qa/`)
- Production cutover checklist

Related: [`docs/23_MVP_BUILD_ORDER_AND_QA.md`](docs/23_MVP_BUILD_ORDER_AND_QA.md) · [`docs/19_CI_CD_AND_ENVIRONMENTS.md`](docs/19_CI_CD_AND_ENVIRONMENTS.md)
