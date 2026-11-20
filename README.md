# CTI Report — StreamRat/XWorm Campaign Against the SSN (Fake Healthcare Website)

Cyber Threat Intelligence report on a real malicious campaign detected by CERT-AGID (Italy's government CERT, 24/09/2026), which distributes **StreamRat** (Android) and **XWorm** (Windows) through a fake Servizio Sanitario Nazionale (SSN, Italian National Health Service) website, with the payload differentiated by the visitor's User-Agent.

Full report: [`report/CTI-report.md`](report/CTI-report.md) (technical annex) · [`report/executive-summary.md`](report/executive-summary.md) (non-technical summary)

## Key Findings

- **5 sources evaluated** with the Admiralty Code; primary source CERT-AGID (A1), independently corroborated by ThreatFabric (discoverer of StreamRat)
- **63 IOCs** normalized and enriched (VirusTotal 17/17 hashes, ThreatFox 3/3 IPs) — revealed **at least 4 distinct families/stages** in the infection chain, including one family ("Alien") not mentioned in the original report
- **Infrastructure reused against at least 5 countries** (Italy, South Africa, New Zealand, United Kingdom, Spain), discovered through passive pivoting on Certificate Transparency — not a campaign dedicated to Italy, but an instance of commodity phishing infrastructure
- **11 MITRE ATT&CK techniques** mapped and individually verified against the official source (Enterprise + Mobile), with exported ATT&CK Navigator layers
- TTPs linked to the NIS2 risk-management measures (Art. 24 of D.Lgs. 138/2024, the Italian transposition of NIS2) and to the notification timelines (Art. 25)

## Repository Structure

- `sources/` — source evaluation using the Admiralty Code
- `iocs/` — collected and enriched indicators of compromise
- `infrastructure/` — OSINT pivoting on the attackers' infrastructure
- `attack/` — technique mapping to MITRE ATT&CK + Navigator layers
- `context/` — regulatory context assessment (NIS2)
- `report/` — final report with executive summary and technical annex

## Safety Rules Followed

- OSINT pivoting always passive: only through third-party services (VirusTotal, ThreatFox, Censys), no direct visits to malicious domains/IPs
- No malware sample (APK/BAT) downloaded or executed — work based exclusively on IOCs and public reports already analyzed by third parties

## Primary Source

- CERT-AGID: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
