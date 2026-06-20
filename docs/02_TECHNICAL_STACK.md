# SOCVault — Technical Stack & Architecture
**Version 1.2 | June 2026** — MVP: serverless staging (ADR-006)

---

## 1. Architecture Overview

SOCVault is a **cloud-native, multi-tenant SaaS platform** built on a microservices architecture. Each scanning layer runs in an isolated execution environment, ensuring tenant separation and cost predictability.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SOCVault Platform (MVP = staging)                     │
│                                                                         │
│  ┌──────────────┐   ┌─────────────────┐   ┌──────────────────────────┐ │
│  │  React/TS    │   │  API Gateway     │   │   Scan Runtimes          │ │
│  │  Dashboard   │──►│  HTTP API →      │──►│   L1 Lambda · L2+ Fargate│ │
│  │  (Amplify)   │   │  Lambda (FastAPI)│   │   (paid tier / EKS)      │ │
│  └──────────────┘   └────────┬────────┘   └──────────────────────────┘ │
│                              │                        │                  │
│                    ┌─────────▼────────┐    ┌──────────▼───────┐         │
│                    │ MongoDB Atlas M0 │    │   Claude API      │         │
│                    │ (on AWS eu-west-2)│   │   (Anthropic)     │         │
│                    └──────────────────┘    └──────────────────┘         │
│         SQS + Lambda workers (async scans) · Cognito · S3 · DynamoDB     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  SOC Layer (paid) — Wazuh EC2 → Claude Triage → SOAR             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Technology Stack

### 2.1 Backend

| Component | Technology | Rationale |
|---|---|---|
| **API edge** | Amazon API Gateway HTTP API | Auth, throttling, routing to Lambda |
| **API runtime (MVP)** | AWS Lambda + FastAPI (Mangum) | Serverless sync handlers; Free Tier |
| **Task Queue (MVP)** | Amazon SQS + Lambda workers | Async scan execution; replaces Celery on MVP |
| **Task Queue (paid)** | ElastiCache Redis + Celery on EKS | Long-running workers at scale |
| **Database (primary)** | MongoDB Atlas M0 on AWS (Motor) | Document-per-tenant; full MongoDB API |
| **Database (cache, paid)** | ElastiCache Redis | Rate limits, session cache at scale |
| **Auth** | AWS Cognito | JWT; API Gateway authorizer |
| **Cost Telemetry** | DynamoDB | Scan COGS, AI credits ledger |
| **File Storage** | AWS S3 | Scan artifacts, tenant-scoped paths |
| **Notifications** | AWS SNS | OTP SMS, alerts |
| **Secrets (MVP)** | SSM Parameter Store | Free Tier; Secrets Manager at paid tier |

### 2.2 AI & Intelligence Layer

| Component | Technology | Purpose |
|---|---|---|
| **Threat Translation** | Claude claude-sonnet-4-6 (Anthropic) | CVE-to-financial-risk translation, executive reports |
| **SOAR Reasoning** | Claude claude-sonnet-4-6 (Anthropic) | Incident triage, playbook selection, contain vs escalate |
| **Malware Analysis** | Claude claude-sonnet-4-6 (Anthropic) | Malware family ID, severity scoring, quarantine + removal commands |
| **L9 Agent** | Claude claude-opus-4-8 (Anthropic) | Autonomous app security assessment with extended thinking |
| **AI Chat** | Claude claude-sonnet-4-6 (Anthropic) | Conversational assistant, action dispatch |
| **Prompt Caching** | Anthropic Prompt Caching API | Reduce input token costs by 90% for repeated system prompts |
| **Threat Intel** | AbuseIPDB, AlienVault OTX, GreyNoise | IP reputation, threat actor attribution |
| **Cost Tracking** | Per-request token counting | Admin margin telemetry, per-tenant COGS |

**Model IDs:**
- Primary reasoning (financial risk, SOAR, malware): `claude-sonnet-4-6`
- Fast triage (cost-optimised, enrichment): `claude-haiku-4-5-20251001`
- L9 autonomous agent: `claude-opus-4-8`

### 2.3 Scanning Engine

