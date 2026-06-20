# SOCVault — Free & Freemium External API Registry
**Version 1.0 | June 2026**

---

## 1. Purpose

SOCVault enriches every scan layer and SOC alert with **external intelligence APIs** — CVE databases, reputation feeds, IOC lookups, breach data, and threat feeds. All credentials are configured once in the **Super Admin → Pass & Keys** vault (and optionally the **Metrics Observatory → API Settings** panel), then consumed on-demand by a central **`ThreatIntelManager`** service.

**Design principles:**

| Principle | Implementation |
|---|---|
| **Configure once, call when required** | Keys stored encrypted (KMS); scanners request enrichment by *intent* (`enrich_ip`, `lookup_cve`), not by raw URL |
| **Cache aggressively** | DynamoDB `ti_cache` + MongoDB `enrichment_refs` — TTL per feed type (24h IPs, 7d CVEs, 1h IOCs) |
| **Free tier first** | Every integration below has a **free or community tier**; paid upgrade path documented |
| **Fail open on enrichment** | Scan/report completes even if a feed is down; finding marked `enrichment_status: partial` |
| **Cross-tenant correlation (anonymised)** | Normalised IOC hits aggregated platform-wide for early-warning patterns (no PII) |

---

## 2. Super Admin Configuration

### 2.1 Where operators manage APIs

| UI | Location | What it controls |
|---|---|---|
| **Pass & Keys vault** | `24-admin-api-explorer.html` → right panel | API keys, base URLs, per-environment overrides (`staging` / `production`) |
| **API Settings** | `23-metrics-observatory.html` → Settings tab | Rate limits, enable/disable feeds, daily quota alerts, fallback order |
| **Development Tracker** | `25-admin-dev-tracker.html` → External accounts | `EXT-###` onboarding status (key obtained, stored in SSM, verified) |

### 2.2 Vault variable naming convention

```
ti_{provider}_{env}          → API key or token
ti_{provider}_base_url       → Optional override (defaults in code)
ti_{provider}_enabled        → true | false
ti_{provider}_daily_limit    → Soft cap before queue deferral
```

**Examples:**

| Vault key | Service | Layer(s) |
|---|---|---|
| `ti_abuseipdb_staging` | AbuseIPDB | L1, L7, L8, L9 |
| `ti_otx_production` | AlienVault OTX | L7, L8, correlation |
| `ti_virustotal_staging` | VirusTotal | L1 (passive DNS), L2, L8 |
| `ti_hibp_production` | Have I Been Pwned | L1 |
| `ti_nvd_production` | NIST NVD | L2, L3, L4, L9 |
| `ti_malwarebazaar_production` | MalwareBazaar | L8, correlation |

Keys are mirrored to **AWS SSM** (`/socvault/{env}/ti/{provider}/api_key`) at deploy time; vault is the operator UI.

### 2.3 Runtime call flow

```
Scan worker / SOAR pipeline
        │
        ▼
 ThreatIntelManager.enrich(context)
        │
        ├── Read enabled feeds + keys from cache (SSM/vault snapshot)
        ├── Check DynamoDB ti_cache for existing result
        ├── If miss → call provider(s) in priority order
        ├── Normalise to EnrichmentRecord schema
        ├── Write cache + append to scan.enrichment_refs[]
        └── Emit correlation event → CorrelationEngine (async)
```

---

## 3. Cross-Layer Correlation & Pattern Engine

All enrichment results normalise to a shared schema so Claude AI and dashboards can correlate across layers:

```javascript
// enrichment_records (MongoDB) + ti_events (DynamoDB stream)
{
  record_id: UUID,
  tenant_id: UUID,
  source_layer: "L1" | "L2" | ... | "L7",
  scan_id: UUID | null,
  alert_id: UUID | null,
  ioc_type: "ip" | "domain" | "url" | "hash" | "cve" | "email" | "certificate",
  ioc_value: String,
  providers: [{ name, confidence, raw_summary }],
  mitre_techniques: [String],      // mapped where available
  severity_score: Number,          // 0–10 normalised
  first_seen: Date,
  last_seen: Date,
  correlation_cluster_id: UUID     // assigned by CorrelationEngine
}
```

