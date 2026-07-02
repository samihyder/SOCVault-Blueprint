# SOCVault Admin Setup Roadmap & GitHub Projects Guide

## Overview

This guide covers:
1. **Admin Setup Roadmap** — Complete phases and milestones for admin infrastructure
2. **GitHub Projects Setup** — How to organize and track admin work
3. **User Stories** — Detailed acceptance criteria for each feature
4. **Automation** — How to auto-create issues and sync with GitHub Projects

---

## Admin Setup Roadmap

### Timeline: Weeks 1–10

```
PHASE 0 (Weeks 1–3): Admin Infrastructure Foundation
├─ M0.1: AWS Account Setup (Week 1)
├─ M0.2: Terraform IaC (Week 1–2)
├─ M0.3: Database Setup (Week 2)
├─ M0.4: Secrets Management (Week 2–3)
├─ M0.5: Monitoring & Alerting (Week 3)
└─ M0.6: Admin API Skeleton (Week 3)

PHASE 1A (Weeks 4–6): Admin Core Features
├─ M1.1: Super Admin Users (Week 4)
├─ M1.2: Tenant Management (Week 4–5)
├─ M1.3: Admin Dashboard (Week 5)
├─ M1.4: Audit Log Viewer (Week 5–6)
├─ M1.5: System Settings (Week 6)
└─ M1.6: API Documentation (Week 6)

PHASE 1B (Weeks 7–8): Security & Compliance
├─ M1.7: 2FA Authentication
├─ M1.8: RBAC (Admin/Operator/Viewer)
├─ M1.9: Compliance Dashboard
├─ M1.10: Audit Trail
├─ M1.11: Security Events
└─ M1.12: Admin Portal UI

PHASE 2+ (Weeks 9–10): Advanced Admin & User-Facing Modules
```

### Success Criteria

Admin module is **COMPLETE** when all milestones satisfy:

- ✅ All acceptance criteria for all user stories met
- ✅ 100+ automated tests passing (unit + integration)
- ✅ API fully documented (OpenAPI spec)
- ✅ All CI/CD checks passing
- ✅ Admin portal deployed to staging
- ✅ 0 CRITICAL security vulnerabilities
- ✅ Code coverage >80%
- ✅ GitHub Projects board auto-syncing
- ✅ Production-ready infrastructure

---

## GitHub Projects Setup

### Step 1: Create GitHub Projects v2 Board

1. Navigate to: **[Your Repository] → Projects tab → New project**
2. Click **"New project"** → **"Table" template**
3. Name it: **"SOCVault - Admin Setup"**
4. Add description: *"Phase 0-2: Admin infrastructure & core management features. Foundational for all modules."*

### Step 2: Configure Board Columns

Create custom columns for status tracking:

| Column | Purpose | Auto-Move Rules |
|--------|---------|-----------------|
| 📋 **Backlog** | Issues not started | Default for new issues |
| 🔄 **In Progress** | Assigned to engineer, actively developed | When label `in-progress` added |
| 🧪 **In Review** | PR opened, awaiting approval | When PR opened |
| ✅ **Done (Sprint)** | Completed this sprint | When PR merged |
| 📊 **Done (All Time)** | Historical (read-only) | Auto-archive after 30 days |

**To create columns:**
1. Click **"Add column"** button
2. Name each column
3. Configure automation in column settings

### Step 3: Add Custom Fields

Add these custom fields for better tracking:

| Field | Type | Values |
|-------|------|--------|
| **Story Points** | Number | 1, 2, 3, 5, 8, 13, 21 |
| **Priority** | Single select | CRITICAL, HIGH, MEDIUM, LOW |
| **Phase** | Single select | Phase 0, Phase 1A, Phase 1B, Phase 2+ |
| **Team** | Single select | Frontend, Backend, DevOps, QA |
| **Risk Level** | Single select | Low, Medium, High |

**To add custom fields:**
1. Click **⚙️ Settings** in project header
2. Under "Custom fields", click **"Add field"**
3. Choose field type and values

### Step 4: Set Up Automation

Click **⚙️ Settings → Workflows** and enable:

1. **Auto-move to In Progress**
   - When issue is assigned → Move to "In Progress"

2. **Auto-move to In Review**
   - When PR is opened on issue → Move to "In Review"

3. **Auto-move to Done**
   - When PR is merged → Move to "Done (Sprint)"

4. **Auto-archive after 30 days**
   - Done (Sprint) → Done (All Time) after 30 days

### Step 5: Set Up Issue Templates

Create issue templates in `.github/issue_templates/` for consistency:

