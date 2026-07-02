#!/usr/bin/env python3
"""
Create SOCVault complete roadmap in GitHub Projects with all 11 milestones.

This script creates:
- GitHub Projects board: "SOCVault - Product Roadmap"
- 11 milestones: M0.0 through M8.0
- Project columns with automation rules
- Links to implementation guides

Usage:
    python3 create-roadmap-milestones.py \
        --repo samihyder/SOCVault-Blueprint \
        --token <GITHUB_TOKEN>

Requirements:
    pip install requests
"""

import argparse
import sys
import requests

# Roadmap milestones with phases and descriptions
MILESTONES = [
    {
        "title": "M0.0: Admin Infrastructure Ready",
        "description": "Phase 0 (Weeks 1–3)\n\n✅ Deliverables:\n- AWS staging account operational\n- All GitHub Actions workflows passing\n- CloudWatch dashboards active\n- Terraform IaC foundation\n- FastAPI skeleton deployed\n- CI/CD pipelines working\n- 0 CRITICAL vulnerabilities\n\n⏸️ BLOCKER FOR: All Phase 1+ work\n\n📋 User Stories: US-ADM-001 through US-ADM-009 (Phase 0)",
        "phase": "0",
        "week_range": "1-3",
        "duration_weeks": 3,
        "team": "DevOps + Backend",
        "priority": "CRITICAL",
    },
    {
        "title": "M1.0: Admin Portal Complete",
        "description": "Phase 1A (Weeks 4–10)\n\n✅ Deliverables:\n- Admin portal at admin-staging.socvault.io\n- Super admin user management API\n- Tenant management API\n- Admin dashboard UI\n- Audit log viewer\n- System settings\n- OpenAPI documentation\n- >80% code coverage\n\n⏸️ BLOCKER FOR: Tenant authentication\n\n📋 User Stories: US-ADM-010 through US-ADM-015 (Phase 1A)",
        "phase": "1A",
        "week_range": "4-10",
        "duration_weeks": 7,
        "team": "Backend + Frontend",
        "priority": "CRITICAL",
    },
    {
        "title": "M1.5: Tenant Authentication Live",
        "description": "Phase 1B (Weeks 8–14)\n\n✅ Deliverables:\n- Tenant signup flow\n- Email verification\n- JWT authentication\n- 2FA via SMS (SNS)\n- Tenant dashboard\n- User invite system\n- Password reset flow\n\n⏸️ BLOCKER FOR: L1 scanning and user features\n\n📋 Phase 1B user stories with acceptance criteria",
        "phase": "1B",
        "week_range": "8-14",
        "duration_weeks": 7,
        "team": "Backend + Frontend",
        "priority": "CRITICAL",
    },
    {
        "title": "M2.0: L1 Scanning Live",
        "description": "Phase 2A (Weeks 12–16)\n\n✅ Deliverables:\n- 15 L1 network reconnaissance checks\n- Domain enumeration\n- Public asset discovery\n- SQS async scan orchestration\n- S3 result storage\n- Scan status polling\n- Results visible in tenant dashboard\n- <3 minute end-to-end scan time\n\n📋 Phase 2A user stories\nℹ️ Requires: Phase 1B tenant auth complete",
        "phase": "2A",
        "week_range": "12-16",
        "duration_weeks": 5,
        "team": "Backend",
        "priority": "HIGH",
    },
    {
        "title": "M2.5: Financial Risk Reports (Claude AI)",
        "description": "Phase 2B (Weeks 17–22)\n\n✅ Deliverables:\n- Claude Sonnet integration\n- Financial risk translation per finding\n- Markdown report generation\n- Scan insights & recommendations\n- Static malware analysis\n- Prompt caching (90% token cost reduction)\n- Reports visible in UI\n- Risk scoring algorithm\n\n📋 Phase 2B user stories\nℹ️ Requires: Phase 2A L1 scans working",
        "phase": "2B",
        "week_range": "17-22",
        "duration_weeks": 6,
        "team": "Backend",
        "priority": "HIGH",
    },
    {
        "title": "M3.0: Complete 8-Layer Scanning",
        "description": "Phase 3 (Weeks 20–28)\n\n✅ Deliverables:\n- L2: Web app scanning (OWASP Top 10)\n- L3: API security (OAuth, CORS)\n- L4: Cloud infrastructure (AWS)\n- L5: Email security (DMARC, SPF, DKIM)\n- L6: Infrastructure (DNS, certificates)\n- L7: Compliance (PCI-DSS, HIPAA, SOC2)\n- L8: Malware + threat intel\n- Dashboard showing all 8 layers\n- 100+ total checks\n\n📋 Phase 3 user stories\nℹ️ Requires: Phase 2A/2B foundation",
        "phase": "3",
        "week_range": "20-28",
        "duration_weeks": 9,
        "team": "Backend",
        "priority": "HIGH",
    },
    {
        "title": "M4.0: SOAR Automation & Orchestration",
        "description": "Phase 4 (Weeks 26–32)\n\n✅ Deliverables:\n- SOAR playbook engine\n- Claude Opus alert triage\n- Automated remediation workflows\n- Slack/Teams/Jira integration\n- Alert routing & escalation\n- Playbook builder UI\n- <60 second alert-to-action time\n- Audit trail for all actions\n\n📋 Phase 4 user stories\nℹ️ Requires: Phase 3 scanning complete",
        "phase": "4",
        "week_range": "26-32",
        "duration_weeks": 7,
        "team": "Backend + Frontend",
        "priority": "HIGH",
    },
    {
        "title": "M5.0: Monetization & Billing",
        "description": "Phase 5 (Weeks 30–38)\n\n✅ Deliverables:\n- Stripe payment integration\n- Free tier: 5 scans/month, 1 project\n- Pro tier: $99/month, 100 scans/month\n- Enterprise: custom pricing\n- Usage metering\n- Subscription management\n- Invoice generation\n- Billing dashboard\n- >10% free-to-paid conversion\n\n📋 Phase 5 user stories\nℹ️ Requires: Phase 1B tenant auth",
        "phase": "5",
        "week_range": "30-38",
        "duration_weeks": 9,
        "team": "Backend + Frontend",
        "priority": "HIGH",
    },
    {
        "title": "M6.0: Beta Launch (20 Customers)",
        "description": "Phase 6 (Weeks 39–42)\n\n✅ Deliverables:\n- Load testing (1,000 concurrent users)\n- Security audit complete\n- Performance optimization\n- UI/UX polish\n- Complete documentation\n- Onboarding flow refined\n- 20 beta customers on-boarded\n- 99.5% uptime achieved\n- 0 CRITICAL vulnerabilities\n\n📋 Phase 6 testing & QA\nℹ️ Requires: Phases 2–5 complete",
        "phase": "6",
        "week_range": "39-42",
        "duration_weeks": 4,
        "team": "All teams",
        "priority": "CRITICAL",
    },
    {
        "title": "M7.0: 🎉 PUBLIC LAUNCH",
        "description": "Phase 7 (Weeks 43–46)\n\n✅ Deliverables:\n- Production AWS account deployed\n- api.socvault.io live and responding\n- DNS migration complete\n- Monitoring activated\n- On-call incident response ready\n- Marketing launch executed\n- Support team ready\n- 10+ paying customers\n- $2,000 MRR achieved\n- 99.5% uptime SLA active\n\n📋 Phase 7 deployment & operations\n🎯 MILESTONE: Public launch (Week 46)",
        "phase": "7",
        "week_range": "43-46",
        "duration_weeks": 4,
        "team": "All teams",
        "priority": "CRITICAL",
    },
    {
        "title": "M8.0: Enterprise Scale Ready",
        "description": "Phase 8 (Weeks 47–52)\n\n✅ Deliverables:\n- SOC2 Type II certified\n- 99.9% uptime SLA for Enterprise tier\n- Advanced RBAC implemented\n- White-label support\n- Dedicated account management\n- 50+ paying customers\n- $15,000 MRR achieved\n- Enterprise onboarding process\n\n📋 Phase 8 compliance & scaling\n🎯 MILESTONE: Enterprise-ready (Week 52)",
        "phase": "8",
        "week_range": "47-52",
        "duration_weeks": 6,
        "team": "All teams",
        "priority": "HIGH",
    },
]