| Layer | Tier | Tools | Runtime | Trigger |
|---|---|---|---|---|
| **L1 — Recon (15 steps)** | **Free** | Subfinder, Naabu, httpx, crt.sh, WHOIS, MXToolbox, HaveIBeenPwned | AWS Lambda | On-demand |
| **L2 — Web AppSec** | Paid | Nuclei, OWASP ZAP, Semgrep, Trivy | AWS Fargate | On-demand |
| **L3 — Mobile** | Paid | MobSF | Fargate (GPU optional) | On-demand |
| **L4 — API Security** | Paid | Nuclei API templates, ZAP API | Lambda | On-demand |
| **L5 — Compliance** | Paid | Custom Python rule engine, Prowler | Lambda | Scheduled |
| **L6 — Cloud** | Paid | CloudFox, Pacu, Prowler, Steampipe | Fargate | On-demand |
| **L7 — SOC/SIEM** | SOC Pro | Wazuh Manager + Agents | EC2 (persistent) | Continuous |
| **L8 — Malware D&R** | SOC Pro | ClamAV, YARA, Trivy, VirusTotal | Fargate + EC2 | Continuous + on-demand |
| **L9 — AI Agent Scan** | SOC Pro | Claude Opus 4.8 (extended thinking) | Fargate | On-demand |

#### L1 Free Recon — Complete 15-Step Scan Process

Every free scan runs all 15 steps in parallel, completing in under 90 seconds:

| Step | Action | Tool | What Is Flagged |
|---|---|---|---|
| 1 | WHOIS Lookup | Python-whois | Domain expiry <30 days, privacy shield on business domain, registrar mismatch |
| 2 | DNS Record Analysis | dnspython | Missing A/MX/NS, wildcard DNS, zone transfer enabled |
| 3 | Email Security (SPF/DKIM/DMARC) | checkdmarc | None/fail/softfail SPF policy; missing DMARC; email spoofing fully possible |
| 4 | SSL/TLS Certificate Audit | sslyze, crt.sh API | Cert expiry <30 days, self-signed, TLS 1.0/1.1 active, weak ciphers |
| 5 | HTTP Security Headers | Python requests | Missing CSP, HSTS, X-Frame-Options, X-Content-Type-Options |
| 6 | Certificate Transparency Lookup | crt.sh REST API | Subdomains exposed via SSL certificate history |
| 7 | Subdomain Discovery (passive) | Subfinder | Live subdomains via DNS, VirusTotal, Censys, DNSdumpster |
| 8 | Live Host Validation | httpx | HTTP status, redirect chains, server technology headers |
| 9 | Port Discovery | Naabu (top 100 ports) | High-risk open ports: 22 (SSH), 3306 (MySQL), 6379 (Redis), 27017 (MongoDB), 9200 (Elasticsearch) |
| 10 | Technology Fingerprinting | httpx + Wappalyzer sigs | CMS (WordPress/Joomla/Drupal), frameworks, CDN, version exposure |
| 11 | IP Reputation Check | AbuseIPDB | Blacklisted IPs, offshore hosting flags |
| 12 | Domain Reputation Check | Google Safe Browsing, URLhaus | Phishing/malware classification, blocklist status |
| 13 | Credential Leak Check | HaveIBeenPwned domain API | Number of exposed accounts, breach database names, credential exposure date |
| 14 | Subdomain Takeover Detection | Custom CNAME checker | CNAMEs pointing to unclaimed AWS/Azure/GitHub/Heroku services |
| 15 | Service Banner Analysis | Naabu + Nmap banners | Outdated service versions (e.g. OpenSSH 7.2 → multiple known CVEs) |

#### L8 Malware Detection & Response Engine

```
Detection Sources
│
├── Wazuh Agent (ClamAV real-time scan)
├── Wazuh FIM (file integrity monitoring — new/modified files)
├── Wazuh Rootkit Detection
├── L2 Web Scan (Nuclei webshell templates — paid)
├── Container Scan (Trivy — malicious layers)
└── Process Monitor (Wazuh — crypto miners, ransomware behaviour)
         │
         ▼
   SOCVault MDRM Microservice
         │
         ├── Hash lookup: VirusTotal / local YARA rules
         ├── File context: path, owner, creation time, size
         └── Host context: agent ID, hostname, running services
                  │
                  ▼
            Claude API (claude-sonnet-4-6)
                  │ Determines:
                  │ - Malware family (ransomware/trojan/cryptominer/webshell/rootkit/spyware)
                  │ - Severity score (1–10 with business impact)
                  │ - Lateral movement risk
                  │ - Data exfiltration likelihood
                  │ - Quarantine command
                  │ - Removal command + persistence cleanup
                  │ - Post-remediation verification command
                  │
            ┌─────▼─────────────────────────┐
            │                               │
    Confidence >95%               High-risk / system-wide
    Isolated file/process         (core services, databases)
            │                               │
            ▼                               ▼
    AUTO-REMEDIATE                  HUMAN APPROVAL GATE
    - Quarantine file               - Full context displayed
    - Kill process                  - Analyst approves action
    - Update blocklist              - Options: quarantine /
    - Alert sent                      isolate host / escalate
            │
            ▼
    Post-Remediation Verification
    - Re-scan with ClamAV
    - Confirm hash removed
    - Update health score
    - Generate incident report
```

