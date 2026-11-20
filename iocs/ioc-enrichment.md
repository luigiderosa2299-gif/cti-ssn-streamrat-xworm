# IOC Enrichment — VirusTotal and ThreatFox

Methodology: initially 3 representative SHA256 hashes were sampled per suspected stage type; since CERT-AGID's IOCA format does not explicitly correlate the MD5/SHA1/SHA256 of the same sample (9 MD5, 9 SHA1, but 17 SHA256 — an asymmetry that prevents assuming 1:1 relationships), the enrichment was extended to **all 17 available SHA256 hashes** to verify how many distinct stages/families were actually present.

## VirusTotal Results (17/17 hashes checked)

| SHA256 Hash (truncated) | Detection ratio | Main tags | Interpretation |
|---|---|---|---|
| `bd183756...` | **52/71** | Trojan:MSIL/XWorm.c1879efe | **Final Windows payload** — XWorm, compiled MSIL (.NET), consistent with the BAT→PowerShell→loader chain described by CERT-AGID |
| `af46824...` | 5/61 | trojan.base64/bhgd, Trojan.Base64.Reverser | **Intermediate loader** — low detection because the content is mainly Base64 obfuscation, not recognizable malicious code. Probable match with the `2.jpg` file described by CERT-AGID |
| `e38a08f7...` | 16/59 | TrojanDropper:Android/Hqwar.cec09aff | **Android dropper — Hqwar family** (variant 1) |
| `c28f5f55...` | 16/60 | TrojanDropper:Android/Hqwar.85022f23, APK:CRepMalware | **Android dropper — Hqwar family** (variant 2, different hash, same family tag) |
| `7b38338d...` | 25/61 | trojan.alien/batagent, Dropper.DR/SNH | **Finding not described in the original article** — "Alien" family, a known Android banking trojan, distinct from StreamRat and Hqwar |
| `d3a7938d...` | 15/67 | Android.Trojan.Banker.BCP, Trojan:Win32/Ravartar!rfn | Inconsistent tags across engines (Windows name on a probable Android file) — probably a generic heuristic, inconclusive |
| `492682f8...` | **0/61** | — | File known to VirusTotal but **no engine flags it** — possible effective evasion or a component that is not malicious in itself |
| 10 remaining hashes | no result | — | Not present on VirusTotal — the majority of the files in the chain have never been publicly uploaded/analyzed |

## Summary of Identified Stages

Contrary to the initial hypothesis (3 hashes = 3 simple stages), the full enrichment reveals **at least 4 distinct families/stages**:
1. Initial Android dropper — **Hqwar** family (2 samples)
2. Component tagged **Alien** (Android banking trojan) — not mentioned in the original CERT-AGID article, possible reuse of techniques/code between families
3. Obfuscated Base64 loader (low detection, consistent with the `2.jpg` file on the Windows side)
4. Final **XWorm** payload (Windows, MSIL/.NET)

Plus a zero-detection component (`492682f8...`) that would require dynamic analysis to be classified with certainty — out of scope for this lab (no sample execution, passive OSINT analysis only).

## ThreatFox Results (3/3 IPs checked)

| IP | Result |
|---|---|
| All 3 campaign IPs | `no_result` — none of the three IPs is present in the ThreatFox database |

Interpretation: the network infrastructure used in this campaign does not appear in ThreatFox at the time of the check — a possible indication of infrastructure used in a targeted way/limited to this Italian campaign, not yet (or never) shared with the international intelligence feeds aggregated by abuse.ch.

## Stated Limitations

- The IOCA format does not allow determining with certainty which MD5/SHA1 correspond to which SHA256 of the same file.
- No malware sample was executed (nor any file downloaded) — the analysis is based exclusively on public hashes/detection ratios already processed by VirusTotal.
- The 0/61 component and the inconsistent tags (Win32 on a probable Android file) would require dynamic/manual analysis to be interpreted with certainty — not performed, out of scope per the lab's safety policy.