### 3.1 How correlation strengthens reporting

| Pattern | Inputs | Output in report |
|---|---|---|
| **Attack surface → active threat** | L1 subdomain + L2 CVE + OTX pulse on same host | "Known exploited CVE on internet-facing asset also seen in OTX campaign" |
| **Credential → breach → access** | HIBP domain breach + L7 brute-force alert on same tenant | "Leaked credentials may explain authentication anomaly" |
| **Malware family cluster** | L8 VT hash + MalwareBazaar + ThreatFox IOC | Unified malware family, shared C2 IPs blocked in SOAR |
| **Supply-chain CVE burst** | OSV/NVD same CVE across L2 web + L3 mobile + L6 cloud | Single remediation playbook for one library version |
| **Reputation convergence** | AbuseIPDB + GreyNoise + Spamhaus on same IP | Confidence-weighted block decision for SOAR |
| **Dark-web / leak mention** | Ransomware.live + HIBP (where applicable) | Executive summary: "Organisation/domain referenced in leak tracker" |

### 3.2 CorrelationEngine (async, platform-wide)

1. **Ingest** — every `EnrichmentRecord` publishes to SQS `ti-correlation`.
2. **Cluster** — match on `ioc_value`, `mitre_techniques`, or `malware_family` within 72h window.
3. **Score** — raise `tenant_risk_delta` when ≥2 layers hit same IOC.
4. **Pattern rules** — YAML rules (e.g. "CVE + OTX + external recon on same IP → Critical").
5. **Claude synthesis** — batch cluster summary for dashboard "Threat Patterns" widget.
6. **Early warning** — if same IOC hits ≥5 tenants (anonymised), flag Super Admin observatory.

---

## 4. API Registry by Layer

Legend: **Free** = no key or open data · **Freemium** = free tier with registration · **Key** = API key required

---

### L1 — External Recon (Free tier)

| API / Feed | Type | Free tier limit | L1 step(s) | Usage | Reporting / correlation value |
|---|---|---|---|---|---|
| **crt.sh** | CT logs | Unlimited (fair use) | 4, 6, 7 | Certificate transparency JSON API — historical subdomains, cert expiry | Shadow IT discovery; correlate new subdomains with L2 findings |
| **WHOIS / RDAP** | Domain reg | Free (registrar RDAP) | 1 | Registration expiry, nameservers, privacy flags | Domain expiry risk; nameserver change detection over time |
| **Cloudflare DoH / Google DNS** | DNS | Unlimited | 2 | Resolve A/AAAA/MX/TXT/NS | Baseline DNS; DMARC/SPF parsing input |
| **checkdmarc** (library) | Email auth | N/A (local) | 3 | SPF/DKIM/DMARC validation | Spoofing risk score; feeds compliance (L5) |
| **sslyze** (local) + **SSL Labs API** | TLS | SSL Labs: ~25 assessments/day | 4 | Grade, protocol/cipher weaknesses | TLS downgrade patterns; link to CVE via NVD |
| **Subfinder** (passive sources) | Subdomains | Uses VT, Censys, etc. | 7 | Passive subdomain enum | Attack surface map; input to L2 target list |
| **AbuseIPDB** | IP reputation | 1,000 checks/day | 11 | Abuse confidence %, categories, country | IP cluster across tenants; SOAR blocklist seed |
| **Google Safe Browsing** | URL/domain rep | Free (quota) | 12 | Phishing/malware URL status | Cross-check discovered URLs from httpx |
| **URLhaus** (abuse.ch) | Malicious URLs | Free API | 12 | Recent malware URL feed lookup | URL IOC correlation with L2/L8 |
| **Have I Been Pwned** | Breach data | Domain search free (key) | 13 | Breached accounts for domain | Credential risk; explains L7 auth alerts |
| **VirusTotal** | Passive DNS | 500 req/day | 7 (via Subfinder), 11 | Historical resolutions, subdomains | Link domain ↔ IP ↔ file hashes |
| **GreyNoise Community** | IP context | 100 queries/day | 11 | Scanning vs benign internet noise | Reduce false positives on L7 scan alerts |
| **Shodan** | Internet DB | 100 queries/month | 9, 15 | Open ports, banners, vuln tags | Enrich Naabu hits with global exposure context |
| **Censys** | Internet DB | Limited free tier | 7, 9 | Host certs, services | Secondary passive recon validation |
| **Spamhaus DROP/EDROP** | IP blocklists | Free lists | 11 | Known spam/malware netblocks | Fast local check before AbuseIPDB quota |
| **PhishTank** | Phishing URLs | Free API | 12 | Verified phishing URL check | Brand impersonation detection |

