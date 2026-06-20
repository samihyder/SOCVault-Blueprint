# SOCVault — Requirements Specification
**Version 1.1 | June 2026**

---

## 1. Functional Requirements

### 1.1 User Onboarding & Authentication

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-001 | System shall accept signup with only a business email and phone number | Must Have | 1 |
| FR-002 | System shall block registrations from free webmail domains (Gmail, Yahoo, Hotmail, Outlook, Live, iCloud, AOL) | Must Have | 1 |
| FR-003 | System shall extract and validate the company domain from the business email | Must Have | 1 |
| FR-004 | System shall send a 6-digit OTP to the provided phone number via SMS (AWS SNS) | Must Have | 1 |
| FR-005 | System shall provision a unique tenant workspace (UUID-based `tenant_id`) within 60 seconds of signup | Must Have | 1 |
| FR-006 | System shall return **Cognito-issued** JWT access and refresh tokens on OTP verification (token TTLs configured in Cognito User Pool per ADR-003; API Gateway validates via Cognito authorizer) | Must Have | 1 |
| FR-007 | System shall support MFA (TOTP authenticator app) as a second factor for Pro and Enterprise tiers | Should Have | 2 |
| FR-008 | System shall support password-less login (magic link to business email) as an alternative to OTP | Should Have | 2 |
| FR-009 | System shall support SSO (SAML 2.0 / OAuth 2.0) for Enterprise tier clients | Nice to Have | 3 |
| FR-010 | System shall enforce business domain verification — user must prove ownership of the domain they register | Must Have | 2 |
| FR-011 | System shall offer DNS TXT record domain verification with token format `_socvault-verify.{domain}` | Must Have | 2 |
| FR-012 | System shall offer HTML meta tag domain verification (`<meta name="socvault-verify" content="{token}">`) | Must Have | 2 |
| FR-013 | System shall poll for domain verification every 60 seconds until confirmed or 24-hour timeout | Must Have | 2 |
| FR-014 | System shall display a verified badge on the dashboard for each confirmed domain | Must Have | 2 |
| FR-015 | System shall block active scans (L2–L9) until domain ownership is verified; L1 passive recon permitted pre-verification | Must Have | 2 |
| FR-016 | System shall provide a guided Wazuh agent deployment wizard (install script, enrollment key, agent health check) | Must Have | 2 |
| FR-017 | System shall accept OpenAPI/Swagger spec upload for L4 API scans (JSON/YAML, max 5 MB) | Should Have | 2 |
| FR-018 | System shall support CI/CD webhook trigger for L3 mobile binary scans | Should Have | 3 |

### 1.2 Scanning Engine

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-019 | L1 Recon shall execute all 15 scanning steps: WHOIS, DNS analysis, email security (SPF/DKIM/DMARC), SSL/TLS audit, HTTP security headers, certificate transparency lookup, subdomain discovery, live host validation, port discovery (top 100), technology fingerprinting, IP reputation, domain reputation, credential leak check (HaveIBeenPwned), subdomain takeover detection, service banner analysis | Must Have | 1 |
| FR-020 | System shall execute Layer 2 Web AppSec scans (CVE detection, SAST, DAST, web shell detection) | Must Have | 2 |
| FR-022 | System shall execute Layer 3 Mobile binary analysis (Android APK, iOS IPA via MobSF) | Should Have | 2 |
| FR-023 | System shall execute Layer 4 API security scans (OWASP API Top 10) | Should Have | 2 |
| FR-024 | System shall execute Layer 5 Compliance gap analysis (PCI-DSS, GDPR, ISO 27001, SOC2) | Should Have | 2 |
| FR-024A | System shall accept PDF/DOCX policy uploads and gap-analyse against ISO 27001 controls via Claude AI | Should Have | 2 |
| FR-025 | System shall execute Layer 6 Cloud infrastructure penetration testing (AWS, Azure, GCP — IAM, storage, privilege escalation) | Should Have | 3 |
| FR-025A | L1 Recon shall fingerprint CMS platforms (WordPress/Joomla/Drupal), enumerate plugins passively, and flag abandoned plugins and version CVEs | Should Have | 2 |
| FR-026 | System shall enforce Freemium rate limit: exactly 1 Recon scan per calendar month per tenant | Must Have | 1 |
| FR-027 | System shall enforce per-IP/domain licensing: paid scans require a valid active licence for the target | Must Have | 2 |
| FR-028 | System shall require explicit user consent (scan authorisation checkbox) before executing any active scan | Must Have | 1 |
| FR-029 | System shall verify the scan target is within the tenant's registered domain (prevent scanning of 3rd-party targets) | Must Have | 2 |
| FR-030 | System shall run each scan in an isolated execution environment (no shared memory between tenants) | Must Have | 1 |
| FR-031 | System shall return scan status updates via polling endpoint within 5 seconds of status change | Must Have | 1 |
| FR-032 | System shall support concurrent scans (multiple layers simultaneously) for Pro and Enterprise tiers | Should Have | 3 |