### 2.4 Frontend

| Component | Technology | Rationale |
|---|---|---|
| **Framework** | React 18 + TypeScript | Type safety, component reuse, large ecosystem |
| **State Management** | Zustand | Lightweight, no Redux boilerplate |
| **UI Library** | shadcn/ui + Tailwind CSS | Accessible, customisable, brand-colour compatible |
| **Charts** | Recharts | Financial risk visualisation, health score dials |
| **API Client** | Axios + React Query (TanStack) | Caching, auto-retry, loading states |
| **Hosting** | AWS Amplify Hosting | Serverless React; staging MVP (`app-staging.socvault.io`) |
| **Auth (client)** | AWS Amplify UI + Cognito | JWT integration with API Gateway |

### 2.5 Infrastructure & DevOps

| Component | Technology | Purpose |
|---|---|---|
| **Containerisation** | Docker (Lambda images / EKS) | Scanner tool images; no local Compose runtime |
| **MVP orchestration** | API Gateway + Lambda + SQS | Serverless; staging-only until cutover |
| **Paid orchestration** | Amazon EKS (Kubernetes) | Full platform; migrate from Lambda at scale |
| **Scan bridge (paid)** | ECS Fargate (ADR-005) | Optional path before EKS |
| **CI/CD (MVP)** | GitHub Actions + Terraform | Lint, QA, deploy staging |
| **CI/CD (paid)** | AWS CodePipeline + CodeBuild | AWS-managed deploy orchestration |
| **IaC** | Terraform | All infrastructure |
| **Monitoring** | AWS CloudWatch | Metrics, logs, alarms |
| **CDN (paid)** | Amazon CloudFront | Edge cache for Amplify/API |
| **API Gateway** | HTTP API (v2) | Edge routing, Cognito JWT authorizer |

### 2.6 Security Stack (Platform Self-Security)

| Control | Implementation |
|---|---|
| **Transport** | TLS 1.3 enforced everywhere; HSTS headers |
| **Auth** | **Cognito-issued** JWT + refresh tokens (pool TTLs); MFA for admin (ADR-003) |
| **CORS** | Strict allowlist (not `*`); per-environment origin control |
| **Input Validation** | Pydantic v2 strict models on all API boundaries |
| **Scan Isolation** | Lambda/Fargate per invocation; tenant_id on all data paths |
| **Secrets** | SSM (MVP) → Secrets Manager (paid); zero secrets in git |
| **WAF (paid)** | AWS WAF + GuardDuty |
| **Penetration Testing** | Quarterly self-scan using SOCVault's own platform |
| **Data Encryption** | AES-256 at rest (MongoDB Atlas, S3, DynamoDB); envelope encryption |
| **Audit Logging** | AWS CloudTrail for all API and infrastructure events |

### 2.7 Access control (RBAC)

Three **separate** models — do not merge:

| Scope | Model | Source |
|---|---|---|
| **Tenant sub-users** | 3 fixed slots: Support Sub-Tenant, Viewer-Only Exec, Manager | FR-141–150 · wireframe `21` · Milestone 2.7 |
| **SOCVault internal staff** | 12 roles (SOC L1–L4, GRC, VA/PT, DevOps, SysOps, Billing, Exec, Manager, …) | FR-151–165 · wireframe `22` · Milestone 2.7 |
| **Enterprise SSO (Phase 4+)** | SAML 2.0 federation; maps IdP groups → tenant roles | FR-009 · Roadmap 4.2.1 |

Tenant primary admin is the Cognito user who completed onboarding; sub-users are additional Cognito accounts linked via `tenant_id`.

### 2.8 Observability

| Layer | Tool | Audience | When |
|---|---|---|---|
| **Metrics Observatory** | Custom admin UI (FR-170–182, wireframe `23`) | Super Admin / internal roles | Milestone **2.8** — product-facing cost, Claude, API, Lambda/SQS health |
| **Grafana + CloudWatch** | Infra dashboards | DevOps / on-call | Milestone **4.4** — SRE latency, throughput, paging |
| **CloudWatch alarms** | AWS native | All envs | MVP — Lambda errors, API 5xx, SQS depth |

