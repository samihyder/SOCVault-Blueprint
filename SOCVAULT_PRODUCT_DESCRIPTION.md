# SOCVault — Complete Product Description
**Unified AI-Enabled Cybersecurity Solution for SMBs**

**Document Version:** 1.0  
**Last Updated:** June 2026  
**Scope:** Comprehensive product overview for engineering, skills development, and AI agent generation  
**Status:** Phase 1 MVP (Staging Active; Production Dormant)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Development Workflow & Automation](#development-workflow--automation)
3. [Product Vision & Problem Statement](#product-vision--problem-statement)
4. [Core Value Proposition](#core-value-proposition)
5. [Market Opportunity](#market-opportunity)
6. [Product Architecture](#product-architecture)
7. [Scanning Engine — 8 Attack Surface Layers](#scanning-engine--8-attack-surface-layers)
8. [AI Intelligence Layer](#ai-intelligence-layer)
9. [SOAR (Security Orchestration, Automation & Response)](#soar-security-orchestration-automation--response)
10. [Malware Detection & Response Engine (L8)](#malware-detection--response-engine-l8)
11. [Business Model & Revenue Streams](#business-model--revenue-streams)
12. [Functional Requirements](#functional-requirements)
13. [API Specification](#api-specification)
14. [Technology Stack](#technology-stack)
15. [Authentication & Security](#authentication--security)
16. [Data Model & Database Schema](#data-model--database-schema)
17. [Deployment & Infrastructure](#deployment--infrastructure)
18. [User Tiers & Feature Gates](#user-tiers--feature-gates)
19. [Compliance & Data Protection](#compliance--data-protection)
20. [Admin Setup Roadmap & GitHub Projects](#admin-setup-roadmap--github-projects)
21. [Development Roadmap](#development-roadmap)
22. [Competitive Advantage & USPs](#competitive-advantage--usps)
23. [Key Metrics & Success Criteria](#key-metrics--success-criteria)

---

## 1. Development Workflow & Automation

### 1.1 Development Team Structure & Tools

SOCVault development is fully automated and AI-augmented, with clear separation of concerns:

| Role | Tool | Responsibility | Agent/Skill |
|---|---|---|---|
| **Frontend Engineer** | Claude (AI) + Cursor (IDE) | React/TypeScript UI development | Claude UI Agent |
| **Backend Engineer** | Cursor (IDE) + Claude (optional pairing) | Python/FastAPI backend development | Cursor Backend Agent |
| **UI/UX Designer** | Stitch (optional) + Claude | UI design system, component library | Stitch Design System |
| **DevOps/Infra** | Terraform + GitHub Actions | AWS infrastructure, CI/CD pipelines | DevOps Sub-Agent |
| **QA/Testing** | GitHub Actions + Playwright | Automated E2E testing, Bruno API tests | QA Automation Agent |
| **Project Manager** | GitHub Projects + Automation | Roadmap tracking, milestone management | Project Management Bot |

### 1.2 AI-Augmented Development Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SOCVault Development Workflow                         │
│                     (100% Automated + AI-Driven)                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Product Manager / Engineer                                             │
│  ↓                                                                      │
│  Create issue in GitHub Projects                                        │
│  (User story + acceptance criteria + technical specs)                   │
│  ↓                                                                      │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ FRONTEND TRACK (Claude AI Agent)                               │  │
│  │ ├─ Generate React/TypeScript component                         │  │
│  │ ├─ Apply Tailwind CSS + shadcn/ui styling                      │  │
│  │ ├─ Implement state management (Zustand)                        │  │
│  │ ├─ Connect to API endpoints (Axios + React Query)              │  │
│  │ ├─ Generate unit tests (Jest)                                  │  │
│  │ └─ Create Storybook stories (optional)                         │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│  ↓ (parallel)                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐  │
│  │ BACKEND TRACK (Cursor + Claude Agent)                          │  │
│  │ ├─ Define API endpoint (FastAPI + Pydantic)                    │  │
│  │ ├─ Implement business logic (Python async)                     │  │
│  │ ├─ Add database operations (Motor + MongoDB)                   │  │
│  │ ├─ Implement error handling + validation                       │  │
│  │ ├─ Generate unit tests (pytest)                                │  │
│  │ ├─ Update OpenAPI spec                                         │  │
│  │ └─ Add CloudWatch logging                                      │  │
│  └─────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                      │
│  GitHub Actions: Automated CI Pipeline                                 │
│  ├─ Lint (ruff for Python; ESLint for TS)                            │
│  ├─ Type check (mypy for Python; tsc for TS)                         │
│  ├─ Unit tests (pytest + Jest)                                        │
│  ├─ Integration tests (against staging Lambda)                        │
│  ├─ API contract tests (Bruno collection)                             │
│  ├─ Security scan (Trivy, pre-commit hooks)                           │
│  ├─ Build artifacts (Docker images for Lambda)                        │
│  └─ Deploy to staging (Terraform apply)                               │
│  ↓                                                                      │
│  Automated E2E Tests (Playwright + Bruno)                              │
│  ├─ UI smoke tests (login → scan → dashboard)                         │
│  ├─ API contract validation (10 MVP endpoints)                        │
│  ├─ Performance validation (p95 latency <500ms)                       │
│  └─ Freemium rate limiting validation                                 │
│  ↓                                                                      │
│  ✓ All green → Staging deployment complete                             │
│  ✓ GitHub Projects status auto-updates: "Done"                         │
│  ✓ Automated Slack notification                                        │
│  ↓ (on tag / manual approval)                                          │
│  Production Deployment                                                 │
│  ├─ Deploy-production.yml (on-demand, approval gated)                 │
│  ├─ Blue-green deployment (new infra, cutover on green)               │
│  ├─ Smoke tests on production (GET /health, basic workflow)           │
│  └─ Rollback on failure (automated)                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 1.3 GitHub Projects Automation

**Repository:** [https://github.com/samihyder/SOCVault-Blueprint](https://github.com/samihyder/SOCVault-Blueprint)

### Project Board Structure

```
SOCVault Project Board (GitHub Projects v2)
│
├─ 📋 Backlog
│  ├─ US-001: User signup with business email
│  ├─ US-002: OTP verification
│  └─ ... (all user stories from roadmap)
│
├─ 🔄 In Progress
│  ├─ [Claude AI] Build dashboard layout component
│  ├─ [Cursor Backend] Implement POST /scan/execute endpoint
│  └─ [DevOps] Set up Terraform staging VPC
│
├─ 🧪 In Review
│  ├─ [PR #42] React dashboard health score widget
│  ├─ [PR #43] L1 scanner driver implementation
│  └─ [PR #44] CloudWatch monitoring setup
│
├─ ✅ Done (This Sprint)
│  ├─ ✓ API Gateway HTTP API + Lambda skeleton
│  ├─ ✓ Cognito user pool configuration
│  └─ ✓ S3 artifact bucket + DynamoDB setup
│
└─ 📊 Done (All Time)
   └─ [Historical completed issues]
```

### Automation Rules

| Trigger | Action | Tool |
|---|---|---|
| Issue created with label `frontend` | Add to "In Progress" → assign Claude AI Agent | GitHub Actions |
| Issue created with label `backend` | Add to "In Progress" → assign Cursor Agent | GitHub Actions |
| PR opened | Run CI pipeline (lint, test, build) | GitHub Actions |
| CI pipeline passes | Auto-merge (if auto-merge enabled); update board status | GitHub Actions |
| Deployment to staging succeeds | Move to "Done" + add comment with staging URL | GitHub Actions |
| Production deployment requested | Send Slack notification + require approval | GitHub Actions |
| Sprint ends (Friday EOD) | Generate burndown report + next sprint setup | GitHub Actions + Scheduled |

### Issue Templates

**Frontend Issue Template:**
```markdown
## Frontend Feature: {feature_name}

### Description
{User story from roadmap}

### Acceptance Criteria
- [ ] Component renders without errors
- [ ] Responsive on mobile/tablet/desktop
- [ ] Tailwind CSS styling applied (SOCVault brand colors)
- [ ] Unit tests written (>80% coverage)
- [ ] Storybook stories created (if component library)
- [ ] API integration complete (Axios + React Query)
- [ ] E2E test passes (Playwright)

### Design
[Link to Stitch design / wireframe]

### API Endpoints Required
- `GET /dashboard/summary` (for data fetch)

### Labels
- `frontend`
- `phase-1`
- `ui-component`

### Assigned To
Claude UI Agent (AI-driven development)
```

**Backend Issue Template:**
```markdown
## Backend Feature: {feature_name}

### Description
{Technical spec from product doc}

### Acceptance Criteria
- [ ] Endpoint implemented (FastAPI + Pydantic)
- [ ] Request/response matches OpenAPI spec
- [ ] Error handling for edge cases
- [ ] Database operations correct (tenant_id scoped)
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests pass (against MongoDB Atlas M0)
- [ ] OpenAPI spec updated
- [ ] CloudWatch logging added
- [ ] Deployed to staging (via CI/CD)

### API Endpoint
```
POST /api/v1/scan/execute
{
  "layer": "RECON",
  "target": "example.com",
  "consent": true
}
```

### Labels
- `backend`
- `phase-1`
- `api-endpoint`

### Assigned To
Cursor Backend Agent (IDE-driven development)
```

---

## 1.4 CI/CD Pipeline (GitHub Actions → AWS)

### Pipeline Stages

**File:** `.github/workflows/ci.yml`

```yaml
name: CI Pipeline (Lint + Test)

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies (backend)
        run: pip install -r requirements.txt
      
      - name: Install dependencies (frontend)
        run: cd frontend && npm install
      
      - name: Lint (Python)
        run: ruff check . --select=E,W,F
      
      - name: Type check (Python)
        run: mypy . --ignore-missing-imports
      
      - name: Lint (TypeScript)
        run: cd frontend && npm run lint
      
      - name: Type check (TypeScript)
        run: cd frontend && npm run type-check
      
      - name: Security scan (Python)
        run: bandit -r . -ll
      
      - name: Unit tests (backend)
        run: pytest tests/unit/ -v --cov=app --cov-report=xml
      
      - name: Unit tests (frontend)
        run: cd frontend && npm run test -- --coverage
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml, ./frontend/coverage/coverage-final.json
```

**File:** `.github/workflows/deploy-staging.yml`

```yaml
name: Deploy to Staging

on:
  push:
    branches: [main]

jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    env:
      AWS_REGION: eu-west-2
      ENVIRONMENT: staging
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-2
      
      - name: Build backend Docker image
        run: |
          docker build -t socvault-api:latest -f Dockerfile.api .
          aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin ${{ secrets.ECR_REGISTRY }}
          docker tag socvault-api:latest ${{ secrets.ECR_REGISTRY }}/socvault-api:latest
          docker push ${{ secrets.ECR_REGISTRY }}/socvault-api:latest
      
      - name: Build frontend
        run: |
          cd frontend
          npm install
          npm run build -- --mode staging
      
      - name: Deploy infrastructure (Terraform)
        run: |
          cd terraform
          terraform init -backend-config=staging.tfbackend
          terraform plan -var-file=staging.tfvars -out=tfplan
          terraform apply tfplan
      
      - name: Deploy frontend to Amplify
        run: |
          aws amplify start-deployment --app-id ${{ secrets.AMPLIFY_APP_ID }} --branch-name staging
      
      - name: Run E2E tests (staging)
        run: |
          npm run test:e2e -- --config=playwright.staging.config.ts
      
      - name: Run API contract tests (Bruno)
        run: |
          npm run test:api -- --environment=staging
      
      - name: Notify Slack on success
        if: success()
        uses: slackapi/slack-github-action@v1.24.0
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
          payload: |
            {
              "text": "✅ SOCVault Staging Deployment Successful",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Staging deployment complete*\n*Frontend:* https://app-staging.socvault.io\n*API:* https://api-staging.socvault.io/api/v1\n*Status:* ${{ job.status }}"
                  }
                }
              ]
            }
      
      - name: Update GitHub Projects
        if: success()
        run: |
          curl -X POST https://api.github.com/repos/samihyder/SOCVault-Blueprint/issues/${{ github.event.pull_request.number }}/comments \
            -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            -d '{"body": "✅ Deployed to staging: https://app-staging.socvault.io"}'
```

**File:** `.github/workflows/deploy-production.yml`

```yaml
name: Deploy to Production (Manual + Approval)

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Release version'
        required: true
  push:
    tags:
      - 'v*'

jobs:
  production-deploy:
    runs-on: ubuntu-latest
    environment: production  # Requires approval
    env:
      AWS_REGION: eu-west-2
      ENVIRONMENT: production
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS credentials (production)
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.PROD_AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.PROD_AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-2
          role-to-assume: arn:aws:iam::${{ secrets.PROD_AWS_ACCOUNT }}:role/GitHubActionsRole
      
      - name: Blue-green deployment (create new infra)
        run: |
          cd terraform
          terraform init -backend-config=production.tfbackend
          # Deploy to green environment
          terraform workspace select green || terraform workspace new green
          terraform apply -var-file=production.tfvars -auto-approve
      
      - name: Smoke tests (production)
        run: |
          curl -f https://api.socvault.io/api/v1/health || exit 1
          npm run test:smoke -- --environment=production
      
      - name: Switch to new infrastructure (blue-green cutover)
        if: success()
        run: |
          # Update load balancer to route to green environment
          aws elbv2 modify-rule --rule-arn arn:aws:elasticloadbalancing:... --conditions Field=path-pattern,Values="/api/*"
      
      - name: Rollback on failure
        if: failure()
        run: |
          # Switch back to blue environment
          aws elbv2 modify-rule --rule-arn arn:aws:elasticloadbalancing:... --conditions Field=path-pattern,Values="/api/*"
      
      - name: Notify team (Slack + Email)
        if: always()
        uses: slackapi/slack-github-action@v1.24.0
        with:
          webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
          payload: |
            {
              "text": "${{ job.status == 'success' && '✅' || '❌' }} Production Deployment",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "Production deployment: ${{ job.status }}\nVersion: ${{ inputs.version }}\nAPI: https://api.socvault.io/api/v1"
                  }
                }
              ]
            }
```

---

## 1.5 Automated QA Testing Suite

**File:** `tests/qa/run-staging-qa.sh`

```bash
#!/bin/bash
set -e

export SOCVAULT_API="https://api-staging.socvault.io/api/v1"
export SOCVAULT_APP="https://app-staging.socvault.io"

echo "🧪 Starting SOCVault Automated QA Suite"
echo "=========================================="

# 1. API Contract Tests (Bruno Collection)
echo "📋 Running API contract tests (Bruno)..."
npm run test:api:bruno -- \
  --environment=staging \
  --reporters=cli,json:test-results/bruno.json

# 2. Playwright E2E Tests
echo "🎭 Running Playwright E2E tests..."
npx playwright test --config=playwright.staging.config.ts

# 3. Performance Tests (k6)
echo "⚡ Running performance tests..."
k6 run tests/performance/scan-execution.js \
  --vus 10 --duration 30s \
  --out json=test-results/performance.json

# 4. Security Scanning
echo "🔒 Running security scan..."
trivy image ${{ secrets.ECR_REGISTRY }}/socvault-api:latest \
  --format json \
  --output test-results/trivy.json

# 5. Data Validation
echo "💾 Validating data integrity..."
pytest tests/qa/data_validation.py -v --junit-xml=test-results/data-validation.xml

# 6. Compliance Checks
echo "⚖️ Running compliance checks..."
npm run test:compliance -- --output=json:test-results/compliance.json

echo ""
echo "✅ QA Suite Complete"
echo "Test results: test-results/"
```

---

## 1.6 Automated Agent Responsibilities

### Claude UI Agent

**Responsibilities:**
- Generate React/TypeScript components from GitHub issues
- Apply Tailwind CSS + SOCVault brand styling
- Implement state management (Zustand) and API integration
- Write Jest unit tests (target >80% coverage)
- Create Storybook stories for component library
- Generate PR descriptions with change summaries
- Self-review code for accessibility (WCAG 2.1 AA)

**Integration:**
- Receives issue data via GitHub Actions
- Commits code to feature branch
- Opens PR with auto-generated description
- Responds to review comments

**Example Issue → Code Flow:**
```
GitHub Issue (frontend/dashboard):
  "Build dashboard health score widget"
  
↓ (Claude AI Agent activated)

Generated Code:
  ✓ components/Dashboard/HealthScoreWidget.tsx
  ✓ components/Dashboard/HealthScoreWidget.test.tsx
  ✓ components/Dashboard/HealthScoreWidget.stories.tsx
  ✓ Updated dashboard.api.ts with query hook
  
↓ (Auto-commit + PR)

PR #52: "feat: Add dashboard health score widget"
  - Component renders 0–100 gauge
  - Tailwind styling + animations
  - React Query integration
  - 85% test coverage
```

### Cursor Backend Agent

**Responsibilities:**
- Generate FastAPI endpoints from technical specifications
- Implement Pydantic models for request/response validation
- Write MongoDB queries with Motor (async)
- Implement error handling + HTTP status codes
- Write pytest unit + integration tests (>80% coverage)
- Update OpenAPI specification
- Add CloudWatch logging + metrics
- Generate commit messages and PR descriptions

**Integration:**
- Receives issue data via GitHub Actions
- Develops locally in Cursor IDE (AI-assisted)
- Commits to feature branch with conventional commits
- Opens PR with technical summary

**Example Issue → Code Flow:**
```
GitHub Issue (backend/api):
  "Implement POST /scan/execute endpoint"
  
↓ (Cursor Backend Agent activated)

Generated Code:
  ✓ app/api/routes/scan.py
  ✓ app/schemas/scan.py (Pydantic models)
  ✓ app/services/scan_driver.py (business logic)
  ✓ tests/unit/routes/test_scan.py
  ✓ tests/integration/test_scan_e2e.py
  ✓ Updated api/openapi.yaml
  
↓ (Auto-commit + PR)

PR #53: "feat(api): Implement POST /scan/execute endpoint"
  - Validates layer, target, consent
  - Enforces freemium rate limit
  - Enqueues to SQS
  - Returns 202 + scan_id
  - Includes CloudWatch logging
  - 87% test coverage
```

### DevOps Sub-Agent

**Responsibilities:**
- Generate Terraform code for infrastructure
- Maintain CI/CD workflows (GitHub Actions)
- Manage AWS IAM roles + secrets
- Monitor deployment health (CloudWatch)
- Execute rollbacks on failure
- Generate infrastructure documentation

### QA Automation Agent

**Responsibilities:**
- Generate Playwright E2E test suites
- Write API contract tests (Bruno)
- Generate performance test scenarios (k6)
- Monitor test health + flakiness
- Report test coverage metrics
- Execute smoke tests on production

---

## 1.7 Repository Structure (GitHub)

```
SOCVault-Blueprint/
├─ .github/
│  ├─ workflows/
│  │  ├─ ci.yml                    # Lint + unit tests
│  │  ├─ deploy-staging.yml        # Deploy to staging
│  │  ├─ deploy-production.yml     # Deploy to prod (approval-gated)
│  │  ├─ security-scan.yml         # Trivy + Bandit scans
│  │  └─ scheduled-tests.yml       # Nightly QA runs
│  ├─ issue_templates/
│  │  ├─ frontend-feature.md       # Frontend issue template
│  │  ├─ backend-feature.md        # Backend issue template
│  │  ├─ bug-report.md             # Bug template
│  │  └─ infrastructure.md         # Infra change template
│  ├─ pull_request_template.md     # PR template (auto-filled by agents)
│  └─ CONTRIBUTING.md              # Contributing guide
│
├─ frontend/                       # React/TypeScript application
│  ├─ src/
│  │  ├─ components/              # shadcn/ui + custom components
│  │  ├─ pages/                   # Page routes
│  │  ├─ hooks/                   # Custom React hooks
│  │  ├─ api/                     # API client (Axios + React Query)
│  │  ├─ store/                   # Zustand state management
│  │  ├─ styles/                  # Global styles + Tailwind config
│  │  └─ __tests__/               # Jest unit tests
│  ├─ stories/                    # Storybook component stories
│  ├─ tests/
│  │  ├─ e2e/                     # Playwright E2E tests
│  │  └─ integration/             # Integration tests
│  ├─ package.json
│  ├─ tsconfig.json
│  ├─ vitest.config.ts
│  └─ playwright.config.ts
│
├─ backend/                       # Python FastAPI application
│  ├─ app/
│  │  ├─ api/
│  │  │  ├─ routes/              # API endpoints
│  │  │  ├─ dependencies.py       # Shared dependencies
│  │  │  └─ __init__.py
│  │  ├─ schemas/                # Pydantic models
│  │  ├─ services/               # Business logic
│  │  ├─ db/                     # MongoDB operations (Motor)
│  │  ├─ models/                 # MongoDB document models
│  │  ├─ security/               # Auth, encryption, validation
│  │  ├─ integrations/           # Claude, Wazuh, Stripe APIs
│  │  ├─ workers/                # Async workers (SQS consumers)
│  │  ├─ config.py               # Configuration + environment
│  │  └─ main.py                 # FastAPI app entry point
│  ├─ tests/
│  │  ├─ unit/                   # Unit tests (pytest)
│  │  ├─ integration/            # Integration tests (MongoDB + real APIs)
│  │  ├─ e2e/                    # End-to-end tests
│  │  └─ fixtures/               # Test fixtures + mocks
│  ├─ requirements.txt            # Python dependencies
│  ├─ requirements-dev.txt        # Dev dependencies
│  ├─ Dockerfile.api              # Lambda-compatible Docker image
│  ├─ pyproject.toml              # Python project config (ruff, mypy)
│  └─ pytest.ini
│
├─ terraform/                     # AWS Infrastructure as Code
│  ├─ main.tf                     # Main configuration
│  ├─ variables.tf
│  ├─ outputs.tf
│  ├─ locals.tf
│  ├─ backend.tf                  # S3 state + DynamoDB lock
│  ├─ environments/
│  │  ├─ staging.tfvars
│  │  ├─ production.tfvars
│  │  └─ staging.tfbackend
│  ├─ modules/
│  │  ├─ api_gateway/
│  │  ├─ lambda/
│  │  ├─ cognito/
│  │  ├─ s3/
│  │  ├─ dynamodb/
│  │  ├─ rds/
│  │  ├─ sqs/
│  │  ├─ sns/
│  │  ├─ amplify/
│  │  ├─ ssm/
│  │  ├─ cloudwatch/
│  │  └─ vpc/
│  └─ README.md
│
├─ collections/
│  ├─ bruno/
│  │  └─ SOCVault-MVP/
│  │     ├─ auth/
│  │     ├─ scans/
│  │     ├─ dashboard/
│  │     └─ admin/
│  └─ postman/
│     └─ SOCVault-MVP.postman_collection.json
│
├─ tests/
│  ├─ qa/                        # QA automation scripts
│  │  ├─ run-staging-qa.sh
│  │  ├─ data_validation.py
│  │  └─ compliance_checks.py
│  ├─ performance/               # k6 performance tests
│  │  ├─ scan-execution.js
│  │  └─ dashboard-load.js
│  └─ security/                  # OWASP / security tests
│     └─ owasp-top-10.js
│
├─ docs/
│  ├─ DEVELOPMENT.md             # Development guide
│  ├─ API.md                      # API documentation
│  ├─ ARCHITECTURE.md             # Architecture overview
│  ├─ DEPLOYMENT.md               # Deployment procedures
│  └─ TROUBLESHOOTING.md          # Common issues
│
├─ .env.example
├─ .gitignore
├─ .pre-commit-config.yaml        # Git pre-commit hooks
├─ docker-compose.yml             # Local dev environment
├─ SOCVAULT_PRODUCT_DESCRIPTION.md
├─ README.md
└─ LICENSE
```

---

## 1.8 Automation Rules & Guardrails

### Commit Message Convention

All commits follow **Conventional Commits** format (enforced by pre-commit hooks):

```
<type>(<scope>): <subject>

<body>

<footer>

Types: feat | fix | docs | style | refactor | test | chore | perf
Scopes: api | frontend | db | auth | scan | soar | infra | etc.

Examples:
  feat(api): Implement POST /scan/execute endpoint
  fix(frontend): Resolve health score widget display bug
  test(backend): Add integration tests for L1 scanner
  chore(infra): Update Terraform Cognito configuration
```

### PR Merge Strategy

| Condition | Action |
|---|---|
| **All CI checks pass** | Auto-merge enabled (squash + rebase) |
| **Code coverage decreases** | Blocks merge until coverage restored |
| **Security scan finds vulnerabilities** | Manual review required before merge |
| **Production branch** | Requires 1 human approval + all checks green |

### Deployment Automation

| Branch | Trigger | Target | Approval |
|---|---|---|---|
| `main` | Push to main | Staging | Automatic |
| Tag `v*` | Create release tag | Staging | Automatic |
| Manual trigger | `workflow_dispatch` | Production | Required (GitHub environment) |

---

## 1.9 Monitoring & Alerting

**CloudWatch Dashboards (AWS):**
```
┌─ SOCVault Staging Dashboard ───────────────────┐
│                                               │
│ ✓ API Latency (p95):         248ms           │
│ ✓ Error Rate:                0.02%            │
│ ✓ Successful Scans:          1,243 (24h)     │
│ ✓ Claude API Cost:           £23.45 (24h)    │
│ ✓ Lambda Duration (avg):     1.2 seconds     │
│ ✓ DynamoDB Throttles:        0 (24h)        │
│ ✓ Test Coverage:             84.2%            │
│                                               │
│ [View Full Dashboard] [Alerts] [Logs]        │
└───────────────────────────────────────────────┘
```

**Automated Alerts (Slack):**
- ❌ CI pipeline failure → Slack #incidents
- ❌ Deployment failure → Slack #incidents
- ⚠️ Test coverage drops below 80% → Slack #qa
- ⚠️ API latency exceeds 500ms (p95) → Slack #performance
- ⚠️ Error rate exceeds 1% → Slack #incidents
- ✅ Staging deployment successful → Slack #deployments
- ✅ Production cutover complete → Slack #announcements

---

## 2. Comprehensive Automation: Audit, Security & Bug Fixing (Pre-Production)

### 2.1 Complete CI/CD Security & Quality Automation Pipeline

**Objective:** Zero security vulnerabilities, zero bugs, and zero regressions reach production. All validation happens automatically in CI/CD; only green pipelines deploy.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             SOCVault Automated Pre-Production Quality Gate                  │
│                  (Audit → Security → Bug Detection → Fixes)                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Developer commits code to feature branch                                   │
│  ↓                                                                          │
│  ┌─ Trigger: GitHub Webhook → CI Pipeline                                 │
│  │                                                                          │
│  ├─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 1: CODE QUALITY & FORMATTING (5 min)                         │  │
│  │ ├─ Prettier (auto-format) → Fix formatting                          │  │
│  │ ├─ Black (Python formatting) → Fix formatting                       │  │
│  │ ├─ Ruff (linting) → Detect style violations                         │  │
│  │ ├─ ESLint (TS linting) → Detect code smells                         │  │
│  │ └─ Auto-commit fixes if formatting detected                         │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓ (all green) or (auto-fixed & re-check)                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 2: TYPE CHECKING & VALIDATION (3 min)                        │  │
│  │ ├─ mypy (Python type checking) → Catch type errors                  │  │
│  │ ├─ tsc (TypeScript type checking) → Catch type errors               │  │
│  │ ├─ Pydantic schema validation → Catch validation errors             │  │
│  │ └─ Fail build if type errors found                                  │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 3: SECURITY SCANNING (8 min)                                  │  │
│  │ ├─ Bandit (Python security) → Detect security issues               │  │
│  │ ├─ ESLint Security Plugin → Detect JS/TS security issues            │  │
│  │ ├─ Trivy (dependencies) → Scan for CVEs in packages                │  │
│  │ ├─ OWASP Dependency Check → Check for known vulnerabilities        │  │
│  │ ├─ SonarQube (SAST) → Static code analysis                          │  │
│  │ ├─ Semgrep (pattern-based) → Custom security rules                  │  │
│  │ ├─ Secret scanning (GitGuardian) → Detect leaked credentials        │  │
│  │ ├─ Container scanning (Trivy Docker) → Scan Lambda images           │  │
│  │ └─ Fail build if HIGH/CRITICAL vulnerabilities found                │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 4: AUTOMATED BUG DETECTION & FIXING (10 min)                 │  │
│  │ ├─ CodeQL (variant analysis) → Detect logical bugs                  │  │
│  │ ├─ AI Bug Fixer Agent → Analyze & auto-fix detected bugs            │  │
│  │ ├─ Automated unit tests → Verify fixes work                         │  │
│  │ ├─ Auto-commit fixes if corrections made                            │  │
│  │ └─ Fail build if unfixable bugs detected                            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 5: TEST COVERAGE & EXECUTION (12 min)                        │  │
│  │ ├─ pytest (backend unit tests) → Run all tests                      │  │
│  │ ├─ Jest (frontend unit tests) → Run all tests                       │  │
│  │ ├─ Coverage check (>80% required)                                   │  │
│  │ ├─ Integration tests (against staging DB)                           │  │
│  │ ├─ Fail build if coverage below threshold                           │  │
│  │ └─ Generate coverage report + upload to Codecov                     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 6: API CONTRACT TESTS (5 min)                                 │  │
│  │ ├─ Bruno collection tests (OpenAPI validation)                      │  │
│  │ ├─ Schema validation (request/response match spec)                  │  │
│  │ ├─ Error handling tests (all error codes tested)                    │  │
│  │ └─ Fail build if contract violated                                  │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 7: COMPLIANCE & AUDIT CHECKS (4 min)                         │  │
│  │ ├─ GDPR compliance check (data handling)                            │  │
│  │ ├─ PCI-DSS compliance check (payment handling)                      │  │
│  │ ├─ License audit (dependencies)                                     │  │
│  │ ├─ Audit trail verification (logging present)                       │  │
│  │ └─ Fail build if compliance violation detected                      │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 8: BUILD & ARTIFACT GENERATION (5 min)                       │  │
│  │ ├─ Build Docker image (backend)                                     │  │
│  │ ├─ Build frontend bundle (React)                                    │  │
│  │ ├─ Generate OpenAPI spec                                            │  │
│  │ ├─ Push to ECR (backend)                                            │  │
│  │ └─ Push to S3 (frontend)                                            │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │ STAGE 9: AUTOMATED GITHUB PROJECTS UPDATE                          │  │
│  │ ├─ Update PR with checklist: ✓ Lint, ✓ Types, ✓ Security, etc.    │  │
│  │ ├─ Move issue to "Ready for Review" if all checks pass              │  │
│  │ ├─ Auto-assign reviewers based on code changes                      │  │
│  │ ├─ Add labels: `backend` `security-scanned` `tests-passing`         │  │
│  │ └─ Tag PR with risk level: `low-risk` / `medium-risk` / `high-risk` │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ↓                                                                          │
│  ✓ ALL GREEN → Ready for human review + staging deployment                │
│  ✗ FAILURE → Automated issue created with fix details                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Total Pipeline Duration: ~45 minutes
Failure Scenarios: 0 reach production (blocked at source)
```

---

### 2.2 Security Automation: Detailed Scanning & Remediation

#### 2.2.1 Security Scanning Tools & Actions

**File:** `.github/workflows/security-scan.yml`

```yaml
name: Security & Compliance Scan

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'  # Nightly scan

jobs:
  security-scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
      issues: write
      pull-requests: write

    steps:
      # 1. DEPENDENCY SCANNING
      - name: Trivy - Dependency Vulnerability Scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'config,fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Upload Trivy results to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'
          category: 'trivy'
      
      - name: Parse Trivy results & create issues
        if: failure()
        run: |
          python scripts/security/parse-trivy-results.py \
            --sarif trivy-results.sarif \
            --repo ${{ github.repository }} \
            --token ${{ secrets.GITHUB_TOKEN }}
      
      # 2. PYTHON SECURITY SCANNING
      - name: Bandit - Python Security Scanner
        run: |
          pip install bandit[toml]
          bandit -r backend/ -f json -o bandit-results.json || true
      
      - name: Parse Bandit results & report
        run: |
          python scripts/security/parse-bandit.py \
            --results bandit-results.json \
            --repo ${{ github.repository }}
      
      # 3. JAVASCRIPT/TYPESCRIPT SECURITY
      - name: ESLint Security Plugin
        run: |
          cd frontend
          npm install
          npx eslint . --format json --output-file eslint-results.json || true
      
      # 4. SAST ANALYSIS
      - name: SonarQube SAST Analysis
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      
      # 5. SECRET SCANNING
      - name: GitGuardian Secret Scan
        uses: GitGuardian/ggshield-action@master
        env:
          GITHUB_PUSH_BEFORE_SHA: ${{ github.event.before }}
          GITHUB_PUSH_BASE_SHA: ${{ github.event.base }}
          GITHUB_PULL_REQUEST_BASE_SHA: ${{ github.event.pull_request.base.sha }}
          GITHUB_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}
      
      # 6. CONTAINER IMAGE SCANNING
      - name: Build & Scan Docker Image
        run: |
          docker build -t socvault-api:test -f Dockerfile.api .
          trivy image socvault-api:test \
            --format json \
            --output docker-trivy.json
          
          # Fail if CRITICAL vulnerabilities found
          CRITICAL=$(jq '[.Results[].Vulnerabilities[] | select(.Severity=="CRITICAL")] | length' docker-trivy.json)
          if [ $CRITICAL -gt 0 ]; then
            echo "❌ Found $CRITICAL CRITICAL vulnerabilities in container"
            exit 1
          fi
      
      # 7. POLICY AS CODE (OPA/Conftest)
      - name: Terraform Security (Checkov)
        uses: bridgecrewio/checkov-action@master
        with:
          directory: terraform/
          framework: terraform
          output_format: sarif
          output_file_path: 'checkov-results.sarif'
      
      # 8. LICENSE AUDIT
      - name: License Compliance Audit
        run: |
          pip install pip-audit
          pip-audit --desc > license-audit.txt || true
      
      - name: Check for incompatible licenses
        run: |
          python scripts/security/check-licenses.py \
            --audit-file license-audit.txt \
            --allowed-licenses "MIT,Apache-2.0,BSD-3-Clause"
      
      # 9. GENERATE SECURITY REPORT
      - name: Consolidate Security Findings
        run: |
          python scripts/security/consolidate-report.py \
            --trivy trivy-results.sarif \
            --bandit bandit-results.json \
            --eslint eslint-results.json \
            --sonar sonarqube-report.json \
            --output security-report.json
      
      # 10. UPDATE GITHUB SECURITY SUMMARY
      - name: Comment PR with Security Summary
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('security-report.json', 'utf8'));
            
            const comment = `
            ## 🔒 Security Scan Results
            
            | Check | Status | Details |
            |-------|--------|---------|
            | Dependencies | ${report.dependencies.passed ? '✅' : '❌'} | ${report.dependencies.vulnerabilities} vulnerabilities |
            | SAST | ${report.sast.passed ? '✅' : '❌'} | ${report.sast.issues} issues found |
            | Secrets | ${report.secrets.passed ? '✅' : '❌'} | ${report.secrets.exposed ? 'Exposed!' : 'Clean'} |
            | Container | ${report.container.passed ? '✅' : '❌'} | ${report.container.vulnerabilities} vulnerabilities |
            | Compliance | ${report.compliance.passed ? '✅' : '❌'} | ${report.compliance.violations} violations |
            
            ${report.recommendations.map(r => `- ⚠️ ${r}`).join('\n')}
            `;
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

---

### 2.3 Automated Bug Detection & Fixing (AI-Driven)

#### 2.3.1 Bug Detection Agent

**File:** `.github/workflows/bug-detection-and-fix.yml`

```yaml
name: Automated Bug Detection & Fixing

on:
  pull_request:
    branches: [main, develop]

jobs:
  bug-detection:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for analysis
      
      # 1. STATIC BUG ANALYSIS
      - name: CodeQL - Variant Analysis
        uses: github/codeql-action/init@v2
        with:
          languages: 'python,javascript,typescript'
      
      - name: CodeQL - Analyze
        uses: github/codeql-action/analyze@v2
        with:
          output: 'codeql-results.sarif'
      
      # 2. AI BUG DETECTION (Claude API)
      - name: AI-Powered Bug Analysis
        run: |
          python scripts/agents/bug-detector.py \
            --pr-number ${{ github.event.pull_request.number }} \
            --repo ${{ github.repository }} \
            --token ${{ secrets.GITHUB_TOKEN }} \
            --claude-key ${{ secrets.ANTHROPIC_API_KEY }}
      
      # 3. COMPLEXITY ANALYSIS
      - name: Radon - Code Complexity Check
        run: |
          pip install radon
          radon cc backend/ -a -s > complexity-report.txt
          radon mi backend/ -s > maintainability-report.txt
          
          # Fail if complexity too high
          python scripts/quality/check-complexity.py --report complexity-report.txt
      
      # 4. DUPLICATE CODE DETECTION
      - name: CPD - Detect Code Duplication
        run: |
          npm install -g pmd
          pmd cpd \
            --minimum-tokens 30 \
            --files 'backend/**/*.py,frontend/src/**/*.ts' \
            --format json \
            --output-file cpd-results.json || true
      
      # 5. PERFORMANCE ANTIPATTERNS
      - name: Detect Performance Issues
        run: |
          python scripts/quality/detect-antipatterns.py \
            --codebase backend/ \
            --output perf-issues.json
      
      # 6. AI BUG FIXER AGENT
      - name: AI Bug Fixer - Generate Fixes
        run: |
          python scripts/agents/bug-fixer.py \
            --issues codeql-results.sarif \
            --complexity complexity-report.txt \
            --duplication cpd-results.json \
            --performance perf-issues.json \
            --output fixes.json \
            --claude-key ${{ secrets.ANTHROPIC_API_KEY }}
      
      # 7. AUTO-APPLY FIXES
      - name: Auto-Apply Bug Fixes
        run: |
          python scripts/agents/apply-fixes.py \
            --fixes fixes.json \
            --repo-path .
      
      # 8. VERIFY FIXES
      - name: Verify Fixes Don't Break Tests
        run: |
          pytest tests/unit/ -v --tb=short
          npm run test -- --coverage
      
      # 9. AUTO-COMMIT FIXES
      - name: Auto-Commit Fixes
        if: success()
        run: |
          git config user.name "SOCVault Bot"
          git config user.email "bot@socvault.io"
          git add -A
          git diff --cached --exit-code || \
            git commit -m "fix: Auto-fix detected bugs and code issues

- Fixed ${{ env.BUG_COUNT }} bugs detected by CodeQL and AI analysis
- Resolved complexity violations
- Removed code duplication
- Applied performance optimizations

Generated by SOCVault Automated Bug Fixer"
          git push origin ${{ github.head_ref }}
```

**File:** `scripts/agents/bug-detector.py`

```python
"""
AI-Powered Bug Detection Agent
Uses Claude API to analyze code changes for potential bugs
"""

import json
import subprocess
from anthropic import Anthropic

class BugDetectorAgent:
    def __init__(self, claude_key: str):
        self.client = Anthropic(api_key=claude_key)
        self.model = "claude-opus-4-8"
    
    def analyze_pr_changes(self, pr_number: str, repo: str, token: str) -> dict:
        """Analyze PR changes for potential bugs"""
        
        # 1. Get PR diff
        diff = subprocess.run(
            ["gh", "pr", "diff", pr_number, f"--repo={repo}"],
            capture_output=True,
            text=True,
            env={"GH_TOKEN": token}
        ).stdout
        
        # 2. Get CodeQL SARIF results
        codeql_results = self._load_json("codeql-results.sarif")
        
        # 3. Prepare analysis prompt
        prompt = f"""
        Analyze the following code changes for potential bugs, vulnerabilities, 
        and logical errors.
        
        ## Code Diff
        ```diff
        {diff[:5000]}  # Truncate for token limits
        ```
        
        ## CodeQL Findings
        {json.dumps(codeql_results.get('runs', [{}])[0].get('results', [])[:10])}
        
        ## Analysis Checklist
        - [ ] Null/undefined reference errors
        - [ ] Off-by-one errors in loops
        - [ ] Race conditions (async code)
        - [ ] Resource leaks (file handles, DB connections)
        - [ ] SQL injection / NoSQL injection risks
        - [ ] Incorrect error handling
        - [ ] Type mismatches
        - [ ] Unreachable code paths
        - [ ] Logic errors in conditionals
        - [ ] Missing input validation
        
        Provide structured output with:
        1. Bug name and severity (CRITICAL/HIGH/MEDIUM/LOW)
        2. Location (file:line)
        3. Description of the bug
        4. Recommended fix
        5. Confidence score (0-100)
        """
        
        # 4. Call Claude with extended thinking
        response = self.client.messages.create(
            model=self.model,
            max_tokens=16000,
            thinking={
                "type": "enabled",
                "budget_tokens": 10000
            },
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # 5. Parse response
        bugs = self._parse_bug_findings(response.content)
        
        return {
            "bug_count": len(bugs),
            "bugs": bugs,
            "analysis_depth": "extended_thinking",
            "model": self.model
        }
    
    def _parse_bug_findings(self, content: list) -> list:
        """Extract bug findings from Claude response"""
        bugs = []
        
        for block in content:
            if hasattr(block, 'text'):
                # Parse structured text response
                text = block.text
                # Use regex/JSON parsing to extract bugs
                # (simplified here)
                bugs.append({
                    "name": "Detected bug",
                    "severity": "HIGH",
                    "description": text[:200],
                    "confidence": 0.85
                })
        
        return bugs
    
    def _load_json(self, filepath: str) -> dict:
        try:
            with open(filepath) as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


if __name__ == "__main__":
    import os
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr-number")
    parser.add_argument("--repo")
    parser.add_argument("--token")
    parser.add_argument("--claude-key")
    
    args = parser.parse_args()
    
    detector = BugDetectorAgent(args.claude_key)
    results = detector.analyze_pr_changes(args.pr_number, args.repo, args.token)
    
    print(json.dumps(results, indent=2))
    
    # Save results
    with open("bug-detection-results.json", "w") as f:
        json.dump(results, f, indent=2)
```

---

### 2.4 Automated GitHub Projects Management

#### 2.4.1 Issue & PR State Machine

```
┌─────────────────────────────────────────────────────────────────┐
│           GitHub Projects Automated State Machine               │
└─────────────────────────────────────────────────────────────────┘

Issue Created (Frontend/Backend)
  ↓
[🟡 Backlog] 
  - Awaiting implementation
  - Waiting for assignment
  ↓ (Developer picks up)
[🔄 In Progress]
  - Feature branch created
  - Auto-assigned to developer/agent
  ↓ (Code committed)
[🧪 CI/CD Running]
  - Linting, type-checking, security scans
  - Tests running
  - Cannot merge until green
  ↓ (PR opened + all checks pass)
[📋 Ready for Review]
  - Auto-assigned reviewers based on code expertise
  - Awaiting human approval
  - Comments can trigger fixes
  ↓ (Approved & merged)
[✅ Deployed to Staging]
  - E2E tests running on staging
  - Integration tests passing
  - Link to staging URL added
  ↓ (Tagged for production)
[🚀 Ready for Production]
  - Awaiting production approval
  - Blue-green deployment configured
  ↓ (Manual approval + deployment)
[✅ In Production]
  - Smoke tests passing
  - Rollback plan ready
  - Monitoring active
  ↓ (Post-deployment validation)
[✅ Done]
  - Feature complete
  - All tests passing
  - Monitoring shows stable
  - Ready for next sprint review

ERROR PATHS:
├─ CI Failure → [❌ CI Failed] → Auto-issue created with fix details
├─ Security Scan Failure → [🔒 Security Review Needed] → Manual review required
├─ Test Failure → [❌ Tests Failing] → Auto-bug-fixer agent kicks in
└─ Performance Regression → [⚠️ Performance Check] → Performance analysis + recommendations
```

#### 2.4.1 GitHub Projects Automation Workflows

**File:** `.github/workflows/github-projects-sync.yml`

```yaml
name: GitHub Projects Automation

on:
  issues:
    types: [opened, closed, reopened]
  pull_request:
    types: [opened, closed, converted_to_draft, ready_for_review, review_requested]
  workflow_run:
    workflows: ["CI Pipeline", "Security & Compliance Scan"]
    types: [completed]
  check_run:
    types: [completed]

jobs:
  sync-projects:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      issues: write
      pull-requests: write

    steps:
      - uses: actions/checkout@v4
      
      # 1. SYNC ISSUES TO PROJECT
      - name: Sync New Issues to Project Board
        if: github.event_name == 'issues' && github.event.action == 'opened'
        uses: actions/github-script@v6
        with:
          script: |
            const projectId = process.env.PROJECT_ID;
            const status = 'Backlog';
            
            // Get label to determine track
            const labels = context.payload.issue.labels;
            const track = labels.map(l => l.name).includes('frontend') 
              ? 'Frontend' 
              : 'Backend';
            
            // Create project item
            const mutation = `
              mutation {
                addProjectV2ItemById(input: {
                  projectId: "${projectId}"
                  contentId: "${context.payload.issue.node_id}"
                }) {
                  item {
                    id
                  }
                }
              }
            `;
            
            const result = await github.graphql(mutation);
            console.log('Added to project:', result);
      
      # 2. MOVE PR TO IN PROGRESS
      - name: Move PR to 'In Progress' When Draft Created
        if: github.event_name == 'pull_request' && github.event.action == 'converted_to_draft'
        uses: actions/github-script@v6
        with:
          script: |
            const projectId = process.env.PROJECT_ID;
            
            // Update project item field
            const query = `
              query {
                repository(owner: "${context.repo.owner}", name: "${context.repo.repo}") {
                  pullRequest(number: ${context.issue.number}) {
                    projectItems(first: 10) {
                      nodes {
                        id
                        fieldValues(first: 10) {
                          nodes {
                            field { name }
                            value
                          }
                        }
                      }
                    }
                  }
                }
              }
            `;
      
      # 3. UPDATE STATUS ON CI SUCCESS/FAILURE
      - name: Update Project Status - CI Success
        if: github.event_name == 'workflow_run' && github.event.workflow_run.conclusion == 'success'
        uses: actions/github-script@v6
        with:
          script: |
            // Find associated PR
            const prs = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open',
              head: `${context.repo.owner}:${github.event.workflow_run.head_branch}`
            });
            
            if (prs.data.length > 0) {
              const pr = prs.data[0];
              
              // Update project status to "Ready for Review"
              const comment = `✅ All CI checks passed!\n- Linting: ✓\n- Types: ✓\n- Tests: ✓\n- Security: ✓\n\nReady for review.`;
              
              github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: pr.number,
                body: comment
              });
            }
      
      - name: Update Project Status - CI Failure
        if: github.event_name == 'workflow_run' && github.event.workflow_run.conclusion == 'failure'
        uses: actions/github-script@v6
        with:
          script: |
            // Auto-create issue for failure
            const prList = await github.rest.pulls.list({
              owner: context.repo.owner,
              repo: context.repo.repo,
              state: 'open',
              head: `${context.repo.owner}:${github.event.workflow_run.head_branch}`
            });
            
            if (prList.data.length > 0) {
              const pr = prList.data[0];
              
              const issue = await github.rest.issues.create({
                owner: context.repo.owner,
                repo: context.repo.repo,
                title: `🔴 CI Failed - ${pr.title}`,
                body: `PR #${pr.number} failed CI checks.\n\n[View workflow run](${github.event.workflow_run.html_url})`,
                labels: ['ci-failure', 'needs-fix']
              });
            }
      
      # 4. AUTO-ASSIGN REVIEWERS
      - name: Auto-Assign Code Reviewers
        if: github.event_name == 'pull_request' && github.event.action == 'ready_for_review'
        uses: actions/github-script@v6
        with:
          script: |
            const reviewers = await github.rest.pulls.getRequestedReviewers({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });
            
            // Assign based on code changes
            const files = await github.rest.pulls.listFiles({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });
            
            let suggestedReviewers = [];
            
            for (const file of files.data) {
              if (file.filename.startsWith('backend/')) {
                suggestedReviewers.push('backend-reviewer');
              } else if (file.filename.startsWith('frontend/')) {
                suggestedReviewers.push('frontend-reviewer');
              } else if (file.filename.startsWith('terraform/')) {
                suggestedReviewers.push('devops-reviewer');
              }
            }
            
            // Request review
            if (suggestedReviewers.length > 0) {
              await github.rest.pulls.requestReviewers({
                owner: context.repo.owner,
                repo: context.repo.repo,
                pull_number: context.issue.number,
                reviewers: [...new Set(suggestedReviewers)]
              });
            }
      
      # 5. ADD LABELS BASED ON RESULTS
      - name: Add Labels - Risk Level
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const files = await github.rest.pulls.listFiles({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });
            
            let riskLevel = 'low-risk';
            let fileCount = files.data.length;
            
            // Determine risk level
            if (fileCount > 10) riskLevel = 'high-risk';
            else if (fileCount > 5) riskLevel = 'medium-risk';
            
            // Check for critical files
            const criticalFiles = ['app/security/', 'app/db/', 'terraform/'];
            if (files.data.some(f => 
              criticalFiles.some(cf => f.filename.startsWith(cf))
            )) {
              riskLevel = 'high-risk';
            }
            
            // Add label
            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              labels: [riskLevel]
            });
      
      # 6. GENERATE PR SUMMARY CHECKLIST
      - name: Add PR Checklist Summary
        if: github.event_name == 'pull_request' && github.event.action == 'opened'
        uses: actions/github-script@v6
        with:
          script: |
            const checklist = `## 🚀 Pre-Merge Checklist

### Automated Checks
- [ ] ✅ Linting & Formatting
- [ ] ✅ Type Checking  
- [ ] ✅ Unit Tests (>80% coverage)
- [ ] ✅ Integration Tests
- [ ] ✅ Security Scan (Bandit, SonarQube, Trivy)
- [ ] ✅ API Contract Tests (Bruno)
- [ ] ✅ Compliance Check
- [ ] ✅ Performance Validation

### Manual Review
- [ ] Code review approved
- [ ] Architecture review (if applicable)
- [ ] Design review (if applicable)

### Staging
- [ ] Deployed to staging
- [ ] E2E tests passing on staging
- [ ] Manual QA sign-off

### Production Ready
- [ ] Rollback plan documented
- [ ] Monitoring configured
- [ ] On-call notified
`;
            
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: checklist
            });

  # 7. CREATE METRICS & REPORTING
  generate-metrics:
    runs-on: ubuntu-latest
    if: github.event_name == 'workflow_run' && github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      
      - name: Generate CI/CD Metrics
        run: |
          python scripts/metrics/generate-metrics.py \
            --github-token ${{ secrets.GITHUB_TOKEN }} \
            --repo ${{ github.repository }} \
            --output metrics.json
      
      - name: Upload Metrics to CloudWatch
        run: |
          python scripts/metrics/upload-to-cloudwatch.py \
            --metrics metrics.json \
            --aws-region eu-west-2 \
            --namespace SOCVault/CI-CD
      
      - name: Post to Slack (#metrics channel)
        uses: slackapi/slack-github-action@v1.24.0
        with:
          webhook-url: ${{ secrets.SLACK_METRICS_WEBHOOK }}
          payload: |
            {
              "text": "📊 Daily CI/CD Metrics",
              "attachments": [
                {
                  "fields": [
                    {"title": "Pipeline Success Rate", "value": "${{ env.SUCCESS_RATE }}%"},
                    {"title": "Avg Pipeline Duration", "value": "${{ env.AVG_DURATION }}m"},
                    {"title": "Security Issues Found", "value": "${{ env.SECURITY_ISSUES }}"},
                    {"title": "Bugs Auto-Fixed", "value": "${{ env.BUGS_FIXED }}"}
                  ]
                }
              ]
            }
```

---

### 2.5 Audit Automation: Pre-Production Quality Gates

#### 2.5.1 Automated Audit Checklist

**File:** `.github/workflows/pre-deployment-audit.yml`

```yaml
name: Pre-Deployment Audit & Compliance

on:
  workflow_dispatch:  # Manual trigger for staging/production
  workflow_run:
    workflows: ["CI Pipeline", "Security & Compliance Scan"]
    types: [completed]
    branches: [main]

jobs:
  audit-checks:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      checks: write

    steps:
      - uses: actions/checkout@v4
      
      - name: AUDIT 1 - Code Quality Standards
        run: |
          echo "🔍 Auditing code quality standards..."
          python scripts/audit/check-code-quality.py \
            --min-coverage 80 \
            --max-complexity 10 \
            --fail-on-violations
      
      - name: AUDIT 2 - Security Controls
        run: |
          echo "🔒 Auditing security controls..."
          python scripts/audit/check-security-controls.py \
            --check-auth \
            --check-encryption \
            --check-secrets \
            --check-logs
      
      - name: AUDIT 3 - API Contract Compliance
        run: |
          echo "📋 Auditing API contracts..."
          npm run test:api -- --audit-mode \
            --check-response-schemas \
            --check-error-codes \
            --check-rate-limits
      
      - name: AUDIT 4 - Data Protection Compliance
        run: |
          echo "🔐 Auditing data protection..."
          python scripts/audit/check-gdpr-compliance.py \
            --check-data-retention \
            --check-encryption \
            --check-access-controls
      
      - name: AUDIT 5 - Infrastructure & Deployment
        run: |
          echo "🏗️ Auditing infrastructure..."
          python scripts/audit/check-infrastructure.py \
            --terraform-path terraform/ \
            --check-ha \
            --check-backup \
            --check-monitoring
      
      - name: AUDIT 6 - Dependency Audit
        run: |
          echo "📦 Auditing dependencies..."
          pip-audit --strict
          npm audit --audit-level=moderate
      
      - name: AUDIT 7 - Documentation & Comments
        run: |
          echo "📚 Auditing documentation..."
          python scripts/audit/check-documentation.py \
            --check-docstrings \
            --check-comments \
            --check-readme
      
      - name: AUDIT 8 - Testing Coverage
        run: |
          echo "🧪 Auditing test coverage..."
          python scripts/audit/check-test-coverage.py \
            --min-coverage 80 \
            --check-edge-cases \
            --check-error-scenarios
      
      - name: Generate Audit Report
        if: always()
        run: |
          python scripts/audit/generate-audit-report.py \
            --output audit-report.json \
            --format markdown > AUDIT_REPORT.md
      
      - name: Upload Audit Report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: audit-report
          path: AUDIT_REPORT.md
      
      - name: Comment with Audit Results
        if: always()
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('AUDIT_REPORT.md', 'utf8');
            
            github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number,
              body: report
            });
      
      - name: Fail if Audit Fails
        if: failure()
        run: |
          echo "❌ Pre-deployment audit failed!"
          echo "Fix issues before proceeding to production."
          exit 1
```

---

### 2.6 Skills & Sub-Agents for Automated Workflow

#### 2.6.1 Core Skills

| Skill | Agent | Purpose | Auto-Trigger |
|---|---|---|---|
| **Frontend Code Generation** | Claude UI Agent | Generate React/TypeScript components | GitHub issue labeled `frontend` |
| **Backend Code Generation** | Cursor Backend Agent | Generate FastAPI endpoints | GitHub issue labeled `backend` |
| **Security Scanning** | Security Agent | Run SAST, dependency scans, secret detection | Every PR |
| **Bug Detection & Fixing** | Bug Fixer Agent | Detect & auto-fix bugs | PR with code changes |
| **Code Review** | Code Review Agent | Provide automated code review comments | PR ready for review |
| **Documentation** | Doc Agent | Generate API docs, README updates | Code changes |
| **Test Generation** | Test Agent | Generate unit & integration tests | New feature code |
| **Infrastructure Deployment** | DevOps Agent | Deploy to staging/production | On tag or manual trigger |
| **Performance Analysis** | Perf Agent | Detect & recommend optimizations | Staging deployment |
| **Compliance Check** | Compliance Agent | Verify GDPR, PCI-DSS, ISO 27001 | Every commit |

#### 2.6.2 Sub-Agent Workflows

```
GitHub Issue Created
  ↓
ROUTE BY LABEL
├─ [frontend] → Claude UI Agent
│   ├─ Generate React component
│   ├─ Add Tailwind styling
│   ├─ Write Jest tests
│   ├─ Create Storybook story
│   └─ Open PR with auto-description
│
├─ [backend] → Cursor Backend Agent
│   ├─ Generate FastAPI endpoint
│   ├─ Add Pydantic validation
│   ├─ Write pytest tests
│   ├─ Update OpenAPI spec
│   └─ Open PR with auto-description
│
├─ [infrastructure] → DevOps Agent
│   ├─ Generate Terraform code
│   ├─ Validate configuration
│   ├─ Plan infrastructure changes
│   └─ Open PR with infrastructure diff
│
└─ [bug-report] → Bug Analyzer Agent
    ├─ Analyze bug description
    ├─ Locate affected code
    ├─ Generate fix
    ├─ Create PR with fix
    └─ Reference original issue

PR OPENED
  ↓
PARALLEL EXECUTION
├─ Security Agent
│  ├─ Run Bandit (Python)
│  ├─ Run SonarQube (SAST)
│  ├─ Scan dependencies (Trivy)
│  └─ Check for secrets (GitGuardian)
│
├─ Code Review Agent
│  ├─ Check code style
│  ├─ Verify architecture
│  ├─ Check for anti-patterns
│  └─ Post review comments
│
├─ Bug Fixer Agent
│  ├─ Run CodeQL analysis
│  ├─ Detect logical bugs
│  ├─ Auto-fix if possible
│  └─ Create commit if fixed
│
├─ Test Agent
│  ├─ Check test coverage
│  ├─ Run pytest/Jest
│  ├─ Verify edge cases
│  └─ Report coverage
│
└─ Compliance Agent
   ├─ Check GDPR compliance
   ├─ Check data handling
   ├─ Verify audit logging
   └─ Report violations

ALL CHECKS PASS
  ↓
GitHub Projects Auto-Update
├─ Move to "Ready for Review"
├─ Add labels: `tests-passing`, `security-scanned`
├─ Auto-assign reviewers
└─ Post checklist comment

REVIEW APPROVED
  ↓
Auto-Merge (if enabled)
  ├─ Squash + rebase
  ├─ Delete feature branch
  └─ Trigger deployment

DEPLOYMENT
  ├─ Staging: Automatic
  ├─ Production: Requires approval
  └─ Post-deployment: Run smoke tests
```

---

## 2.7 Complete Automation Metrics & Monitoring

**Tracked Metrics:**

| Metric | Target | Alert Threshold |
|---|---|---|
| **CI Pipeline Success Rate** | >95% | <90% |
| **Average Pipeline Duration** | <45 min | >60 min |
| **Code Coverage** | >80% | <75% |
| **Security Issues (CRITICAL)** | 0 | >0 |
| **Security Issues (HIGH)** | <5 | >10 |
| **Bug Auto-Fix Rate** | >70% | <50% |
| **Mean Time to Fix (MTTR)** | <2 hours | >4 hours |
| **Deployment Success Rate** | >98% | <95% |
| **Production Incidents** | 0 | >0 |
| **Rollback Rate** | <1% | >2% |

---

## 3. Executive Summary

### What is SOCVault?

**SOCVault** is a **multi-tenant, cloud-native SaaS cybersecurity platform** that unifies the complete security assessment and response lifecycle into a single, AI-powered dashboard. It consolidates eight attack surface layers (external recon, web applications, mobile, APIs, compliance, cloud, SOC/SIEM, and malware detection & response) powered by **Anthropic Claude AI** for intelligent threat translation, financial risk quantification, and automated security orchestration.

### Core Problem Solved

Small and Medium-Sized Businesses (SMBs, 50–500 employees) are **the most targeted yet least protected** segment in cybersecurity:

- **Capital Barrier:** Traditional VAPT engagements cost **$10,000–$50,000/year** — inaccessible for most SMBs
- **Talent Barrier:** SMBs cannot recruit or retain specialist security engineers
- **Translation Barrier:** Raw CVE outputs and technical logs are meaningless to non-technical business owners
- **Fragmentation Barrier:** Existing SMB tools cover only 1–2 attack surface layers; SMBs drown in point solutions

**Market Impact:** Average SMB breach costs **$4.45M** (IBM 2024). **60% of SMBs close within 6 months of a major breach.**

### The Solution: Unified + AI-Enabled

SOCVault fixes all four barriers in one platform:

1. **Accessible pricing:** Free tier + $15–199/month paid tiers (vs. $3,000–$50,000 enterprise alternatives)
2. **No security expertise required:** Business email signup; domain entry; financial risk report in minutes
3. **AI-translated findings:** Every CVE → quantified financial exposure (£/$) in plain English
4. **Unified attack surface:** All 8 layers in one dashboard, one AI engine, one health score
5. **Automated response:** SOAR playbooks execute automatically for confirmed threats; human approval gate for risky actions

---

## 2. Product Vision & Problem Statement

### 2.1 The SMB Security Crisis

**Market Reality:**
- SMBs represent **43% of all cyberattack targets** globally yet receive <15% of cybersecurity investment
- **3.4 million cybersecurity workforce shortage** globally — SMBs cannot compete with enterprise salaries
- **60% of targeted SMBs lack effective incident response capability**
- Only **14% of SMBs rate their ability to mitigate cyber risks as "highly effective"** (National Cyber Security Alliance)

**Why Existing Tools Fail SMBs:**

| Problem | Current Tool Response |
|---|---|
| Too expensive | Enterprise tools: $3,000–$50,000/year; fragmented SMB tools: $79–$500/month each (no unified coverage) |
| Too complex | Requires security engineer to interpret technical outputs; non-technical executives cannot act |
| Incomplete coverage | Every tool covers 1–2 layers; SMBs need 5–6 tools simultaneously |
| No AI translation | Raw CVE IDs, CVSS scores, NVD links — no financial risk quantification |
| No automation | Every alert requires manual investigation; no SOAR response at SMB price points |

### 2.2 The Regulatory Pressure Accelerator

**UK/EU Focus:**
- **GDPR enforcement:** ICO issued **£1.2B in fines in 2023 alone**
- **Cyber Essentials mandate:** UK government supply chain suppliers must comply
- **NCSC Active Cyber Defence:** Pushing SMBs toward automated security tools
- **NIS Directive 2:** Expanding compliance requirements to smaller entities

**This creates an immediate market:**
- **UK SMBs in regulated sectors (finance, healthcare, e-commerce):** ~48,000 businesses
- **Willing-to-pay (budget >£200/month for IT security):** ~12,000
- **TAM at $199/month ARPU:** **$28.8M ARR potential in UK alone**

### 2.3 SOCVault's Founding Premise

> *Make enterprise-grade cybersecurity accessible to every business through unified AI-enabled automation — removing the barriers of cost, complexity, and talent that leave SMBs exposed.*

**Vision:** Become the default security operations centre for the global SMB market — the single platform where any business can understand its full risk exposure, meet compliance obligations, and respond to threats automatically, without needing an in-house security team.

---

## 3. Core Value Proposition

### 3.1 One Platform. Eight Layers. AI-Enabled.

SOCVault is the **only SMB-accessible platform** that covers all eight attack surface layers in a unified interface:

```
[SMB Domain / IP / Endpoint]
         │
         ▼
[Unified 8-Layer Scanning Engine]
  L1 — External Recon (FREE)        │ WHOIS, DNS, email security, SSL/TLS, headers, subdomains, ports
  L2 — Web AppSec (PAID)            │ CVE detection, SAST, DAST, web shell detection
  L3 — Mobile (PAID)                │ Android/iOS binary analysis
  L4 — API (PAID)                   │ OWASP API Top 10, auth bypass, injection
  L5 — Compliance (PAID)            │ PCI-DSS, GDPR, ISO 27001, SOC2 gap analysis
  L6 — Cloud (PAID)                 │ AWS/Azure/GCP IAM misconfigs, privilege escalation
  L7 — SOC/SIEM (SOC PRO)           │ Wazuh + real-time threat detection
  L8 — Malware D&R (SOC PRO)        │ ClamAV, YARA, AI triage, auto-remediation
         │
         ▼
[Claude AI — Unified Intelligence Layer]
  ✓ Financial risk translation (£/$ per finding)
  ✓ Plain-English business summaries
  ✓ Remediation scripts
  ✓ SOAR auto-response (contain, quarantine, block)
         │
         ├──► Executive Risk Report (Health Score + total exposure)
         ├──► 1-Click Remediation Scripts (per vulnerability)
         ├──► SOAR Auto-Response (contain, quarantine, block)
         └──► Compliance Register (PCI-DSS · GDPR · ISO 27001 · SOC2 · CE+)
```

### 3.2 Nine Unique Selling Propositions (USPs)

#### USP 1: AI Financial Risk Translation

**Unique capability:** Every vulnerability → quantified financial exposure in GBP/USD.

Claude AI calculates multi-factor financial risk per finding:
- **Operational risk:** Downtime hours × £500/hour loss rate
- **Regulatory risk:** GDPR Article 83 maximum fine brackets
- **Recovery cost:** Forensics + notification + PR model
- **Insurance impact:** Void risk + premium increase

**Why competitors can't copy:** Requires months of calibration against IBM Cost of Breach database, ICO fine records, and Verizon DBIR data. No other SMB tool offers this.

#### USP 2: Freemium With Real Scan Value

15-step external recon scan (L1) executed against user's real domain — **free forever, once per month** — with genuine findings and financial exposure calculation.

**Competitors:** Time-limited trials or no free tier at all.

#### USP 3: SOAR Automation at SMB Price Points

Fully automated Security Orchestration, Automation & Response (SOAR) engine at **$199/month** — comparable enterprise SOAR costs $5,000–$20,000+/month.

Includes:
- AI triage (Claude determines contain vs. escalate)
- Automated playbook execution (quarantine, block, isolate)
- Human approval gate for high-risk actions
- Full audit trail

#### USP 4: Full 8-Layer Attack Surface Coverage

Every competitor covers 1–2 layers. SOCVault covers all 8 in one platform, one AI engine, one health score.

#### USP 5: Malware Detection & Response With AI Triage

L8 integrates:
- **Detection:** Wazuh ClamAV, FIM, rootkit detection, Trivy container scans, Nuclei webshell templates
- **AI Triage:** Claude determines malware family, severity, lateral movement risk, data exfiltration likelihood
- **Auto-Remediation:** Quarantine, process kill, persistence cleanup for isolated threats; human gate for system-critical files
- **Verification:** Post-remediation re-scan; incident report

#### USP 6: 60-Second Onboarding

- Business email + phone number signup
- OTP verification
- Domain extracted automatically
- Tenant workspace provisioned in <60 seconds
- First scan ready to execute

No procurement contracts, no implementation project, no security expertise required.

#### USP 7: Open-Source Scanning Core

All scanning tools are open-source (Nmap, Nuclei, Semgrep, MobSF, Wazuh, ClamAV, YARA) — transparent, auditable, community-vetted.

#### USP 8: Compliance as Standard

Every finding maps automatically to:
- **PCI-DSS** controls
- **GDPR** articles
- **ISO 27001** domains
- **SOC2** trust service categories
- **Cyber Essentials+** controls

#### USP 9: Conversational AI Security Assistant

Embedded Claude AI in dashboard — tenants ask security questions, trigger scans, generate scripts, approve SOAR actions, and create reports — all in natural language via credit-based pricing.

---

## 4. Market Opportunity

### 4.1 Total Addressable Market (TAM)

| Geography | SMBs (50–500 employees) | Potential Addressable |
|---|---|---|
| United Kingdom | ~160,000 | ~48,000 |
| United States | ~1,400,000 | ~420,000 |
| Australia / NZ | ~90,000 | ~27,000 |
| EU (ex-UK) | ~850,000 | ~255,000 |
| **Global TAM** | **~8,400,000** | **~2,520,000** |

**At $199/month average ARPU:** TAM revenue potential = **$500M+/year**

**Global SMB Cybersecurity Market:**
- 2024: $67.4B
- 2030: $156.2B
- CAGR: ~15.2%

### 4.2 Serviceable Addressable Market (SAM)

**Phase 1 focus:** UK-based SMBs in regulated sectors (financial services, healthcare, e-commerce, legal).

- UK SMBs in regulated sectors: ~48,000
- Willing-to-pay (budget >£200/month for IT security): ~12,000
- **SAM at launch = ~$28.8M ARR potential**

### 4.3 Serviceable Obtainable Market (SOM)

| Year | Timeline | Target Clients | Blended ARPU | ARR Target |
|---|---|---|---|---|
| **Year 1** | Month 1–12 | 150 paying clients | $60 | $108,000 |
| **Year 2** | Month 13–24 | 600 paying clients | $75 | $540,000 |
| **Year 3** | Month 25–36 | 2,000 paying clients | $90 | $1.8M |

**Key milestones:**
- 10 beta clients: October 2026
- 50 paying clients → $10K MRR (Feb 2027) — Seed unlock
- 323 clients → $22K MRR (Nov 2027) — EBITDA milestone
- Cash-flow break-even: September 2028 (Month 28)

### 4.4 Market Trends Supporting SOCVault

1. **UK NCSC Active Cyber Defence** — pushing SMBs toward automated tools
2. **GDPR enforcement** — ICO issuing record fines; compliance automation demand rising
3. **Cyber Essentials mandate** — UK government supply chain pressure
4. **AI security tools viability** — Claude API pricing makes SMB deployment feasible
5. **Managed SOC staffing crisis** — MSSP workforce shortage → automation requirement

---

## 5. Product Architecture

### 5.1 System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SOCVault Platform (MVP = AWS Staging)                 │
│                                                                         │
│  Frontend:           │  API Layer:              │  Scanning Engines:  │
│  ┌──────────────┐    │  ┌──────────────────┐   │  ┌───────────────┐ │
│  │ React/TS     │───►│  │ API Gateway HTTP │───►│  │ Lambda (L1)   │ │
│  │ Dashboard    │    │  │ + Lambda         │   │  │ + Fargate/EKS │ │
│  │ (Amplify)    │    │  │ (FastAPI/Mangum) │   │  │ (L2–L8 paid)  │ │
│  └──────────────┘    │  └──────────────────┘   │  └───────────────┘ │
│                      │           │              │         │           │
│                      │   ┌───────▼────────┐    │    ┌────▼──────┐  │
│                      │   │ Cognito        │    │    │ Claude    │  │
│                      │   │ (Auth + JWT)   │    │    │ API       │  │
│                      │   └────────────────┘    │    │(Sonnet 4) │  │
│                      │                         │    └───────────┘  │
│  Persistence:        │  Messaging:             │  Threat Intel:     │
│  ┌──────────────┐    │  ┌──────────────────┐   │  ┌───────────────┐ │
│  │ MongoDB      │    │  │ SQS + Lambda     │   │  │ AbuseIPDB,    │ │
│  │ Atlas M0     │    │  │ (async workers)  │   │  │ AlienVault OTX│ │
│  │ (production) │    │  └──────────────────┘   │  │ GreyNoise     │ │
│  ├──────────────┤    │                         │  └───────────────┘ │
│  │ DynamoDB     │    │  ┌──────────────────┐   │                     │
│  │ (cost + rate)│    │  │ SNS              │   │  ┌───────────────┐ │
│  ├──────────────┤    │  │ (notifications)  │   │  │ Wazuh Manager │ │
│  │ S3           │    │  └──────────────────┘   │  │ (Phase 2+)    │ │
│  │ (scan data)  │    │                         │  └───────────────┘ │
│  └──────────────┘    │                         │                     │
│                      │  Admin Vault:           │  Payments:          │
│                      │  ┌──────────────────┐   │  ┌───────────────┐ │
│                      │  │ SSM Parameter    │   │  │ Stripe        │ │
│                      │  │ Store + KMS      │   │  │ (webhooks)    │ │
│                      │  └──────────────────┘   │  └───────────────┘ │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ Monitoring: CloudWatch | Logging: CloudTrail | CI/CD: GitHub Actions │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Execution Model

| Environment | Status | API | Workers | Scan Runtime | Duration |
|---|---|---|---|---|---|
| **Staging (MVP)** | 🟢 Active | Lambda + API GW | SQS + Lambda | Lambda (L1) + Fargate optional (L2+) | 90s–15m |
| **Production** | ⏸ Dormant (until cutover) | Same as staging | Same as staging | Same as staging | — |

**Key Principle (ADR-006):** MVP = staging only. Production dormant until cutover checklist complete.

---

## 6. Scanning Engine — 8 Attack Surface Layers

### 6.1 Layer Breakdown

#### L1 — External Reconnaissance (FREE)

**Tier:** Freemium (1 scan/month/tenant)  
**Runtime:** AWS Lambda  
**Duration:** ~90 seconds (15 steps in parallel)  
**Tools:** Subfinder, Naabu, httpx, sslyze, checkdmarc, crt.sh, HaveIBeenPwned, AbuseIPDB, Google Safe Browsing

**15-Step Scan Process:**

| Step | Action | Tool | What Is Flagged |
|---|---|---|---|
| 1 | WHOIS Lookup | python-whois | Domain expiry <30 days, privacy shield, registrar mismatch |
| 2 | DNS Record Analysis | dnspython | Missing A/MX/NS, wildcard DNS, zone transfer enabled |
| 3 | Email Security (SPF/DKIM/DMARC) | checkdmarc | None/fail/softfail SPF; missing DMARC; email spoofing possible |
| 4 | SSL/TLS Certificate Audit | sslyze, crt.sh | Cert expiry <30 days, self-signed, TLS 1.0/1.1, weak ciphers |
| 5 | HTTP Security Headers | python-requests | Missing CSP, HSTS, X-Frame-Options, X-Content-Type-Options |
| 6 | Certificate Transparency Lookup | crt.sh REST API | Subdomains exposed via SSL cert history |
| 7 | Subdomain Discovery (passive) | Subfinder | Live subdomains via DNS, VirusTotal, Censys, DNSdumpster |
| 8 | Live Host Validation | httpx | HTTP status, redirect chains, server technology headers |
| 9 | Port Discovery | Naabu (top 100 TCP) | High-risk open ports: 22 (SSH), 3306 (MySQL), 6379 (Redis), 27017 (MongoDB), 9200 (Elasticsearch) |
| 10 | Technology Fingerprinting | httpx + Wappalyzer | CMS (WordPress/Joomla/Drupal), frameworks, CDN, version exposure |
| 11 | IP Reputation Check | AbuseIPDB | Blacklisted IPs, offshore hosting flags |
| 12 | Domain Reputation Check | Google Safe Browsing, URLhaus | Phishing/malware classification, blocklist status |
| 13 | Credential Leak Check | HaveIBeenPwned API | Number of exposed accounts, breach database names, exposure date |
| 14 | Subdomain Takeover Detection | Custom CNAME checker | CNAMEs pointing to unclaimed AWS/Azure/GitHub/Heroku services |
| 15 | Service Banner Analysis | Naabu + Nmap banners | Outdated service versions (e.g. OpenSSH 7.2 → multiple CVEs) |

**Output Schema:**
```json
{
  "scan_id": "uuid",
  "layer": "L1",
  "target": "example.com",
  "status": "COMPLETE",
  "raw_findings": {
    "step_1_whois": {...},
    "step_2_dns": {...},
    ...
    "step_15_banners": {...}
  },
  "aggregated_findings": [
    {
      "finding_id": "uuid",
      "step": 4,
      "severity": "high",
      "title": "SSL Certificate Expires in 15 Days",
      "description": "...",
      "affected_asset": "www.example.com:443"
    }
  ],
  "scanned_at": "2026-06-18T10:00:00Z",
  "duration_seconds": 87,
  "cogs": {
    "compute_cost": 0.000002,
    "threat_intel_cost": 0.03,
    "total": 0.032
  }
}
```

#### L2 — Web Application Security (PAID)

**Tier:** Paid ($15/IP/month)  
**Runtime:** AWS Fargate  
**Duration:** ~15 minutes  
**Tools:** Nuclei, OWASP ZAP, Semgrep, Trivy

**Coverage:**
- CVE detection + version mapping
- SAST (Static Application Security Testing)
- DAST (Dynamic Application Security Testing)
- Web shell detection
- Outdated library/framework detection

#### L3 — Mobile Application Security (PAID)

**Tier:** Paid ($20/app/month)  
**Runtime:** AWS Fargate  
**Duration:** ~20 minutes  
**Tools:** MobSF, Trivy (container)

**Coverage:**
- Android APK binary analysis
- iOS IPA binary analysis
- MASVS (Mobile Application Security Verification Standard) compliance
- Hardcoding detection (API keys, secrets)
- Crypto algorithm audit

#### L4 — API Security (PAID)

**Tier:** Paid ($15/endpoint/month)  
**Runtime:** AWS Lambda  
**Duration:** ~10 minutes  
**Tools:** Nuclei API templates, OWASP ZAP API, Semgrep API rules

**Coverage:**
- OWASP API Top 10 (broken object level authorization, user authentication, excessive data exposure, etc.)
- Auth bypass attempts
- Injection flaws (SQLi, command injection, etc.)
- Rate limiting enforcement

#### L5 — Compliance Gap Analysis (PAID)

**Tier:** Paid ($30/month/domain)  
**Runtime:** AWS Lambda  
**Duration:** ~5 minutes  
**Tools:** Custom Python rule engine, Prowler

**Coverage:**
- **PCI-DSS** v3.2.1 control mapping
- **GDPR** article cross-reference
- **ISO 27001** domain alignment
- **SOC2** trust service categories
- **Cyber Essentials+** mappings

**Output:** PDF report showing pass/fail status per control + remediation guidance.

#### L6 — Cloud Infrastructure Security (PAID)

**Tier:** Paid ($25/environment/month)  
**Runtime:** AWS Fargate  
**Duration:** ~10 minutes  
**Tools:** CloudFox, Pacu, Prowler, Steampipe

**Coverage (AWS/Azure/GCP):**
- IAM misconfigurations
- Overpermissioned roles
- Privilege escalation paths
- Storage bucket exposure
- Network exposure

#### L7 — SOC/SIEM Real-Time Threat Detection (SOC PRO)

**Tier:** SOC Pro ($199/month)  
**Runtime:** Wazuh EC2 Manager (persistent, Phase 2+)  
**Duration:** Continuous  
**Tools:** Wazuh agent + manager

**Coverage:**
- Real-time process monitoring
- File integrity monitoring (FIM)
- Log aggregation + analysis
- Rootkit detection
- Brute-force detection
- Alert correlation

#### L8 — Malware Detection & Response (SOC PRO)

**Tier:** SOC Pro ($199/month)  
**Runtime:** Wazuh EC2 + Lambda + Fargate  
**Duration:** Continuous + on-demand  
**Tools:** ClamAV, YARA, Trivy, Nuclei webshell templates, Claude AI

**Full Detection & Response Flow:**

```
Detection Sources
├── Wazuh Agent ClamAV real-time scan
├── Wazuh File Integrity Monitoring (FIM)
├── Wazuh Rootkit Detection
├── L2 Web Scan (Nuclei webshell templates)
├── Container scan (Trivy malicious layers)
└── Process Monitor (crypto miners, ransomware behaviour)
        │
        ▼
   SOCVault MDRM Microservice
        │
        ├── Hash lookup: VirusTotal + local YARA rules
        ├── File context: path, owner, creation time, size
        └── Host context: agent ID, hostname, running services
                 │
                 ▼
           Claude API (claude-sonnet-4-6)
                 │ Determines:
                 │ ✓ Malware family (ransomware/trojan/cryptominer/webshell/rootkit/spyware)
                 │ ✓ Severity score (1–10)
                 │ ✓ Lateral movement risk
                 │ ✓ Data exfiltration likelihood
                 │ ✓ Quarantine command
                 │ ✓ Removal command + persistence cleanup
                 │ ✓ Post-remediation verification command
                 │
        ┌────────▼───────────────────┐
        │                            │
 Confidence >95%         High-risk / system-wide
 Isolated file/process  (core services, databases)
        │                            │
        ▼                            ▼
 AUTO-REMEDIATE          HUMAN APPROVAL GATE
 - Quarantine file       - Full context displayed
 - Kill process          - Analyst approves action
 - Update blocklist      - Options: quarantine /
 - Send alert              isolate host / escalate
```

**Auto-Remediation (High Confidence):**
- Quarantine file to `/var/ossec/quarantine/{hash}`
- Kill process + remove from startup
- Update Wazuh blocklist
- Send Slack + email + dashboard notification

**Human Gate (System-Critical):**
- Database service affected
- Core OS service affected
- Enterprise-wide impact
- Requires manager approval with full context

**Post-Remediation:**
- Re-scan with ClamAV to confirm removal
- Update Workspace Health Score
- Generate incident report (malware family, timeline, actions taken)

#### L9 — AI Agent Autonomous Security Assessment (FUTURE — Phase 2)

**Tier:** SOC Pro (included)  
**Runtime:** AWS Fargate  
**Duration:** 30–60 minutes  
**Model:** Claude Opus 4.8 (extended thinking)

**Capability:** Autonomous multi-step security assessment using extended thinking, able to:
- Correlate findings across all 8 layers
- Identify attack chains
- Prioritize by business impact
- Generate executive-level strategic recommendations

---

## 7. AI Intelligence Layer

### 7.1 Claude AI Models & Roles

| Model | Use Case | Token Budget | Features |
|---|---|---|---|
| **claude-sonnet-4-6** | Financial risk translation, SOAR triage, malware analysis, chat | 200K ctx | Primary reasoning; ~600 req/min |
| **claude-haiku-4-5-20251001** | Fast enrichment, light triage | 200K ctx | Cost-optimized; fallback triage |
| **claude-opus-4-8** | L9 AI Agent (extended thinking) | 200K ctx | Extended thinking mode enabled |

### 7.2 Financial Risk Translation

**Input:** Raw scan findings (L1–L8)  
**Process:** Claude calculates multi-factor financial risk per finding

**Calculation Factors:**

| Risk Category | Calculation | Example Output |
|---|---|---|
| **Operational Risk** | Downtime hours × £500/hour business impact | SSL cert expiry → 4 hours downtime → £2,000 operational loss |
| **Regulatory Risk** | GDPR fine bracket × exposure scope | Credential leak (1000 accounts) → Article 83 bracket → £75,000–375,000 exposure |
| **Recovery Cost** | Forensics (£5,000) + notification (£2/per affected record) + PR damage | Breach of 10K records → £5,000 + £20,000 + £50,000 incident cost = £75,000 |
| **Insurance Impact** | Premium increase × years until renewal + void risk | Unpatched server → 20% premium increase × 3 years = £6,000 extra; void risk on claim |
| **Compliance Penalty** | Industry + jurisdiction-specific fine models | E-commerce company + PCI-DSS breach → £100,000–500,000 + payment processor termination |

**Output Schema:**
```json
{
  "findings": [
    {
      "finding_id": "uuid",
      "title": "SSL Certificate Expires in 15 Days",
      "technical_description": "...",
      "business_impact": "Payment processing will become unavailable; customers unable to complete transactions",
      "financial_exposure": {
        "operational_risk_gbp": 2000,
        "regulatory_risk_gbp": 0,
        "recovery_cost_gbp": 5000,
        "insurance_impact_gbp": 1500,
        "total_exposure_gbp": 8500
      },
      "remediation_timeline_hours": 0.5,
      "severity": "high",
      "confidence_score": 0.99
    }
  ],
  "health_score": 68,
  "total_financial_exposure_gbp": 142500,
  "executive_summary": "Your external attack surface shows moderate risk with £142,500 exposure. Top priority: SSL certificate renewal (£8,500) and email security hardening (£35,000). These two remediations will reduce exposure to £99,200.",
  "ai_status": "complete",
  "token_usage": {
    "input": 2400,
    "output": 1200,
    "total": 3600,
    "cost_gbp": 0.18
  }
}
```

### 7.3 Remediation Script Generation

**Input:** Single vulnerability finding  
**Process:** Claude generates copy-paste fix for target platform

**Example:**

```
Finding: "DNS Zone Transfer Enabled on ns1.example.com"

Remediation Script:
---
# BIND DNS Server - Disable Zone Transfers

1. SSH to ns1.example.com
2. Edit /etc/bind/named.conf.options:
   
   // Before:
   // (no zone transfer restrictions)
   
   // After:
   allow-transfer { none; };  // Reject all zone transfer requests
   
3. Validate config:
   $ sudo named-checkconf
   
4. Restart BIND:
   $ sudo systemctl restart bind9
   
5. Verify:
   $ dig @ns1.example.com example.com axfr
   ; <<>> DiG 9.16.1-Ubuntu <<>> @ns1.example.com example.com axfr
   ; (0 servers found)
   ;; global options: +cmd
   ;; Query time: 1 msec
   ;; SERVER: ns1.example.com#53(ns1.example.com)
   ;; WHEN: Sun Jun 18 10:00:00 UTC 2026
   ;; MSG SIZE  rcvd: 97
   
   ✓ Zone transfers successfully blocked.
```

### 7.4 Fallback Offline Reporting

**Scenario:** Claude API unavailable (rate limit, network error, outage)  
**Behavior:** Return pre-defined offline report based on finding patterns

```json
{
  "ai_status": "degraded",
  "health_score": null,
  "total_financial_exposure_gbp": null,
  "executive_summary": "AI analysis temporarily unavailable. Raw findings displayed below with standard severity classification.",
  "findings": [
    {
      "finding_id": "uuid",
      "title": "SSL Certificate Expires in 15 Days",
      "severity": "high",
      "standard_risk_gbp": 8500,  // Pre-calculated default
      "ai_generated": false
    }
  ],
  "retry_after_seconds": 300
}
```

### 7.5 Prompt Caching

**Implementation:** Cache system prompts on repeated calls  
**Benefit:** 90% reduction in input token costs for repeated prompts  
**Cost impact:** From $0.18 per scan → $0.018 per scan (after cache hit)

---

## 8. SOAR (Security Orchestration, Automation & Response)

### 8.1 SOAR Architecture

```
Wazuh Alert (severity ≥10)
         │
         ▼
   SOAR Ingestion
         │
   ├─ Extract: src_ip, dst_ip, alert_name, evidence
   ├─ Enrich: IP reputation (AbuseIPDB), threat actor (AlienVault OTX)
   └─ Score: Confidence (0–100)
         │
         ▼
   Claude AI Triage
         │
   ├─ Decision: "CONTAIN" or "ESCALATE"?
   ├─ Reasoning: Attack pattern, lateral movement risk, data exposure likelihood
   └─ Confidence: High (>90%) or Low (<70%)
         │
   ┌─────▼─────────────────────────┐
   │                               │
  CONTAIN                      ESCALATE
  (confidence >90%)          (confidence <70% or system-critical)
   │                               │
   ▼                               ▼
 AUTO-EXECUTE                 HUMAN REVIEW QUEUE
 (no approval)                (requires manager approval)
```

### 8.2 Default SOAR Playbooks

#### Playbook 1: Ransomware Containment

**Trigger:** Wazuh alert = "Ransomware behaviour detected" (file encryption pattern + encrypted extension writing)

**Actions:**
1. Isolate host from network (disable network interface)
2. Kill suspicious processes (ranked by CPU/memory)
3. Block outbound HTTPS connections to suspicious IPs
4. Snapshot current state for forensics
5. Notify IT manager + SOCVault admin dashboard

#### Playbook 2: SSH Brute-Force Block

**Trigger:** Wazuh alert = "SSH brute-force attempt" (>10 failed logins from single IP in 5 min)

**Actions:**
1. Add source IP to firewall blocklist (iptables/UFW)
2. Add source IP to Wazuh blocklist (future connections blocked)
3. Disable SSH password auth temporarily; require MFA for next 24h
4. Notify IT manager
5. Create incident ticket in ServiceNow/Jira (if integrated)

#### Playbook 3: Phishing Email Purge

**Trigger:** Wazuh alert = "Phishing email detected" + manual analyst flagging

**Actions:**
1. Query email server (O365/GSuite API) for message ID
2. Delete email from all mailboxes
3. Add sender to organization blocklist
4. Notify affected users via email
5. Create incident ticket + training flag

### 8.3 Human Approval Gate

**Triggers requiring human approval:**
- Host isolation (disconnects production server)
- Process termination (core OS service)
- Firewall rule modification (system-wide)
- Email deletion (irreversible)
- Data quarantine (loss of access)

**Approval UI:**
```
┌─────────────────────────────────────────┐
│ SOAR Action Pending Approval             │
├─────────────────────────────────────────┤
│ Alert: SSH Brute-Force (8 failed logins)│
│ Source IP: 203.0.113.45                  │
│ Threat Level: Medium                     │
│ Proposed Action: Block IP + enable MFA  │
│ Affected Systems: 3 servers              │
│                                          │
│ [Approve] [Reject] [Modify] [Escalate]  │
└─────────────────────────────────────────┘
```

**Response SLA:**
- Critical: 15 minutes
- High: 1 hour
- Medium: 4 hours
- Low: 24 hours

---

## 9. Malware Detection & Response Engine (L8)

### 9.1 Detection Pipeline

**Real-Time Detection Sources:**

1. **Wazuh ClamAV Integration**
   - Real-time file scanning on all monitored endpoints
   - Signature database updated daily
   - Alert on known malware hash match

2. **File Integrity Monitoring (FIM)**
   - New/modified executable files flagged
   - Permission changes on system binaries monitored
   - Binary timestamps validated against known safe version

3. **Wazuh Rootkit Detection**
   - Kernel module scanning
   - System call table integrity check
   - Running process vs. filesystem discrepancy detection

4. **Web Shell Detection (L2 paid tier)**
   - Nuclei webshell templates on L2 scans
   - PHP/ASP/JSP suspicious code patterns
   - Execution path monitoring for web-accessible directories

5. **Container Malicious Layer Detection**
   - Trivy container image scanning (L2)
   - Known malware signatures + OS vulnerability patterns
   - Privilege escalation paths in image layers

6. **Process Monitor (Wazuh behavioral)**
   - Crypto miner detection (CPU intensive + network beaconing)
   - Ransomware detection (rapid file encryption + extension modification)
   - Rootkit detection (suspicious kernel operations)

### 9.2 AI Triage & Analysis

**Input to Claude (claude-sonnet-4-6):**
```json
{
  "detection": {
    "type": "file",
    "hash": "5d41402abc4b2a76b9719d911017c592",
    "path": "/var/www/html/shell.php",
    "size_bytes": 2048,
    "created_timestamp": "2026-06-18T09:45:00Z",
    "modified_timestamp": "2026-06-18T10:15:00Z",
    "owner": "www-data",
    "permissions": "644"
  },
  "virustotal_lookup": {
    "found_signatures": 42,
    "malware_family": "PHP/Shell.Generic",
    "first_submission": "2026-06-10",
    "last_submission": "2026-06-18"
  },
  "yara_matches": ["Web_Shell_PHP", "Webshell_C99", "File_Encrypted"],
  "host_context": {
    "hostname": "web-server-03",
    "agent_id": "uuid",
    "os": "Ubuntu 20.04 LTS",
    "running_services": ["apache2", "mysql", "ssh"],
    "network_connections": [
      {"protocol": "tcp", "remote_ip": "203.0.113.99", "remote_port": 443, "state": "ESTABLISHED"}
    ]
  }
}
```

**Claude Output:**
```json
{
  "malware_family": "PHP Web Shell (C99-variant)",
  "severity_score": 10,
  "confidence": 0.99,
  "analysis": {
    "type": "Web shell enabling remote code execution",
    "infection_vector": "Likely uploaded via vulnerable file upload or compromised admin account",
    "lateral_movement_risk": "HIGH — Attacker can pivot to database, internal network via web server compromise",
    "data_exfiltration_likelihood": "CRITICAL — Web shell can access database directly; customer data at risk",
    "persistence_mechanism": "File persists; requires removal. Check for backdoor accounts, cron jobs."
  },
  "recommended_actions": {
    "immediate": [
      "Isolate web-server-03 from network (HIGH RISK)",
      "Kill Apache process to prevent further shell access",
      "Block outbound connections from web-server-03",
      "Snapshot system for forensics"
    ],
    "follow_up": [
      "Re-scan entire /var/www for similar shells",
      "Audit file upload mechanisms for vulnerability",
      "Review authentication logs for unauthorized access",
      "Notify database team of potential credential compromise"
    ]
  },
  "auto_remediation": {
    "confidence_threshold_met": true,
    "action": "AUTO_REMEDIATE",
    "steps": [
      "quarantine /var/www/html/shell.php to /var/ossec/quarantine/5d41402abc4b2a76b9719d911017c592.php",
      "kill apache2 process group",
      "add 5d41402abc4b2a76b9719d911017c592 to Wazuh global blocklist",
      "snapshot filesystem state for forensics",
      "run post-remediation ClamAV full scan"
    ],
    "requires_human_approval": false
  }
}
```

### 9.3 Remediation Execution

#### Auto-Remediation (Confidence >95%, Isolated File/Process)

```bash
#!/bin/bash
# Auto-Remediation Script — Web Shell Removal

HASH="5d41402abc4b2a76b9719d911017c592"
FILE_PATH="/var/www/html/shell.php"
QUARANTINE_DIR="/var/ossec/quarantine"

# Step 1: Quarantine file
mkdir -p "$QUARANTINE_DIR"
cp "$FILE_PATH" "$QUARANTINE_DIR/${HASH}.php"
rm "$FILE_PATH"
echo "[$(date)] File quarantined: $FILE_PATH" >> /var/ossec/logs/remediation.log

# Step 2: Kill Apache process
systemctl stop apache2
echo "[$(date)] Apache2 stopped" >> /var/ossec/logs/remediation.log

# Step 3: Add to blocklist (prevent re-execution)
# (Wazuh API call)
curl -X POST https://wazuh-manager:55000/security/users/authenticate \
  -d '{"user":"admin","password":"..."}' \
  -H "Content-Type: application/json" > /tmp/auth.json

TOKEN=$(jq -r '.data.token' /tmp/auth.json)

curl -X POST https://wazuh-manager:55000/rules \
  -H "Authorization: Bearer $TOKEN" \
  -d "{
    \"rule_id\": \"$HASH\",
    \"rule_type\": \"file_hash_blocklist\",
    \"action\": \"block\"
  }" >> /var/ossec/logs/remediation.log

# Step 4: Re-scan system
clamscan -r --remove /var/www/ > /var/ossec/logs/post_remediation_scan.log

# Step 5: Notify SOCVault
curl -X POST https://api-staging.socvault.io/api/v1/malware/{incident_id}/remediation-complete \
  -H "Authorization: Bearer $SYSTEM_TOKEN" \
  -d "{ \"status\": \"remediated\", \"scan_result\": \"clean\" }"

echo "[$(date)] Remediation complete" >> /var/ossec/logs/remediation.log
```

#### Human Approval Gate (System-Critical)

**Scenario:** Malware detected in `/usr/bin/sshd` (SSH daemon)

**Approval Request:**
```
URGENT: Malware Detected in Core System Service

Finding: Ransomware (Cerber variant) in /usr/bin/sshd
Confidence: 98%
File Hash: a1b2c3d4e5f6g7h8...
Severity: CRITICAL

AUTOMATIC ACTION BLOCKED (system-critical file)

Proposed Remediation:
✗ Remove /usr/bin/sshd (WOULD BREAK SSH ACCESS)
✗ Isolate host from network (BLOCKS ALL REMOTE ACCESS)
✓ Backup SSH daemon to /var/ossec/quarantine/
✓ Replace with clean version from package manager
✓ Verify SSH service starts
✓ Authenticate remote users only
✓ Monitor for rootkit persistence

Manager Approval Required
[Approve] [Reject] [Escalate] [Call Incident Response]
```

### 9.4 Post-Remediation Verification

```json
{
  "remediation_id": "uuid",
  "incident_id": "uuid",
  "original_finding": "PHP Web Shell in /var/www/html/shell.php",
  "remediation_actions": [
    "File quarantined",
    "Apache process terminated",
    "IP blocklist updated",
    "System snapshot created"
  ],
  "post_remediation_scan": {
    "timestamp": "2026-06-18T11:30:00Z",
    "scanner": "ClamAV + YARA",
    "results": {
      "file_hash_found": false,
      "similar_signatures": 0,
      "clean_status": true
    }
  },
  "verification": {
    "status": "PASSED",
    "confidence": 1.0,
    "message": "File hash not detected in post-remediation scan. System clean."
  },
  "incident_report": {
    "title": "Web Shell Remediation Successful",
    "summary": "PHP web shell (C99-variant) successfully removed from production web server.",
    "timeline": [
      {"timestamp": "2026-06-18T10:15:00Z", "event": "Malware detected"},
      {"timestamp": "2026-06-18T10:16:30Z", "event": "AI analysis complete"},
      {"timestamp": "2026-06-18T10:17:00Z", "event": "Auto-remediation executed"},
      {"timestamp": "2026-06-18T11:30:00Z", "event": "Post-remediation verification passed"}
    ],
    "recommendations": [
      "Investigate file upload mechanisms for vulnerability",
      "Review admin account access logs",
      "Patch web application framework",
      "Enable Web Application Firewall (WAF)"
    ]
  }
}
```

---

## 10. Business Model & Revenue Streams

### 10.1 Pricing Tiers

#### Free Tier

| Feature | Free |
|---|---|
| Price | $0 |
| Recon scans/month | 1 |
| Domains | 1 |
| Financial risk map | ✓ |
| Remediation scripts | ✗ |
| Health score | ✓ |
| API access | ✗ |

#### Web VAPT ($15/IP/month or $180/IP/year)

| Feature | Web VAPT |
|---|---|
| Recon scans | Unlimited |
| Web AppSec (L2) scans | Unlimited |
| CVE remediation scripts | ✓ |
| Financial risk translation | ✓ |
| Compliance mapping | ✓ |
| Team sub-users | 2 |
| API access | ✗ |

#### Mobile ($20/app/month or $240/app/year)

| Feature | Mobile |
|---|---|
| All Web VAPT features | ✓ |
| Mobile binary analysis (L3) | Unlimited |
| MASVS compliance reports | ✓ |
| Android/iOS vulnerability mapping | ✓ |
| Team sub-users | 3 |

#### Cloud ($25/environment/month or $300/environment/year)

| Feature | Cloud |
|---|---|
| All Web VAPT features | ✓ |
| Cloud infrastructure scanning (L6) | Unlimited |
| IAM audit + privilege escalation paths | ✓ |
| Multi-cloud (AWS/Azure/GCP) | ✓ |
| Compliance (PCI, GDPR, ISO27001, SOC2) | ✓ |
| Team sub-users | 4 |

#### SOC Pro ($199/month or $2,388/year)

| Feature | SOC Pro |
|---|---|
| All paid layer scans (L2–L6) | Unlimited |
| Wazuh agents included | 50 |
| SOAR playbooks + auto-remediation | ✓ |
| Malware detection & response (L8) | ✓ |
| Claude AI triage | Unlimited |
| Real-time threat detection | ✓ |
| Incident response SLA (8h) | ✓ |
| API access | ✓ |
| Team sub-users | 10 |
| Custom playbooks | Coming Phase 2 |

#### SOC Enterprise ($499/month or $5,988/year)

| Feature | SOC Enterprise |
|---|---|
| All SOC Pro features | ✓ |
| Unlimited Wazuh agents | ✓ |
| White-label dashboard + branding | ✓ |
| API key authentication | ✓ |
| Custom SLA (4h incident response) | ✓ |
| Dedicated account manager | ✓ |
| Team sub-users | Unlimited |
| L9 AI Agent autonomous assessment | Coming Phase 2 |
| Custom integrations (Slack, Teams, Jira) | ✓ |

### 10.2 Revenue Streams

#### Stream 1: Freemium-to-Paid Conversion

- Entry: 1 free L1 scan/month
- Conversion trigger: User discovers £X financial exposure
- Conversion path: Upgrade to Web VAPT ($15/mo) to unlock remediation scripts
- Blended conversion rate (DevTools SaaS): 12%

**Economics:**
```
10,000 Free Signups
     ↓ (12% conversion)
1,200 Trial-to-Paid
     × $180/year first year ARPU
= $216,000 Year 1 revenue (free tier contribution)
```

#### Stream 2: Pay-Per-IP/Domain Licensing (Transactional)

| Product | Price | Annual | Gross Margin |
|---|---|---|---|
| Web VAPT | $15/IP/mo | $180 | 97.6% ($0.36 COGS) |
| Mobile | $20/app/mo | $240 | 97.8% ($0.41 COGS) |
| Cloud | $25/env/mo | $300 | 97.8% ($0.52 COGS) |
| API | $15/endpoint/mo | $180 | 97.6% ($0.36 COGS) |
| Compliance | $30/domain/mo | $360 | 99.7% ($0.09 COGS) |

#### Stream 3: SOC Pro Subscription (Recurring)

| Tier | Price | Included | Margin |
|---|---|---|---|
| SOC Pro | $199/mo | Unlimited L2–L8, 50 Wazuh agents, SOAR | ~85% |
| SOC Enterprise | $499/mo | + unlimited agents, white-label, SLA | ~80% |

#### Stream 4: AI Chat Credit-Based (Phase 2)

**Credit Model:**

| Bundle | Credits | Price | Per-Credit | Saving |
|---|---|---|---|---|
| Starter | 50 | $5.00 | $0.100 | — |
| Standard | 200 | $15.00 | $0.075 | 25% |
| Pro | 500 | $30.00 | $0.060 | 40% |
| Enterprise | 2,000 | $99.00 | $0.050 | 50% |

**Credit Costs:**

| Action | Credits | Example |
|---|---|---|
| Ask security question | 1 | "What's my compliance gap for ISO 27001?" |
| Show findings/reports | 1 | Display scan results in chat |
| Generate remediation script | 2 | Generate fix for specific CVE |
| Trigger L1 recon scan | 3 | Start new scan via chat command |
| Trigger L2 VAPT scan | 5 | Start comprehensive web app scan |
| Compliance gap analysis | 3 | Map findings to compliance frameworks |
| Cloud posture check | 4 | Trigger CloudFox/Prowler scan |
| Approve/reject SOAR action | 2 | Approve malware remediation |
| Generate board report | 5 | Create executive PDF summary |
| Create Jira/ServiceNow ticket | 1 | Auto-create issue from finding |

**Unit Economics (AI Chat):**
- Average credit bundle: $18 (blended)
- Claude API cost per credit: ~$0.008 (with 84% prompt cache hit)
- Gross margin: **~87%**
- Expected burn per active user/month: 40–80 credits ($3–6 cost, $3.20–6.40 revenue)

#### Stream 5: Professional Services (Future — Year 2+)

- Incident response retainers
- Custom playbook development
- Compliance audit services
- Security training workshops

### 10.3 Unit Economics

**L1 Recon Scan (Free tier):**
```
Revenue per scan: $0 (free)
COGS per scan: $0.032 (compute + TI)
Margin: N/A (acquisition funnel)
Annual payoff: Convert to paid within 12 months
```

**L2 Web VAPT Scan ($15/month):**
```
Monthly revenue per IP: $15
Annual revenue per IP: $180
Monthly COGS: $0.36 ($0.03/scan avg × 12 scans)
Annual COGS: $4.32
Annual margin: $175.68 (97.6%)
Customer LTV (assuming 24-month retention): $360–420
CAC (from free tier): ~$2–5 (acquisition already paid from free funnel)
LTV:CAC ratio: 84–210x (exceptionally strong)
```

**SOC Pro Subscription ($199/month):**
```
Monthly revenue: $199
Monthly COGS (compute + AI + TI): ~$30
Monthly margin: $169 (85%)
Annual margin: $2,028
Customer LTV (assuming 24-month retention): $4,056–4,800
CAC (from free tier + trial): ~$20–50
LTV:CAC ratio: 81–240x
```

### 10.4 Freemium Funnel to Revenue

```
10,000 Free Signups (Month 1)
  ↓ (4.2% try paid after 30 days)
420 Trial conversions
  ↓ (28.6% convert to paying after trial)
120 Paying customers (Month 3)
  ├─ 30% upgrade Web VAPT ($15/mo)        = 36 customers = $540/mo
  ├─ 50% stay SOC Pro ($199/mo)           = 60 customers = $11,940/mo
  └─ 20% upgrade to Cloud ($25/mo)        = 24 customers = $600/mo
  
TOTAL: 120 paying customers = $13,080/mo (Month 3 run rate)
```

---

## 11. Functional Requirements

### 11.1 Authentication & Onboarding (FR-001–018)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-001 | Accept signup: business email + phone only | Must Have | 1 |
| FR-002 | Block freemail domains (Gmail, Yahoo, Hotmail, etc.) | Must Have | 1 |
| FR-003 | Extract + validate company domain from email | Must Have | 1 |
| FR-004 | Send 6-digit OTP via SMS (AWS SNS) | Must Have | 1 |
| FR-005 | Provision unique tenant (UUID `tenant_id`) within 60 seconds | Must Have | 1 |
| FR-006 | Return Cognito-issued JWT (access + refresh tokens) | Must Have | 1 |
| FR-007 | Support TOTP MFA (Pro/Enterprise) | Should Have | 2 |
| FR-008 | Support magic link login (email alternative) | Should Have | 2 |
| FR-009 | Support SAML 2.0 SSO (Enterprise) | Nice to Have | 3 |
| FR-010 | Require DNS TXT record verification | Must Have | 2 |
| FR-011 | Require HTML meta tag verification | Must Have | 2 |
| FR-012 | Poll verification status every 60 seconds | Must Have | 2 |
| FR-013 | Display verified domain badge | Must Have | 2 |
| FR-014 | Block active scans (L2+) until verified; L1 pre-verification OK | Must Have | 2 |
| FR-015 | Provide Wazuh agent deployment wizard | Must Have | 2 |
| FR-016 | Accept OpenAPI/Swagger spec for L4 API scans | Should Have | 2 |
| FR-017 | Accept CI/CD webhook trigger for L3 mobile scans | Should Have | 3 |
| FR-018 | Support password-less authentication | Should Have | 2 |

### 11.2 Scanning Engine (FR-019–032)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-019 | L1: Execute all 15 steps (WHOIS, DNS, email, SSL, headers, cert transparency, subdomains, hosts, ports, fingerprinting, IP rep, domain rep, credential leaks, subdomain takeover, banners) | Must Have | 1 |
| FR-020 | L2: Execute web app scanning (CVE detection, SAST, DAST, webshell detection) | Must Have | 2 |
| FR-022 | L3: Execute mobile binary analysis (Android APK, iOS IPA via MobSF) | Should Have | 2 |
| FR-023 | L4: Execute API security scans (OWASP API Top 10) | Should Have | 2 |
| FR-024 | L5: Execute compliance gap analysis (PCI, GDPR, ISO27001, SOC2) | Should Have | 2 |
| FR-024A | Accept PDF/DOCX policy uploads for ISO 27001 gap analysis via Claude | Should Have | 2 |
| FR-025 | L6: Execute cloud infrastructure penetration testing (AWS, Azure, GCP) | Should Have | 3 |
| FR-025A | L1: Fingerprint CMS platforms + enumerate plugins + flag abandoned/CVE versions | Should Have | 2 |
| FR-026 | Enforce Freemium rate limit: 1 L1 scan per calendar month per tenant | Must Have | 1 |
| FR-027 | Enforce per-IP/domain licensing: paid scans require active license | Must Have | 2 |
| FR-028 | Require explicit scan authorization consent checkbox | Must Have | 1 |
| FR-029 | Validate scan target within tenant's registered domain (prevent 3rd-party scanning) | Must Have | 2 |
| FR-030 | Run each scan in isolated execution environment (no cross-tenant memory sharing) | Must Have | 1 |
| FR-031 | Return scan status updates via polling endpoint within 5 seconds of change | Must Have | 1 |
| FR-032 | Support concurrent scans (multiple layers simultaneously) for Pro/Enterprise | Should Have | 3 |

### 11.3 AI Intelligence (FR-040–052)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-040 | Translate all findings into plain-English business risk summaries | Must Have | 1 |
| FR-041 | Calculate quantified financial exposure (USD) per vulnerability | Must Have | 1 |
| FR-042 | Calculate estimated remediation timeline (hours/days) | Must Have | 1 |
| FR-043 | Generate Workspace Health Score (0–100) | Must Have | 1 |
| FR-044 | Generate copy-pasteable remediation scripts | Must Have | 1 |
| FR-045 | Use Anthropic Claude API (not Gemini) | Must Have | 1 |
| FR-046 | Implement prompt caching to reduce AI costs | Should Have | 2 |
| FR-047 | Fallback to offline report if Claude API unavailable | Must Have | 1 |
| FR-048 | Gate remediation scripts behind paid tier (Freemium sees summary only) | Must Have | 2 |
| FR-049 | Include confidence score per AI-generated finding | Should Have | 2 |
| FR-050 | Map findings to MITRE ATT&CK technique ID + link | Should Have | 2 |
| FR-051 | Generate monthly executive summary reports (PDF/DOCX) | Should Have | 2 |
| FR-052 | Provide ATT&CK technique heatmap aggregated across findings | Should Have | 3 |

### 11.4 SOAR (FR-060–06A)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-060 | Ingest Wazuh alerts severity ≥10 | Must Have | 2 |
| FR-061 | Enrich alert IPs with threat intelligence (AbuseIPDB, OTX) | Must Have | 2 |
| FR-062 | Route enriched alerts through Claude AI triage (contain vs escalate) | Must Have | 2 |
| FR-063 | Auto-execute "CONTAIN" playbook for low-risk confirmed threats | Must Have | 2 |
| FR-064 | Route high-risk decisions to human approval queue with full context | Must Have | 2 |
| FR-065 | Support default playbooks: Ransomware Containment, SSH Brute-Force Block, Phishing Email Purge | Must Have | 2 |
| FR-066 | Allow Pro/Enterprise to define custom SOAR playbooks | Should Have | 3 |
| FR-067 | Send real-time notifications (email, Slack, SMS) for every incident | Must Have | 2 |
| FR-068 | Maintain full audit trail of all SOAR actions | Must Have | 2 |
| FR-069 | Allow human operators to approve/reject queued playbook execution | Must Have | 2 |
| FR-06A | Allow IT managers to mark Wazuh alerts as false positives + suppress rule for 30 days | Should Have | 2 |

### 11.5 Malware Detection & Response (FR-070–085)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-070 | Detect malware via Wazuh ClamAV on enrolled SOC Pro endpoints | Must Have | 2 |
| FR-071 | Detect malware via Wazuh File Integrity Monitoring (FIM) | Must Have | 2 |
| FR-072 | Detect web shells during L2 scans using Nuclei templates | Must Have | 2 |
| FR-073 | Detect malicious container layers via Trivy | Should Have | 3 |
| FR-074 | Enrich malware detections with VirusTotal lookup + local YARA rules | Must Have | 2 |
| FR-075 | Send every confirmed malware detection to Claude AI for analysis | Must Have | 2 |
| FR-076 | Claude determines: malware family, severity (1–10), lateral movement risk, data exfil likelihood | Must Have | 2 |
| FR-077 | Claude generates: quarantine command, removal command, persistence cleanup, IOC list, verification command | Must Have | 2 |
| FR-078 | AUTO-REMEDIATE when confidence >95% + isolated file/process (quarantine, kill, update blocklist) | Must Have | 2 |
| FR-079 | Route to HUMAN APPROVAL GATE when remediation affects core services, databases, or requires isolation | Must Have | 2 |
| FR-080 | Send immediate Slack + email + dashboard notification for malware detection | Must Have | 2 |
| FR-081 | Run post-remediation re-scan to confirm successful removal | Must Have | 2 |
| FR-082 | Generate malware incident report (family, affected files, actions, clean status) | Must Have | 2 |
| FR-083 | Update Workspace Health Score after confirmed malware remediation | Must Have | 2 |
| FR-084 | Restrict L8 to SOC Pro/Enterprise tiers only | Must Have | 2 |
| FR-085 | Maintain audit log of all quarantine/removal actions with actor, timestamp, hash | Must Have | 2 |

### 11.6 Dashboard & Reporting (FR-090–099)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-090 | Display real-time Workspace Health Score on dashboard | Must Have | 1 |
| FR-091 | Display total financial exposure in USD/GBP on dashboard | Must Have | 1 |
| FR-092 | Display prioritised vulnerability list ranked by financial impact | Must Have | 1 |
| FR-093 | Display historical scan results with 12-month health score trend | Should Have | 2 |
| FR-094 | Display compliance posture map (PCI-DSS, GDPR, ISO27001, SOC2, CE+) | Should Have | 2 |
| FR-095 | Allow users to download PDF executive reports | Should Have | 2 |
| FR-096 | Display incident feed for SOAR events | Must Have | 2 |
| FR-097 | Support white-label reporting (custom logo/brand) for Enterprise | Nice to Have | 3 |
| FR-098 | Display admin telemetry (COGS per scan, total cost, margin) for admin users | Must Have | 1 |
| FR-099 | Display anonymised industry benchmark comparison (opt-in tenants) | Should Have | 3 |

### 11.7 Billing (FR-100–106)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-100 | Integrate Stripe for subscription management + payment processing | Must Have | 2 |
| FR-101 | Automatically gate paid features based on subscription tier | Must Have | 2 |
| FR-102 | Send invoice emails via Stripe on successful payment | Must Have | 2 |
| FR-103 | Handle failed payments with 7-day grace period before service downgrade | Must Have | 2 |
| FR-104 | Provide self-service Stripe Customer Portal | Should Have | 2 |
| FR-105 | Calculate variable costs per scan + maintain per-tenant COGS records | Must Have | 1 |
| FR-106 | Prevent scans exceeding pre-set budget cap (configurable by admin) | Should Have | 3 |

---

## 12. API Specification

### 12.1 Base URLs

| Environment | URL | Status |
|---|---|---|
| Staging (MVP) | `https://api-staging.socvault.io/api/v1` | 🟢 Active |
| Production | `https://api.socvault.io/api/v1` | ⏸ Dormant |
| Local (dev) | `http://localhost:8000/api/v1` | 🟢 Dev |

### 12.2 Authentication

**All protected endpoints require Bearer JWT token from Cognito.**

```
Authorization: Bearer {access_token}
```

**Token TTL:**
- Access token: 15 minutes
- Refresh token: 30 days

### 12.3 Core Endpoints

#### Health

```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "version": "0.1.0-mvp",
  "environment": "staging"
}
```

#### Authentication

```http
POST /auth/signup
Content-Type: application/json

{
  "email": "jane@acmecorp.com",
  "phone": "+447700900123"
}
```

**Response (202 Accepted):**
```json
{
  "message": "OTP sent",
  "email": "jane@acmecorp.com"
}
```

---

```http
POST /auth/verify-otp
Content-Type: application/json

{
  "email": "jane@acmecorp.com",
  "otp": "482910"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 900,
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
}
```

---

```http
GET /auth/me
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "email": "jane@acmecorp.com",
  "workspace_domain": "acmecorp.com",
  "domain_verified": false,
  "tier": "free",
  "created_at": "2026-06-18T09:00:00Z",
  "last_login_at": "2026-06-18T10:15:00Z",
  "subscription_status": null
}
```

#### Scanning

```http
POST /scan/execute
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "layer": "RECON",
  "target": "acmecorp.com",
  "consent": true
}
```

**Response (202 Accepted):**
```json
{
  "scan_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "status": "QUEUED",
  "created_at": "2026-06-18T10:00:00Z",
  "estimated_duration_seconds": 90
}
```

---

```http
GET /scan/{scan_id}
Authorization: Bearer {access_token}
```

**Response (while running):**
```json
{
  "scan_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "status": "RUNNING",
  "progress_percent": 47,
  "started_at": "2026-06-18T10:00:00Z",
  "estimated_completion": "2026-06-18T10:01:30Z",
  "steps": [
    { "step": 1, "name": "WHOIS Lookup", "status": "COMPLETE", "duration_ms": 2100 },
    { "step": 2, "name": "DNS Analysis", "status": "COMPLETE", "duration_ms": 1800 },
    { "step": 3, "name": "Email Security", "status": "RUNNING", "duration_ms": 450 }
  ]
}
```

**Response (complete):**
```json
{
  "scan_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "status": "COMPLETE",
  "progress_percent": 100,
  "started_at": "2026-06-18T10:00:00Z",
  "completed_at": "2026-06-18T10:02:14Z",
  "executive_report": {
    "health_score": 68,
    "financial_exposure_usd": 142500,
    "summary": "Your external attack surface shows moderate risk...",
    "findings_count": 12,
    "remediation_count": 7
  },
  "cogs": {
    "compute_cost": 0.000002,
    "ai_token_cost": 0.18,
    "threat_intel_cost": 0.03,
    "total": 0.21
  }
}
```

#### Dashboard

```http
GET /dashboard/summary
Authorization: Bearer {access_token}
```

**Response:**
```json
{
  "health_score": 68,
  "financial_exposure_usd": 142500,
  "last_scan_at": "2026-06-18T10:00:00Z",
  "top_findings": [
    {
      "finding_id": "f1",
      "title": "SSL Certificate Expires in 15 Days",
      "severity": "high",
      "financial_impact_usd": 8500,
      "remediation_time_hours": 0.5
    }
  ],
  "tier_limits": {
    "scans_this_month": 1,
    "scans_limit": 1,
    "freemium_reset_date": "2026-07-01T00:00:00Z"
  }
}
```

#### Admin Telemetry

```http
GET /admin/telemetry
Authorization: Bearer {admin_token}
```

**Response:**
```json
{
  "platform_stats": {
    "active_tenants": 342,
    "total_scans": 8421,
    "total_scans_this_month": 1203
  },
  "unit_economics": {
    "total_cogs": 1842.33,
    "total_revenue": 23400.00,
    "blended_margin": 0.921,
    "avg_cogs_per_scan": 0.218,
    "avg_revenue_per_tenant": 68.42
  },
  "per_tenant_sample": [
    {
      "tenant_id": "...",
      "email": "jane@acmecorp.com",
      "tier": "soc_pro",
      "scans": 24,
      "cogs": 5.28,
      "revenue": 199.00,
      "margin": 0.973
    }
  ]
}
```

---

## 13. Technology Stack

### 13.1 Frontend

| Technology | Purpose |
|---|---|
| **React 18** | UI framework |
| **TypeScript** | Type safety |
| **Zustand** | State management (lightweight) |
| **shadcn/ui** | Component library (Tailwind-based) |
| **Tailwind CSS** | Styling + brand theme |
| **Recharts** | Financial risk visualization |
| **Axios + React Query** | API client + caching |
| **AWS Amplify** | Hosting + auth SDK |
| **AWS Amplify UI** | Pre-built auth components |

### 13.2 Backend

| Component | Technology | Purpose |
|---|---|---|
| **API Runtime** | AWS Lambda + FastAPI (Mangum) | Serverless sync handlers |
| **Task Queue (MVP)** | SQS + Lambda workers | Async scan execution |
| **Task Queue (paid)** | Redis + Celery on EKS | Long-running workers at scale |
| **Database (primary)** | MongoDB Atlas M0 (Motor) | Multi-tenant document store |
| **Database (cache)** | ElastiCache Redis (paid tier) | Session + rate limit cache |
| **Auth** | AWS Cognito | JWT + OTP validation |
| **Cost tracking** | DynamoDB | COGS ledger + per-tenant accounting |
| **File storage** | AWS S3 | Scan artifacts + tenant-scoped paths |
| **Notifications** | AWS SNS | OTP SMS + alerts |
| **Secrets** | SSM Parameter Store (MVP) → Secrets Manager (paid) | API keys, tokens |

### 13.3 AI & Intelligence

| Component | Technology | Purpose |
|---|---|---|
| **Financial risk translation** | Claude claude-sonnet-4-6 | CVE → financial exposure |
| **SOAR triage** | Claude claude-sonnet-4-6 | Incident routing |
| **Malware analysis** | Claude claude-sonnet-4-6 | Family ID, severity, remediation |
| **L9 autonomous** | Claude claude-opus-4-8 | Extended thinking assessment |
| **AI Chat** | Claude claude-sonnet-4-6 | Conversational assistant |
| **Fast triage** | Claude claude-haiku-4-5 | Cost-optimized enrichment |
| **Prompt caching** | Anthropic Prompt Caching API | 90% input token cost reduction |
| **Threat intelligence** | AbuseIPDB, AlienVault OTX, GreyNoise | IP reputation, threat actor data |

### 13.4 Scanning Tools

| Layer | Tools |
|---|---|
| **L1 Recon** | Subfinder, Naabu, httpx, sslyze, checkdmarc, crt.sh, HaveIBeenPwned, AbuseIPDB |
| **L2 Web AppSec** | Nuclei, OWASP ZAP, Semgrep, Trivy |
| **L3 Mobile** | MobSF, Trivy |
| **L4 API** | Nuclei API templates, OWASP ZAP API, Semgrep API |
| **L5 Compliance** | Custom Python engine, Prowler |
| **L6 Cloud** | CloudFox, Pacu, Prowler, Steampipe |
| **L7 SOC/SIEM** | Wazuh manager + agents |
| **L8 Malware** | ClamAV, YARA, Trivy, Nuclei webshell, custom signatures |

### 13.5 Infrastructure & DevOps

| Component | Technology | Purpose |
|---|---|---|
| **Container images** | Docker (for Lambda + EKS) | Scanner tool packaging |
| **MVP orchestration** | API Gateway + Lambda + SQS | Serverless-only until scale |
| **Paid orchestration** | Amazon EKS (Kubernetes) | Full platform scaling |
| **Scan offload (paid)** | ECS Fargate | Optional intermediate tier |
| **CI/CD** | GitHub Actions + Terraform | Lint, test, deploy staging |
| **IaC** | Terraform | All infrastructure (ADR-004) |
| **Monitoring** | CloudWatch | Metrics, logs, alarms |
| **CDN (paid)** | CloudFront | Edge cache for Amplify + API |
| **API Gateway** | HTTP API v2 | Routing + Cognito JWT authorizer |

### 13.6 Security & Compliance

| Control | Implementation |
|---|---|
| **Transport** | TLS 1.3 enforced; HSTS headers |
| **Auth** | Cognito JWT + refresh tokens; token TTLs per pool |
| **CORS** | Strict allowlist per environment; never `*` |
| **Input validation** | Pydantic v2 strict models on all API boundaries |
| **Scan isolation** | Lambda/Fargate per invocation; `tenant_id` on all data queries |
| **Secrets** | SSM (MVP) → Secrets Manager (paid); zero in git |
| **WAF (paid)** | AWS WAF + GuardDuty |
| **Penetration testing** | Quarterly self-scans using SOCVault's own platform |
| **Encryption at rest** | AES-256 (MongoDB, S3, DynamoDB, EBS) |
| **Audit logging** | CloudTrail for all API + infrastructure events |
| **RBAC** | Three-tier model: tenant user, admin, super admin (see ADR-003) |

---

## 14. Authentication & Security

### 14.1 Authentication Flow

```
User Signup
    │
    ▼
POST /auth/signup
├─ Extract domain from email
├─ Validate business domain (blocklist freemail)
├─ Generate OTP
├─ Send via SNS (or Mailhog in dev)
└─ Store provisional tenant record
    │
    ▼
User receives OTP
    │
    ▼
POST /auth/verify-otp
├─ Validate OTP (6-digit, TTL 10 min)
├─ Create Cognito user with custom `tenant_id` attribute
├─ Link MongoDB tenant record to Cognito user
├─ Issue JWT access + refresh tokens (Cognito-signed)
└─ Return tokens + tenant_id
    │
    ▼
Subsequent Requests
├─ Include `Authorization: Bearer {access_token}` header
├─ API Gateway Cognito authorizer validates JWT signature
├─ Lambda receives `tenant_id` from JWT claims
├─ All DB queries scoped by `tenant_id` (middleware)
└─ Response returned to authenticated user
```

### 14.2 RBAC Model

**Three separate access models (do not merge):**

#### Model 1: Tenant User RBAC

| Role | Permissions | Tier |
|---|---|---|
| **Owner** | All tenant actions; billing; invite sub-users; delete account | Any |
| **Admin** | Configure scans; view all findings; approve SOAR; manage integrations | Paid |
| **Analyst** | View findings; generate reports; approve SOAR (limited); no billing access | Paid |
| **Viewer** | Read-only access to dashboard; no scan triggers; no approvals | Paid |

#### Model 2: Admin/Internal RBAC

| Role | Permissions |
|---|---|
| **Super Admin** | All platform actions; telemetry; tenant management; system config |
| **Support** | View customer data; troubleshoot; cannot modify |
| **DevOps** | Infrastructure changes; deployments; monitoring |

#### Model 3: Wazuh Agent RBAC

| Role | Permissions |
|---|---|
| **Agent (per tenant)** | Send logs + alerts to SOAR ingestion; encrypted connection |
| **Manager (internal)** | Aggregate alerts; trigger Claude triage; dispatch playbooks |

### 14.3 Data Security

**Tenant Isolation:**
- Every MongoDB document: `tenant_id` partition key (indexed)
- Every API response: filtered by `tenant_id` from JWT
- Every S3 path: `s3://{bucket}/{tenant_id}/{resource_id}/`
- Every scan sandbox: isolated Lambda/Fargate invocation (no shared memory)

**Encryption:**
- **In Transit:** TLS 1.3 on all endpoints; CORS strict allowlist
- **At Rest:** AES-256 on MongoDB (application-level), S3 (KMS), DynamoDB (KMS), EBS (KMS)
- **Secrets:** SSM Parameter Store (MVP) → Secrets Manager (paid); KMS encryption for sensitive keys

**Audit Logging:**
- All API calls: CloudTrail
- All admin actions: SOCVault audit collection (MongoDB)
- All scan actions: per-scan log
- All SOAR actions: per-action audit with actor, timestamp, result

---

## 15. Data Model & Database Schema

### 15.1 MongoDB Collections

#### `tenants`

```json
{
  "_id": ObjectId,
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "email": "jane@acmecorp.com",
  "phone": "+447700900123",
  "workspace_domain": "acmecorp.com",
  "domain_verified": false,
  "domain_verification_token": "token_xyz",
  "tier": "free",  // free | web_vapt | mobile | cloud | soc_pro | soc_enterprise
  "subscription_stripe_id": "sub_...",
  "subscription_status": null,  // active | past_due | cancelled
  "subscription_renewal_date": null,
  "scans_this_month": 1,
  "wazuh_agents": 0,
  "created_at": ISODate("2026-06-18T09:00:00Z"),
  "updated_at": ISODate("2026-06-18T10:15:00Z"),
  "deleted_at": null,
  "metadata": {
    "country": "GB",
    "industry": "financial_services",
    "employees": 85,
    "annual_revenue_usd": 5000000
  }
}
```

#### `scans`

```json
{
  "_id": ObjectId,
  "scan_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "layer": "L1",  // L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9
  "target": "acmecorp.com",
  "status": "COMPLETE",  // QUEUED | RUNNING | COMPLETE | FAILED
  "progress_percent": 100,
  "initiated_by": "jane@acmecorp.com",
  "consent_given": true,
  "started_at": ISODate("2026-06-18T10:00:00Z"),
  "completed_at": ISODate("2026-06-18T10:02:14Z"),
  "raw_findings": {
    "step_1_whois": {...},
    "step_2_dns": {...},
    // ... all 15 L1 steps
  },
  "aggregated_findings": [
    {
      "finding_id": "f1",
      "step": 4,
      "severity": "high",  // critical | high | medium | low | info
      "title": "SSL Certificate Expires in 15 Days",
      "description": "...",
      "affected_asset": "www.acmecorp.com:443",
      "mitre_technique": "T1562.008",
      "financial_exposure_usd": 8500,
      "remediation_time_hours": 0.5,
      "remediation_script": "...",  // Paywalled for free tier
      "ai_generated": true,
      "confidence_score": 0.99
    }
  ],
  "executive_report": {
    "health_score": 68,
    "financial_exposure_usd": 142500,
    "summary": "Your external attack surface shows moderate risk...",
    "top_risks": [
      { "title": "SSL Certificate Expires in 15 Days", "impact": 8500 }
    ],
    "remediation_count": 7,
    "compliance_gaps": ["PCI-DSS 6.2", "ISO 27001 A.14.2"]
  },
  "ai_analysis": {
    "model": "claude-sonnet-4-6",
    "tokens_input": 2400,
    "tokens_output": 1200,
    "tokens_cached": 600,
    "cost_gbp": 0.18,
    "cache_hit": true,
    "latency_ms": 1240
  },
  "cogs": {
    "compute_cost": 0.000002,
    "ai_token_cost": 0.18,
    "threat_intel_cost": 0.03,
    "total": 0.21
  },
  "artifacts_s3": {
    "raw_output": "s3://socvault-artifacts/a1b2c3d4.../raw.json",
    "report_pdf": "s3://socvault-artifacts/a1b2c3d4.../report.pdf"
  },
  "error_message": null,
  "retry_count": 0
}
```

#### `findings`

```json
{
  "_id": ObjectId,
  "finding_id": "f1",
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "scan_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "title": "SSL Certificate Expires in 15 Days",
  "severity": "high",
  "financial_exposure_usd": 8500,
  "status": "open",  // open | acknowledged | remediated | false_positive
  "acknowledged_at": null,
  "acknowledged_by": null,
  "remediated_at": null,
  "remediated_by": null,
  "remediation_script": "...",
  "remediation_proof": null,  // Evidence of fix (screenshot, log, ticket #)
  "created_at": ISODate("2026-06-18T10:02:14Z"),
  "updated_at": ISODate("2026-06-18T10:02:14Z")
}
```

#### `incidents` (SOAR)

```json
{
  "_id": ObjectId,
  "incident_id": "inc-xyz",
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "wazuh_alert_id": "1234567890",
  "alert_name": "SSH Brute-Force Detected",
  "severity": 10,
  "source_ip": "203.0.113.45",
  "destination_ip": "10.0.1.100",
  "evidence": "10 failed login attempts in 5 minutes",
  "threat_intelligence": {
    "ip_reputation": "malicious",
    "abuse_ipdb_score": 98,
    "last_reported": "2026-06-17T15:00:00Z"
  },
  "ai_triage": {
    "decision": "CONTAIN",
    "reasoning": "Confirmed brute-force; high confidence malicious intent",
    "confidence": 0.96,
    "model": "claude-sonnet-4-6"
  },
  "status": "auto_remediated",  // awaiting_approval | auto_remediated | escalated | false_positive
  "assigned_playbook": "SSH_BRUTE_FORCE_BLOCK",
  "actions_executed": [
    {
      "step": 1,
      "action": "Add IP to firewall blocklist",
      "result": "success",
      "command": "iptables -A INPUT -s 203.0.113.45 -j DROP",
      "executed_at": ISODate("2026-06-18T10:15:30Z")
    }
  ],
  "notifications_sent": ["slack", "email", "sms"],
  "created_at": ISODate("2026-06-18T10:15:00Z"),
  "updated_at": ISODate("2026-06-18T10:16:00Z"),
  "closed_at": ISODate("2026-06-18T10:16:30Z")
}
```

#### `audit_log`

```json
{
  "_id": ObjectId,
  "tenant_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "actor": "jane@acmecorp.com",
  "action": "SCAN_INITIATED",  // SCAN_INITIATED | FINDING_REMEDIATED | SOAR_ACTION_APPROVED | etc.
  "resource_type": "scan",
  "resource_id": "7f3c2a1b-9e4d-4c8a-b2f1-6d5e4a3b2c1d",
  "details": {
    "layer": "L1",
    "target": "acmecorp.com",
    "reason": "User clicked 'Scan Now'"
  },
  "ip_address": "192.0.2.100",
  "user_agent": "Mozilla/5.0...",
  "timestamp": ISODate("2026-06-18T10:00:00Z")
}
```

### 15.2 DynamoDB Tables

#### `cost_telemetry`

Stores per-scan COGS data for admin reporting.

```
PK: tenant_id | SK: scan_id
├─ compute_cost: 0.000002
├─ ai_token_cost: 0.18
├─ threat_intel_cost: 0.03
├─ total: 0.21
└─ timestamp: 2026-06-18T10:02:14Z
```

#### `rate_limits`

Stores per-tenant + per-IP rate limit state.

```
PK: tenant_id | SK: endpoint_name#date
├─ requests_this_period: 42
├─ limit: 100
├─ reset_timestamp: 2026-07-01T00:00:00Z
└─ last_request_at: 2026-06-18T10:02:14Z
```

---

## 16. Deployment & Infrastructure

### 16.1 Environments

| Environment | Status | Database | API | Workers | Wazuh |
|---|---|---|---|---|---|
| **Staging (MVP)** | 🟢 Active | MongoDB Atlas M0 | Lambda + API GW | SQS + Lambda | EC2 (Phase 2+) |
| **Production** | ⏸ Dormant (until cutover) | Atlas prod cluster | Lambda + API GW | SQS + Lambda | EC2 (post-cutover) |

**MVP Principle (ADR-006):** Staging only. Production dormant until cutover checklist complete.

### 16.2 Terraform Structure

```
terraform/
├─ main.tf                  # Shared staging/prod configs
├─ variables.tf             # Input variables + defaults
├─ outputs.tf               # Outputs (API URL, bucket names, etc.)
├─ locals.tf                # Local values
├─ backend.tf               # S3 state + DynamoDB lock
├─ environments/
│  ├─ staging.tfvars       # Staging-specific values
│  └─ production.tfvars    # Production-specific values
├─ modules/
│  ├─ api_gateway/         # HTTP API + Lambda integration
│  ├─ lambda/              # Lambda functions (API, workers)
│  ├─ cognito/             # User pool + auth config
│  ├─ rds/                 # (N/A — using MongoDB Atlas)
│  ├─ s3/                  # Artifact buckets + scan data
│  ├─ dynamodb/            # Cost telemetry, rate limits
│  ├─ sqs/                 # Scan job queue
│  ├─ sns/                 # OTP + alerts
│  ├─ amplify/             # Frontend hosting
│  ├─ ssm/                 # Parameter store for secrets
│  ├─ cloudwatch/          # Monitoring + alarms
│  └─ vpc/                 # VPC (future — on demand for Wazuh EC2)
└─ README.md
```

### 16.3 CI/CD Pipeline

**GitHub Actions Workflows:**

```
.github/workflows/
├─ ci.yml                  # Lint + unit tests (on PR/push main)
├─ deploy-staging.yml      # Deploy to staging (on push main)
├─ qa-staging.yml          # Run automated QA on staging (after deploy)
└─ deploy-production.yml   # Deploy to production (on tag + approval)
```

**Staging Deploy Pipeline:**
```
Push to main
  ↓
[ci.yml] Lint + Unit Tests (pass required)
  ↓
[deploy-staging.yml] Apply Terraform → Update Lambda/Amplify
  ↓
[qa-staging.yml] Run automated QA (Bruno + custom tests)
  ↓
✓ Staging live or ✗ Blocks deployment on QA failure
```

### 16.4 Monitoring & Observability

| Tool | Purpose |
|---|---|
| **CloudWatch** | API latency, Lambda errors, DynamoDB throttles, Lambda duration distribution |
| **CloudTrail** | All API calls + infrastructure changes (compliance audit trail) |
| **X-Ray** | Lambda service map + request tracing (optional — Phase 2) |
| **Custom metrics** | Scan completion rate, COGS per layer, conversion funnel metrics |

---

## 17. User Tiers & Feature Gates

### 17.1 Tier Comparison Matrix

| Feature | Free | Web VAPT | Mobile | Cloud | SOC Pro | SOC Ent |
|---|---|---|---|---|---|---|
| **Price/month** | $0 | $15 | $20 | $25 | $199 | $499 |
| **Price/year** | — | $180 | $240 | $300 | $2,388 | $5,988 |
| **Recon scans** | 1/mo | ∞ | ∞ | ∞ | ∞ | ∞ |
| **L2 Web AppSec** | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **L3 Mobile** | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |
| **L4 API** | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| **L5 Compliance** | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| **L6 Cloud** | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ |
| **L7 SIEM** | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| **L8 Malware D&R** | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| **Remediation scripts** | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Financial risk translation** | ✓ Summary only | ✓ | ✓ | ✓ | ✓ | ✓ |
| **SOAR playbooks** | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| **Wazuh agents** | — | — | — | — | 50 | ∞ |
| **Team members** | 1 | 2 | 3 | 4 | 10 | ∞ |
| **Custom playbooks** | ✗ | ✗ | ✗ | ✗ | Phase 2 | Phase 2 |
| **White-label** | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Custom SLA** | — | — | — | — | 8h | 4h |
| **API access** | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| **Priority support** | No | Email only | Email | Email | Chat + Email | 24/7 phone |

### 17.2 Feature Gate Logic

```python
# Pseudocode for tier-based feature access

class FeatureGate:
    
    def can_scan(tenant: Tenant, layer: str) -> bool:
        if layer == "L1":
            return True  # All tiers can scan L1 after domain verification
        elif layer in ["L2", "L3", "L4", "L5", "L6"]:
            return tenant.tier in ["web_vapt", "mobile", "cloud", "soc_pro", "soc_enterprise"]
        elif layer in ["L7", "L8"]:
            return tenant.tier in ["soc_pro", "soc_enterprise"]
        else:
            return False
    
    def can_see_remediation_scripts(tenant: Tenant) -> bool:
        return tenant.tier != "free"
    
    def wazuh_agent_limit(tenant: Tenant) -> int:
        if tenant.tier == "soc_pro":
            return 50
        elif tenant.tier == "soc_enterprise":
            return None  # Unlimited
        else:
            return 0
```

---

## 18. Compliance & Data Protection

### 18.1 Regulatory Compliance

| Regulation | Implementation |
|---|---|
| **GDPR** | DPA template provided; UK data residency (AWS eu-west-2); data deletion mechanism (FR-042) |
| **UK Data Protection Act 2018** | Privacy policy + processing terms; audit trail (3-year retention) |
| **PCI-DSS** (if processing cards) | Stripe-only integration; no direct card storage |
| **ISO 27001** | Compliance gap analysis module (L5) maps findings to controls |
| **SOC2 Type II** | Target for Phase 3 (post-launch) |
| **Cyber Essentials+** | Compliance mapping on dashboard; self-scan coverage |

### 18.2 Data Residency & Retention

| Data Type | Location | Retention |
|---|---|---|
| **Tenant scan results** | AWS eu-west-2 (London) — EU customers | 12 months (configurable) |
| **Audit logs** | AWS eu-west-2 | 3 years (compliance requirement) |
| **Backup** | AWS eu-west-2 + cross-region | 30-day retention |
| **Deleted tenant data** | Hard delete within 30 days of erasure request | FR-042 |

### 18.3 Security Controls

| Control | Level | Implementation |
|---|---|---|
| **Access control** | Preventive | Cognito RBAC + API Gateway + tenant_id middleware |
| **Encryption** | Preventive | TLS 1.3 + AES-256 at rest (KMS) |
| **Authentication** | Preventive | JWT + refresh token rotation; MFA for admin |
| **Intrusion detection** | Detective | CloudWatch + GuardDuty (paid tier) |
| **Incident response** | Responsive | Automated SOAR playbooks + manual escalation queue |
| **Audit trail** | Detective | CloudTrail + MongoDB audit collection |
| **Vulnerability scanning** | Preventive | Quarterly self-scans using SOCVault (FR-029) |
| **Penetration testing** | Preventive | Annual external pentest (Phase 3) |

---

## 20. Admin Setup Roadmap & GitHub Projects

### 20.1 Admin Setup Phases & Milestones

SOCVault development begins with **complete admin infrastructure** before user-facing features. This ensures secure tenant management, monitoring, and operational control from day one.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                   SOCVault Admin Setup Roadmap                          │
│                   (Foundation for All Modules)                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  PHASE 0: ADMIN INFRASTRUCTURE (Weeks 1–3)                             │
│  ├─ [M0.1] AWS Account Setup & IAM Configuration                       │
│  ├─ [M0.2] Terraform IaC Foundation                                    │
│  ├─ [M0.3] Database Setup (MongoDB, DynamoDB)                          │
│  ├─ [M0.4] Secrets Management (AWS Secrets Manager)                    │
│  ├─ [M0.5] Monitoring & Alerting (CloudWatch)                          │
│  └─ [M0.6] Admin API Skeleton (Cognito + FastAPI)                      │
│              Status: ⚪ Not Started                                     │
│                                                                         │
│  PHASE 1A: ADMIN CORE (Weeks 4–6)                                      │
│  ├─ [M1.1] Super Admin User Management (Create/List/Disable)           │
│  ├─ [M1.2] Tenant Management (Create/Suspend/Delete tenants)           │
│  ├─ [M1.3] Admin Dashboard (Overview, metrics, health)                 │
│  ├─ [M1.4] Audit Log Viewer (CloudTrail + MongoDB)                     │
│  ├─ [M1.5] System Settings (Rate limits, feature flags)                │
│  └─ [M1.6] Admin API Documentation (OpenAPI)                           │
│              Status: ⚪ Not Started                                     │
│                                                                         │
│  PHASE 1B: SECURITY & COMPLIANCE (Weeks 7–8)                           │
│  ├─ [M1.7] Admin Authentication (2FA, IP whitelist)                    │
│  ├─ [M1.8] Role-Based Access Control (Admin/Operator/Viewer)           │
│  ├─ [M1.9] Compliance Dashboard (GDPR, PCI-DSS, ISO 27001)             │
│  ├─ [M1.10] Audit Trail (All admin actions logged)                     │
│  ├─ [M1.11] Security Events (Login attempts, permission changes)       │
│  └─ [M1.12] Admin Portal UI (React dashboard)                          │
│              Status: ⚪ Not Started                                     │
│                                                                         │
│  PHASE 2: ADVANCED ADMIN (Weeks 9–10)                                  │
│  ├─ [M2.1] Billing & Subscription Management                           │
│  ├─ [M2.2] Usage Analytics & Reporting                                 │
│  ├─ [M2.3] Tenant Health Monitoring                                    │
│  ├─ [M2.4] Backup & Recovery Management                                │
│  └─ [M2.5] Admin Automation & Scheduled Jobs                           │
│              Status: ⚪ Planned                                         │
│                                                                         │
│  PHASE 3+: USER-FACING MODULES (After admin complete)                  │
│  ├─ Tenant signup & onboarding                                         │
│  ├─ User management                                                    │
│  ├─ Scanning engine                                                    │
│  └─ Dashboard & reporting                                              │
│              Status: ⚪ Blocked (awaits admin completion)              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Timeline**: Weeks 1–10 for admin foundation before any user-facing features

---

### 20.2 GitHub Projects Setup for Admin Module

#### 20.2.1 Create Project & Milestones

**GitHub Projects Board: SOCVault - Admin Setup**

**Columns:**
1. 📋 **Backlog** — Issues not yet started
2. 🔄 **In Progress** — Assigned to engineer, actively developed
3. 🧪 **In Review** — PR opened, awaiting approval
4. ✅ **Done (Sprint)** — Completed this sprint
5. 📊 **Done (All Time)** — Historical completed issues

**Milestones to Create:**
```
M0.1: AWS Account Setup & IAM              (target: Week 1)
M0.2: Terraform IaC Foundation             (target: Week 1-2)
M0.3: Database Setup                       (target: Week 2)
M0.4: Secrets Management                   (target: Week 2-3)
M0.5: Monitoring & Alerting                (target: Week 3)
M0.6: Admin API Skeleton                   (target: Week 3)
M1.1: Super Admin User Management          (target: Week 4)
M1.2: Tenant Management                    (target: Week 4-5)
M1.3: Admin Dashboard                      (target: Week 5)
M1.4: Audit Log Viewer                     (target: Week 5-6)
M1.5: System Settings                      (target: Week 6)
M1.6: Admin API Documentation              (target: Week 6)
M1.7: Admin Authentication (2FA)           (target: Week 7)
M1.8: RBAC (Admin/Operator/Viewer)        (target: Week 7)
M1.9: Compliance Dashboard                 (target: Week 7-8)
M1.10: Audit Trail                         (target: Week 8)
M1.11: Security Events                     (target: Week 8)
M1.12: Admin Portal UI                     (target: Week 8)
```

---

### 20.3 Admin Module User Stories (Phase 0)

#### Milestone M0.1: AWS Account Setup & IAM Configuration

**US-ADM-001: Create AWS Organization & Accounts**

```markdown
### US-ADM-001: Create AWS Organization & Accounts

**As a** DevOps Engineer  
**I want to** set up AWS organization with separate accounts for staging/production  
**So that** we have proper cost allocation and blast radius containment

**Acceptance Criteria:**
- [ ] AWS Organization created with billing consolidated in root account
- [ ] Staging account created (eu-west-2 region)
- [ ] Production account created (eu-west-2 region)
- [ ] Cross-account roles configured (AssumeRole from primary account)
- [ ] CloudTrail enabled across all accounts
- [ ] Billing alerts configured ($1,000 daily threshold)
- [ ] AWS SSO configured with IAM users from root account

**Technical Details:**
- Use AWS Organizations API (not Management Console)
- Enable AWS CloudFormation StackSets for cross-account deployments
- Document account IDs in `.env.terraform`
- Store account ARNs in AWS Secrets Manager

**Assigned To:** DevOps Agent  
**Labels:** `infrastructure` `aws` `phase-0` `blocking`  
**Milestone:** M0.1  
**Story Points:** 5  
**Priority:** CRITICAL
```

**US-ADM-002: Set Up IAM Roles & Policies**

```markdown
### US-ADM-002: Set Up IAM Roles & Policies

**As a** Security Engineer  
**I want to** configure IAM roles with principle of least privilege  
**So that** all system access follows security best practices

**Acceptance Criteria:**
- [ ] GitHub Actions role created (permissions: Lambda deploy, ECR push, Terraform apply)
- [ ] Terraform execution role created (permissions: all AWS services needed)
- [ ] Admin user role created (permissions: read-only + admin console access)
- [ ] Operator role created (permissions: read, scan execution, logs)
- [ ] Viewer role created (permissions: read-only)
- [ ] All roles enforce MFA for console access
- [ ] All roles have 1-hour session duration
- [ ] All role assumptions logged to CloudTrail

**Terraform Code Required:**
```
modules/iam/github-actions-role.tf
modules/iam/terraform-role.tf
modules/iam/admin-role.tf
modules/iam/operator-role.tf
modules/iam/viewer-role.tf
```

**Assigned To:** DevOps Agent  
**Labels:** `infrastructure` `security` `iam` `phase-0`  
**Milestone:** M0.1  
**Story Points:** 8  
**Blocks:** M0.2, M0.3, M0.6
```

**US-ADM-003: Configure VPC with Multi-AZ Network**

```markdown
### US-ADM-003: Configure VPC with Multi-AZ Network

**As a** DevOps Engineer  
**I want to** set up VPC with public/private subnets across 2 AZs  
**So that** we have high availability and proper network isolation

**Acceptance Criteria:**
- [ ] VPC created (CIDR: 10.0.0.0/16)
- [ ] 2 public subnets (10.0.1.0/24, 10.0.2.0/24) in AZ-a, AZ-b
- [ ] 2 private subnets (10.0.10.0/24, 10.0.11.0/24) in AZ-a, AZ-b
- [ ] 1 NAT Gateway in each AZ (public subnet)
- [ ] Internet Gateway configured
- [ ] Route tables configured (public → IGW, private → NAT)
- [ ] Security groups defined (ALB, Lambda, RDS)
- [ ] Network ACLs reviewed

**Terraform Modules:**
```
terraform/modules/vpc/
├── main.tf
├── subnets.tf
├── nat-gateway.tf
├── security-groups.tf
└── variables.tf
```

**Assigned To:** DevOps Agent  
**Labels:** `infrastructure` `networking` `phase-0`  
**Milestone:** M0.1  
**Story Points:** 13  
**Blocks:** M0.3, M0.5
```

#### Milestone M0.2: Terraform IaC Foundation

**US-ADM-004: Initialize Terraform Project with Remote State**

```markdown
### US-ADM-004: Initialize Terraform Project with Remote State

**As a** DevOps Engineer  
**I want to** set up Terraform with S3 backend and DynamoDB lock  
**So that** infrastructure state is secure and team changes are coordinated

**Acceptance Criteria:**
- [ ] Terraform project initialized in `terraform/` folder
- [ ] S3 backend bucket created (versioning, encryption, public access blocked)
- [ ] DynamoDB table created for state locking
- [ ] Backend configuration in `terraform/backend.tf`
- [ ] `.terraformignore` configured
- [ ] `terraform.tfvars` gitignored but `.tfvars.example` committed
- [ ] Workspaces created: `staging`, `production`
- [ ] All Terraform files validated (fmt, validate)

**File Structure:**
```
terraform/
├── backend.tf
├── main.tf
├── variables.tf
├── outputs.tf
├── locals.tf
├── terraform.tfvars (gitignored)
├── terraform.tfvars.example
├── staging.tfvars
├── production.tfvars
├── .gitignore
├── .terraformignore
└── modules/
    ├── vpc/
    ├── lambda/
    ├── apigateway/
    ├── cognito/
    ├── rds/
    ├── dynamodb/
    ├── s3/
    ├── sqs/
    ├── sns/
    ├── iam/
    ├── cloudwatch/
    └── secrets/
```

**Assigned To:** DevOps Agent  
**Labels:** `infrastructure` `terraform` `phase-0`  
**Milestone:** M0.2  
**Story Points:** 5  
**Depends On:** US-ADM-002
```

#### Milestone M0.3: Database Setup

**US-ADM-005: Set Up MongoDB Atlas Cluster**

```markdown
### US-ADM-005: Set Up MongoDB Atlas Cluster

**As a** Backend Engineer  
**I want to** configure MongoDB Atlas cluster with proper security  
**So that** we have a scalable, secure primary data store

**Acceptance Criteria:**
- [ ] MongoDB Atlas M0 cluster created (eu-west-2, 3-node replica set)
- [ ] Database user created (strong password, least privilege)
- [ ] IP whitelist configured (restrict to AWS security group)
- [ ] Encryption at rest enabled (AWS KMS)
- [ ] Encryption in transit enabled (TLS 1.3)
- [ ] Automatic backups configured (daily, 30-day retention)
- [ ] Monitoring enabled (alerts on CPU, memory, connections)
- [ ] Connection string stored in AWS Secrets Manager
- [ ] Test connection from staging Lambda succeeds

**Connection String Pattern:**
```
mongodb+srv://socvault-user:${PASSWORD}@cluster0.mongodb.net/socvault?retryWrites=true&w=majority&tls=true
```

**Database Collections (initial schema):**
- `tenants` (tenant registry)
- `users` (user accounts)
- `scans` (scan records)
- `findings` (vulnerability findings)
- `incidents` (security incidents)
- `audit_log` (all admin actions)

**Assigned To:** Backend Agent  
**Labels:** `database` `mongodb` `phase-0` `blocking`  
**Milestone:** M0.3  
**Story Points:** 8
```

**US-ADM-006: Create DynamoDB Tables**

```markdown
### US-ADM-006: Create DynamoDB Tables

**As a** Backend Engineer  
**I want to** set up DynamoDB for high-write telemetry  
**So that** we can track costs and rate limits without MongoDB write overhead

**Acceptance Criteria:**
- [ ] `cost_telemetry` table created (partition key: `tenant_id`, sort key: `timestamp`)
- [ ] `rate_limits` table created (partition key: `tenant_id`, sort key: `endpoint`)
- [ ] TTL configured (cost_telemetry: 90 days, rate_limits: 1 day)
- [ ] Encryption enabled (AWS KMS)
- [ ] Provisioned capacity: read 10, write 100 (scale for Phase 2)
- [ ] Backup enabled (point-in-time recovery)
- [ ] CloudWatch alarms configured (throttles, latency)
- [ ] Tables accessible from Lambda security group

**Terraform Modules:**
```
terraform/modules/dynamodb/
├── cost-telemetry.tf
├── rate-limits.tf
└── variables.tf
```

**Assigned To:** DevOps Agent  
**Labels:** `database` `dynamodb` `phase-0`  
**Milestone:** M0.3  
**Story Points:** 5
```

#### Milestone M0.4: Secrets Management

**US-ADM-007: Configure AWS Secrets Manager**

```markdown
### US-ADM-007: Configure AWS Secrets Manager

**As a** Security Engineer  
**I want to** centralize all secrets in AWS Secrets Manager  
**So that** secrets are encrypted, rotatable, and auditable

**Acceptance Criteria:**
- [ ] Secrets Manager KMS key created (staging + production)
- [ ] Secrets created and stored:
  - `socvault/staging/db-connection-string`
  - `socvault/staging/cognito-client-secret`
  - `socvault/staging/stripe-api-key`
  - `socvault/staging/claude-api-key`
  - `socvault/staging/github-token`
  - `socvault/staging/mailgun-api-key`
- [ ] Automatic rotation enabled for database passwords (90 days)
- [ ] Lambda execution role can read secrets (KMS decrypt permission)
- [ ] Secrets tagged by environment, application, team
- [ ] CloudTrail logging enabled for secret access
- [ ] No secrets in Git history (scanned with GitGuardian)

**Assigned To:** DevOps Agent  
**Labels:** `security` `secrets` `phase-0` `blocking`  
**Milestone:** M0.4  
**Story Points:** 5  
**Depends On:** US-ADM-002
```

#### Milestone M0.5: Monitoring & Alerting

**US-ADM-008: Configure CloudWatch Dashboards & Alarms**

```markdown
### US-ADM-008: Configure CloudWatch Dashboards & Alarms

**As a** DevOps Engineer  
**I want to** set up comprehensive monitoring across all infrastructure  
**So that** we can detect and respond to issues quickly

**Acceptance Criteria:**
- [ ] CloudWatch dashboard created (SOCVault-Staging) with:
  - API Gateway: Request count, latency (p50, p95, p99), error rate
  - Lambda: Invocations, duration, errors, throttles, cost
  - MongoDB: Connections, operations, latency
  - DynamoDB: Read/write capacity, throttles
  - RDS: CPU, memory, connections, replication lag
- [ ] Alarms configured:
  - API error rate > 1% → SNS → Slack #incidents
  - Lambda duration > 30s → SNS → Slack #performance
  - DynamoDB throttles > 0 → SNS → Slack #performance
  - MongoDB connections > 80% → SNS → email
  - Costs > daily budget → SNS → email
- [ ] Log groups configured (30-day retention)
- [ ] Metric filters created (custom metrics)

**Terraform Code Required:**
```
terraform/modules/cloudwatch/
├── dashboard.tf
├── alarms.tf
├── log-groups.tf
└── sns-topics.tf
```

**Assigned To:** DevOps Agent  
**Labels:** `monitoring` `observability` `phase-0`  
**Milestone:** M0.5  
**Story Points:** 8
```

#### Milestone M0.6: Admin API Skeleton

**US-ADM-009: Initialize FastAPI Admin API Project**

```markdown
### US-ADM-009: Initialize FastAPI Admin API Project

**As a** Backend Engineer  
**I want to** set up FastAPI project with basic structure  
**So that** we have a foundation for admin endpoints

**Acceptance Criteria:**
- [ ] FastAPI project initialized in `backend/`
- [ ] `requirements.txt` includes: FastAPI, Uvicorn, Motor, Pydantic, pytest
- [ ] `main.py` created with FastAPI app initialization
- [ ] `config.py` created with environment-based configuration
- [ ] CORS configured (staging: localhost, production: admin.socvault.io)
- [ ] Request/response logging configured
- [ ] Health check endpoint (`GET /health`) working
- [ ] Dockerfile created (Lambda-compatible)
- [ ] pytest structure set up (`tests/unit/`, `tests/integration/`)
- [ ] GitHub Actions workflow can build and test

**File Structure:**
```
backend/
├── app/
│  ├── main.py
│  ├── config.py
│  ├── api/
│  ├── schemas/
│  ├── services/
│  ├── db/
│  └── security/
├── tests/
├── requirements.txt
├── Dockerfile.api
├── pytest.ini
└── pyproject.toml
```

**Assigned To:** Backend Agent  
**Labels:** `backend` `api` `phase-0` `blocking`  
**Milestone:** M0.6  
**Story Points:** 5  
**Depends On:** US-ADM-004
```

---

### 20.4 Admin Module User Stories (Phase 1A)

#### Milestone M1.1: Super Admin User Management

**US-ADM-010: Implement POST /admin/users (Create Super Admin)**

```markdown
### US-ADM-010: Implement POST /admin/users

**As a** Super Admin  
**I want to** create new super admin users  
**So that** I can delegate admin responsibilities

**Acceptance Criteria:**
- [ ] Endpoint `POST /admin/users` implemented
- [ ] Request validates: email, full_name, role, 2fa_enabled
- [ ] User created in Cognito (temporary password sent via email)
- [ ] User record created in MongoDB (admins collection)
- [ ] 2FA enforced for console access
- [ ] Audit log entry created (who created user, when)
- [ ] Response includes: user_id, email, created_at
- [ ] Integration test verifies user can log in after email confirmation

**Request Schema:**
```json
{
  "email": "admin@example.com",
  "full_name": "Admin User",
  "role": "SUPER_ADMIN",
  "2fa_enabled": true
}
```

**Assigned To:** Backend Agent  
**Labels:** `backend` `admin-users` `phase-1a`  
**Milestone:** M1.1  
**Story Points:** 8
```

#### Milestone M1.2: Tenant Management

**US-ADM-011: Implement POST /admin/tenants (Create Tenant)**

```markdown
### US-ADM-011: Implement POST /admin/tenants

**As a** Super Admin  
**I want to** create new tenants  
**So that** new customers can access SOCVault

**Acceptance Criteria:**
- [ ] Endpoint `POST /admin/tenants` implemented
- [ ] Request validates: company_name, industry, tier, contact_email
- [ ] Tenant created in MongoDB (tenants collection)
- [ ] Stripe customer created if paid tier
- [ ] Tenant ID (UUID) generated
- [ ] Default rate limits set based on tier
- [ ] Audit log entry created
- [ ] Response includes: tenant_id, api_key, webhook_secret
- [ ] Integration test creates tenant and verifies in DB

**Request Schema:**
```json
{
  "company_name": "ACME Corp",
  "industry": "Manufacturing",
  "tier": "free",
  "contact_email": "contact@acme.com",
  "country": "GB"
}
```

**Assigned To:** Backend Agent  
**Labels:** `backend` `tenant-management` `phase-1a`  
**Milestone:** M1.2  
**Story Points:** 13
```

#### Milestone M1.3: Admin Dashboard

**US-ADM-012: Create Admin Dashboard React Component**

```markdown
### US-ADM-012: Create Admin Dashboard UI

**As a** Admin User  
**I want to** see system overview on dashboard  
**So that** I can monitor platform health at a glance

**Acceptance Criteria:**
- [ ] Dashboard component created in React
- [ ] Displays: total tenants, active users, scans today, revenue, API uptime
- [ ] Real-time metrics updated every 10 seconds
- [ ] Charts: tenant growth (7-day), revenue trend (30-day), scan volume
- [ ] Top alerts section (critical issues)
- [ ] Quick actions (create tenant, view audit log)
- [ ] Responsive design (mobile, tablet, desktop)
- [ ] Jest tests cover all sections
- [ ] Storybook stories created

**Components:**
- DashboardMetricsCard (reusable metric display)
- SystemHealthIndicator (API, DB, Lambda status)
- AlertsPanel (critical issues list)
- RevenueChart (Recharts)
- TenantGrowthChart (Recharts)

**Assigned To:** Frontend Agent  
**Labels:** `frontend` `admin-dashboard` `phase-1a`  
**Milestone:** M1.3  
**Story Points:** 13
```

#### Milestone M1.4: Audit Log Viewer

**US-ADM-013: Implement GET /admin/audit-logs with Filtering**

```markdown
### US-ADM-013: Implement Audit Log Viewer

**As a** Compliance Officer  
**I want to** search and filter audit logs  
**So that** I can prove regulatory compliance

**Acceptance Criteria:**
- [ ] Endpoint `GET /admin/audit-logs` with filters: date range, user, action, resource
- [ ] Pagination: 50 records per page
- [ ] Export to CSV (timestamp, actor, action, resource)
- [ ] Frontend: React table with sorting, filtering, pagination
- [ ] Audit log data immutable (only append)
- [ ] Integration test queries MongoDB audit_log
- [ ] E2E test: Filter by date range, export CSV

**Assigned To:** Backend Agent (API) + Frontend Agent (UI)  
**Labels:** `backend` `frontend` `audit-logs` `phase-1a`  
**Milestone:** M1.4  
**Story Points:** 13
```

#### Milestone M1.5: System Settings

**US-ADM-014: Implement GET/PUT /admin/settings**

```markdown
### US-ADM-014: System Settings Management

**As a** Super Admin  
**I want to** manage global settings  
**So that** I can control system behavior

**Acceptance Criteria:**
- [ ] Endpoint `GET /admin/settings` returns current settings
- [ ] Endpoint `PUT /admin/settings` updates settings (super admin only)
- [ ] Settings stored in MongoDB, cached in Redis (5-min TTL)
- [ ] Audit log entry on every change
- [ ] Settings include: global rate limits, feature flags, maintenance mode
- [ ] All changes logged and auditable

**Assigned To:** Backend Agent  
**Labels:** `backend` `admin-settings` `phase-1a`  
**Milestone:** M1.5  
**Story Points:** 8
```

#### Milestone M1.6: Admin API Documentation

**US-ADM-015: Create Complete Admin API OpenAPI Specification**

```markdown
### US-ADM-015: Document Admin API (OpenAPI)

**As a** Backend Engineer  
**I want to** maintain OpenAPI spec  
**So that** API consumers know exact endpoint contracts

**Acceptance Criteria:**
- [ ] OpenAPI 3.1 spec created at `api/openapi-admin.yaml`
- [ ] All endpoints documented (methods, paths, request/response)
- [ ] All schemas defined (User, Tenant, AuditLog, etc.)
- [ ] All status codes documented
- [ ] Authentication scheme documented (Bearer JWT)
- [ ] Rate limit headers documented
- [ ] Example requests/responses for each endpoint
- [ ] Swagger UI at `GET /admin/api/docs`
- [ ] ReDoc at `GET /admin/api/redoc`

**Assigned To:** Backend Agent  
**Labels:** `backend` `documentation` `openapi` `phase-1a`  
**Milestone:** M1.6  
**Story Points:** 5
```

---

### 20.5 Admin Success Criteria

Admin module is **COMPLETE & PRODUCTION-READY** when:
- ✅ All Phase 0 milestones (M0.1–M0.6) **green** with passing tests
- ✅ All Phase 1A milestones (M1.1–M1.6) **green** with passing tests
- ✅ 100+ automated tests passing (unit + integration)
- ✅ All 15 user stories completed with acceptance criteria met
- ✅ API fully documented (OpenAPI spec + Swagger UI)
- ✅ GitHub Projects board auto-syncing all issues
- ✅ All CI/CD checks passing (linting, types, security, tests)
- ✅ Admin portal deployed to staging (https://admin-staging.socvault.io)
- ✅ Security scan: 0 CRITICAL, <5 HIGH vulnerabilities
- ✅ Code coverage: >80%
- ✅ Production admin account ready for deployment

**Next Steps After Admin Complete:**
1. Phase 1B: Security & Compliance (M1.7–M1.12)
2. Phase 2: Advanced Admin (M2.1–M2.5)
3. Phase 3+: User-facing modules (Tenant signup, scanning engine, etc.)

---

## 19. Development Roadmap

### 19.1 Phased Delivery

| Phase | Duration | Goal | Status |
|---|---|---|---|
| **Phase 0** | Weeks 1–4 | AWS staging + IaC + CI/CD | 🔴 Not started |
| **Phase 1** | Weeks 5–16 | Auth + L1 + Claude + dashboard (staging MVP) | 🔴 Not started |
| **Phase 2** | Weeks 17–24 | Payments, SOAR, L2–L8, beta users | 🔴 Planned |
| **Phase 3** | Weeks 25–36 | Public launch + GTM | 🔴 Planned |
| **Phase 4** | Weeks 37–52 | Scale + enterprise tier + compliance | 🔴 Planned |
| **Phase 5** | Year 2+ | International expansion + Series A | 🔴 Planned |

### 19.2 Key Milestones

| Milestone | Target | Status |
|---|---|---|
| **0.1** | AWS staging + CI/CD ready | 🔴 |
| **1.1** | Authentication & onboarding live | 🔴 |
| **1.2** | Scanning engine (L1) complete | 🔴 |
| **1.3** | Claude AI integration complete | 🔴 |
| **1.4** | Dashboard live | 🔴 |
| **2.1** | Payments (Stripe) integrated | 🔴 |
| **2.2** | SOAR playbooks live | 🔴 |
| **2.9** | API Explorer + Pass & Keys | 🔴 |
| **3.0** | Public launch (api.socvault.io) | 🔴 |

---

## 20. Competitive Advantage & USPs

### 20.1 Why SOCVault Wins

| Competitor | Advantage Over Them |
|---|---|
| **Intruder.io** | 8 layers vs 1–2; AI financial translation; SOAR; $101→$15/mo |
| **Detectify** | 8 layers vs web-only; AI financial translation; $89→$15/mo |
| **Guardz** | Unified scanning (not fragmented); AI financial translation; lower price |
| **Todyl** | AI financial risk; SOAR automation; better UX |
| **Tenable/Qualys** | **93% cheaper** ($199/mo vs $3,000+); AI translation; SMB focus; no implementation project |

### 20.2 Three-Layer Moat

**Layer 1 — Surface Differentiation**
- Freemium with real scans (competitors: trial-only or no free tier)
- 60-second onboarding (competitors: procurement contracts)
- Plain-English financial risk reports (competitors: raw CVSS scores)

**Layer 2 — Structural Differentiation**
- AI-powered financial translation built into every finding (proprietary prompt)
- 8-layer unified attack surface vs fragmented point solutions
- SOAR at SMB price ($199/mo vs $5,000+ enterprise SOAR)

**Layer 3 — Compounding Advantage**
- Proprietary scan corpus (customer finding database → training data)
- Compliance history switching cost (once mapped to PCI-DSS/GDPR, hard to abandon)
- Network threat intelligence (customer threat signals → collective defense)

---

## 21. Key Metrics & Success Criteria

### 21.1 Business Metrics

| Metric | Phase 1 Target | Phase 2 Target | Phase 3 Target |
|---|---|---|---|
| **Active tenants** | 50 free | 150 paying | 500+ paying |
| **MRR** | $0 | $10,000 | $50,000 |
| **ARR** | $0 | $120,000 | $600,000 |
| **Free-to-paid conversion** | 12% (standard SaaS) | 15% | 18% |
| **CAC** | $20–50 | $15–30 | $10–20 |
| **LTV** | $300–600 | $600–1,200 | $1,500+ |
| **Churn** | <5% (new product) | <3% | <2% |
| **NPS** | >40 | >50 | >60 |

### 21.2 Product Metrics

| Metric | Target | Acceptance |
|---|---|---|
| **L1 scan duration (end-to-end)** | <3 minutes | <180s from signup to report visible |
| **L1 scan pipeline (15 steps)** | <90 seconds | Parallel execution in Lambda |
| **API response time (p95)** | <500ms | Excluding scan execution time |
| **Dashboard page load** | <2 seconds | Initial render |
| **SOAR alert-to-triage** | <60 seconds | Claude analysis complete |
| **Malware detection latency** | Real-time | Within 1 second of ClamAV detection |
| **Uptime (MVP)** | 99.5% | Rolling 30-day SLA |
| **Uptime (Prod)** | 99.9% | Rolling 30-day SLA |

### 21.3 Adoption Metrics

| Metric | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| **Signups (cumulative)** | 50 | 500 | 5,000 |
| **Free scans run** | 50 | 2,000 | 25,000 |
| **Paid scans run** | 0 | 1,500 | 50,000 |
| **Health score improvement** | — | +15 pts avg (free → paid) | +20 pts avg |
| **Compliance gaps remediated** | — | 40% of flagged findings | 65% of flagged findings |

---

## 22. Conclusion

SOCVault is a **unified, AI-powered cybersecurity platform** that transforms how SMBs understand and manage their security exposure. By consolidating eight attack surface layers, translating findings into financial risk in plain English, and automating response playbooks, SOCVault removes the barriers of cost, complexity, and expertise that leave SMBs exposed.

**Key differentiators:**
1. **AI Financial Risk Translation** — converts CVEs to £/$ exposure
2. **8-Layer Unified Coverage** — replaces fragmented point solutions
3. **Freemium Path-to-Revenue** — 1 real L1 scan/month (free); conversion via financial exposure discovery
4. **SOAR at SMB Pricing** — $199/mo for full automation vs $5,000+ enterprise
5. **60-Second Onboarding** — no procurement, no implementation project

**Timeline:**
- **Phase 0 (Weeks 1–4):** AWS staging + IaC + CI/CD (blueprint complete)
- **Phase 1 (Weeks 5–16):** Auth + L1 + Claude + dashboard (MVP staging)
- **Phase 2 (Weeks 17–24):** Payments + SOAR + L2–L8 + beta launch
- **Phase 3 (Weeks 25–36):** Public launch + GTM
- **Phase 4+:** Scale, enterprise, international expansion

**Market:** UK-first launch targeting 450,000 SMBs in regulated sectors; £28.8M SAM; $500M+ global TAM.

**Traction targets:** 50 paying clients by Feb 2027 ($10K MRR); 323 clients by Nov 2027 ($22K MRR); cash-flow break-even by Sep 2028.

---

**Document prepared for:** Engineering teams, AI agent/skills development, investor pitch deck, go-to-market strategy

**Next steps:** 
1. Validate Phase 0 blueprint (AWS + Terraform + CI/CD)
2. Build Phase 1 MVP on staging (auth + L1 + Claude)
3. Run E2E testing with 3 friendly SMB beta users
4. Prepare Phase 2 beta roadmap (Stripe + SOAR)