- `admin-infrastructure.md` — Infrastructure issues (terraform, AWS, networking)
- `admin-api.md` — API endpoint issues
- `admin-frontend.md` — Admin UI issues
- `admin-bug.md` — Bug reports

---

## Creating Admin Issues

### Option 1: Automated (Python Script + GitHub Actions)

**Trigger the workflow:**
```bash
# Via GitHub UI
1. Go to Actions tab
2. Find "Create Admin Setup Issues"
3. Click "Run workflow"
4. Select environment (staging/production)
5. Workflow creates all 15 issues + milestones
```

**Or run script locally:**
```bash
cd SOCVault-Blueprint
python3 scripts/github-projects/create-admin-issues.py \
  --repo samihyder/SOCVault-Blueprint \
  --token <YOUR_GITHUB_TOKEN>
```

Required permissions in token:
- `repo` (full)
- `issues` (read/write)

### Option 2: Manual Creation

Go to **Issues → New issue** and fill in:

```
Title: US-ADM-001: Create AWS Organization & Accounts
Milestone: M0.1: AWS Account Setup & IAM
Labels: infrastructure, aws, phase-0, blocking
Body: [Copy from SOCVAULT_PRODUCT_DESCRIPTION.md section 20.3]
```

Repeat for all 15 user stories.

---

## User Stories Overview

### Phase 0: Infrastructure Foundation (Weeks 1–3)

| Story | Title | Assigned To | Points |
|-------|-------|-------------|--------|
| US-ADM-001 | Create AWS Organization & Accounts | DevOps | 5 |
| US-ADM-002 | Set Up IAM Roles & Policies | DevOps | 8 |
| US-ADM-003 | Configure VPC with Multi-AZ | DevOps | 13 |
| US-ADM-004 | Terraform Project Setup | DevOps | 5 |
| US-ADM-005 | MongoDB Atlas Configuration | Backend | 8 |
| US-ADM-006 | DynamoDB Tables | DevOps | 5 |
| US-ADM-007 | AWS Secrets Manager | DevOps | 5 |
| US-ADM-008 | CloudWatch Monitoring | DevOps | 8 |
| US-ADM-009 | FastAPI Admin API Skeleton | Backend | 5 |

**Total Phase 0: 62 story points (3 weeks, 1 DevOps + 1 Backend engineer)**

### Phase 1A: Admin Core (Weeks 4–6)

| Story | Title | Assigned To | Points |
|-------|-------|-------------|--------|
| US-ADM-010 | Super Admin User Management | Backend | 8 |
| US-ADM-011 | Tenant Management | Backend | 13 |
| US-ADM-012 | Admin Dashboard | Frontend | 13 |
| US-ADM-013 | Audit Log Viewer | Backend + Frontend | 13 |
| US-ADM-014 | System Settings | Backend | 8 |
| US-ADM-015 | Admin API Documentation | Backend | 5 |

**Total Phase 1A: 60 story points (3 weeks, 1 Backend + 1 Frontend engineer)**

### Phase 1B: Security & Compliance (Weeks 7–8)

To be created after Phase 1A completion. Follow same process.

---

## Sprint Planning

### Sprint 1 (Week 1): M0.1–M0.2 Start

**In Progress:**
- US-ADM-001: AWS Organization (DevOps)
- US-ADM-002: IAM Roles (DevOps)
- US-ADM-003: VPC Setup (DevOps)
- US-ADM-004: Terraform (DevOps)

**Blocked by:**
- None (foundational work)

**Definition of Done:**
- ✅ All acceptance criteria met
- ✅ Infrastructure tested (manual)
- ✅ Documentation updated
- ✅ Pull request merged
- ✅ Staging infrastructure ready

### Sprint 2 (Week 2–3): M0.3–M0.6 Complete

**In Progress:**
- US-ADM-005: MongoDB (Backend)
- US-ADM-006: DynamoDB (DevOps)
- US-ADM-007: Secrets Manager (DevOps)
- US-ADM-008: CloudWatch (DevOps)
- US-ADM-009: FastAPI Skeleton (Backend)

**Blocked by:**
- M0.1, M0.2 completion

### Sprint 3 (Week 4–5): M1.1–M1.3

**In Progress:**
- US-ADM-010: Admin Users (Backend)
- US-ADM-011: Tenant Management (Backend)
- US-ADM-012: Admin Dashboard (Frontend)

**Depends On:**
- Phase 0 infrastructure complete

### Sprint 4 (Week 6): M1.4–M1.6

