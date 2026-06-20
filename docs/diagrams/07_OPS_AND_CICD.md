# SOCVault — Ops, CI/CD & Observability
**Version 1.0 | June 2026**

Deployment, environment promotion, monitoring, and disaster recovery flows.

**Related:** [`19_CI_CD_AND_ENVIRONMENTS.md`](../19_CI_CD_AND_ENVIRONMENTS.md) · [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md) · ADR-006

---

## 1. CI/CD pipeline (staging MVP)

```mermaid
flowchart TB
  DEV([Engineer])
  GH[GitHub repo\nsocvault-app]
  PR[Pull Request]
  MAIN[main branch]
  GHA[GitHub Actions]

  subgraph Jobs
    LINT[Lint + typecheck]
    TF[Terraform plan/apply\nstaging]
    DEPLOY[Deploy Lambda + Amplify]
    QA[run-staging-qa.sh]
    BRUNO[Bruno collection]
  end

  DEV --> PR --> GHA
  PR --> LINT
  MAIN --> GHA
  GHA --> TF --> DEPLOY --> QA --> BRUNO
  QA -->|fail| BLOCK[Block merge / alert]
  QA -->|pass| OK[Staging updated]
```

---

## 2. Terraform module map

```mermaid
flowchart TB
  ROOT[terraform/ root]

  ROOT --> NET[networking\nVPC optional MVP]
  ROOT --> APIGW[api_gateway]
  ROOT --> LAM[lambda_api + workers]
  ROOT --> SQS[sqs_queues]
  ROOT --> COG[cognito_pool]
  ROOT --> S3[s3_artifacts]
  ROOT --> DDB[dynamodb_tables]
  ROOT --> SSM[ssm_parameters]
  ROOT --> AMP[amplify_app]
  ROOT --> IAM[iam_roles]
  ROOT --> CW[cloudwatch_alarms]

  subgraph PerEnv["per environment workspace"]
    STG[staging.tfvars]
    PRD[production.tfvars]
  end

  STG --> ROOT
  PRD -.->|cutover only| ROOT
```

---

## 3. Environment promotion flow

```mermaid
stateDiagram-v2
  [*] --> StagingActive: Phase 0 bootstrap
  StagingActive --> StagingActive: Every main push
  StagingActive --> CutoverReview: Checklist complete
  CutoverReview --> ProdActive: DNS + terraform apply prod
  ProdActive --> ProdActive: Prod deploy with approval
  StagingActive --> ProdActive: Parallel soak optional
```

### Cutover checklist (summary)

| # | Gate |
|---|---|
| 1 | Staging Bruno + `run-staging-qa.sh` green 7 consecutive days |
| 2 | Security review / threat model sign-off |
| 3 | Production Cognito pool + MongoDB provisioned (isolated) |
| 4 | DNS `api.socvault.io` + `app.socvault.io` |
| 5 | Post-cutover smoke QA on production |
| 6 | Rollback plan documented |

