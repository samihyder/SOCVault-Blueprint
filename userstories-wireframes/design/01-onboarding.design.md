# Design Specification — `01-onboarding.html`
## Onboarding & Registration

**Wireframe file:** `userstories-wireframes/01-onboarding.html`  
**User stories covered:** US-001, US-002, US-003, US-004, US-005, US-006, US-007, US-008  
**Goal:** Take a new user from zero to their first free L1 recon scan in under 60 seconds across a 4-step wizard.

---

## 1. Layout Structure

The page uses a three-region shell that is shared across every screen in the SOCVault application:

```
┌─────────────────────────────────────────────┐
│              TOPBAR (fixed, 52px)            │
├──────────────┬──────────────────────────────┤
│              │                              │
│   SIDEBAR    │         MAIN CONTENT         │
│  (fixed,     │         (scrollable)         │
│   210px)     │                              │
│              │                              │
└──────────────┴──────────────────────────────┘
```

- **Topbar** is fixed at the top (z-index 100), 52px tall, spans full width.
- **Sidebar** is fixed on the left, starts below the topbar (`top: 52px`), 210px wide, scrollable vertically.
- **Main content** has `margin-left: 210px` and `margin-top: 52px`, padded `22px 24px`.

---

## 2. Topbar

**Background:** `#1B3D35` (deep forest green)  
**Height:** 52px, fixed, full width

### Left — Logo
- Text: `SOCVault` in `#4CC844` (brand green), 17px bold
- Subtitle beside it: `— The Unified AI-Enabled Cybersecurity Solution` in white, 13px regular weight, with 6px left margin

### Right — Controls (flex row, 14px gap)
| Element | Description |
|---|---|
| **SOC Pro badge** | Pill badge, `#4CC844` background, `#1B3D35` text, 10px bold. Shows the current user's subscription tier. |
| **Notification bell** | 🔔 icon with a `#DC2626` (red) dot indicator in the top-right corner indicating unread alerts. |
| **Avatar** | 32×32px circle, `#4CC844` background, `#1B3D35` initials. Shows `JD` for "Jane Doe". Represents the logged-in user. |

---

## 3. Sidebar Navigation

**Background:** `#1B3D35`  
**Width:** 210px  
**Active state:** `rgba(76,200,68,.12)` background + `#4CC844` left border (3px) + white text  
**Default state:** `#b8d4c8` text, transparent left border

The sidebar is divided into three labeled sections rendered as uppercase tracking labels in `#4CC844` at 9px.

### Section: Overview

| Label | Icon | Route / href | Notes |
|---|---|---|---|
| Dashboard | 🏠 | `02-dashboard.html` | Main security posture overview |
| Domains & Assets | 🌐 | `17-settings.html` | Manages registered domains and asset inventory |

### Section: Scan Layers

| Label | Icon | Route / href | Badge | Notes |
|---|---|---|---|---|
| L1 — Free Recon | 🔍 | `03-l1-recon.html` | — | Passive open-source recon. Free tier. |
| L2 — Web AppSec | 🕸️ | `05-l2-web.html` | — | Web application vulnerability scanning |
| L3 — Mobile | 📱 | `06-l3-mobile.html` | — | iOS and Android APK/IPA analysis |
| L4 — API | ⚡ | `07-l4-api.html` | — | REST/GraphQL API fuzzing and testing |
| L5 — Compliance | 📋 | `08-l5-compliance.html` | — | Compliance framework checks (ISO, SOC 2, etc.) |
| L6 — Cloud | ☁️ | `09-l6-cloud.html` | — | Cloud misconfiguration and posture scans |
| L7 — SOC/SIEM | 🛡️ | `10-l7-soc.html` | **3** (red) | Active SOC alerts; badge count shows 3 unresolved |
| L8 — Malware | 🦠 | `11-l8-malware.html` | **1** (red) | Malware and threat intel feeds; 1 active finding |

### Section: Platform

