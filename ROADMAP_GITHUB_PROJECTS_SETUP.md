# SOCVault GitHub Projects Setup Guide

**Complete setup for GitHub Projects v2 board to track roadmap across all 9 phases**

---

## 1. Create GitHub Projects Board

### Step 1: Create New Project

1. Go to: https://github.com/samihyder/SOCVault-Blueprint/projects
2. Click **"New project"** (green button)
3. Select **"Table"** view
4. Name: **"SOCVault - Product Roadmap"**
5. Description: "46-week development roadmap from admin infrastructure (Phase 0) to public launch (Phase 7) and enterprise scale (Phase 8)"
6. Click **"Create project"**

---

## 2. Configure Board Columns

Add these columns to organize work by status:

| Column | Purpose | Auto-Transition |
|--------|---------|-----------------|
| **📋 Backlog** | New issues, not yet started | Issues created auto-add here |
| **🔄 In Progress** | Active work | When assigned |
| **🧪 In Review** | Pull requests, code review | When PR opened |
| **✅ Done** | Completed & merged | When PR merged |
| **🗂️ Archive** | Historic, no longer relevant | Manual (30+ days in Done) |

### Add Columns:

1. Click **"+ Add column"** in the board header
2. For each column:
   - Enter name from table above
   - Set status: "not started" → "in progress" → "in review" → "done"
   - Click "Add column"

---

## 3. Configure Custom Fields

These fields help categorize work across the 46-week roadmap:

### Field 1: Story Points
- **Name:** Story Points
- **Type:** Number
- **Options:** 1, 2, 3, 5, 8, 13, 21
- **Default:** (blank)

### Field 2: Phase
- **Name:** Phase
- **Type:** Single select
- **Options:**
  - 0 (Admin Infrastructure)
  - 1A (Admin Core)
  - 1B (Tenant Auth)
  - 2A (L1 Scanning)
  - 2B (AI Intelligence)
  - 3 (L2-L8 Scanning)
  - 4 (SOAR)
  - 5 (Monetization)
  - 6 (Beta)
  - 7 (Launch)
  - 8 (Enterprise)

### Field 3: Priority
- **Name:** Priority
- **Type:** Single select
- **Options:**
  - CRITICAL (red)
  - HIGH (orange)
  - MEDIUM (yellow)
  - LOW (green)

### Field 4: Risk Level
- **Name:** Risk Level
- **Type:** Single select
- **Options:**
  - High (red - Phase 0, auth, payments)
  - Medium (orange - scanning, SOAR)
  - Low (green - UI polish, docs)

### Field 5: Milestone
- **Name:** Milestone
- **Type:** Single select
- **Options:**
  - M0.0 (Admin Infrastructure)
  - M1.0 (Admin Portal)
  - M1.5 (Tenant Auth)
  - M2.0 (L1 Scanning)
  - M2.5 (AI Reports)
  - M3.0 (Complete 8 Layers)
  - M4.0 (SOAR)
  - M5.0 (Monetization)
  - M6.0 (Beta)
  - M7.0 (Public Launch)
  - M8.0 (Enterprise)

### Field 6: Duration (Weeks)
- **Name:** Duration (Weeks)
- **Type:** Number
- **Default:** (blank)

---

## 4. Set Up Automation Rules

These rules auto-manage issues as they progress:

### Rule 1: New Issues → Backlog
```
When: Issue opened
Then: Add to column "Backlog"
And: Set Status to "not started"
```

### Rule 2: Assigned → In Progress
```
When: Issue assigned
Then: Move to column "In Progress"
And: Set Status to "in progress"
```

### Rule 3: PR Opened → In Review
```
When: Pull request opened
Then: Move linked issue to column "In Review"
And: Set Status to "in review"
```

### Rule 4: PR Merged → Done
```
When: Pull request merged
Then: Move linked issue to column "Done"
And: Set Status to "done"
```

### Rule 5: Done 30+ Days → Archive
```
When: Card in "Done" for 30+ days
Then: Move to column "Archive"
And: Set Status to "archived"
```

---

## 5. Roadmap Milestones Overview

### Phase 0: Admin Infrastructure (Weeks 1–3)
- **Milestone:** M0.0
- **Duration:** 3 weeks
- **Team:** DevOps + Backend
- **Priority:** 🔴 CRITICAL
- **Risk:** High
- **Key Issues:** US-ADM-001 through US-ADM-009

### Phase 1A: Admin Core (Weeks 4–10)
- **Milestone:** M1.0
- **Duration:** 7 weeks
- **Team:** Backend + Frontend
- **Priority:** 🔴 CRITICAL
- **Risk:** High
- **Key Issues:** US-ADM-010 through US-ADM-015