Build **Observatory first** for operator UX; Grafana supplements for production SRE — not a duplicate product surface.

---

## 3. Data Architecture

### 3.1 MongoDB Collections (Primary Database)

```javascript
// tenants — core user/company record
{
  tenant_id: UUID,           // partition key
  business_email: String,    // unique
  phone_number: String,
  workspace_domain: String,
  payment_tier: Enum["FREEMIUM", "STARTER", "PRO", "ENTERPRISE"],
  licensed_targets: [String], // IPs and domains with active licenses
  last_scan_timestamp: Number,
  wazuh_agents: [String],
  stripe_customer_id: String, // Phase 2
  created_at: Date,
  is_verified: Boolean,
  mfa_enabled: Boolean
}

// scans — immutable scan records
{
  scan_id: UUID,
  tenant_id: UUID,           // foreign key
  layer: Enum["RECON","APPSEC","MOBILE","API","COMPLIANCE","CLOUD","SOC","MALWARE","L9_AGENT"],
  target: String,
  status: Enum["QUEUED","RUNNING","COMPLETE","FAILED"],
  raw_findings: Object,
  executive_report: Object,  // AI-translated output
  cogs: {
    compute_cost: Number,
    ai_token_cost: Number,
    threat_intel_cost: Number,
    total: Number
  },
  started_at: Date,
  completed_at: Date
}

// incidents — SOC/SOAR events
{
  incident_id: UUID,
  tenant_id: UUID,
  wazuh_alert_id: String,
  severity: Number,
  agent_id: String,
  rule_description: String,
  ti_enrichment: Object,     // AbuseIPDB, OTX report
  ai_analysis: Object,       // Claude triage result
  selected_playbook: String,
  execution_status: Enum["QUEUED","AWAITING_APPROVAL","EXECUTING","COMPLETED","FAILED"],
  steps_completed: [Object],
  created_at: Date
}

// sub_users — tenant team members (max 3 per tenant)
{
  user_id: UUID,
  tenant_id: UUID,
  email: String,
  role: Enum["SUPPORT","VIEWER","MANAGER"],
  status: Enum["PENDING","ACTIVE","REVOKED"],
  invited_at: Date,
  accepted_at: Date
}

// malware_incidents — L8 MDRM events
{
  incident_id: UUID,
  tenant_id: UUID,
  file_hash: String,
  family: String,
  severity: Number,
  auto_remediated: Boolean,
  actions: [Object],
  created_at: Date
}

// internal_users — SOCVault staff RBAC
{
  user_id: UUID,
  team_id: UUID,
  role: Enum["SOC_L1","SOC_L2",...,"MANAGER"],
  mfa_enrolled: Boolean
}
```

DynamoDB tables: `credits` (tenant_id, balance, reserved), `credit_transactions` (ledger), `cost_telemetry` (per-scan COGS writes)

### 3.2 Multi-Tenant Isolation Model

```
S3 Bucket: socvault-artifacts/
  └── {tenant_id}/
      └── {scan_id}/
          ├── raw_output.json
          ├── executive_report.json
          └── remediation_scripts/

MongoDB: all queries include tenant_id filter (middleware-enforced)
DynamoDB: tenant_id as partition key — no cross-tenant reads possible
Cognito: custom attribute `tenant_id` on every token
Fargate: each scan task in ephemeral isolated subnet
```

---

## 4. API Design

### 4.1 Core Endpoints