**L1 correlation example:** Subdomain found via crt.sh → resolves to IP flagged AbuseIPDB + GreyNoise → HIBP shows admin@domain in breach → Claude generates unified "Critical exposure chain" narrative.

---

### L2 — Web Application Security (Paid)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **NIST NVD API 2.0** | CVE/CVSS | Unlimited (rate limited) | Map Nuclei/ZAP CVE IDs → CVSS, CWE, description | Financial risk translation input; EPSS prioritisation |
| **FIRST EPSS** | Exploit probability | Free CSV/API | Sort CVEs by exploitation likelihood | "Patch this first" ordering in report |
| **OSV.dev** | Open-source vulns | Unlimited | Package → CVE for Trivy/Semgrep findings | Same CVE across web deps and L3 mobile |
| **GitHub Advisory DB** | Supply chain | Free (GraphQL) | npm/PyPI/Maven advisories | Cross-repo pattern for monorepos |
| **CISA KEV** | Known exploited | Free JSON feed | Flag CVEs in CISA catalogue | Regulatory urgency badge on findings |
| **URLhaus** | Malicious URLs | Free | URLs discovered in ZAP spider | Malware delivery chain linking to L8 |
| **VirusTotal** | URL/file rep | 500/day | Suspicious links from crawl | Pre-malware-stage detection |
| **OWASP ZAP** (local) | DAST | N/A | Active/passive scan | Primary findings source |
| **Nuclei** (local templates) | DAST/CVE | N/A | Template-based CVE/exposure | Template ID → NVD enrichment |
| **OpenPhish** | Phishing feed | Free feed | Check if crawled login pages match | Credential harvesting detection |

**L2 correlation example:** Nuclei finds CVE-2024-XXXX → NVD + EPSS + CISA KEV → same component in OSV for mobile app (L3) → single remediation script.

---

### L3 — Mobile Binary Security (Paid)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **NIST NVD / OSV.dev** | CVE | Free | Library versions from MobSF SBOM | Shared vulns with L2 web stack |
| **VirusTotal** | APK/IPA hash | 500/day | Hash reputation for uploaded binaries | Malware overlap with L8 endpoint hashes |
| **MalwareBazaar** (abuse.ch) | Sample hashes | Free API | Known Android malware hashes | Family correlation with L8 |
| **MobSF** (local) | SAST/MAST | N/A | Primary mobile analysis | Hardcoded secrets → HIBP email check |

---

### L4 — API Security (Paid)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **NVD / OSV** | CVE | Free | API framework/library CVEs | Same as L2 |
| **OWASP API Security Top 10** | Taxonomy | Free docs | Classify Nuclei API template findings | Compliance mapping (L5) |
| **JWT.io / local decode** | Token analysis | N/A | Inspect exposed JWT weaknesses | Link to L7 auth anomaly alerts |

---

### L5 — Compliance (Paid)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **NVD + CISA KEV** | Control evidence | Free | Prove patch cadence for PCI 6.3 | Audit-ready evidence bundle |
| **HIBP** | GDPR Art. 32 | Domain breach | Breach notification evidence | Cross-reference with L1 step 13 |
| **MITRE ATT&CK** | Framework | Free STIX/data | Map findings → techniques | Unified ATT&CK heatmap across layers |
| **Prowler** (local/AWS API) | Cloud controls | Customer AWS creds | AWS CIS/NIST checks | Feeds L6; same control IDs in report |

