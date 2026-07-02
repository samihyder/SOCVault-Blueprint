# Quick Start: Admin Setup Implementation

**Goal:** Get admin infrastructure running in staging in 10 weeks

**Team:** 2 engineers (1 DevOps, 1 Backend)

---

## Pre-Flight Checklist (Before Starting)

- [ ] GitHub repository cloned: `git clone https://github.com/samihyder/SOCVault-Blueprint.git`
- [ ] Python 3.11+ installed: `python --version`
- [ ] GitHub token generated with `repo` + `issues` permissions
- [ ] Terraform installed: `terraform --version`
- [ ] AWS CLI configured: `aws configure` (staging account)
- [ ] Docker installed: `docker --version`
- [ ] GitHub Projects v2 board created: "SOCVault - Admin Setup"

---

## Step 1: Create GitHub Issues (15 min)

**Option A: Automated (Recommended)**
```bash
cd SOCVault-Blueprint
python3 scripts/github-projects/create-admin-issues.py \
  --repo samihyder/SOCVault-Blueprint \
  --token <YOUR_GITHUB_TOKEN>
```

**Option B: Manual**
1. Copy user stories from `SOCVAULT_PRODUCT_DESCRIPTION.md` Section 20.3
2. Create 15 issues in GitHub manually
3. Assign milestones: M0.1–M1.6

---

## Step 2: Configure GitHub Projects Board (10 min)

1. **Create columns:**
   - 📋 Backlog
   - 🔄 In Progress
   - 🧪 In Review
   - ✅ Done (Sprint)
   - 📊 Done (All Time)

2. **Add custom fields:**
   - Story Points (number: 1–21)
   - Priority (HIGH, MEDIUM, LOW)
   - Phase (0, 1A, 1B, 2+)
   - Risk Level (Low, Medium, High)

3. **Enable automation:**
   - Issue created → Backlog
   - PR opened → In Review
   - PR merged → Done
   - Assigned → In Progress (manual trigger)

---

## Step 3: Phase 0 Kickoff (Week 1)

### Day 1: AWS Account Setup

**Assigned To:** DevOps Engineer

**Tasks:**
1. Create AWS Organization (1 hour)
2. Create staging + production accounts (30 min)
3. Enable CloudTrail (15 min)
4. Set billing alerts (15 min)

**PR Checklist:**
- [ ] AWS Organization created
- [ ] Account IDs documented
- [ ] CloudTrail enabled
- [ ] Billing configured

**Mark Complete:** Move US-ADM-001 to Done

### Day 2–3: IAM & VPC

**Tasks:**
1. Create IAM roles (GitHub Actions, Terraform, Admin) — 2 hours
2. Create VPC with subnets — 3 hours
3. Configure security groups — 1 hour

**Mark Complete:** Move US-ADM-002 & US-ADM-003 to Done

### Day 4–5: Terraform Setup

**Tasks:**
1. Initialize Terraform project (30 min)
2. Create S3 backend + DynamoDB lock (1 hour)
3. Set up workspaces (staging, production) (30 min)
4. Validate all configurations (30 min)

**Mark Complete:** Move US-ADM-004 to Done

---

## Step 4: Phase 0 Databases (Week 2)

### Day 1–2: MongoDB Atlas

**Assigned To:** Backend Engineer

**Tasks:**
1. Create MongoDB Atlas cluster — 30 min
2. Configure encryption + backups — 30 min
3. Create database collections (tenants, users, etc.) — 30 min
4. Store connection string in Secrets Manager — 30 min

**Mark Complete:** Move US-ADM-005 to Done

### Day 3: DynamoDB

**Tasks:**
1. Create `cost_telemetry` table — 30 min
2. Create `rate_limits` table — 30 min
3. Configure TTL — 15 min
4. Test connections from Lambda — 30 min

**Mark Complete:** Move US-ADM-006 to Done

### Day 4: Secrets Manager

**Tasks:**
1. Create KMS encryption key — 15 min
2. Create all secrets (DB, API keys, etc.) — 30 min
3. Configure automatic rotation — 15 min
4. Test secret retrieval from Lambda — 30 min

**Mark Complete:** Move US-ADM-007 to Done

---

## Step 5: Phase 0 Monitoring (Week 2–3)

### Days 1–2: CloudWatch Setup

**Tasks:**
1. Create CloudWatch dashboard — 1 hour
2. Create alarms (error rate, latency, costs) — 1 hour
3. Configure SNS topics for alerts — 30 min
4. Set up Slack integration — 30 min

**Mark Complete:** Move US-ADM-008 to Done

### Days 3–5: FastAPI Skeleton

**Assigned To:** Backend Engineer

**Tasks:**
1. Initialize FastAPI project — 30 min
2. Create project structure (routes, schemas, config) — 1 hour
3. Implement `/health` endpoint — 30 min
4. Create Dockerfile (Lambda-compatible) — 30 min
5. Set up pytest + CI/CD — 1 hour

**Mark Complete:** Move US-ADM-009 to Done

---

## Step 6: Phase 1A Kickoff (Week 4)

### Week 4–5: Core API Endpoints

**Assigned To:** Backend Engineer

**Create these endpoints:**
1. `POST /admin/users` — Create admin users (2 days)
2. `POST /admin/tenants` — Create tenants (2 days)
3. `GET /admin/audit-logs` — Query audit logs (2 days)
4. `GET/PUT /admin/settings` — Manage settings (1 day)