### Phase 1B: Tenant Auth (Weeks 8–14)
- **Milestone:** M1.5
- **Duration:** 7 weeks
- **Team:** Backend + Frontend
- **Priority:** 🔴 CRITICAL
- **Risk:** Medium
- **Depends On:** Phase 0

### Phase 2A: L1 Scanning (Weeks 12–16)
- **Milestone:** M2.0
- **Duration:** 5 weeks
- **Team:** Backend
- **Priority:** 🟠 HIGH
- **Risk:** Medium
- **Depends On:** Phase 1B

### Phase 2B: AI Intelligence (Weeks 17–22)
- **Milestone:** M2.5
- **Duration:** 6 weeks
- **Team:** Backend
- **Priority:** 🟠 HIGH
- **Risk:** Medium
- **Depends On:** Phase 2A

### Phase 3: Full 8-Layer Scanning (Weeks 20–28)
- **Milestone:** M3.0
- **Duration:** 9 weeks
- **Team:** Backend
- **Priority:** 🟠 HIGH
- **Risk:** Medium
- **Depends On:** Phase 2A

### Phase 4: SOAR Automation (Weeks 26–32)
- **Milestone:** M4.0
- **Duration:** 7 weeks
- **Team:** Backend + Frontend
- **Priority:** 🟠 HIGH
- **Risk:** Medium
- **Depends On:** Phase 3

### Phase 5: Monetization (Weeks 30–38)
- **Milestone:** M5.0
- **Duration:** 9 weeks
- **Team:** Backend + Frontend
- **Priority:** 🟠 HIGH
- **Risk:** Low
- **Depends On:** Phase 1B

### Phase 6: Beta Launch (Weeks 39–42)
- **Milestone:** M6.0
- **Duration:** 4 weeks
- **Team:** All
- **Priority:** 🔴 CRITICAL
- **Risk:** High
- **Depends On:** Phases 2–5

### Phase 7: Public Launch (Weeks 43–46)
- **Milestone:** M7.0
- **Duration:** 4 weeks
- **Team:** All
- **Priority:** 🔴 CRITICAL
- **Risk:** High
- **Depends On:** Phase 6
- **🎉 Target:** api.socvault.io live

### Phase 8: Enterprise Scale (Weeks 47–52)
- **Milestone:** M8.0
- **Duration:** 6 weeks
- **Team:** All
- **Priority:** 🟠 HIGH
- **Risk:** Low
- **Depends On:** Phase 7

---

## 6. Assigning Issues to Milestones

### Automated (via script):
```bash
python3 scripts/github-projects/create-admin-issues.py \
  --repo samihyder/SOCVault-Blueprint \
  --token <GITHUB_TOKEN>
```

### Manual:
1. Go to issue
2. Click "Milestone" dropdown
3. Select milestone (M0.0, M1.0, etc.)
4. Click checkbox to confirm

---

## 7. Sprint Planning Template

Each sprint should follow this structure:

### Sprint Goal
```
Complete Phase X.Y to deliver [feature/capability]
Blockers resolved: [dependent phase]
```

### Sprint Issues
- Issues assigned to current phase
- Story points totaling 20-30 points/sprint
- All CRITICAL priority items included
- Dependencies marked with "Depends on: issue #123"

### Sprint Metrics
- Target Velocity: 20-30 points/sprint
- Completion Rate: >90%
- Critical Bug Rate: <5%

### Daily Standup Format
```
What did I complete? (yesterday)
What will I complete? (today)
Any blockers? (escalate immediately)
```

### Sprint Review (Friday)
```
Completed Issues: [count] pts
In Progress: [count] pts
Blocked: [count] pts
Velocity: [pts/week]
Next Sprint Target: [focus]
```

---

## 8. Dependency Tracking

### Critical Dependencies (Phase-to-Phase)

```
Phase 0 (Admin Infra)
  ↓ BLOCKS
Phase 1A (Admin Core) + Phase 1B (Tenant Auth) starts week 8
  ↓ BLOCKS
Phase 2A (L1 Scanning)
  ↓ FEEDS
Phase 2B (AI) + Phase 3 (Full Scanning) parallel
  ↓
Phase 4 (SOAR) + Phase 5 (Payments) parallel
  ↓
Phase 6 (Beta)
  ↓
Phase 7 (LAUNCH) 🎉
  ↓
Phase 8 (Enterprise)
```

### In GitHub:
- Use issue references: "Depends on #123"
- Use PR templates to link issues
- Add comments with dependency notes

---

## 9. Board Views & Filters

### View 1: By Milestone
- Filter: Milestone = "M0.0"
- Shows: All issues in current milestone
- Use for: Sprint planning