### 1.3 AI Intelligence Layer

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-040 | System shall translate all scan findings into plain-English business risk summaries | Must Have | 1 |
| FR-041 | System shall calculate a quantified financial exposure estimate (USD) for each identified vulnerability | Must Have | 1 |
| FR-042 | System shall calculate an estimated remediation timeline (hours/days) per vulnerability | Must Have | 1 |
| FR-043 | System shall generate a Workspace Health Score (0–100) for each scan | Must Have | 1 |
| FR-044 | System shall generate copy-pasteable remediation scripts for each identified vulnerability | Must Have | 1 |
| FR-045 | System shall use Anthropic Claude API (not Gemini) for all AI reasoning | Must Have | 1 |
| FR-046 | System shall implement prompt caching for system prompts to reduce AI API costs | Should Have | 2 |
| FR-047 | System shall fall back to a pre-defined offline report if the AI API is unavailable | Must Have | 1 |
| FR-048 | System shall gate AI-generated remediation scripts behind the paid tier (Freemium sees threat summary only) | Must Have | 2 |
| FR-049 | System shall include a confidence score for each AI-generated finding | Should Have | 2 |
| FR-050 | System shall map each finding to MITRE ATT&CK technique ID and name with link to attack.mitre.org | Should Have | 2 |
| FR-051 | System shall generate monthly executive summary reports (health trend, exposure delta, PDF/DOCX) | Should Have | 2 |
| FR-052 | System shall provide an ATT&CK technique heatmap aggregated across tenant findings | Should Have | 3 |

### 1.4 SOAR (Security Orchestration, Automation, and Response)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-060 | System shall ingest Wazuh alerts at severity level 10 and above | Must Have | 2 |
| FR-061 | System shall enrich every alert IP with threat intelligence (AbuseIPDB, AlienVault OTX) | Must Have | 2 |
| FR-062 | System shall route each enriched alert through Claude AI triage (contain vs escalate decision) | Must Have | 2 |
| FR-063 | System shall automatically execute the "CONTAIN" playbook for low-risk confirmed threats | Must Have | 2 |
| FR-064 | System shall route high-risk decisions to a human approval queue with full context | Must Have | 2 |
| FR-065 | System shall support the following default playbooks: Ransomware Containment, SSH Brute-Force Block, Phishing Email Purge | Must Have | 2 |
| FR-066 | System shall allow Pro/Enterprise clients to define custom SOAR playbooks | Should Have | 3 |
| FR-067 | System shall send real-time notifications (email, Slack, SMS) for every incident created | Must Have | 2 |
| FR-068 | System shall maintain a full audit trail of all SOAR actions taken | Must Have | 2 |
| FR-069 | System shall allow human operators to approve or reject any queued playbook execution | Must Have | 2 |
| FR-06A | System shall allow IT managers to mark Wazuh alerts as false positives with reason and suppress rule for 30 days | Should Have | 2 |

### 1.5 Dashboard & Reporting

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-090 | System shall display a real-time Workspace Health Score on the dashboard | Must Have | 1 |
| FR-091 | System shall display total financial exposure in USD/GBP on the dashboard | Must Have | 1 |
| FR-092 | System shall display a prioritised list of vulnerabilities ranked by financial impact | Must Have | 1 |
| FR-093 | System shall display historical scan results with 12-month health score trend lines | Should Have | 2 |
| FR-094 | System shall display a compliance posture map (PCI-DSS, GDPR, ISO 27001, SOC2, CE+) | Should Have | 2 |
| FR-095 | System shall allow users to download PDF executive reports | Should Have | 2 |
| FR-096 | System shall display an incident feed for SOAR events | Must Have | 2 |
| FR-097 | System shall support white-label reporting (custom logo and brand colours) for Enterprise tier | Nice to Have | 3 |
| FR-098 | System shall display admin telemetry (COGS per scan, total accumulated cost, margin) for admin users | Must Have | 1 |
| FR-099 | System shall display anonymised industry benchmark comparison (opt-in tenants only) | Should Have | 3 |

### 1.6 Billing & Subscription

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-100 | System shall integrate Stripe for subscription management and payment processing | Must Have | 2 |
| FR-101 | System shall automatically gate paid features based on tenant subscription tier | Must Have | 2 |
| FR-102 | System shall send invoice emails via Stripe on successful payment | Must Have | 2 |
| FR-103 | System shall handle failed payments with a 7-day grace period before service downgrade | Must Have | 2 |
| FR-104 | System shall provide a self-service billing portal (Stripe Customer Portal) | Should Have | 2 |
| FR-105 | System shall calculate variable costs per scan and maintain per-tenant COGS records | Must Have | 1 |
| FR-106 | System shall prevent scans that would exceed a pre-set budget cap (configurable by admin) | Should Have | 3 |

