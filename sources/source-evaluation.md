# Source Evaluation — Admiralty Code

Methodology: each source is evaluated along two independent axes — **source reliability** (A-F) and **credibility of the specific information cited** (1-6). The code is assigned per individual claim cited, not for the whole document, because a single source can contain information with different levels of certainty.

## Primary Source

### CERT-AGID — "Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows" ("Fake Servizio Sanitario Nazionale website distributes StreamRat on Android and XWorm on Windows"; SSN = Italian National Health Service)
- **URL**: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
- **Date**: 24/09/2026
- **Type**: Italian government CERT (AgID), direct technical analysis (reverse engineering of APK and BAT)

| Claim cited | Admiralty Code | Note |
|---|---|---|
| The fake site distributes different payloads based on the User-Agent (APK on Android, BAT on Windows) | **A1** | Direct technical analysis of the sample by CERT-AGID |
| StreamRat abuses Android Accessibility services for remote control, HTML overlays, screen capture | **A1** | Confirmed by direct analysis; independently corroborated by ThreatFabric |
| The "SSN" name is only a lure and does not prove that the healthcare sector is the target | **A1** | Explicit statement of caution by the source itself — good practice of honest analysis |
| The Windows chain goes from BAT → PowerShell → in-memory .NET loader → XWorm | **A1** | Direct analysis of the sample, including class names (`myprogram.Homees`, metodo `runss`) |

## Secondary Sources for Corroboration and Context

### ThreatFabric — "Uncovering StreamRat: From Meta Ads to Full Device Takeover"
- **URL**: https://www.threatfabric.com/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat
- **Date**: 02/09/2026
- **Type**: Mobile threat intelligence research lab — **discoverer and author of the name "StreamRat"**

| Claim cited | Admiralty Code | Note |
|---|---|---|
| StreamRat abuses Accessibility services for VNC/HVNC, overlays, keylogging, screen-blocking | **A1** | First-hand direct analysis, including bot commands documented one by one |
| Distribution campaign on Meta/TikTok targeting Spanish users (TV streaming theme, ~570,000 impressions) | **A1** | Fact directly observed by ThreatFabric — **but it concerns a different campaign from the Italian SSN one**, not applicable as evidence for the CERT-AGID campaign |
| StreamRat is distributed as MaaS (Malware-as-a-Service) by the same actor behind GodFather and Mirax | **A2** | Analyst inference based on control panel code similarities — probably true, not confirmed by an independent third-party source |

### Fortinet FortiGuard Labs — "Deep Dive into New XWorm Campaign Utilizing Multiple-Themed Phishing Emails"
- **URL**: https://www.fortinet.com/it/blog/threat-research/deep-dive-into-new-xworm-campaign-utilizing-multiple-themed-phishing-emails
- **Date**: 10/02/2026
- **Type**: Primary security vendor, in-house threat research lab

| Claim cited | Admiralty Code | Note |
|---|---|---|
| XWorm is a commodity RAT active since 2022, also distributed via Telegram marketplaces, used by multiple distinct groups | **A1** | Fact directly confirmed by its own lab — useful as general context on XWorm |
| This specific campaign (Excel attachment + CVE-2018-0802) is the same one observed by CERT-AGID in Italy | — | **Not applicable**: completely different infection vector (email/Excel vs website/BAT) — must not be cited as evidence for the SSN campaign |

### 2-spyware.com — "XWorm RAT: what it is..."
- **URL**: https://www.2-spyware.com/remove-xworm-rat.html
- **Date**: facts verified 25/10/2026
- **Type**: Consumer-oriented malware removal site, aggregator of vendor sources (Trellix, Gurucul, The Hacker News, Logpoint)

| Claim cited | Admiralty Code | Note |
|---|---|---|
| XWorm uses AMSI bypass via script and process hollowing in RegSvcs.exe to hide | **B1** | Not original analysis, but correctly reports (citing sources) Trellix analysis; corroborated by multiple vendors cited in the same article |
| XWorm is also distributed via trojanized builders shared on GitHub/Telegram/YouTube | **B2** | Reported citing The Hacker News; good transparency about the original source but second-hand information |

### Matricedigitale.it — "Falso sito SSN infetta Android e Windows: StreamRAT e XWorm in Italia" ("Fake SSN site infects Android and Windows: StreamRAT and XWorm in Italy")
- **URL**: https://www.matricedigitale.it/2026/09/24/falso-sito-ssn-streamrat-android-xworm-windows/
- **Date**: 24/09/2026 (same day as the CERT-AGID report)
- **Type**: Italian tech/security news outlet, reports without original technical analysis

| Claim cited | Admiralty Code | Note |
|---|---|---|
| StreamRAT on Android, XWorm on Windows, differentiated distribution from the same fake SSN site | **C1** | Matches the CERT-AGID primary source exactly — maximum credibility because corroborated, lower source reliability because it is not original technical analysis |
| The campaign fits a trend of healthcare/public-services lures in Italy in 2026 (Fascicolo Sanitario Elettronico [Electronic Health Record] refund, Agenzia Entrate [Italian Revenue Agency] holiday bonus) | **C2** | Plausible contextual observation by the journalist, not verified with own aggregate data |

## Summary

5 sources evaluated: 1 primary (CERT-AGID) and 4 secondary for corroboration/context. The central technical claims of the campaign (platform-differentiated distribution, StreamRat capabilities, XWorm infection chain) reach **A1** thanks to independent corroboration between CERT-AGID and ThreatFabric. The Fortinet and matricedigitale sources are used exclusively for broader context (XWorm as commodity malware, trend of Italian public-themed campaigns), not as direct evidence of specific details of the SSN campaign.