**Detail:** [`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md) §7

---

## 4. Observability architecture

```mermaid
flowchart TB
  subgraph Product["Product observability — build first"]
    OBS[Metrics Observatory UI\nwireframe 23]
    COGS[DynamoDB COGS aggregates]
    OBS --> COGS
  end

  subgraph AWS["AWS native — MVP"]
    CW[CloudWatch Logs + Metrics]
    ALM[CloudWatch Alarms\nLambda 5xx · SQS depth]
  end

  subgraph SRE["SRE — Milestone 4.4"]
    GRAF[Grafana dashboards]
    PD[PagerDuty / on-call]
  end

  LAPI[Lambda API] --> CW
  LWRK[Scan Workers] --> CW
  CW --> ALM
  CW --> GRAF
  ALM --> PD
  COGS --> OBS

  SA[Super Admin / DevOps] --> OBS
  SRE[On-call engineer] --> GRAF
```

| Tool | Audience | Metrics |
|---|---|---|
| Metrics Observatory | Super Admin, Billing, Exec | MRR vs COGS, Claude spend, per-tenant caps |
| CloudWatch | DevOps | Lambda duration, errors, API latency |
| Grafana | SRE | Throughput, queue depth, Atlas connections |

**Rule ([`02_TECHNICAL_STACK.md`](../02_TECHNICAL_STACK.md) §2.8):** Observatory first for operator UX; Grafana supplements for production SRE.

---

## 5. Alert routing

```mermaid
flowchart LR
  subgraph Triggers
    E1[Lambda error rate > 1%]
    E2[SQS age > 5 min]
    E3[API 5xx spike]
    E4[Claude daily cap FR-112]
    E5[Atlas connection fail]
  end

  E1 & E2 & E3 & E5 --> CW[CloudWatch Alarm]
  E4 --> OBS[Observatory alert]
  CW --> SNS[SNS topic]
  SNS --> EMAIL[Engineer email]
  SNS --> PD[PagerDuty — prod only]
```

---

## 6. Backup & disaster recovery

```mermaid
flowchart TB
  MDB[(MongoDB Atlas M0)] -->|continuous backup| SNAP[Atlas snapshots]
  S3[(S3 artifacts)] -->|versioning| S3V[S3 versions]
  DDB[(DynamoDB)] -->|PITR optional paid| DDBB[Point-in-time recovery]
  TF[Terraform state] -->|S3 backend + lock| TFSTATE[Remote state]

  SNAP --> RESTORE[Restore procedure]
  S3V --> RESTORE
  TFSTATE --> RESTORE
```

| Asset | RPO target | RTO target |
|---|---|---|
| MongoDB tenants/scans | 24h (M0 snapshot) | 4h |
| S3 scan artifacts | Real-time versioning | 1h |
| Terraform state | Per commit | 30 min |
| Cognito users | Export weekly | 2h |

---

## 7. Secret rotation flow (paid tier)

```mermaid
sequenceDiagram
  participant Dev as DevOps
  participant SM as Secrets Manager
  participant SSM as SSM (MVP)
  participant L as Lambda
  participant AUD as audit_log

  Note over SSM: MVP uses SSM Parameter Store
  Dev->>SSM: Update parameter version
  Dev->>L: Trigger redeploy / warm refresh
  L->>SSM: Read new version at cold start
  Dev->>AUD: Log rotation event

  Note over SM: Paid tier — automatic rotation
  Dev->>SM: Enable rotation Lambda
  SM->>L: Gradual credential swap
```

---

## 8. User story build loop (operational)

```mermaid
flowchart LR
  US[Pick US from xlsx] --> API[Implement API route]
  API --> OAPI[Update openapi.yaml]
  OAPI --> QA[QA script green]
  QA --> WF[Wireframe link]
  WF --> TRACK[Dev Tracker ACT row]
  TRACK --> US
```

**Rule:** One user story at a time · API-first · staging QA green before next story ([`23_MVP_BUILD_ORDER_AND_QA.md`](../23_MVP_BUILD_ORDER_AND_QA.md))

---

## 9. Scaling path (Free Tier → paid)

```mermaid
flowchart LR
  MVP[Serverless MVP\n~$100-115/mo] --> PAID[Paid tier\nCloudFront · WAF · EKS]
  MVP --> MKT[AWS Marketplace listing]
  PAID --> SCALE[Multi-region us-east-1]
  SCALE --> ENT[Enterprise SSO · dedicated pools]
```

| Stage | Architecture | ~Monthly cost |
|---|---|---|
| MVP staging | API GW + Lambda + Amplify + SQS | $100–115 |
| Paid tier | + CloudFront, WAF, EKS workers | $433+ |
| Scale | + us-east-1, ElastiCache | Custom |

---

## Related documents

| Doc | Role |
|---|---|
| [`01_C4_CONTEXT_CONTAINER.md`](./01_C4_CONTEXT_CONTAINER.md) | Container view |
| [`22_DATA_FLOW_DIAGRAMS.md`](../22_DATA_FLOW_DIAGRAMS.md) §7 | CI/CD DFD |
| [`DEVELOPMENT_TRACKER.md`](../../DEVELOPMENT_TRACKER.md) | Live stack status |