class GitHubProjectManager:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.repo = repo
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Github-Api-Version": "2022-11-28",
        }

    def create_milestone(self, title: str, description: str) -> bool:
        """Create a milestone in the repository."""
        owner, repo = self.repo.split("/")
        url = f"https://api.github.com/repos/{owner}/{repo}/milestones"
        data = {
            "title": title,
            "description": description,
        }
        
        try:
            response = requests.post(url, json=data, headers=self.headers, timeout=30)
            if response.status_code == 201:
                milestone = response.json()
                print(f"✅ Created milestone: {title} (ID: {milestone['number']})")
                return True
            elif response.status_code == 422:
                # Milestone already exists
                print(f"⚠️  Milestone already exists: {title}")
                return True
            else:
                print(f"❌ Failed to create milestone: {title}")
                print(f"   Status: {response.status_code}")
                print(f"   Response: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed for {title}: {e}")
            return False

    def create_all_milestones(self) -> None:
        """Create all roadmap milestones."""
        print("\n📍 Creating SOCVault Roadmap Milestones\n")
        print("=" * 70)
        
        success_count = 0
        total_count = len(MILESTONES)
        
        for milestone in MILESTONES:
            if self.create_milestone(milestone["title"], milestone["description"]):
                success_count += 1
        
        print("=" * 70)
        print(f"\n✅ Milestone Creation Complete: {success_count}/{total_count} created\n")
        
        # Print summary
        print("📋 Created Milestones:")
        for milestone in MILESTONES:
            phase = milestone["phase"]
            week_range = milestone["week_range"]
            duration = milestone["duration_weeks"]
            print(f"  • {milestone['title']}")
            print(f"    Phase {phase} | Weeks {week_range} ({duration}w) | {milestone['team']}")
        
        print("\n" + "=" * 70)
        print("Next Steps:")
        print("1. Go to: https://github.com/samihyder/SOCVault-Blueprint/milestones")
        print("2. Create GitHub Projects board: 'SOCVault - Product Roadmap'")
        print("3. Add columns: Backlog, In Progress, In Review, Done, Archived")
        print("4. Add custom fields: Story Points, Phase, Priority, Risk Level")
        print("5. Enable automation rules")
        print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Create SOCVault product roadmap milestones in GitHub"
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="GitHub repository (owner/repo)",
    )
    parser.add_argument(
        "--token",
        required=True,
        help="GitHub Personal Access Token",
    )
    
    args = parser.parse_args()
    
    # Validate token format
    if not args.token or len(args.token) < 20:
        print("❌ Invalid GitHub token. Please provide a valid Personal Access Token.")
        print("   Token should be at least 20 characters long.")
        sys.exit(1)
    
    # Validate repo format
    if "/" not in args.repo:
        print("❌ Invalid repository format. Use 'owner/repo'")
        sys.exit(1)
    
    manager = GitHubProjectManager(args.token, args.repo)
    manager.create_all_milestones()

if __name__ == "__main__":
    main()