```
POST   /api/v1/auth/signup              — Business email + phone onboarding
POST   /api/v1/auth/verify-otp          — OTP verification
POST   /api/v1/auth/refresh             — JWT refresh
GET    /api/v1/auth/me                  — Current tenant profile

POST   /api/v1/scan/execute             — Trigger scan (layer + target)
GET    /api/v1/scan/{scan_id}           — Polling: scan status + results
GET    /api/v1/scan/history             — Tenant scan history

GET    /api/v1/dashboard/summary        — Health score, top risks, exposure
GET    /api/v1/dashboard/compliance     — Compliance control status

POST   /api/v1/incidents/{id}/approve   — Human approval gate (SOAR)
POST   /api/v1/incidents/{id}/reject    — Reject playbook execution
GET    /api/v1/incidents                — Incident feed for tenant

POST   /api/v1/billing/subscribe        — Stripe subscription creation (Phase 2)
POST   /api/v1/billing/portal           — Stripe customer portal link

GET    /api/v1/admin/telemetry          — COGS dashboard (admin only)
GET    /api/v1/admin/tenants            — Tenant management (admin only)

POST   /api/v1/malware/ingest           — Wazuh ClamAV/FIM webhook (Phase 2)
GET    /api/v1/malware/incidents        — Malware incident list
POST   /api/v1/malware/{id}/approve     — Approve remediation
POST   /api/v1/malware/{id}/reject      — Reject remediation

POST   /api/v1/scan/l9/execute          — L9 AI agent scan
GET    /api/v1/scan/l9/{id}/log         — Live agent activity log

GET    /api/v1/credits/balance          — AI Chat credit balance
POST   /api/v1/credits/purchase         — Stripe credit checkout
POST   /api/v1/ai/chat                  — AI Chat (streaming)
POST   /api/v1/ai/action                — Execute chat action

GET    /api/v1/team/members             — Tenant sub-users
POST   /api/v1/team/invite              — Invite sub-user
GET    /api/v1/admin/metrics/summary    — Metrics Observatory feeds
```

See [`06_API_SPECIFICATION.md`](./06_API_SPECIFICATION.md) for the full catalogue.

### 4.2 Async Scan Flow

```
Client POST /scan/execute
     │
     ▼
API validates tenant entitlement
     │
     ▼
Scan request → API Gateway → Lambda API → **SQS message**
Lambda worker consumes SQS → invokes L1 Lambda / writes status
     │
     ▼
API returns { scan_id, status: "QUEUED" } immediately
     │
     ▼  (background)
Fargate/Lambda runs scanner binary
     │
     ▼
Claude API generates executive report
     │
     ▼
Scan record updated: status = "COMPLETE"
     │
     ▼
Client polls GET /scan/{scan_id} or receives WebSocket push
```

---

## 5. Local development stack

> **Deprecated for SOCVault.** ADR-006: all development runs on **AWS staging** via API Gateway + Lambda + Amplify. Compose snippet below is **Lambda container build reference only**.

```yaml
# docker-compose.yml — Lambda container build reference only (no Redis/Celery on MVP)
services:
  socvault-api:       FastAPI (port 8000 — local unit test image build only)
  worker:             SQS consumer (same codebase; runs on Lambda in staging)
```

Scanner binaries (subfinder, naabu, httpx, nuclei) run in **Lambda** or scanner containers on AWS — not installed locally.

Unit tests run on **GitHub Actions** runners. Integration tests target **staging API**.

---

## 6. AWS Infrastructure

### 6.1 MVP bootstrap (staging-only, serverless, Free Tier–first)

**MVP = staging** until production cutover. All infra via **Terraform**. See ADR-006.

| Layer | Staging (active) | Production | Scale / paid tier |
|---|---|---|---|
| **Frontend** | **AWS Amplify Hosting** | Dormant until cutover | + **CloudFront** CDN (paid) |
| **API edge** | **API Gateway HTTP API** | Same module, dormant | + **WAF** (paid) |
| **Sync backend** | **AWS Lambda** (FastAPI/Mangum) | Dormant | ECS Fargate → **EKS** (paid) |
| **Async jobs** | **SQS + Lambda** | Dormant | ElastiCache + workers on EKS |
| **L1 recon** | **Lambda** | — | Lambda / Fargate |
| **Database** | **MongoDB Atlas M0 on AWS** | Dormant cluster | M10+ · **AWS Backup** (paid) |
| **Auth** | **Cognito** | Dormant pool | MFA, SSO |
| **Secrets** | **SSM Parameter Store** | — | Secrets Manager (paid) |
| **CI/CD** | **GitHub Actions** → staging | Post-cutover approval | **CodePipeline** (paid) |
| **Security** | Baseline IAM + TLS | — | GuardDuty, WAF, Shield (paid) |

**Guides:** [`AWS_SETUP_README.md`](./AWS_SETUP_README.md) · [`19_CI_CD_AND_ENVIRONMENTS.md`](./19_CI_CD_AND_ENVIRONMENTS.md) · [`23_MVP_BUILD_ORDER_AND_QA.md`](./23_MVP_BUILD_ORDER_AND_QA.md) · ADR-004 · ADR-006

### 6.2 Production topology (paid tier — EKS target)

