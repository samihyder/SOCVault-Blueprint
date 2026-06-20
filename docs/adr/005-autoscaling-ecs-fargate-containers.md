# ADR 005: Auto-scaling ECS Fargate for container workloads

**Status:** Accepted — **MVP superseded by ADR-006** (serverless Lambda path for staging MVP)  
**Date:** June 2026  
**Still applies to:** Paid-tier scale path before / alongside EKS (see ADR-006 §4)

## Context

SOCVault runs multiple container types: always-on API and Celery workers, ephemeral scan tasks (L2+), and persistent SOC components (Wazuh on EC2). Fixed single-instance EC2 with Docker Compose does not scale with traffic or scan load and creates a manual resize path.

Investor and technical docs already describe Fargate as the scan runtime and production target. Platform containers must follow the same model from bootstrap.

## Decision

> **MVP note (ADR-006):** Staging bootstrap uses **API Gateway + Lambda + SQS + Amplify**. The Fargate/Celery/ALB decisions below apply to **paid-tier scale** (Phase 2b+) before or alongside EKS — not the serverless MVP path.

1. **All stateless platform containers run on ECS Fargate** with **Application Auto Scaling** — not on a fixed EC2 Compose stack.

2. **One ECS cluster per AWS account** (`socvault-main`), with **separate services per environment**:
   - `api-staging` / `celery-staging`
   - `api-production` / `celery-production`

3. **Application Load Balancer (ALB)** — one shared ALB, host-based routing:
   - `api-staging.socvault.io` → staging target group
   - `api.socvault.io` → production target group

4. **Auto-scaling policies** (Application Auto Scaling on ECS service desired count):

   | Service | Staging (min → max) | Production (min → max) | Primary metric |
   |---|---|---|---|
   | API | 1 → 4 | 2 → 10 | ALB `RequestCountPerTarget` + CPU 70% |
   | Celery workers | 0 → 4 | 1 → 20 | Custom: Redis queue depth (`celery_queue_depth`) |
   | Scan execution (L2+) | 0 → 10 | 0 → 50 | SQS visible messages / Step Functions concurrency |
   | L1 recon | — | — | **Lambda** (AWS-managed concurrency) |

5. **Redis broker** — **ElastiCache Redis** (`t4g.micro` per environment namespace, or one cluster with logical DB index 0/1). Not a Compose sidecar on EC2.

6. **Deploy path** — GitHub Actions → ECR → `aws ecs update-service --force-new-deployment` (no SSM Run Command on EC2 for API).

7. **Network bootstrap** — Fargate tasks in **public subnets** with public IPs until NAT Gateway is justified (~$32/mo); then move tasks to private subnets.

8. **Exceptions** (not Fargate-autoscaled):
   - **Wazuh Manager** — persistent EC2 (ASG optional at scale)
   - **Local engineer machines** — no runtime (ADR-004)

## Cost note

Auto-scaling Fargate replaces Free Tier EC2 savings. Expect **~$70–95/mo** base for dual-env bootstrap (ALB + minimal Fargate tasks + ElastiCache) vs **~$100–115/mo** total Phase 0 budget including Anthropic testing. Scale-out adds cost only when metrics trigger new tasks.

## Consequences

- No SSH/Compose ops for API deploys; infra is Terraform + ECS.
- Celery scale-to-zero on staging saves idle worker cost.
- Production API **min 2 tasks** across AZs when second AZ is added (HA).
- FR-159, FR-174 (Metrics Observatory) must surface ECS task count and scaling events.
- Phase 2.1b “migrate EC2 → Fargate” step is **removed** — Fargate is day-one.

## Alternatives rejected

| Alternative | Why rejected |
|---|---|
| EC2 Docker Compose (fixed t3.micro) | No autoscale; manual resize; contradicts platform target |
| Kubernetes (EKS) | Cluster ops overhead; overkill for team size |
| Always-on Fargate without auto-scaling | Pays for idle capacity; misses scan burst handling |

## References

- [`19_CI_CD_AND_ENVIRONMENTS.md`](../19_CI_CD_AND_ENVIRONMENTS.md)
- [`02_TECHNICAL_STACK.md`](../02_TECHNICAL_STACK.md) §6
- [`AWS_SETUP_README.md`](../AWS_SETUP_README.md)
