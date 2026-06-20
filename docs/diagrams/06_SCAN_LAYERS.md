# SOCVault — Scan Layers L1–L9 Reference
**Version 1.0 | June 2026**

Per-layer catalogue: tools, tier, rate limits, data flows, wireframes. **8 core layers + L9 AI Agent Scan.**

**FR rate limits:** FR-110–115 · **Wireframes:** `03`–`11`, `20`

---

## 1. Layer overview map

```mermaid
flowchart TB
  subgraph Passive["Passive / External"]
    L1[L1 Recon\nSubfinder · Naabu · httpx]
    L4[L4 API Security\nPostman · OpenAPI fuzz]
  end

  subgraph Active["Active Testing"]
    L2[L2 Web AppSec\nNuclei · Semgrep · ZAP]
    L3[L3 Mobile\nMobSF · MASVS]
    L6[L6 Cloud\nCloudFox · Pacu · Prowler]
  end

  subgraph Posture["Posture & Ops"]
    L5[L5 Compliance\nPCI · GDPR · ISO mapping]
    L7[L7 SOC/SIEM\nWazuh SIEM]
    L8[L8 Malware D&R\nWazuh EDR · ClamAV · FIM]
  end

  subgraph AI["AI-Native"]
    L9[L9 AI Agent Scan\nClaude Opus autonomous]
  end

  CL[Claude Intelligence\nall layers] --> L1 & L2 & L3 & L4 & L5 & L6 & L7 & L8 & L9
  TI[Threat Intel] --> L1 & L7 & L8
```

---

## 2. Layer reference table

| Layer | Name | Key tools | Min tier | Rate limit | Wireframe | US range |
|---|---|---|---|---|---|---|
| **L1** | External Recon | Subfinder, Naabu, httpx, dnsx | Freemium | 1/month free · 2/7d paid | `03`, `04` | US-008–020 |
| **L2** | Web AppSec | Nuclei, Semgrep, OWASP ZAP | Starter+ | 1/15 days | `05` | US-021–026 |
| **L3** | Mobile AppSec | MobSF, MASVS checker | Starter+ | 1/15 days | `06` | US-027–029 |
| **L4** | API Security | OpenAPI fuzz, auth testing | Starter+ | 2/7 days | `07` | US-030–032 |
| **L5** | Compliance | Framework mappers, policy gaps | Pro+ | 1/30 days | `08` | US-033–036 |
| **L6** | Cloud Pentest | CloudFox, Pacu, Prowler | Pro+ | 1/15 days | `09` | US-037–040 |
| **L7** | SOC / SIEM | Wazuh manager + agents | SOC Pro | Continuous ingest | `10` | US-041–045 |
| **L8** | Malware D&R | Wazuh FIM, ClamAV, YARA | SOC Pro | Event-driven | `11` | US-046–054 |
| **L9** | AI Agent Scan | Claude Opus extended thinking | Pro+ (Ph2) | 1/7 days | `20` | US-130–140 |

---

## 3. Per-layer data flow pattern (common template)

All scan layers follow this pattern unless noted (L7/L8 are event-driven):

```mermaid
flowchart LR
  U[User] --> API[Scan Orchestrator]
  API --> Q[SQS]
  Q --> W[Layer Worker]
  W --> TOOLS[OSS Scanner tools]
  W --> TI[Threat Intel]
  W --> S3[S3 raw output]
  W --> CL[Claude translation]
  CL --> MDB[MongoDB scan record]
  U --> API2[Poll GET /scan/id]
  API2 --> MDB
```

---

## 4. L1 — External Recon (MVP)

```mermaid
flowchart TB
  IN[Input: domain] --> S1[Subdomain enum]
  S1 --> S2[Port scan passive]
  S2 --> S3[HTTP probe · tech stack]
  S3 --> S4[SSL/TLS · headers]
  S4 --> S5[DNS · email security]
  S5 --> TI[TI enrichment]
  TI --> CL[Claude report]
  CL --> OUT[health_score · exposure · CVE narratives]
```

| Step | Tool | Output store |
|---|---|---|
| 15-step pipeline | Subfinder, Naabu, httpx, etc. | S3 + MongoDB |
| AI translation | claude-sonnet-4-6 | MongoDB `executive_report` |
| Freemium gate | FR-026 | DynamoDB rate limit |

---

## 5. L2 — Web AppSec

| Phase | Activity |
|---|---|
| Discovery | Crawl sitemap, identify endpoints |
| SAST | Semgrep rulesets |
| DAST | Nuclei templates, ZAP active scan |
| AI | Claude maps to OWASP Top 10 + business risk |