| Label | Icon | Route / href | Badge | Notes |
|---|---|---|---|---|
| SOAR & Playbooks | ⚙️ | `13-soar.html` | — | Automated response playbooks |
| AI Risk Report | 🤖 | `04-l1-report.html` | — | Claude AI-generated plain-English risk narrative |
| Billing | 💳 | `14-billing.html` | — | Subscription, invoices, usage |
| MSP Portal | 🏢 | `15-msp-portal.html` | — | Multi-tenant management for MSP resellers |
| Notifications | 🔔 | `16-notifications.html` | **5** (red) | 5 unread platform notifications |
| Settings | ⚙️ | `17-settings.html` | — | Account, integrations, domain management |
| Audit Log | 📜 | `18-audit-log.html` | — | Immutable action history |
| Admin Console | 🔧 | `19-admin.html` | — | SOCVault internal admin (super-admin only) |

---

## 4. Main Content Area

### 4.1 User Story Tags

Displayed as a row of small pill badges at the very top of the main area, before the page title. Each badge references a linked user story.

**Tags shown:** `US-001` `US-002` `US-003` `US-004` `US-005` `US-006` `US-007`  
**Style:** `#E8F0E8` background, `#1B3D35` text, `#b8d4c8` border, 9px bold, 4px radius

These tags tie every visible element back to a documented requirement in the user story backlog (`SOCVault-User-Stories.xlsx`).

### 4.2 Page Header

| Element | Value |
|---|---|
| **Page title** | `Onboarding & Registration` — 18px, 800 weight, `#1B3D35` |
| **Subtitle** | `New user journey — from sign-up to first scan in 60 seconds` — 12px, `#888` |
| **Wireframe note** | Yellow dashed info box: `📐 Wireframe shows 4-step wizard. Steps 1–3 are pre-auth; Step 4 triggers first free L1 scan automatically.` |

---

## 5. Wizard — 4-Step Grid

The four wizard steps are laid out in a `2×2` CSS grid (`grid-template-columns: 1fr 1fr`, 16px gap). Each step is a white card with a `#4CC844` bottom border on its title.

---

### Step 1 — Create Account
**Card subtitle:** `US-001, US-005`

This is the entry point for new users. The card presents a branded sign-up form.

**Branding block (top center):**
- Logo text `SOCVault` — 28px, 800 weight, `#1B3D35`
- Tagline `The Unified AI-Enabled Cybersecurity Solution` — 12px, `#888`

**Form fields:**

| Field | Pre-filled value | Validation rule |
|---|---|---|
| Business Email * | `jane@acmecorp.com` | Business domain only — personal emails (gmail, yahoo, etc.) rejected. Hint: "No personal emails — business domain required" |
| Phone Number * | `+44 7700 900123` | International format required |
| Password * | `••••••••••` | Masked. Min-length and strength rules enforced server-side |

**Primary CTA:** Full-width `Create Free Account →` button (`#4CC844` background, `#1B3D35` text, 10px padding)

**Social/SSO alternatives (below a divider "— or continue with —"):**
- `🔵 Google` — OAuth 2.0 sign-in
- `🟦 Microsoft SSO` — Azure AD / Entra ID federation

**Trust copy (bottom, 10px `#aaa`):**  
`No credit card required · Free forever on L1 tier`

---

### Step 2 — Verify Email
**Card subtitle:** `US-001`

Triggered immediately after Step 1 form submission. The card confirms an OTP was dispatched.

**Illustration:** Large 📧 emoji (40px) centered at the top

**Copy:**
- Heading: `Check your inbox` — 14px bold, `#1B3D35`
- Body: `We sent a 6-digit code to` + `jane@acmecorp.com` in bold

**OTP Input Row:**  
Six individual 40×44px input boxes arranged in a horizontal flex row with 6px gaps.  
- Active/focused box has `2px solid #4CC844` border  
- Remaining boxes have `2px solid #d1d5db` (grey) border  
- Font inside each box: 18px, 700 weight  
- Pre-filled wireframe state: `4 8 2 1 9 3`

**Primary CTA:** Full-width `Verify & Continue →` button (`#4CC844`)

**Fallback link:** `Didn't receive it?` + `Resend code` anchor in `#4CC844`

---

### Step 3 — Add Your Domain
**Card subtitle:** `US-002, US-003`

Collects and verifies the primary domain the user wants scanned. Domain ownership proof is mandatory before any scan can run.

**Info alert strip (blue, info style):**  
`🔒 You must verify ownership before we scan your domain.`  
(`#EFF6FF` background, `3B82F6` left border)

**Domain field:**
- Label: `Primary Domain *`
- Pre-filled: `acmecorp.com`
- Hint: `Auto-filled from your email domain` — the platform infers the domain from the business email entered in Step 1