**In Progress:**
- US-ADM-013: Audit Log Viewer (Backend + Frontend)
- US-ADM-014: System Settings (Backend)
- US-ADM-015: API Documentation (Backend)

---

## GitHub Projects Workflow

### Issue Lifecycle

```
1. NEW ISSUE CREATED
   ↓
   Labels: backend, admin-users, phase-1a
   Milestone: M1.1
   Status: Backlog
   ↓
   
2. ASSIGNMENT & START
   Developer picks up → Update status to "In Progress"
   ↓
   
3. DEVELOPMENT
   Create feature branch: git checkout -b feat/admin-users-001
   Code + tests + PR
   ↓
   
4. CODE REVIEW
   PR auto-moves to "In Review"
   Reviewers assigned automatically (by labels)
   ↓
   
5. APPROVAL & MERGE
   All CI checks pass → Auto-merge
   Status: "Done (Sprint)"
   ↓
   
6. ARCHIVED
   After 30 days → Move to "Done (All Time)"
   ↓
   
7. RETROSPECTIVE
   At sprint end: "What went well? What could improve?"
```

### Checklist for Each Issue

```markdown
## ✅ Definition of Done Checklist

- [ ] Acceptance criteria all met
- [ ] Code written (following standards)
- [ ] Unit tests written (>80% coverage)
- [ ] Integration tests pass
- [ ] No new linting/type errors
- [ ] No new security vulnerabilities (CRITICAL/HIGH)
- [ ] Documentation updated
- [ ] Code reviewed and approved
- [ ] Deployed to staging
- [ ] Smoke tests pass on staging
- [ ] PR merged to main
```

---

## Monitoring & Metrics

### Track These Metrics Weekly

| Metric | Target | How to Track |
|--------|--------|--------------|
| **Velocity** | 60 points/sprint | Sum story points completed |
| **Burndown** | Linear decrease | Chart on project board |
| **Cycle Time** | <5 days per issue | Average time: created → merged |
| **Test Coverage** | >80% | CI reports |
| **Security Issues** | 0 CRITICAL | Security scan results |
| **Code Quality** | A grade | SonarQube metrics |

### Weekly Status Report Template

```markdown
## Week X Status - Admin Setup

### Completed This Week
- [x] US-ADM-001: AWS Organization (5 pts)
- [x] US-ADM-002: IAM Roles (8 pts)
**Total: 13 points**

### In Progress
- [ ] US-ADM-003: VPC Setup (50% complete)
- [ ] US-ADM-004: Terraform (30% complete)

### Blocked
- US-ADM-005: MongoDB (waiting on US-ADM-004)

### Metrics
- Velocity: 13 points completed
- Burndown: On track
- Test Coverage: 82%
- Security Issues: 0 CRITICAL, 1 HIGH (fixing)

### Next Week
- Complete US-ADM-003, US-ADM-004
- Start Phase 1A (API development)
```

---

## Troubleshooting

### Issue: Automation not moving issues

**Solution:**
1. Check GitHub Projects settings → Workflows
2. Verify automation rules are enabled
3. Confirm issue has correct label/milestone
4. Try manually moving to test automation

### Issue: CI checks failing

**Solution:**
1. Check GitHub Actions workflow logs
2. Look for specific error (linting, tests, security)
3. Fix locally and push to PR
4. Automation will re-run checks

### Issue: Stories not created by script

**Solution:**
```bash
# Check GitHub token has correct permissions
gh auth status

# Run script with verbose output
python3 scripts/github-projects/create-admin-issues.py \
  --repo samihyder/SOCVault-Blueprint \
  --token <TOKEN> --verbose

# If still failing, create issues manually from doc
```

---

## Resources

- [GitHub Projects Documentation](https://docs.github.com/en/issues/planning-and-tracking-with-projects)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [SOCVault Product Description](../SOCVAULT_PRODUCT_DESCRIPTION.md) — Section 20: Admin Setup Roadmap
- [GitHub API Reference](https://docs.github.com/en/graphql)

---

## Next Steps

1. ✅ Run `create-admin-setup-issues.yml` workflow
2. ✅ Verify 15 issues + milestones created
3. ✅ Configure board columns & automation
4. ✅ Add custom fields (Story Points, Priority, Phase)
5. ✅ Schedule sprint kickoff meeting
6. ✅ Assign Phase 0 issues to DevOps engineer
7. ✅ Begin Sprint 1: AWS Account Setup

---

**Last Updated:** 2026-07-02  
**Maintained By:** SOCVault DevOps Team  
**Questions?** Check SOCVAULT_PRODUCT_DESCRIPTION.md Section 20
