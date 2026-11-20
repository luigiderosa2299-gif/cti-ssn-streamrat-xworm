# From TTPs to NIS2 Requirements (D.Lgs. 138/2024)

Methodology: the NIS2 measures derive directly from the ATT&CK techniques mapped in Phase 4 (not from a fictitious organization) — for each technique, the mitigation recommended by MITRE is linked to the corresponding measure category set out in **Article 24** of D.Lgs. 138/2024 (the Italian transposition of the NIS2 Directive — note: the Italian numbering **does not match** that of the EU directive, where the security measures are in Art. 21; in the Italian decree they are in **Art. 24**).

## TTP → Mitigation → NIS2 Measure Table

| ATT&CK Technique | Mitigation (from MITRE) | NIS2 Art. 24 Measure | Link Confidence |
|---|---|---|---|
| T1566.002 (Spearphishing Link) | User Training, Network Intrusion Prevention | Training and basic cyber hygiene; email security policy | High — direct link, well established in the literature |
| T1027.016 (Junk Code Insertion) | Behavioral Antivirus/Antimalware | Vulnerability management; detection and response (EDR) | Medium — obfuscation is hard to mitigate preventively; it calls for behavioral detection rather than prevention |
| T1059.001 (PowerShell) | Disable or Remove Feature or Program; Execution Prevention (AppLocker/WDAC); Logging PowerShell (ScriptBlock Logging) | Access control; system hardening policy; logging and monitoring | High — specific, well-documented mitigations (restricting unnecessary PowerShell use) |
| T1036.008 (Masquerade File Type) | User Training; Restrict File and Directory Permissions | Staff training; download/attachment security policy | Medium — mitigation is mainly behavioral/human, difficult to block technically at 100% |
| T1620 (Reflective Code Loading) | Behavior Prevention on Endpoint (EDR); Restrict file and directory permissions | Incident management (detection); advanced detection and response solutions (EDR) | Medium — technique hard to prevent, mainly detectable at runtime |
| T1071 (Application Layer Protocol) | Network Intrusion Prevention; Network traffic filtering/monitoring; SSL/TLS Inspection | Network monitoring; segmentation; incident management | High — direct link, network control is an explicit category in NIS2 |
| T1476 (Deliver Malicious App via Other Means) | User Training; Restrict installation from unauthorized sources (MDM) | Training and cyber hygiene; mobile device management policy | High |
| T1406 (Obfuscated Files or Information, Mobile) | Application Vetting | Supply chain risk management (if via app store); control of installable applications | Medium |
| T1626 (Abuse Elevation Control Mechanism) | User Guidance; Use Recent OS Version | Staff training; patch/update management | High — MITRE mitigation is explicitly training-oriented, consistent with Art. 24 |
| T1417.002 (GUI Input Capture / overlay) | Use Recent OS Version (Android 12+ overlay restrictions) | Patch management; mobile device management (MDM) policy | Medium |
| T1437.001 (Application Layer Protocol: Web Protocols, Mobile) | Network Intrusion Prevention | Network monitoring; incident management | High |

## Notification Timelines (Art. 25, D.Lgs. 138/2024)

If a device belonging to a NIS entity (essential or important) were compromised by this attack chain (XWorm on Windows or StreamRat on Android) and the incident were classified as **significant** (severe operational disruption, or considerable material/non-material losses for third parties), the following obligations toward CSIRT Italia (Italy's national CSIRT) would apply:

1. **Within 24 hours** of becoming aware of the incident — early warning, indicating whether the incident appears to result from malicious acts and whether it may have a cross-border impact
2. **Within 72 hours** — notification with updated information, initial severity/impact assessment, and available IoCs (this is exactly where the IOCs collected in Phase 2 of this lab would come into play)
3. **Upon CSIRT request** — intermediate report on updates
4. **Within 1 month** of the notification — final report with detailed description, cause, and mitigation measures adopted

Note: the notification obligation applies from 1 January 2026; voluntary notifications (also of threats or near-misses, not only significant incidents) are possible immediately (Art. 26).

## Perimetro di Sicurezza Nazionale Cibernetica (Italy's National Cybersecurity Perimeter) — Distinguishing Note

The Perimetro di Sicurezza Nazionale Cibernetica (PSNC, Italy's National Cybersecurity Perimeter, introduced by D.L. 105/2019 and distinct from NIS2) is a **separate** regulatory regime, aimed exclusively at public and private entities that provide **functions or services essential to the State** (not all NIS2 companies fall within the Perimeter — it is a narrower, more critical subset). A generic SME subject to NIS2 would not automatically fall within the Perimeter, unless it operates in explicitly identified sectors/infrastructures of national strategic relevance.

## Stated Limitations

- The NIS2 measures listed do not derive from an official, complete list of the "41 security measures" set out in the ACN (Agenzia per la Cybersicurezza Nazionale, Italy's National Cybersecurity Agency) determination (not found in the OSINT research conducted) — they are general categories explicitly cited in Art. 24 and in the secondary sources consulted, not the complete, numbered technical list.
- The "technique → measure" link reflects personal analytical reasoning, not an official mapping published by ACN or MITRE — it should be treated as a reasonable working hypothesis, not as a certified regulatory reference.