### 1.7 Malware Detection & Response Engine (L8 — SOC Pro)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-070 | System shall detect malware via Wazuh ClamAV integration on all enrolled SOC Pro endpoints | Must Have | 2 |
| FR-071 | System shall detect malware via Wazuh File Integrity Monitoring (FIM) flagging new or modified executable files | Must Have | 2 |
| FR-072 | System shall detect web shells during L2 Web AppSec scans using Nuclei webshell detection templates | Must Have | 2 |
| FR-073 | System shall detect malicious container image layers via Trivy scanning (L2 paid tier) | Should Have | 3 |
| FR-074 | System shall enrich every malware detection event with VirusTotal hash lookup and local YARA rule match | Must Have | 2 |
| FR-075 | System shall send every confirmed malware detection event to Claude AI (claude-sonnet-4-6) for analysis | Must Have | 2 |
| FR-076 | Claude AI shall determine: malware family, severity score (1–10), lateral movement risk, data exfiltration likelihood | Must Have | 2 |
| FR-077 | Claude AI shall generate: quarantine command, removal command, persistence cleanup steps, IOC list, post-remediation verification command | Must Have | 2 |
| FR-078 | System shall AUTO-REMEDIATE when confidence >95% and threat is an isolated file or process (quarantine to /var/ossec/quarantine/, kill process, update blocklist) | Must Have | 2 |
| FR-079 | System shall route to HUMAN APPROVAL GATE when remediation affects core services, databases, or requires host isolation | Must Have | 2 |
| FR-080 | System shall send immediate Slack + email + dashboard notification for every malware detection event | Must Have | 2 |
| FR-081 | System shall run a post-remediation re-scan to confirm successful removal | Must Have | 2 |
| FR-082 | System shall generate a malware incident report (malware family, affected files, actions taken, clean bill of health) | Must Have | 2 |
| FR-083 | System shall update the Workspace Health Score after confirmed malware remediation | Must Have | 2 |
| FR-084 | Malware Detection & Response module shall be restricted to SOC Pro and Enterprise tiers only | Must Have | 2 |
| FR-085 | System shall maintain an audit log of all quarantine and removal actions with actor, timestamp, and file hash | Must Have | 2 |

---

## 2. Non-Functional Requirements

### 2.1 Performance

| ID | Requirement | Target |
|---|---|---|
| NFR-001 | API response time (p95, excluding scan execution) | <500ms |
| NFR-002 | Recon scan end-to-end duration (user journey: signup → OTP → scan → report visible) | <3 minutes |
| NFR-002a | L1 scan pipeline execution (15 parallel steps in Lambda) | <90 seconds |
| NFR-003 | Full VAPT scan end-to-end duration | <15 minutes |
| NFR-004 | Dashboard initial page load | <2 seconds |
| NFR-005 | SOAR alert-to-triage cycle time | <60 seconds |
| NFR-006 | System shall support 100 concurrent API requests without degradation | 100 RPS |
| NFR-007 | Scan queue shall process 50 concurrent scan tasks | 50 simultaneous |

### 2.2 Reliability

| ID | Requirement | Target |
|---|---|---|
| NFR-010 | Platform uptime SLA (MVP) | 99.5% |
| NFR-011 | Platform uptime SLA (Production) | 99.9% |
| NFR-012 | System shall recover from scanner binary failure without crashing the API | Must Have |
| NFR-013 | System shall retry failed AI API calls with exponential backoff (5 attempts) | Must Have |
| NFR-014 | System shall maintain a fallback response for all AI features during outage | Must Have |
| NFR-015 | Database shall have daily automated backups with 30-day retention | Must Have |
| NFR-016 | System shall have multi-AZ redundancy for all stateful components | Must Have (Prod) |

### 2.3 Security

| ID | Requirement | Target |
|---|---|---|
| NFR-020 | All API endpoints shall require valid JWT authentication (except signup/verify) | Must Have |
| NFR-021 | All data in transit shall use TLS 1.3 minimum | Must Have |
| NFR-022 | All data at rest shall be encrypted (AES-256) | Must Have |
| NFR-023 | CORS shall be restricted to approved origins only (never `*` in production) | Must Have |
| NFR-024 | All API inputs shall be validated via Pydantic strict models | Must Have |
| NFR-025 | Scan targets shall be validated against tenant's registered domains | Must Have |
| NFR-026 | No credentials or secrets shall exist in source code or environment files | Must Have |
| NFR-027 | Rate limiting shall be applied per IP and per tenant on all endpoints | Must Have |
| NFR-028 | All administrative actions shall be logged with actor, timestamp, and action | Must Have |
| NFR-029 | System shall pass OWASP Top 10 review before production launch | Must Have |
| NFR-030 | System shall implement Content Security Policy (CSP) on the frontend | Must Have |

### 2.4 Compliance

| ID | Requirement | Target |
|---|---|---|
| NFR-040 | System shall comply with UK GDPR and maintain a Data Processing Agreement template | Must Have |
| NFR-041 | UK/EU customer data shall be stored exclusively in AWS eu-west-2 (London) | Must Have |
| NFR-042 | System shall provide a mechanism for customers to request data deletion (right to erasure) | Must Have |
| NFR-043 | System shall maintain an audit log of all scan actions with 12-month retention | Must Have |
| NFR-044 | System shall not store raw customer infrastructure credentials | Must Have |
| NFR-045 | System shall obtain and store explicit scan authorisation consent before executing any active scan | Must Have |