*Compliance layer primarily **correlates findings from L1–L4 and L6** rather than calling standalone feeds.*

---

### L6 — Cloud Posture (Paid)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **AWS APIs** (IAM, S3, EC2) | Cloud config | Customer credentials | Prowler/CloudFox/Pacu | Misconfig → L2 exposure if public |
| **Steampipe plugins** | Multi-cloud | Open-source | Azure/GCP read-only audits | Cross-cloud pattern detection |
| **NVD** | CVE | Free | OS/package CVEs on AMIs | Patch priority with EPSS |

---

### L7 — SOC / SIEM (SOC Pro)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **AbuseIPDB** | IP rep | 1,000/day | Enrich Wazuh `srcip` on every alert | Auto-block playbook input |
| **AlienVault OTX** | Threat pulses | Community free | IP/domain/hash pulses, adversary context | Campaign attribution in incident report |
| **GreyNoise** | IP context | 100/day | Is alert IP internet scanner noise? | FP reduction; analyst time saved |
| **ThreatFox** (abuse.ch) | IOCs | Free API | IP/domain/URL/hash IOC lookup | Match Wazuh IOC to active campaigns |
| **Feodo Tracker** | Botnet C2 | Free feed | C2 IP blocklist | Ransomware/banking trojan C2 correlation |
| **Spamhaus** | Blocklists | Free | DNS/IP reputation | DNS exfil / spam relay detection |
| **Tor exit node list** | Anonymity | Free | Flag Tor-origin connections | Unusual access pattern context |
| **URLhaus** | Malicious URLs | Free | URLs in proxy/logs | Download-stage malware chain |
| **MalwareBazaar** | Hashes | Free | File hash from FIM alerts | Pre-execution hash block |
| **MITRE ATT&CK** | TTP mapping | Free | Map rule names → techniques | SOC analyst dashboard heatmap |

**L7 correlation example:** Wazuh brute-force from IP → AbuseIPDB 100% + OTX pulse "Credential spray" + GreyNoise not scanner → Claude triage: escalate, block IP, force MFA.

---

### L8 — Malware Detection & Response (SOC Pro)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **VirusTotal** | Hash/file/URL | 500/day | Primary hash lookup; engine detection ratio | Confidence score for auto-remediation gate |
| **MalwareBazaar** | Malware samples | Free API | Hash → family, tags, delivery method | Family clustering across tenants |
| **ThreatFox** | IOCs | Free | C2 URLs/IPs from sample | Network blocklist update |
| **URLhaus** | Malware URLs | Free | Download URL validation | Kill-chain stage mapping |
| **Hybrid Analysis** (optional) | Sandbox | Limited free | Deep behaviour (Phase 3+) | Secondary when VT inconclusive |
| **YARAify** (abuse.ch) | YARA matches | Free | Live YARA rule scanning | Community rule correlation |
| **ClamAV / YARA** (local) | Signatures | Free | First-line detection | Zero API cost; VT confirms |

**L8 correlation example:** ClamAV hit → VT 58/70 + MalwareBazaar Emotet tag + ThreatFox C2 IP → same C2 seen in L7 logs → auto-quarantine + network block.

---

### L9 — AI Agent Scan (SOC Pro, Phase 2)

| API / Feed | Type | Free tier limit | Usage | Reporting / correlation value |
|---|---|---|---|---|
| **All L1–L2 feeds above** | Combined | Per feed | Agent invokes enrichment during autonomous steps | Agent activity log shows each API call |
| **NVD + EPSS + CISA KEV** | CVE priority | Free | Agent prioritises exploitable CVEs | Reasoning trace in activity log |
| **OTX + ThreatFox** | Campaign context | Free | Agent correlates findings to active threats | "Same TTP as OTX pulse XYZ" in report |

