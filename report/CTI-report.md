# CTI Report — StreamRat/XWorm Campaign Against the Fake SSN Website

## Executive Summary

See [`executive-summary.md`](executive-summary.md) for the non-technical, decision-oriented summary.

## Technical Annex

### 1. Scenario and Primary Source

On 24/09/2026 CERT-AGID (Italy's government CERT) published its analysis of a malicious campaign that abuses a fake Servizio Sanitario Nazionale (SSN, Italian National Health Service) website, delivering a different payload depending on the visitor's User-Agent: **StreamRat** on Android, **XWorm** on Windows.

Primary source: `cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/`

### 2. Source Evaluation (Admiralty Code)

5 sources evaluated using the Admiralty Code — primary source CERT-AGID (A1 on all direct technical claims), independent corroboration from ThreatFabric (discoverer of StreamRat, A1), general context from Fortinet FortiGuard Labs and Italian news outlets (C1, corroboration without original technical analysis).

Full details: [`../sources/source-evaluation.md`](../sources/source-evaluation.md)

### 3. Indicators of Compromise

63 IOCs normalized (9 MD5, 9 SHA1, 17 SHA256, 10 URLs, 14 domains, 3 IPs) from the two IOCA feeds published by CERT-AGID, merged and deduplicated with a Python script.

Enrichment with VirusTotal (17/17 hashes checked) and ThreatFox (3/3 IPs checked) revealed **at least 4 distinct families/stages** in the infection chain, including one family ("Alien", an Android banking trojan) not mentioned in the original CERT-AGID article.

Full details: [`../iocs/iocs.csv`](../iocs/iocs.csv), [`../iocs/ioc-enrichment.md`](../iocs/ioc-enrichment.md)

### 4. Infrastructure

Passive OSINT pivoting (Certificate Transparency via Censys) on the root domain `v4476.com` revealed a phishing infrastructure **reused against at least 5 countries** (Italy, South Africa, New Zealand, United Kingdom, Spain) and generic brands (Google Meet, Crypto.com) — not a campaign tailored to Italy, but an instance of commodity malware-distribution infrastructure.

Full details: [`../infrastructure/pivot-map.md`](../infrastructure/pivot-map.md)

### 5. Tactics, Techniques and Procedures (MITRE ATT&CK)

11 techniques mapped and individually verified against the official source (6 on the Enterprise/Windows matrix for the XWorm chain, 5 on the Mobile/Android matrix for the StreamRat chain), each linked to the specific observed behavior and to the source with its Admiralty code.

Full details: [`../attack/ttp-mapping.md`](../attack/ttp-mapping.md) — ATT&CK Navigator layers in [`../attack/layer-enterprise.json`](../attack/layer-enterprise.json) and [`../attack/layer-mobile.json`](../attack/layer-mobile.json)

### 6. Regulatory Context (NIS2)

The mapped techniques were linked to the risk-management measures set out in Art. 24 of D.Lgs. 138/2024 (the Italian transposition of the NIS2 Directive), together with the notification timelines to CSIRT Italia (Italy's national CSIRT) in the event of a significant incident (24h early warning, 72h notification, 1 month final report — Art. 25).

Full details: [`../context/nis2-mapping.md`](../context/nis2-mapping.md)

## General Methodology

- No direct interaction with malicious infrastructure or samples: exclusively passive pivoting through third-party services (Censys, VirusTotal, ThreatFox)
- No malware sample downloaded or executed
- Every technical claim is traceable to a source with its Admiralty code
- Limitations and uncertainties are stated explicitly in each detailed document, not hidden