### 2.5 Scalability

| ID | Requirement | Target |
|---|---|---|
| NFR-050 | System shall scale horizontally without code changes | Must Have |
| NFR-051 | New tenant workspaces shall be provisioned without any manual steps | Must Have |
| NFR-052 | Scan execution shall scale from 0 to 50 concurrent tasks automatically | Must Have |
| NFR-053 | Database shall handle 10,000 tenants without schema migrations | Must Have |

### 2.6 Observability

| ID | Requirement | Target |
|---|---|---|
| NFR-060 | All services shall emit structured JSON logs | Must Have |
| NFR-061 | All API endpoints shall emit latency, error rate, and request count metrics | Must Have |
| NFR-062 | System shall alert on-call on >1% error rate sustained for 5 minutes | Must Have |
| NFR-063 | System shall alert on AI API cost exceeding $50/day | Must Have |
| NFR-064 | System shall provide a real-time admin dashboard for COGS and revenue metrics | Must Have |
| NFR-066 | Tenant data deletion (`DELETE /api/v1/account`) shall complete within 30 days per GDPR | Must Have |

---

## 3. User Stories

### 3.1 SMB Owner / Non-Technical User

```
AS AN SMB owner
I WANT TO sign up with just my work email and phone number
SO THAT I can access security scanning without lengthy procurement

AS AN SMB owner
I WANT TO see my security posture in plain English with a financial risk figure
SO THAT I can understand what's at risk without needing a security background

AS AN SMB owner
I WANT TO receive one-click remediation scripts for each vulnerability
SO THAT my developer can fix issues immediately

AS AN SMB owner
I WANT TO see a compliance status dashboard (GDPR, PCI-DSS)
SO THAT I know where my business stands before an audit
```

### 3.2 IT Manager / Technical User

```
AS AN IT Manager
I WANT TO trigger scans across multiple layers (Recon, AppSec, Cloud) for my domain
SO THAT I have comprehensive visibility of my attack surface

AS AN IT Manager
I WANT TO deploy Wazuh agents on our servers
SO THAT I have continuous real-time threat detection

AS AN IT Manager
I WANT TO review and approve SOAR playbook executions
SO THAT automated containment only runs with my authorisation for critical actions

AS AN IT Manager
I WANT TO integrate SOCVault alerts with our Slack workspace
SO THAT my team receives instant incident notifications
```

### 3.3 SOCVault Admin

```
AS A SOCVault admin
I WANT TO see per-tenant COGS and revenue metrics in real time
SO THAT I can monitor platform profitability at the unit economics level

AS A SOCVault admin
I WANT TO configure per-tenant AI cost caps
SO THAT a single heavy user cannot exhaust our API budget

AS A SOCVault admin
I WANT TO flag false-positive-prone scan rules for review
SO THAT I can improve scan accuracy over time
```

---

### 1.8 Scan Rate Limiting (All Modules Except L7 & L8)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-110 | For paid tiers, system shall enforce max 2 L1 Recon and L4 API scans per 7-day rolling window per tenant. Freemium L1 governed by FR-026 | Must Have | 2 |
| FR-111 | L2 Web AppSec scan shall be additionally restricted to 1 scan per 15 calendar days per tenant (industry standard for active DAST/SAST) | Must Have | 2 |
| FR-112 | L3 Mobile binary analysis shall be restricted to 1 scan per 15 calendar days per tenant | Must Have | 2 |
| FR-113 | L6 Cloud Pentest shall be restricted to 1 scan per 15 calendar days per tenant (invasive IAM/privilege escalation probing) | Must Have | 2 |
| FR-114 | L5 Compliance analysis shall be restricted to 1 scan per 30 calendar days per tenant (framework posture does not change more frequently) | Should Have | 2 |
| FR-115 | L9 AI Agent Scan shall be restricted to 1 scan per 7 calendar days per tenant | Must Have | 2 |
| FR-116 | L7 SOC/SIEM and L8 Malware D&R shall be exempt from rate limiting as they are continuous monitoring modules, not triggered scans | Must Have | 2 |
| FR-117 | System shall display a real-time countdown on each scan module showing when the next scan is available | Must Have | 2 |
| FR-118 | System shall send an in-app and email notification when a rate-limited scan window resets and becomes available | Should Have | 3 |
| FR-119 | SOCVault Superadmin shall be able to override scan rate limits for any individual tenant with audit justification required | Must Have | 2 |
| FR-120 | Rate limit state shall survive service restarts (persisted in **DynamoDB** on MVP; ElastiCache optional at paid tier) with `tenant_id` + module key | Must Have | 2 |

**Scan Rate Limit Summary Table:**

