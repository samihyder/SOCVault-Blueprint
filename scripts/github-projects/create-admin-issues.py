#!/usr/bin/env python3
"""
Script to auto-create all admin setup user stories in GitHub
Run: python3 scripts/github-projects/create-admin-issues.py --repo samihyder/SOCVault-Blueprint --token <GITHUB_TOKEN>
"""

import argparse
import json
import requests
from typing import List, Dict

class GitHubIssueCreator:
    def __init__(self, repo: str, token: str):
        self.repo = repo
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def create_milestone(self, title: str, description: str) -> Dict:
        """Create a GitHub milestone"""
        url = f"{self.base_url}/repos/{self.repo}/milestones"
        payload = {
            "title": title,
            "description": description,
            "state": "open"
        }
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def create_issue(self, title: str, body: str, milestone: str = None, labels: List[str] = None) -> Dict:
        """Create a GitHub issue"""
        url = f"{self.base_url}/repos/{self.repo}/issues"
        
        # Get milestone number if needed
        milestone_num = None
        if milestone:
            milestone_num = self._get_milestone_number(milestone)
        
        payload = {
            "title": title,
            "body": body,
            "labels": labels or []
        }
        if milestone_num:
            payload["milestone"] = milestone_num
        
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()
    
    def _get_milestone_number(self, milestone_title: str) -> int:
        """Get milestone number by title"""
        url = f"{self.base_url}/repos/{self.repo}/milestones"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        for milestone in response.json():
            if milestone["title"] == milestone_title:
                return milestone["number"]
        
        # If not found, create it
        print(f"⚠️ Milestone '{milestone_title}' not found. Creating it...")
        created = self.create_milestone(milestone_title, f"Admin setup milestone: {milestone_title}")
        return created["number"]

    def create_all_admin_issues(self):
        """Create all admin setup issues"""
        
        # Phase 0 Milestones
        phase0_milestones = [
            ("M0.1: AWS Account Setup & IAM", "Phase 0 - AWS Account Setup & IAM Configuration"),
            ("M0.2: Terraform IaC Foundation", "Phase 0 - Terraform IaC Foundation"),
            ("M0.3: Database Setup", "Phase 0 - Database Setup (MongoDB, DynamoDB)"),
            ("M0.4: Secrets Management", "Phase 0 - Secrets Management"),
            ("M0.5: Monitoring & Alerting", "Phase 0 - Monitoring & Alerting"),
            ("M0.6: Admin API Skeleton", "Phase 0 - Admin API Skeleton"),
        ]
        
        # Phase 1A Milestones
        phase1a_milestones = [
            ("M1.1: Super Admin User Management", "Phase 1A - Super Admin User Management"),
            ("M1.2: Tenant Management", "Phase 1A - Tenant Management"),
            ("M1.3: Admin Dashboard", "Phase 1A - Admin Dashboard"),
            ("M1.4: Audit Log Viewer", "Phase 1A - Audit Log Viewer"),
            ("M1.5: System Settings", "Phase 1A - System Settings"),
            ("M1.6: Admin API Documentation", "Phase 1A - Admin API Documentation"),
        ]
        
        all_milestones = phase0_milestones + phase1a_milestones
        
        print(f"📋 Creating {len(all_milestones)} milestones...")
        for title, desc in all_milestones:
            try:
                self.create_milestone(title, desc)
                print(f"  ✅ {title}")
            except Exception as e:
                print(f"  ⚠️ {title} - {str(e)}")
        
        # Phase 0 User Stories
        phase0_stories = [
            {
                "title": "US-ADM-001: Create AWS Organization & Accounts",
                "milestone": "M0.1: AWS Account Setup & IAM",
                "labels": ["infrastructure", "aws", "phase-0", "blocking"],
                "body": """### US-ADM-001: Create AWS Organization & Accounts

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

**Story Points:** 5  
**Priority:** CRITICAL"""
            },
            {
                "title": "US-ADM-002: Set Up IAM Roles & Policies",
                "milestone": "M0.1: AWS Account Setup & IAM",
                "labels": ["infrastructure", "security", "iam", "phase-0"],
                "body": """### US-ADM-002: Set Up IAM Roles & Policies

**As a** Security Engineer  
**I want to** configure IAM roles with principle of least privilege  
**So that** all system access follows security best practices

**Acceptance Criteria:**
- [ ] GitHub Actions role created
- [ ] Terraform execution role created
- [ ] Admin user role created
- [ ] Operator role created
- [ ] Viewer role created
- [ ] All roles enforce MFA
- [ ] All roles have 1-hour session duration
- [ ] All role assumptions logged to CloudTrail

**Story Points:** 8  
**Blocks:** M0.2, M0.3, M0.6"""
            },
            {
                "title": "US-ADM-003: Configure VPC with Multi-AZ Network",
                "milestone": "M0.1: AWS Account Setup & IAM",
                "labels": ["infrastructure", "networking", "phase-0"],
                "body": """### US-ADM-003: Configure VPC with Multi-AZ Network

**As a** DevOps Engineer  
**I want to** set up VPC with public/private subnets across 2 AZs  
**So that** we have high availability and proper network isolation

**Acceptance Criteria:**
- [ ] VPC created (CIDR: 10.0.0.0/16)
- [ ] 2 public subnets across 2 AZs
- [ ] 2 private subnets across 2 AZs
- [ ] NAT Gateway in each AZ
- [ ] Internet Gateway configured
- [ ] Route tables configured
- [ ] Security groups defined
- [ ] Network ACLs reviewed

**Story Points:** 13  
**Blocks:** M0.3, M0.5"""
            },
            {
                "title": "US-ADM-004: Initialize Terraform Project with Remote State",
                "milestone": "M0.2: Terraform IaC Foundation",
                "labels": ["infrastructure", "terraform", "phase-0"],
                "body": """### US-ADM-004: Initialize Terraform Project with Remote State

**As a** DevOps Engineer  
**I want to** set up Terraform with S3 backend and DynamoDB lock  
**So that** infrastructure state is secure and team changes are coordinated

**Acceptance Criteria:**
- [ ] Terraform project initialized
- [ ] S3 backend bucket created
- [ ] DynamoDB table created for state locking
- [ ] Backend configuration in terraform/backend.tf
- [ ] .terraformignore configured
- [ ] terraform.tfvars gitignored
- [ ] Workspaces created: staging, production
- [ ] All files validated (fmt, validate)

**Story Points:** 5  
**Depends On:** US-ADM-002"""
            },
            {
                "title": "US-ADM-005: Set Up MongoDB Atlas Cluster",
                "milestone": "M0.3: Database Setup",
                "labels": ["database", "mongodb", "phase-0", "blocking"],
                "body": """### US-ADM-005: Set Up MongoDB Atlas Cluster

**As a** Backend Engineer  
**I want to** configure MongoDB Atlas cluster with proper security  
**So that** we have a scalable, secure primary data store

**Acceptance Criteria:**
- [ ] MongoDB Atlas M0 cluster created
- [ ] Database user created
- [ ] IP whitelist configured
- [ ] Encryption at rest enabled (AWS KMS)
- [ ] Encryption in transit enabled (TLS 1.3)
- [ ] Automatic backups configured
- [ ] Monitoring enabled
- [ ] Connection string stored in Secrets Manager
- [ ] Test connection succeeds

**Story Points:** 8"""
            },
            {
                "title": "US-ADM-006: Create DynamoDB Tables",
                "milestone": "M0.3: Database Setup",
                "labels": ["database", "dynamodb", "phase-0"],
                "body": """### US-ADM-006: Create DynamoDB Tables

**As a** Backend Engineer  
**I want to** set up DynamoDB for high-write telemetry  
**So that** we can track costs and rate limits efficiently

**Acceptance Criteria:**
- [ ] cost_telemetry table created
- [ ] rate_limits table created
- [ ] TTL configured
- [ ] Encryption enabled
- [ ] Provisioned capacity configured
- [ ] Backup enabled
- [ ] CloudWatch alarms configured
- [ ] Tables accessible from Lambda

**Story Points:** 5"""
            },
            {
                "title": "US-ADM-007: Configure AWS Secrets Manager",
                "milestone": "M0.4: Secrets Management",
                "labels": ["security", "secrets", "phase-0", "blocking"],
                "body": """### US-ADM-007: Configure AWS Secrets Manager

**As a** Security Engineer  
**I want to** centralize all secrets in AWS Secrets Manager  
**So that** secrets are encrypted, rotatable, and auditable

**Acceptance Criteria:**
- [ ] KMS key created
- [ ] All secrets created and stored
- [ ] Automatic rotation enabled for passwords
- [ ] Lambda role permissions configured
- [ ] Secrets tagged properly
- [ ] CloudTrail logging enabled
- [ ] No secrets in Git history

**Story Points:** 5  
**Depends On:** US-ADM-002"""
            },
            {
                "title": "US-ADM-008: Configure CloudWatch Dashboards & Alarms",
                "milestone": "M0.5: Monitoring & Alerting",
                "labels": ["monitoring", "observability", "phase-0"],
                "body": """### US-ADM-008: Configure CloudWatch Dashboards & Alarms

**As a** DevOps Engineer  
**I want to** set up comprehensive monitoring  
**So that** we can detect and respond to issues quickly

**Acceptance Criteria:**
- [ ] CloudWatch dashboard created
- [ ] Alarms configured for key metrics
- [ ] Slack integration setup
- [ ] Email alerts configured
- [ ] Log groups configured (30-day retention)
- [ ] Metric filters created
- [ ] Dashboard shows: API, Lambda, MongoDB, DynamoDB metrics

**Story Points:** 8"""
            },
            {
                "title": "US-ADM-009: Initialize FastAPI Admin API Project",
                "milestone": "M0.6: Admin API Skeleton",
                "labels": ["backend", "api", "phase-0", "blocking"],
                "body": """### US-ADM-009: Initialize FastAPI Admin API Project

**As a** Backend Engineer  
**I want to** set up FastAPI project  
**So that** we have a foundation for admin endpoints

**Acceptance Criteria:**
- [ ] FastAPI project initialized
- [ ] requirements.txt configured
- [ ] main.py with app initialization
- [ ] config.py with environment configuration
- [ ] CORS configured
- [ ] Health check endpoint working
- [ ] Dockerfile created (Lambda-compatible)
- [ ] pytest structure set up
- [ ] GitHub Actions workflow working

**Story Points:** 5  
**Depends On:** US-ADM-004"""
            }
        ]
        
        print(f"\n📝 Creating {len(phase0_stories)} Phase 0 user stories...")
        for story in phase0_stories:
            try:
                self.create_issue(
                    title=story["title"],
                    body=story["body"],
                    milestone=story["milestone"],
                    labels=story["labels"]
                )
                print(f"  ✅ {story['title']}")
            except Exception as e:
                print(f"  ❌ {story['title']} - {str(e)}")
        
        # Phase 1A User Stories (abbreviated here, full in doc)
        phase1a_stories = [
            {
                "title": "US-ADM-010: Implement POST /admin/users (Create Super Admin)",
                "milestone": "M1.1: Super Admin User Management",
                "labels": ["backend", "admin-users", "phase-1a"],
                "body": """### US-ADM-010: Implement POST /admin/users

**As a** Super Admin  
**I want to** create new super admin users  
**So that** I can delegate admin responsibilities

**Acceptance Criteria:**
- [ ] Endpoint POST /admin/users implemented
- [ ] User created in Cognito
- [ ] User record created in MongoDB
- [ ] 2FA enforced
- [ ] Audit log entry created
- [ ] Integration test verifies user can log in
- [ ] Response includes user_id, email, created_at

**Story Points:** 8"""
            },
            {
                "title": "US-ADM-011: Implement POST /admin/tenants (Create Tenant)",
                "milestone": "M1.2: Tenant Management",
                "labels": ["backend", "tenant-management", "phase-1a"],
                "body": """### US-ADM-011: Implement POST /admin/tenants

**As a** Super Admin  
**I want to** create new tenants  
**So that** new customers can access SOCVault

**Acceptance Criteria:**
- [ ] Endpoint POST /admin/tenants implemented
- [ ] Tenant created in MongoDB
- [ ] Stripe customer created if paid tier
- [ ] Tenant ID (UUID) generated
- [ ] Default rate limits set
- [ ] Audit log entry created
- [ ] Response includes tenant_id, api_key, webhook_secret
- [ ] Integration test verifies creation

**Story Points:** 13"""
            },
            {
                "title": "US-ADM-012: Create Admin Dashboard React Component",
                "milestone": "M1.3: Admin Dashboard",
                "labels": ["frontend", "admin-dashboard", "phase-1a"],
                "body": """### US-ADM-012: Create Admin Dashboard UI

**As a** Admin User  
**I want to** see system overview  
**So that** I can monitor platform health at a glance

**Acceptance Criteria:**
- [ ] Dashboard component created
- [ ] Displays: tenants, users, scans, revenue, uptime
- [ ] Real-time metrics (10s update)
- [ ] Charts: tenant growth, revenue, scan volume
- [ ] Top alerts section
- [ ] Responsive design
- [ ] Jest tests (>80% coverage)
- [ ] Storybook stories created

**Story Points:** 13"""
            },
            {
                "title": "US-ADM-013: Implement GET /admin/audit-logs with Filtering",
                "milestone": "M1.4: Audit Log Viewer",
                "labels": ["backend", "frontend", "audit-logs", "phase-1a"],
                "body": """### US-ADM-013: Implement Audit Log Viewer

**As a** Compliance Officer  
**I want to** search and filter audit logs  
**So that** I can prove regulatory compliance

**Acceptance Criteria:**
- [ ] Endpoint GET /admin/audit-logs with filters
- [ ] Pagination: 50 per page
- [ ] Export to CSV
- [ ] Frontend: React table with sorting
- [ ] Audit data immutable
- [ ] Integration test queries MongoDB
- [ ] E2E test: Filter and export

**Story Points:** 13"""
            },
            {
                "title": "US-ADM-014: Implement GET/PUT /admin/settings",
                "milestone": "M1.5: System Settings",
                "labels": ["backend", "admin-settings", "phase-1a"],
                "body": """### US-ADM-014: System Settings Management

**As a** Super Admin  
**I want to** manage global settings  
**So that** I can control system behavior

**Acceptance Criteria:**
- [ ] Endpoint GET /admin/settings
- [ ] Endpoint PUT /admin/settings (super admin only)
- [ ] Settings stored in MongoDB, cached in Redis
- [ ] Audit log on every change
- [ ] Settings: rate limits, feature flags, maintenance mode
- [ ] All changes auditable

**Story Points:** 8"""
            },
            {
                "title": "US-ADM-015: Create Complete Admin API OpenAPI Specification",
                "milestone": "M1.6: Admin API Documentation",
                "labels": ["backend", "documentation", "openapi", "phase-1a"],
                "body": """### US-ADM-015: Document Admin API (OpenAPI)

**As a** Backend Engineer  
**I want to** maintain OpenAPI spec  
**So that** API consumers know contracts

**Acceptance Criteria:**
- [ ] OpenAPI 3.1 spec at api/openapi-admin.yaml
- [ ] All endpoints documented
- [ ] All schemas defined
- [ ] All status codes documented
- [ ] Authentication scheme documented
- [ ] Example requests/responses
- [ ] Swagger UI at /admin/api/docs
- [ ] ReDoc at /admin/api/redoc

**Story Points:** 5"""
            }
        ]
        
        print(f"\n📝 Creating {len(phase1a_stories)} Phase 1A user stories...")
        for story in phase1a_stories:
            try:
                self.create_issue(
                    title=story["title"],
                    body=story["body"],
                    milestone=story["milestone"],
                    labels=story["labels"]
                )
                print(f"  ✅ {story['title']}")
            except Exception as e:
                print(f"  ❌ {story['title']} - {str(e)}")
        
        print(f"\n✅ Completed! Created {len(all_milestones)} milestones and {len(phase0_stories) + len(phase1a_stories)} user stories")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create admin setup issues in GitHub")
    parser.add_argument("--repo", required=True, help="GitHub repo (owner/repo)")
    parser.add_argument("--token", required=True, help="GitHub token")
    
    args = parser.parse_args()
    
    creator = GitHubIssueCreator(args.repo, args.token)
    creator.create_all_admin_issues()