---

## 5. Master Reference Table (All Services)

| ID | Provider | Category | Key required | Free tier | Primary layer(s) | Vault key |
|---|---|---|---|---|---|---|
| EXT-007 | AbuseIPDB | IP reputation | Yes | 1,000/day | L1, L7, L8 | `ti_abuseipdb_*` |
| EXT-008 | AlienVault OTX | Threat intel | Yes | Community | L7, L8, L9 | `ti_otx_*` |
| EXT-011 | Have I Been Pwned | Breach | Yes | Domain search | L1, L5 | `ti_hibp_*` |
| EXT-012 | VirusTotal | Multi-purpose | Yes | 500/day | L1, L2, L3, L8 | `ti_virustotal_*` |
| EXT-013 | NIST NVD | CVE | Optional | Rate limited | L2–L4, L9 | `ti_nvd_*` |
| EXT-014 | OSV.dev | Supply chain CVE | No | Unlimited | L2, L3 | — |
| EXT-015 | CISA KEV | Exploited CVEs | No | Public feed | L2, L5, L9 | — |
| EXT-016 | FIRST EPSS | Exploit prob. | No | Public | L2, L9 | — |
| EXT-017 | URLhaus | Malicious URL | No | Free API | L1, L2, L7, L8 | — |
| EXT-018 | MalwareBazaar | Malware hash | No | Free API | L3, L8 | — |
| EXT-019 | ThreatFox | IOC | No | Free API | L7, L8 | — |
| EXT-020 | GreyNoise | IP context | Yes | 100/day | L1, L7 | `ti_greynoise_*` |
| EXT-021 | Shodan | Internet DB | Yes | 100/month | L1 | `ti_shodan_*` |
| EXT-022 | Google Safe Browsing | URL rep | Yes | Quota | L1, L2 | `ti_gsb_*` |
| EXT-023 | PhishTank | Phishing | Yes | Free | L1, L2 | `ti_phishtank_*` |
| EXT-024 | crt.sh | CT logs | No | Fair use | L1 | — |
| EXT-025 | Spamhaus DROP | Blocklist | No | Free lists | L1, L7 | — |
| EXT-026 | Feodo Tracker | Botnet C2 | No | Free feed | L7, L8 | — |
| EXT-027 | MITRE ATT&CK | TTP taxonomy | No | Free | L5, L7, reports | — |
| EXT-028 | OpenPhish | Phishing feed | No | Free feed | L2 | — |
| EXT-029 | Ransomware.live | Leak tracker | No | Public | L1, exec reports | — |
| EXT-030 | SSL Labs | TLS assessment | No | ~25/day | L1 | — |
| EXT-031 | Censys | Internet DB | Yes | Limited | L1 | `ti_censys_*` |
| EXT-032 | GitHub Advisory | Supply chain | Optional | Free | L2, L3 | `ti_github_*` |

---

## 6. Implementation Components

### 6.1 Backend services (FastAPI)

| Module | Responsibility |
|---|---|
| `services/threat_intel/manager.py` | `enrich_ip()`, `lookup_cve()`, `lookup_hash()`, `lookup_domain()`, `lookup_url()` |
| `services/threat_intel/providers/*.py` | One adapter per provider; normalise to `EnrichmentRecord` |
| `services/threat_intel/cache.py` | DynamoDB read/write, TTL enforcement |
| `services/threat_intel/correlation.py` | Cluster IOCs, emit pattern events |
| `services/threat_intel/rate_limiter.py` | Per-provider daily counters; defer to queue when exceeded |
| `admin/vault/` | Pass & Keys CRUD (existing FR-199–204) |
| `admin/ti_feeds/` | **New:** list feeds, test connection, usage stats |

### 6.2 Super Admin — Threat Intel Feeds panel

Tab on **API Explorer** (`24-admin-api-explorer.html`, US-201–208). REST paths and schemas: [`api/openapi.yaml`](../api/openapi.yaml) and [`06_API_SPECIFICATION.md`](./06_API_SPECIFICATION.md) only.