| Module | Tier | Rate Limit | Reasoning |
|---|---|---|---|
| L1 — Recon | Freemium | 1 per calendar month | Per FR-026 — acquisition tier |
| L1 — Recon | Paid | 2 per 7 days | Passive rescan for licensed tenants |
| L2 — Web AppSec | Paid | 1 per 15 days | Active DAST/SAST, invasive |
| L3 — Mobile | Paid | 1 per 15 days | Binary analysis, moderate compute |
| L4 — API Security | Paid | 2 per week | Targeted, lightweight |
| L5 — Compliance | Paid | 1 per 30 days | Framework posture is stable |
| L6 — Cloud Pentest | Paid | 1 per 15 days | Invasive IAM probing |
| L7 — SOC/SIEM | SOC Pro | Exempt | Continuous monitoring |
| L8 — Malware D&R | SOC Pro | Exempt | Real-time detection |
| L9 — AI Agent Scan | SOC Pro | 1 per 7 days | Expensive AI compute |

---

### 1.9 L9 — AI Agent Security Scan (Claude Security)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-125 | System shall provide an L9 AI Agent Scan module powered by Claude Security for autonomous application security assessment | Must Have | 2 |
| FR-126 | L9 shall accept a target application URL, a scan scope selection (auth, session, business logic, input validation, etc.), and an agent depth setting | Must Have | 2 |
| FR-127 | The L9 AI Agent shall operate autonomously — iteratively probing the target, reasoning about findings, and self-directing follow-up checks without manual input | Must Have | 2 |
| FR-128 | L9 shall display a live agent activity log showing each reasoning step (THINK), tool call (TOOL), finding (FIND), and completion (DONE) in real time | Must Have | 2 |
| FR-129 | L9 agent shall be powered by claude-opus-4-8 with extended thinking enabled for deep reasoning | Must Have | 2 |
| FR-130 | L9 shall produce a structured findings report (severity, OWASP category, CWE, confidence score, financial exposure, AI-generated remediation) identical in format to other scan layers | Must Have | 2 |
| FR-131 | L9 shall require explicit scan authorisation consent (checkbox with audit timestamp) before the agent begins any active probing | Must Have | 2 |
| FR-132 | L9 agent token usage and cost shall be tracked against the tenant's AI cost cap in real time | Must Have | 2 |
| FR-133 | L9 shall be available to SOC Pro and Enterprise tiers only | Must Have | 2 |
| FR-134 | L9 agent transcript (full reasoning log) shall be exportable as a JSON/PDF artefact | Should Have | 2 |
| FR-135 | L9 scan target must be within the tenant's registered domain (same validation as other layers) | Must Have | 2 |

---

### 1.10 Tenant Sub-User & Team Management

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-140 | Each tenant workspace shall support exactly 3 named sub-user slots: 1 Support Sub-Tenant, 1 Viewer-Only Executive, 1 Manager | Must Have | 2 |
| FR-141 | Support Sub-Tenant role shall have read-only access to dashboards and reports and may raise support tickets on behalf of the tenant. Cannot trigger scans, modify settings, or view billing | Must Have | 2 |
| FR-142 | Viewer-Only Executive role shall have read-only access to all dashboards and the ability to download PDF reports. Cannot trigger scans, modify settings, or view billing | Must Have | 2 |
| FR-143 | Manager role shall have full operational access: trigger scans (all layers), manage settings, approve SOAR playbooks, deploy Wazuh agents, view billing summary. Cannot delete the account or change payment method | Must Have | 2 |
| FR-144 | The tenant Owner may revoke or re-invite any sub-user at any time | Must Have | 2 |
| FR-145 | Sub-user invitations shall be delivered to a business email address and expire after 48 hours if not accepted | Must Have | 2 |
| FR-146 | Free-webmail addresses shall be rejected for sub-user invitations (same domain validation as tenant signup) | Must Have | 2 |
| FR-147 | All sub-user actions shall be recorded in the tenant's Audit Log with the sub-user's identity, role, action, and timestamp | Must Have | 2 |
| FR-148 | Sub-users shall authenticate using their own credentials; they shall not share the owner's credentials | Must Have | 2 |
| FR-149 | Sub-user slots shall be displayed in the Tenant Settings page with clear filled/empty/pending states | Must Have | 2 |

---