**Consent:** Domain verified (FR-029) · **COGS:** ~$0.36/scan fully loaded

---

## 6. L3 — Mobile

| Input | Process |
|---|---|
| APK/IPA upload | MobSF static + dynamic analysis |
| Output | MASVS report, AI risk summary |

**API:** `POST /scan/mobile` · **Storage:** S3 encrypted binary (tenant-scoped)

---

## 7. L4 — API Security

| Input | Process |
|---|---|
| OpenAPI spec or discovered endpoints | Auth bypass, injection, rate limit tests |
| Output | Endpoint risk map, Claude remediation scripts (paywalled Pro+) |

---

## 8. L5 — Compliance

```mermaid
flowchart LR
  FIND[Findings from L1-L6] --> MAP[Framework mapper]
  MAP --> PCI[PCI-DSS 4.0]
  MAP --> GDPR[UK GDPR]
  MAP --> ISO[ISO 27001:2022]
  MAP --> CE[Cyber Essentials Plus]
  MAP --> SOC2[SOC 2 Type II]
  MAP --> RPT[Compliance dashboard]
```

**USP 8:** All five frameworks included in paid tier — not add-on.

---

## 9. L7 — SOC / SIEM

```mermaid
flowchart TB
  AG[Wazuh Agent\non tenant server] --> WM[Wazuh Manager]
  WM --> INGEST[SOCVault ingest]
  INGEST --> DASH[SIEM dashboard]
  INGEST --> SOAR[SOAR Engine]
  TI[Threat Intel] --> SOAR
```

**Deployment:** Wazuh manager on EKS/EC2 (paid tier) · Agents deployed by Manager role (FR-143)

---

## 10. L8 — Malware Detection & Response

```mermaid
flowchart TB
  AG[Wazuh Agent] -->|FIM · ClamAV alert| WM[Wazuh Manager]
  WM --> API[POST /malware/ingest]
  API --> CL[Claude triage]
  CL --> ACT{Auto-remediate?}
  ACT -->|yes| AR[Active response]
  ACT -->|no| APPROVAL[Human approval queue]
```

---

## 11. L9 — AI Agent Scan (Phase 2)

```mermaid
flowchart TB
  U[Manager] --> API[POST /scan/l9/execute]
  API --> AG[Agent Worker\nClaude Opus]
  AG -->|step 1..n| RECON[Recon actions]
  AG -->|step 1..n| TEST[Active tests]
  AG --> LOG[Live activity log]
  AG --> CL[OWASP-mapped findings]
  U -->|poll| LOG
```

| Property | Value |
|---|---|
| Model | Claude Opus (extended thinking) |
| Limit | 1 scan / 7 days (FR-115) |
| Cost cap | FR-132 real-time against tenant AI budget |

---

## 12. Layer vs tier matrix

```mermaid
flowchart TB
  subgraph Free["Freemium"]
    F1[L1 only · 1/month]
  end

  subgraph Paid["Starter / per-target"]
    P1[L1 expanded]
    P2[L2 · L3 · L4]
  end

  subgraph Pro["SOC Pro $199/mo"]
    S1[All L1-L6]
    S2[L7 SOC]
    S3[L8 Malware]
    S4[L9 Agent]
    S5[SOAR]
  end

  Free --> Paid --> Pro
```

---

## 13. Equivalent multi-vendor stack (competitive context)

| Layer | Typical point solution | SOCVault |
|---|---|---|
| L1 | Shodan, Censys | Included |
| L2 | Intruder.io, Detectify | Included |
| L3 | NowSecure, GuardSquare | Included |
| L4 | 42Crunch, Salt | Included |
| L5 | Vanta, Drata (partial) | Included |
| L6 | ScoutSuite, Prowler SaaS | Included |
| L7 | Blumira, Huntress | Included @ $199 |
| L8 | CrowdStrike (SMB tier) | Included @ $199 |
| L9 | Pentest-as-a-service | AI agent @ Pro |

---

## Related documents

| Doc | Role |
|---|---|
| [`20_FREE_EXTERNAL_APIS.md`](../20_FREE_EXTERNAL_APIS.md) | TI feeds per layer |
| [`03_DATA_FLOW_EXTENDED.md`](./03_DATA_FLOW_EXTENDED.md) | L2/L9 DFD detail |
| [`22_DATA_FLOW_DIAGRAMS.md`](../22_DATA_FLOW_DIAGRAMS.md) | L1 MVP pipeline |