### 6.3 Data stores

| Store | Content |
|---|---|
| DynamoDB `ti_cache` | `{ pk: "IP#1.2.3.4", provider, payload, expires_at }` |
| DynamoDB `ti_usage` | Daily call counts per provider (COGS + quota) |
| MongoDB `enrichment_records` | Full history linked to scans/alerts |
| MongoDB `correlation_clusters` | Pattern groups for dashboard |
| S3 `feeds/snapshots/` | Daily pull of CISA KEV, Spamhaus, Feodo (offline fallback) |

---

## 7. Rate Limits & Fallback Order

When free quota is exhausted, SOCVault applies this order:

| IOC type | Priority 1 | Priority 2 | Priority 3 | Offline fallback |
|---|---|---|---|---|
| IP | Spamhaus DROP (local) | AbuseIPDB | GreyNoise | Cached result |
| Domain | DNS + crt.sh | VT passive DNS | OTX | Cached |
| Hash | ClamAV/YARA (local) | MalwareBazaar | VirusTotal | Cached |
| CVE | NVD | OSV.dev | CISA KEV JSON | S3 snapshot |
| URL | URLhaus | Google Safe Browsing | PhishTank | Cached |

Operators see quota warnings in **Metrics Observatory** at 80% and 95% of daily free tier.

---

## 8. Reporting Enhancements (Claude AI Input)

Each scan report includes an **`enrichment_summary`** block passed to Claude:

```json
{
  "correlation_clusters": 2,
  "critical_iocs": [
    { "type": "ip", "value": "203.0.113.5", "providers": ["AbuseIPDB", "OTX"], "score": 9 },
    { "type": "cve", "value": "CVE-2024-1234", "kev": true, "epss": 0.91 }
  ],
  "patterns_detected": [
    "credential_breach_plus_auth_alert",
    "known_exploited_cve_on_public_host"
  ],
  "threat_campaign_refs": ["OTX pulse: Emotet resurgence 2026-Q2"]
}
```

Claude uses this to produce financial exposure narratives, executive summaries, and SOAR recommendations grounded in **multi-source corroboration** — not single-tool output.

---

## 9. Phase Rollout

| Phase | Feeds to enable | Milestone |
|---|---|---|
| **MVP (L1)** | crt.sh, HIBP, AbuseIPDB, URLhaus, NVD (read-only), Spamhaus lists | 1.3, 1.6 |
| **Beta (L2/L7)** | + OTX, VT, OSV, CISA KEV, EPSS, GreyNoise | 2.4, 2.5 |
| **SOC Pro (L8)** | + MalwareBazaar, ThreatFox, Feodo | 2.5 |
| **Scale** | + Shodan, Censys, SSL Labs, Ransomware.live | 3.x |
| **Super Admin UI** | Feed registry + test + usage in Pass & Keys / Observatory | 2.9, 2.8 |

---

## 10. Related Documents

| Doc | Link |
|---|---|
| Technical stack (L1 steps) | [`02_TECHNICAL_STACK.md`](./02_TECHNICAL_STACK.md) §2.3 |
| MVP functional behaviour | [`21_MVP_FUNCTIONAL_SPEC.md`](./21_MVP_FUNCTIONAL_SPEC.md) |
| Data flow diagrams | [`22_DATA_FLOW_DIAGRAMS.md`](./22_DATA_FLOW_DIAGRAMS.md) |
| Requirements (enrichment FRs) | [`03_REQUIREMENTS.md`](./03_REQUIREMENTS.md) §1.16 |
| API Explorer / Pass & Keys | [`18_API_EXPLORER_IMPLEMENTATION.md`](./18_API_EXPLORER_IMPLEMENTATION.md) |
| Development Tracker EXT IDs | [`DEVELOPMENT_TRACKER.md`](../DEVELOPMENT_TRACKER.md) |
| Financial COGS per lookup | [`04_FINANCIAL_PLAN.md`](./04_FINANCIAL_PLAN.md) §2.1 |