```
VPC (10.0.0.0/16)
├── Edge
│   ├── Amazon CloudFront (paid)
│   ├── AWS WAF (paid)
│   └── API Gateway HTTP API
├── Amazon EKS (Kubernetes — paid)
│   ├── Deployment: API (HPA 2–20)
│   ├── Deployment: Celery workers (KEDA queue scaling)
│   └── Jobs: scan execution (L2–L9)
├── Private Subnets — Data Tier
│   ├── MongoDB Atlas M10+ (VPC Peering)
│   ├── ElastiCache Redis
│   └── EC2 — Wazuh Manager (persistent)
└── AWS Backup (paid) — S3, DynamoDB snapshots

MVP path before EKS: Lambda + SQS (ADR-006) → optional ECS Fargate (ADR-005)

Supporting: Cognito · S3 · DynamoDB · SNS · SQS · Step Functions · CloudWatch · Secrets Manager · ACM
```

### 6.3 Free Tier → paid upgrade triggers

| Signal | Action |
|---|---|
| EC2 CPU > 70% sustained (Wazuh only) | Resize Wazuh instance or add ASG |
| Fargate API p95 latency or CPU > 70% | Raise max task count or task CPU/memory |
| Atlas M0 > 400 MB or connection limits | Upgrade to M10 + VPC peering |
| Need private subnets / multi-AZ | Add NAT Gateway + ALB (accept ~$50+/mo base cost) |
| Redis memory pressure on EC2 | ElastiCache t4g.micro |
| >10 secrets / compliance audit | Secrets Manager + dedicated KMS CMK |
| SOC Pro beta (L7/L8) | Wazuh EC2 + agent fleet |

Full checklist: [`AWS_SETUP_README.md` §4–§6](./AWS_SETUP_README.md).

---

## 7. Scanning Tool Dependencies

### Required System Binaries (Container images)

```dockerfile
# Scanner base image packages
RUN apt-get install -y nmap whois dnsutils curl wget python3-pip

# Go tools (via go install)
RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install github.com/projectdiscovery/httpx/cmd/httpx@latest
RUN go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
RUN go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
RUN go install github.com/smicallef/spiderfoot@latest

# Python tools
RUN pip install semgrep trivy-python cloudfox pacu

# OWASP ZAP (Java)
RUN wget https://github.com/zaproxy/zaproxy/releases/download/v2.14.0/ZAP_2.14.0_Linux.tar.gz
```

### Threat Intelligence API Keys Required

See **[`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md)** for the full per-layer registry, Super Admin Pass & Keys configuration, correlation engine, and phase rollout.

| Service | Free Tier | Paid Threshold | Cost |
|---|---|---|---|
| AbuseIPDB | 1,000 checks/day | >1K/day | $20/month |
| AlienVault OTX | Unlimited (community) | Enterprise features | Free → $150/month |
| GreyNoise | 100 queries/day | >100/day | $99/month |
| Shodan | 100 queries/month | >100/month | $69/month |
| VirusTotal | 500 requests/day | >500/day | $99/month |

---

## 8. Performance & Scaling Targets

| Metric | MVP Target | Scale Target |
|---|---|---|
| API response time (p95) | <500ms | <200ms |
| Recon scan duration (pipeline) | **< 90 seconds** | **< 60 seconds** |
| Recon user journey (NFR-002) | **< 3 minutes** (requirement) | **< 2 minutes** (stretch at scale) |
| Full VAPT scan duration | <15 minutes | <10 minutes |
| Concurrent scan capacity | 10 | 500 |
| Dashboard load time | <2s | <1s |
| Uptime SLA | 99.5% | 99.9% |
| SOAR response loop | <60 seconds | <30 seconds |

---

## 9. Technology Decisions & Trade-offs

| Decision | Chosen | Alternative | Reason |
|---|---|---|---|
| Database | MongoDB | PostgreSQL | Flexible schema for varied scan outputs |
| AI Provider | Anthropic Claude | OpenAI GPT-4 | Better JSON adherence, superior security reasoning, prompt caching |
| Scan runtime | AWS Lambda → Fargate → **EKS** | Kubernetes day one | MVP Free Tier; K8s on paid plan (ADR-006) |
| Frontend | React + TS on **Amplify** | Vercel | AWS-native serverless; CDN via CloudFront at paid tier |
| Auth | AWS Cognito | Auth0 | AWS-native, cheaper at scale, built-in MFA |
| Message queue | SQS + Lambda (MVP) → ElastiCache + Celery (EKS) | AWS SQS only | Serverless MVP; Celery on K8s at scale |
| IaC | Terraform | AWS CDK | Ecosystem breadth; multi-cloud portability later |