### View 2: By Phase
- Filter: Phase = "0"
- Shows: All infrastructure issues
- Use for: Dependency tracking

### View 3: By Priority
- Filter: Priority = "CRITICAL"
- Shows: High-priority blocking work
- Use for: Risk management

### View 4: By Team
- Filter: Assignee team
- Shows: Work assigned to team
- Use for: Daily standups

### View 5: Critical Path
- Filter: Phase in (0, 1A, 1B, 2A, 3) AND Priority = CRITICAL
- Shows: Blocking critical items
- Use for: Executive visibility

---

## 10. Success Metrics

### Roadmap Execution Health

| Metric | Phase 0 | Phase 1A | Phase 1B | Phase 2+ |
|--------|---------|----------|----------|---------|
| **Velocity** | 20 pts/week | 20 pts/week | 15 pts/week | 20 pts/week |
| **Completion** | >90% | >85% | >85% | >90% |
| **Critical Bugs** | <5% | <10% | <10% | <5% |
| **Code Coverage** | >80% | >80% | >70% | >70% |
| **Uptime** | 99% | 99% | 99.5% | 99.5%+ |

### Weekly Tracking

Update this table every Friday:

| Week | Phase | Target Pts | Completed Pts | Velocity | Status |
|------|-------|-----------|--------------|----------|--------|
| 1 | 0 | 15 | ? | ? | ⏳ |
| 2 | 0 | 15 | ? | ? | ⏳ |
| 3 | 0 | 12 | ? | ? | ⏳ |
| 4 | 1A | 15 | ? | ? | ⏳ |
| ... | ... | ... | ... | ... | ... |

---

## 11. Automation Rules in GitHub Projects

### Setup Automation via UI:

1. Click **"…" (three dots)** next to project name
2. Select **"Workflows"**
3. For each automation rule:
   - Click **"New workflow"**
   - Set trigger (e.g., "Issue opened")
   - Set action (e.g., "Add to column: Backlog")
   - Click "Save"

### Available Triggers:
- Issue opened
- Issue closed
- Issue assigned
- Pull request opened
- Pull request merged
- Custom triggers (via GitHub Actions)

---

## 12. Quick Start Checklist

- [ ] Created GitHub Projects board
- [ ] Added 5 columns (Backlog, In Progress, In Review, Done, Archive)
- [ ] Added 6 custom fields (Story Points, Phase, Priority, Risk Level, Milestone, Duration)
- [ ] Set up 5 automation rules
- [ ] Created all 11 milestones (M0.0–M8.0)
- [ ] Assigned Phase 0 issues to M0.0
- [ ] Invited team members to project
- [ ] Scheduled sprint planning meeting (Week 1)
- [ ] Enabled notifications for board changes
- [ ] Bookmarked project for quick access

---

## 13. Team Access & Permissions

### For DevOps Engineer (Phase 0):
- Access to: Infrastructure, Terraform, AWS, Monitoring issues
- Milestones: M0.0, M0.1–M0.6

### For Backend Engineers (Phases 1–5):
- Access to: API, Database, Auth, Scanning, SOAR, Payments
- Milestones: M1.0, M1.5, M2.0, M2.5, M3.0, M4.0, M5.0

### For Frontend Engineers (Phases 1–5):
- Access to: UI, Dashboard, Forms, Components
- Milestones: M1.0, M1.5, M2.0, M2.5, M4.0, M5.0

### For Product Manager:
- Access to: All issues, milestones, reporting
- Can: View all, filter, create reports, update status

---

## 14. Links & Resources

- 📄 [SOCVAULT_PRODUCT_DESCRIPTION.md](../SOCVAULT_PRODUCT_DESCRIPTION.md) — Full product specification
- 📋 [ADMIN_SETUP_GUIDE.md](./ADMIN_SETUP_GUIDE.md) — Admin phase details
- 🚀 [ADMIN_QUICK_START.md](./ADMIN_QUICK_START.md) — Week-by-week execution
- 📊 [GitHub Milestones](https://github.com/samihyder/SOCVault-Blueprint/milestones)
- 🔗 [GitHub Projects](https://github.com/samihyder/SOCVault-Blueprint/projects)

---

## 15. Troubleshooting

### "Custom field not showing in all issues"
- Solution: Fields are project-specific; add field to all issues manually or via bulk action

### "Automation rule not triggering"
- Check: Is rule enabled? Are conditions correct? Try re-saving rule

### "Can't see milestone in dropdown"
- Check: Milestone exists? Your repo has permission? Try refreshing page

### "Board is too cluttered"
- Solution: Create filtered views, hide archived items, archive old milestones

---

**Ready to launch roadmap tracking! 🚀**

Next: Run the milestone creation workflow and start Phase 0 sprint planning.