**Verification Method Selector:**  
A grey box (`#F4F6F4`, 12px padding, 6px radius) containing:

- Section label: `Domain Verification (choose one)` — 11px bold, `#1B3D35`
- Toggle buttons:
  - **`DNS TXT Record`** — primary/active (`#4CC844` background)
  - **`HTML Meta Tag`** — secondary/outline style

**DNS TXT Record instructions (active method shown):**
- Copy: `Add this TXT record to your DNS:`
- Code block (dark terminal style, `#1e2d2a` background, `#4CC844` monospace text):
  ```
  _socvault-verify.acmecorp.com  TXT  "socvault-verify=a3f9b2c1d4e8f7"
  ```
- Footnote: `DNS propagation typically takes 2–10 minutes` — 10px, `#aaa`

**Primary CTA:** Full-width `Check Verification →` button

**Skip option (below CTA):**  
`or` + `Skip for now (verify later)` anchor in `#4CC844`  
Domain is added in unverified state; scanning is gated until verification completes.

---

### Step 4 — Running Your First Free Scan
**Card subtitle:** `US-007, US-008`

Triggered automatically once domain verification passes (or after skip). Runs the 15-step passive L1 recon pipeline with no user action required.

**Scan metadata row (centered, 11px `#888`):**  
`15-step passive recon scan · No active probing · <90 sec pipeline · <3 min to report`

**Scan step list — 15 steps with real-time status indicators:**

Each step has:
- A circular step number (22px, `#1B3D35` bg, `#4CC844` text)
- Status: `done` (green ✓), `running` (amber ▶), or numbered (queued, grey)
- A status text label on the right

| # | Step Name | Tool / Source | Wireframe State |
|---|---|---|---|
| 1 | WHOIS & DNS records | WHOIS databases | ✓ Done |
| 2 | SPF / DKIM / DMARC check | DNS TXT record lookup | ✓ Done |
| 3 | SSL/TLS certificate audit | Certificate transparency / crt.sh | ✓ Done |
| 4 | HTTP security headers | HTTP response header inspection | ▶ Running… |
| 5 | crt.sh CT log lookup | Certificate Transparency logs | Queued |
| 6 | Subfinder passive subdomain enum | Subfinder OSINT tool | Queued |
| 7 | httpx live validation | httpx HTTP prober | Queued |
| 8 | Naabu top-100 port scan | Naabu port scanner | Queued |
| 9 | Wappalyzer tech fingerprinting | Wappalyzer API | Queued |
| 10 | AbuseIPDB & Google Safe Browsing | AbuseIPDB + GSB API | Queued |
| 11 | URLhaus malware check | URLhaus threat intel | Queued |
| 12 | HaveIBeenPwned domain lookup | HIBP API | Queued |
| 13 | Subdomain takeover detection | Passive takeover fingerprinting | Queued |
| 14 | Service banner analysis | Banner grabbing via passive sources | Queued |
| 15 | Claude AI risk translation | Anthropic Claude API | Queued |

**Progress bar:**  
- Full-width, 12px tall, `#e0e8e0` track, `#4CC844` fill
- Current fill: `27%` (steps 1–3 done, step 4 in progress)

**Progress caption (right-aligned, 10px `#888`):**  
`27% complete · ~6 min remaining`

**Post-scan route:**  
On 100% completion, the user is automatically navigated to `04-l1-report.html` (the AI Risk Report for the L1 scan).

---

## 6. Team Members & Roles Card

**Below the 2×2 wizard grid, full-width card**  
**Card subtitle:** `US-006`

Allows the account admin to invite colleagues before or during onboarding.

### Toolbar
- Left text: `Invite colleagues to access your SOCVault account` — 12px, `#888`
- Right CTA: `+ Invite Member` button (primary, small)

### Members Table

| Column | Description |
|---|---|
| **Name** | Display name. Current user marked with `(you)` suffix |
| **Email** | Work email address |
| **Role** | Displayed as a severity-style badge (green = Admin, blue = Analyst) |
| **Status** | Active (green), Invited/pending (blue progress style) |
| **Actions** | `Resend` button for pending invites; `—` for active users |

**Pre-populated rows:**

