# CTI Report — Campagna StreamRat/XWorm contro il SSN (falso sito sanitario)

Report di Cyber Threat Intelligence su una campagna malevola reale rilevata dal CERT-AGID (24/09/2026), che distribuisce **StreamRat** (Android) e **XWorm** (Windows) tramite un falso sito del Servizio Sanitario Nazionale, con payload differenziato in base allo User-Agent del visitatore.

Report completo: [`report/CTI-report.md`](report/CTI-report.md) (allegato tecnico) · [`report/executive-summary.md`](report/executive-summary.md) (sintesi non tecnica)

## Principali risultati

- **5 fonti valutate** con Admiralty Code, fonte primaria CERT-AGID (A1) corroborata indipendentemente da ThreatFabric (scopritore di StreamRat)
- **63 IOC** normalizzati e arricchiti (VirusTotal 17/17 hash, ThreatFox 3/3 IP) — rivelate **almeno 4 famiglie/stadi distinti** nella catena d'infezione, inclusa una famiglia ("Alien") non menzionata nel report originale
- **Infrastruttura riutilizzata contro almeno 5 paesi** (Italia, Sudafrica, Nuova Zelanda, Regno Unito, Spagna) scoperta tramite pivoting passivo su Certificate Transparency — non una campagna dedicata all'Italia, ma un'istanza di infrastruttura phishing commodity
- **11 tecniche MITRE ATT&CK** mappate e verificate individualmente sulla fonte ufficiale (Enterprise + Mobile), con layer ATT&CK Navigator esportati
- TTP collegate alle misure di gestione del rischio NIS2 (Art. 24 D.Lgs. 138/2024) e alle tempistiche di notifica (Art. 25)

## Struttura del repository

- `sources/` — valutazione delle fonti con Admiralty Code
- `iocs/` — indicatori di compromissione raccolti e arricchiti
- `infrastructure/` — pivoting OSINT sull'infrastruttura degli attaccanti
- `attack/` — mappatura delle tecniche su MITRE ATT&CK + layer Navigator
- `context/` — valutazione del contesto normativo (NIS2)
- `report/` — report finale con executive summary e allegato tecnico

## Regole di sicurezza osservate

- Pivoting OSINT sempre passivo: solo tramite servizi terzi (VirusTotal, ThreatFox, Censys), nessuna visita diretta a domini/IP malevoli
- Nessun campione malware (APK/BAT) scaricato o eseguito — lavoro esclusivamente su IOC e report pubblici già analizzati da terzi

## Fonte primaria

- CERT-AGID: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
