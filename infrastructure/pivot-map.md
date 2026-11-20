# Infrastructure Pivoting — v4476.com domain

## Starting Point

All URLs and domains listed in CERT-AGID's IOCs (Phase 2) share the same root domain: **`v4476.com`**. OSINT pivoting starts here, with the goal of understanding whether this infrastructure is dedicated exclusively to the Italian campaign or shared with other targets.

## Method

Passive search via **Certificate Transparency logs** (Censys), no direct visit to the domain.

First attempt (failed): generic query `names: v4476.com` — noisy result, it found completely unrelated domains that coincidentally contain the substring `4476.com` (e.g. `teamcity-9163-4476.com`, legitimate corporate infrastructure with no relation to the campaign). Lesson: a free substring search is not equivalent to an exact subdomain search.

Correct query, with exact suffix match: **`cert.names: ".v4476.com"`** — 3 results, all genuinely related to the infrastructure under examination.

## Results

| Host | Certificate validity | CA | Confidence |
|---|---|---|---|
| `panel.v4476.com` | 24/09/2026 → 23/12/2026 | Let's Encrypt (CN=YE2) | A1 — direct observation from certificate transparency logs |
| `panel.v4476.com` (previous cert.) | 22/09/2026 → 21/12/2026 | Let's Encrypt (CN=YE1) | A1 |
| `panel.v4476.com` (previous cert.) | 23/09/2026 → 22/12/2026 | Let's Encrypt (CN=YE1) | A1 |

~90-day validity and automated issuance (Let's Encrypt) in rapid sequence (3 certificates in under 48 hours) — consistent with automated, "disposable" infrastructure, typical of phishing/malware-as-a-service toolkits.

## Key Finding: Multi-Country Reuse of the Infrastructure

The same certificates list, as **Subject Alternative Names (SAN)**, hostnames referring to entities in **at least 5 different countries**, besides Italy:

| SAN subdomain | Impersonated entity |
|---|---|
| `salute.gov.it.v4476.com` | Ministero della Salute (Italian Ministry of Health) / SSN — Italy (campaign documented by CERT-AGID) |
| `health.gov.za.v4476.com` | Ministry of Health — South Africa |
| `health.govt.nz.v4476.com` | Ministry of Health — New Zealand |
| `met.police.uk.v4476.com` | Metropolitan Police — United Kingdom |
| `ad.gob.es.v4476.com`, `ministeriosanidad.com.v4476.com` | Government/healthcare bodies — Spain |
| `crypto.com.v4476.com`, `meet.google.com.v4476.com`, `google.com.v4476.com` | Generic high-trust brands (not public bodies) |
| `panel.v4476.com` | Probable central control panel of the infrastructure |

**Interpretation (confidence: high, A2)**: `v4476.com` is not infrastructure built specifically to target Italy, but a **reusable, multi-target** phishing/malware-distribution platform, in which the lure theme (healthcare, police, generic services) is swapped depending on the campaign. This directly corroborates what ThreatFabric observed about the StreamRat malware: *"attackers can change targets without modifying or redistributing the malware"* — here the same principle is also observed at the level of the distribution infrastructure, not only of the malware itself.

**Stated caveat**: it is not possible to establish with certainty whether all these instances (Italy, South Africa, New Zealand, UK, Spain) were active simultaneously or spread over time — the three observed certificates relate to the same short period (September 2026), but presence in the SAN does not necessarily imply a concurrent active campaign for each listed entity.