### 1.11 SOCVault Internal Team Administration & RBAC

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-150 | SOCVault Superadmin shall be able to create named internal teams and assign members within the Admin Console | Must Have | 2 |
| FR-151 | System shall support 12 granular internal roles: SOC L1, SOC L2, SOC L3, SOC L4, GRC Analyst, VA/PT Engineer, Recon & Enumeration, DevOps, SystemOps, Billing, Executive, Manager | Must Have | 2 |
| FR-152 | SOC L1 role shall have: alert triage queue (view & escalate), read-only incident details | Must Have | 2 |
| FR-153 | SOC L2 role shall include all L1 permissions plus: full incident analysis, playbook recommendation review | Must Have | 2 |
| FR-154 | SOC L3 role shall include all L2 permissions plus: playbook execution approval, tenant SOAR config | Must Have | 2 |
| FR-155 | SOC L4 role shall include all L3 permissions plus: cross-tenant threat hunting, full platform read access, Metrics Observatory (limited) | Must Have | 2 |
| FR-156 | GRC Analyst role shall have: compliance report access for all tenants, framework gap analysis, policy tooling | Must Have | 2 |
| FR-157 | VA/PT Engineer role shall have: scan execution for all tenants (L1–L9), findings management, report generation | Must Have | 2 |
| FR-158 | Recon & Enumeration role shall have: L1 scan access for all tenants, asset discovery, passive OSINT | Must Have | 2 |
| FR-159 | DevOps role shall have: Fargate/ECS task management, deployment pipeline access, infrastructure config | Must Have | 2 |
| FR-160 | SystemOps role shall have: platform health dashboard, MongoDB ops, Redis ops, SSL certificate management | Must Have | 2 |
| FR-161 | Billing role shall have: Stripe dashboard, invoice management, per-tenant COGS, revenue reporting, AWS cost data | Must Have | 2 |
| FR-162 | Executive role shall have: read-only access to all platform KPIs, MRR/revenue dashboards, aggregate threat landscape reports | Must Have | 2 |
| FR-163 | Manager role shall have: full SOCVault Admin Console access, team provisioning, all Metrics Observatory access. Cannot delete team members | Must Have | 2 |
| FR-164 | New team provisioning shall complete in under 2 minutes end-to-end (invitations dispatched, roles assigned) | Must Have | 3 |
| FR-165 | All internal role assignments and revocations shall be audit-logged with actor, timestamp, target member, and written justification | Must Have | 2 |
| FR-166 | All internal SOCVault team members shall have MFA enrolled (TOTP or hardware key) within 24h of account creation | Must Have | 2 |

---

### 1.12 Metrics Observatory (SOCVault Admin)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-170 | Metrics Observatory shall display real-time AWS cost breakdown by service (**Lambda, API Gateway, SQS** on MVP; plus Fargate/EKS, ElastiCache at paid tier; MongoDB Atlas, S3, SNS, Cognito) sourced from AWS Cost Explorer API | Must Have | 2 |
| FR-171 | Metrics Observatory shall display Claude AI API usage: input tokens, output tokens, cost per day/week/month, per-feature breakdown (scan analysis, SOAR, AI chat, L9 agent, financial reports), model distribution | Must Have | 2 |
| FR-172 | Metrics Observatory shall display prompt caching savings (actual cost vs non-cached equivalent) and current cache hit rate | Should Have | 2 |
| FR-173 | Metrics Observatory shall display API performance metrics: p50/p95/p99 latency, error rate (5min rolling), request volume per endpoint, status code distribution | Must Have | 2 |
| FR-174 | Metrics Observatory shall display compute metrics: **Lambda concurrency, duration, errors** (MVP); **Fargate/EKS** CPU, memory, task count at paid tier | Must Have | 2 |
| FR-175 | Metrics Observatory shall display application metrics: scan volume by layer, scan success rate, scan duration percentiles, queue depth, rate-limit enforcement events | Must Have | 2 |
| FR-176 | Metrics Observatory shall display system health: MongoDB connection count, IOPS, storage used; **SQS queue depth** (MVP); ElastiCache memory at paid tier; S3 request volume; network egress; SSL certificate expiry | Must Have | 2 |
| FR-177 | Metrics Observatory shall provide nano-level drill-down: any API request can be opened to show the full per-request trace (auth middleware → rate limiter → handler → DB queries → Claude API call → response time breakdown) | Must Have | 3 |
| FR-178 | Metrics Observatory shall include an API Settings panel: rate limit configuration per endpoint group, CORS allowed origins management, active API key inventory, Claude model configuration per feature | Must Have | 2 |
| FR-179 | All Metrics Observatory thresholds shall be configurable and trigger notifications via PagerDuty (critical), Slack (high), and email (medium) on breach | Must Have | 3 |
| FR-180 | Metrics Observatory shall display a 30-day rolling cost forecast for AWS and Claude AI at current burn rate, with a configured monthly budget ceiling and visual usage gauge | Should Have | 3 |
| FR-181 | Metrics Observatory shall auto-refresh all metrics every 30 seconds without requiring a page reload | Must Have | 2 |
| FR-182 | Metrics Observatory access shall be controlled by the internal RBAC system (roles: DevOps, SystemOps, Manager access to full view; Billing to cost panels only; SOC L4 and Executive to read-only aggregate views) | Must Have | 2 |

---