| Name | Email | Role | Status | Action |
|---|---|---|---|---|
| Jane Doe (you) | jane@acmecorp.com | Admin (green passed badge) | Active | — |
| Pending Invite | it@acmecorp.com | Analyst (info blue badge) | Invited | Resend button |

**Role legend (below table, 11px `#888`):**  
`Roles: Viewer (read-only) · Analyst (run scans + view) · Admin (full access)`

---

## 7. Routing Map

### Internal page routes referenced in this wireframe

| Destination | Route | Trigger |
|---|---|---|
| Dashboard | `02-dashboard.html` | Sidebar nav link |
| Domains & Assets | `17-settings.html` | Sidebar nav link (also used by Settings) |
| L1 Free Recon | `03-l1-recon.html` | Sidebar nav link |
| L2 Web AppSec | `05-l2-web.html` | Sidebar nav link |
| L3 Mobile | `06-l3-mobile.html` | Sidebar nav link |
| L4 API | `07-l4-api.html` | Sidebar nav link |
| L5 Compliance | `08-l5-compliance.html` | Sidebar nav link |
| L6 Cloud | `09-l6-cloud.html` | Sidebar nav link |
| L7 SOC/SIEM | `10-l7-soc.html` | Sidebar nav link |
| L8 Malware | `11-l8-malware.html` | Sidebar nav link |
| SOAR & Playbooks | `13-soar.html` | Sidebar nav link |
| AI Risk Report | `04-l1-report.html` | Sidebar nav + auto-redirect after Step 4 scan completes |
| Billing | `14-billing.html` | Sidebar nav link |
| MSP Portal | `15-msp-portal.html` | Sidebar nav link |
| Notifications | `16-notifications.html` | Sidebar nav link |
| Settings | `17-settings.html` | Sidebar nav link |
| Audit Log | `18-audit-log.html` | Sidebar nav link |
| Admin Console | `19-admin.html` | Sidebar nav link |

### Wizard step flow

```
[Sign-up Form] → [Email OTP] → [Domain Entry + Verification] → [L1 Scan Progress] → [AI Risk Report]
   Step 1           Step 2              Step 3                        Step 4              04-l1-report.html
```

- Steps 1–3 are **pre-auth** (no session cookie yet).
- Step 4 fires automatically once domain verification passes.
- The `Skip for now` link in Step 3 still proceeds to Step 4 but marks the domain as unverified; paid scan layers remain locked until verification completes.
- Completing Step 4 redirects to `04-l1-report.html` with the scan ID passed as a query parameter.

---

## 8. Color & Token Reference

| Token | Hex | Usage |
|---|---|---|
| Brand green | `#4CC844` | Primary CTA, active sidebar indicator, progress fill, step-done badge |
| Deep forest | `#1B3D35` | Topbar, sidebar background, headings, step number circles |
| Light green tint | `#E8F0E8` | Page background, table even rows, story-ref badge background |
| Border | `#e0e8e0` | Card borders, table borders |
| Body text | `#444` | Table cells, step text |
| Muted | `#888` | Subtitles, hints, labels |
| Very muted | `#aaa` | Footer copy, inactive states |
| Critical red | `#DC2626` | Notification dot, badge counts |
| Amber | `#F59E0B` | Running step indicator, `warn` checklist |
| Info blue | `#3B82F6` | Info alert strip left border |
| Terminal bg | `#1e2d2a` | Code block background |

---

## 9. Component Inventory

| Component | Wireframe location |
|---|---|
| `topbar` | Global chrome |
| `sidebar` | Global chrome |
| `story-ref` badge | Top of main area |
| `page-title` + `page-sub` | Section heading |
| `wf-note` (dashed yellow box) | Wireframe annotation |
| `card` with `card-title` | Each of the 4 wizard steps + team card |
| `form-group` + `form-input` + `form-hint` | Steps 1 and 3 |
| `btn-primary` / `btn-outline` | CTAs, SSO buttons, method toggle |
| OTP input row (custom) | Step 2 |
| `code-block` | DNS TXT record display in Step 3 |
| `alert-strip info` | Domain ownership warning in Step 3 |
| `step-list` with `step-num` states | Step 4 scan progress |
| `progress-bar` + `progress-fill` | Step 4 overall % |
| `table` (thead dark, tbody zebra) | Team members card |
| `sev` badge (passed / info) | Role column |
| `status` badge (active / progress) | Status column |
| `toolbar` (flex row with spacer) | Team members header |