**Parallel: Frontend Engineer**
1. Create Admin Dashboard component (3 days)
2. Create Audit Log table UI (2 days)

### Week 6: Documentation

**Assigned To:** Backend Engineer

**Tasks:**
1. Create OpenAPI spec — 2 hours
2. Generate Swagger UI — 1 hour
3. Update README — 1 hour
4. Create deployment guide — 2 hours

---

## Testing Checklist

After each milestone, verify:

```bash
# Unit tests pass
pytest tests/unit/ -v --cov=app

# Integration tests pass
pytest tests/integration/ -v

# Type checking passes
mypy app/ --ignore-missing-imports

# Linting passes
ruff check .

# Security scan clean
bandit -r app/ -ll

# No secrets leaked
git secrets scan --all
```

---

## Deployment

### Deploy Phase 0 Infrastructure

```bash
cd terraform
terraform init -backend-config=staging.tfbackend
terraform workspace select staging
terraform plan -var-file=staging.tfvars
terraform apply -var-file=staging.tfvars
```

### Deploy Phase 1A API

```bash
# Build Docker image
docker build -t socvault-api:latest -f Dockerfile.api .

# Push to ECR
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin <ECR_URL>
docker tag socvault-api:latest <ECR_URL>/socvault-api:latest
docker push <ECR_URL>/socvault-api:latest

# Deploy Lambda
cd terraform
terraform apply -var-file=staging.tfvars
```

### Verify Deployment

```bash
# Health check
curl https://admin-staging.socvault.io/health

# Create test user
curl -X POST https://admin-staging.socvault.io/api/v1/admin/users \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","full_name":"Test Admin","role":"SUPER_ADMIN"}'

# Create test tenant
curl -X POST https://admin-staging.socvault.io/api/v1/admin/tenants \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"company_name":"Test Co","industry":"Tech","tier":"free","contact_email":"contact@test.co"}'
```

---

## Daily Standups (15 min)

**Format:**
1. **Yesterday:** What did you complete? Any blockers?
2. **Today:** What are you working on?
3. **Blockers:** Anything stuck? Escalate if needed.

**Example:**
```
DevOps Engineer:
- Yesterday: ✅ Completed AWS Organization setup (US-ADM-001)
- Today: Working on VPC configuration (US-ADM-003)
- Blockers: None

Backend Engineer:
- Yesterday: ✅ Completed IAM roles (US-ADM-002)
- Today: Starting Terraform setup (US-ADM-004)
- Blockers: Waiting for AWS account IDs (resolved by DevOps)
```

---

## Weekly Review

Every Friday (30 min):

**Completed This Week:**
- ✅ US-ADM-001: AWS Organization
- ✅ US-ADM-002: IAM Roles
- **Total: 13 story points**

**In Progress:**
- 🔄 US-ADM-003: VPC (75% complete)

**Blocked:**
- ⏸️ None

**Velocity:** 13 points/week

**Next Week Target:** Complete Phase 0 (62 points total, on track)

---

## Success Metrics

| Week | Target | Actual | Status |
|------|--------|--------|--------|
| 1 | M0.1 (AWS) + M0.2 (Terraform) | ? | ⏳ |
| 2 | M0.3 (DB) + M0.4 (Secrets) | ? | ⏳ |
| 3 | M0.5 (Monitoring) + M0.6 (API) | ? | ⏳ |
| 4 | M1.1 (Admin Users) | ? | ⏳ |
| 5 | M1.2 (Tenants) + M1.3 (Dashboard) | ? | ⏳ |
| 6 | M1.4–M1.6 (Logs, Settings, Docs) | ? | ⏳ |

---

## Common Issues & Fixes

### "AWS account creation taking too long"
- AWS Organizations takes 5–10 minutes
- Check email for confirmation if using new AWS account

### "Terraform apply fails with permission denied"
- Verify IAM role has required permissions
- Check AWS credentials: `aws sts get-caller-identity`

### "MongoDB connection timeout"
- Check IP whitelist in Atlas (should include Lambda security group)
- Verify connection string in Secrets Manager
- Test locally: `mongosh "<connection-string>"`

### "CI/CD pipeline failing"
- Check GitHub Actions logs
- Look for specific error: linting, types, tests, security
- Fix locally, commit, and re-run

### "Secrets not accessible from Lambda"
- Verify Lambda execution role has `secretsmanager:GetSecretValue` permission
- Verify KMS key policy allows Lambda role
- Check secret name matches code

---

## Getting Help

1. **Check documentation first:**
   - [SOCVAULT_PRODUCT_DESCRIPTION.md](../SOCVAULT_PRODUCT_DESCRIPTION.md) Section 20
   - [ADMIN_SETUP_GUIDE.md](./ADMIN_SETUP_GUIDE.md)
   - AWS docs: https://docs.aws.amazon.com

2. **Search GitHub issues:**
   - Filter: `label:admin` + `label:phase-0`

3. **Ask in Slack:**
   - #dev-admin (team discussion)
   - #incidents (blocking issues)

4. **Escalate:**
   - DevOps lead for infrastructure issues
   - Backend lead for API issues

---

**Ready to start? Create GitHub issues now!** 🚀