### 1.13 AI Chat Assistant (Credit-Based)

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-183 | System shall provide a conversational AI Chat interface embedded in the tenant dashboard (wireframe: `12-ai-chat.html`) | Must Have | 3 |
| FR-184 | AI Chat shall use Claude (`claude-sonnet-4-6`) with tenant context (domain, findings, health score, scan history) | Must Have | 3 |
| FR-185 | Tenants shall pre-purchase AI credits via Stripe; chat and actions blocked when balance is zero | Must Have | 3 |
| FR-186 | System shall maintain `credits` balance and `credit_transactions` ledger per tenant in DynamoDB | Must Have | 3 |
| FR-187 | System shall reserve credits before AI actions and confirm/release after completion | Must Have | 3 |
| FR-188 | `POST /api/v1/ai/chat` shall accept natural-language queries and return streaming responses | Must Have | 3 |
| FR-189 | Claude responses may embed `[ACTION:type]` markers; UI shall render actionable cards with credit cost | Must Have | 3 |
| FR-190 | `POST /api/v1/ai/action` shall dispatch actions to scan queues, SOAR, compliance, and report generators | Must Have | 3 |
| FR-191 | System shall store last 20 chat messages per tenant (30-day TTL) | Should Have | 3 |
| FR-192 | AI Chat shall rate-limit to 10 queries/minute/tenant regardless of credit balance | Must Have | 3 |
| FR-193 | Extended thinking mode shall be available for complex security questions (budget_tokens: 8000) | Should Have | 3 |

---

### 1.14 Super Admin API Explorer & Pass & Keys Vault

In-app alternative to Bruno/Postman for SOCVault internal staff. Synced from [`api/openapi.yaml`](../api/openapi.yaml). Wireframe: `24-admin-api-explorer.html`.

**Implementation build order (Milestone 2.9):** catalog sync → proxy test runner → encrypted vault → PIN step-up → React screen. See [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md).

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-194 | Super Admin shall provide an **API Explorer** listing all platform endpoints grouped by OpenAPI tags (Auth, Scan, Dashboard, Admin, etc.) | Must Have | 2 |
| FR-195 | Each endpoint row shall expose **Send Test Request** with configurable method, path params, query, headers, and JSON body | Must Have | 2 |
| FR-196 | Test execution shall run server-side (proxy) from the admin backend — secrets never sent to the browser console in plain text in production logs | Must Have | 2 |
| FR-197 | Results panel shall show **success** (2xx) or **failure** (4xx/5xx/network) with HTTP status, latency ms, response headers, and formatted JSON body — equivalent to try/catch visibility for operators | Must Have | 2 |
| FR-198 | On failure, results shall include `error_type` (HTTP_ERROR, TIMEOUT, VALIDATION, NETWORK), `message`, and optional `stack_trace` (dev/staging only; redacted in production) | Must Have | 2 |
| FR-199 | **Pass & Keys** vault shall store reusable variables: `access_token`, `refresh_token`, `tenant_id`, `scan_id`, API keys (Anthropic, Stripe, AWS), webhook secrets, DB passwords — keyed by name | Must Have | 2 |
| FR-200 | Variables shall **auto-save** when an API test response contains mappable fields (e.g. `access_token` from verify-otp, `scan_id` from scan execute) with user confirm or auto-save toggle | Must Have | 2 |
| FR-201 | All vault values shall display masked by default (`••••••••`); **Reveal** and **Copy** require Super Admin **PIN or password** re-auth (step-up) | Must Have | 2 |
| FR-202 | Step-up unlock session shall expire after **5 minutes** of inactivity; re-prompt on next reveal/copy | Must Have | 2 |
| FR-203 | Vault secrets shall be encrypted at rest (AES-256 via AWS KMS); platform never returns decrypted values except in step-up authenticated reveal/copy responses | Must Have | 2 |
| FR-204 | Every reveal, copy, create, update, and delete of vault entries shall be audit-logged (actor, timestamp, key name — never the value) | Must Have | 2 |
| FR-205 | API Explorer access shall be restricted to internal roles: **Manager, DevOps, SystemOps, VA/PT Engineer**; Pass & Keys write access: **Manager, DevOps** only | Must Have | 2 |
| FR-206 | Explorer shall support environment profiles: **`mock`** (Prism contract check), **`staging`** (primary), **`production`** (smoke only) — each with distinct `base_url` and variable namespace; no `local` runtime profile | Should Have | 2 |
| FR-207 | Operators may save named **request presets** (body + headers) linked to an endpoint for regression re-runs | Should Have | 3 |

**Variable auto-map rules (default):**

| Response path | Vault key |
|---|---|
| `access_token` | `access_token` |
| `refresh_token` | `refresh_token` |
| `tenant_id` | `tenant_id` |
| `scan_id` | `scan_id` |

---

### 1.15 Super Admin Development Tracker UI

In-app mirror of [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) for internal product and infrastructure progress. Wireframe: `25-admin-dev-tracker.html`. Combines stack live status, INF/DEV/API checklists, phase progress, and action log.

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-208 | Super Admin shall display a **Stack Live Status** matrix (**Blueprint repo**, **Staging**, **Production dormant**) for each platform layer (Amplify, API Gateway + Lambda, Atlas, SQS, L1 Lambda, Cognito, S3, etc.) | Must Have | 2 |
| FR-209 | Super Admin shall provide editable **Infrastructure (INF)** and **Dev stack (DEV)** checklists synced to roadmap/AWS setup IDs; status values: not started, in progress, live, blocked, spec only | Must Have | 2 |
| FR-210 | Super Admin shall allow **Log Action** form: category, ref ID, summary, result (verified/partial/blocked); auto-assigns next `ACT-###` and timestamps actor | Must Have | 2 |
| FR-211 | Super Admin shall display filterable **Action Log** (newest first) matching repo `DEVELOPMENT_TRACKER.md` format | Must Have | 2 |
| FR-212 | Super Admin shall show **Phase & milestone progress** bars with next recommended action and one-click mark-done | Must Have | 2 |
| FR-213 | System may run optional **stack health probes** (health endpoint, Atlas ping, S3, Lambda) to auto-update live status cells | Should Have | 2 |
| FR-214 | Tracker data shall persist in MongoDB (`dev_tracker_items`, `dev_tracker_actions`); **Export markdown** regenerates `DEVELOPMENT_TRACKER.md` for git commit | Must Have | 2 |
| FR-215 | Tracker access: **Manager, DevOps, SystemOps** read+write; **VA/PT, Billing, Executive** read-only; all mutations audit-logged | Must Have | 2 |

**Admin route:** `/admin/development-tracker`

---

### 1.16 External Threat Intelligence API Registry

Central registry of free/freemium external APIs per scanning layer. All API keys configured in **Super Admin Pass & Keys**; runtime calls via `ThreatIntelManager`. Full catalogue: [`20_FREE_EXTERNAL_APIS.md`](./20_FREE_EXTERNAL_APIS.md).

| ID | Requirement | Priority | Phase |
|---|---|---|---|
| FR-216 | System shall maintain a **Threat Intel Feed Registry** listing all external APIs by layer (L1–L9), provider, free-tier limit, and enabled status | Must Have | 2 |
| FR-217 | Super Admin shall store external API keys in Pass & Keys vault using `ti_{provider}_{env}` naming; keys encrypted at rest (FR-203) | Must Have | 2 |
| FR-218 | `ThreatIntelManager` shall expose enrichment intents: `enrich_ip`, `lookup_domain`, `lookup_url`, `lookup_hash`, `lookup_cve` — scanners call by intent, not raw provider URL | Must Have | 2 |
| FR-219 | All enrichment results shall normalise to `EnrichmentRecord` schema and cache in DynamoDB `ti_cache` with configurable TTL | Must Have | 2 |
| FR-220 | System shall enforce per-provider daily rate limits aligned to free tiers; defer to queue when quota exceeded; never fail primary scan | Must Have | 2 |
| FR-221 | L1 Recon shall integrate at minimum: crt.sh, AbuseIPDB, HIBP, URLhaus, Google Safe Browsing (or URLhaus fallback), Spamhaus DROP lists | Must Have | 1 |
| FR-222 | L2–L4 shall enrich CVE findings via NIST NVD and OSV.dev; prioritise with EPSS and CISA KEV feed | Must Have | 2 |
| FR-223 | L7 SOC alerts shall enrich source IPs with AbuseIPDB, AlienVault OTX, and GreyNoise (when enabled) before Claude triage | Must Have | 2 |
| FR-224 | L8 malware events shall enrich hashes via local YARA/ClamAV first, then MalwareBazaar and VirusTotal | Must Have | 2 |
| FR-225 | **CorrelationEngine** shall cluster enrichment records by IOC value across layers within 72h; raise tenant risk score when ≥2 layers hit same IOC | Must Have | 2 |
| FR-226 | Super Admin shall provide `GET /admin/ti/feeds`, `POST /admin/ti/feeds/{id}/test`, and usage stats for quota monitoring | Must Have | 2 |
| FR-227 | Scan and incident reports shall include `enrichment_summary` and `patterns_detected` for Claude financial-risk translation | Must Have | 2 |
| FR-228 | Platform-wide anonymised IOC frequency (≥5 tenants) shall surface in Metrics Observatory as early-warning signal | Should Have | 3 |
| FR-229 | Daily snapshots of keyless feeds (CISA KEV, Spamhaus, Feodo) shall sync to S3 for offline fallback | Should Have | 2 |

---

## 4. Acceptance Criteria (MVP Definition of Done)

The MVP (Minimum Viable Product) is considered complete when:

- [ ] A user can sign up with a business email and phone number in under 60 seconds
- [ ] The system rejects Gmail, Yahoo, and other free webmail providers
- [ ] An OTP is delivered to the user's phone and must be verified before access
- [ ] A Freemium user can execute exactly one Recon scan per month against their domain
- [ ] Scan results include a Workspace Health Score and financial exposure figure
- [ ] All scan findings are translated into plain-English by Claude AI
- [ ] A remediation script is provided for each finding (behind paywall for Freemium)
- [ ] Admin telemetry endpoint shows accurate COGS per scan
- [ ] The React dashboard loads and displays scan results correctly
- [ ] All API endpoints return 401 without valid JWT
- [ ] CORS is restricted to approved origins
- [ ] Scan execution is isolated per tenant
- [ ] All secrets are stored in AWS SSM / Secrets Manager per workspace (no hardcoded credentials)
- [ ] CI/CD deploys to staging on merge; production requires promotion
- [ ] Staging and production environments are isolated (separate S3, Cognito, SSM, Atlas) within one AWS account
