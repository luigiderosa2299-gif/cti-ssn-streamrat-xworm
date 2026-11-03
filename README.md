# CTI Report — Campagna StreamRat/XWorm contro il SSN (falso sito sanitario)

Report di Cyber Threat Intelligence su una campagna malevola reale rilevata dal CERT-AGID (24/09/2026), che distribuisce **StreamRat** (Android) e **XWorm** (Windows) tramite un falso sito del Servizio Sanitario Nazionale, con payload differenziato in base allo User-Agent del visitatore.

## Struttura del lab

- `sources/` — valutazione delle fonti con Admiralty Code
- `iocs/` — indicatori di compromissione raccolti e arricchiti
- `infrastructure/` — pivoting OSINT sull'infrastruttura degli attaccanti
- `attack/` — mappatura delle tecniche su MITRE ATT&CK
- `context/` — valutazione del contesto normativo (NIS2)
- `detections/` — regole di detection (Sigma/KQL) derivate dalle TTP mappate
- `report/` — report finale con executive summary

## Stato di avanzamento

- [x] Fase 1 — Fonti e valutazione (Admiralty Code)
- [ ] Fase 2 — Raccolta e arricchimento IOC
- [ ] Fase 3 — Infrastructure pivoting OSINT
- [ ] Fase 4 — Analisi cross-platform e mappatura TTP/ATT&CK
- [ ] Fase 5 — Contesto normativo NIS2
- [ ] Fase 6 — Assessment e report finale
- [ ] Fase 7 — Regole di detection (bonus)

## Regole di sicurezza osservate

- Pivoting OSINT sempre passivo: solo tramite servizi terzi (VirusTotal, URLhaus, ThreatFox, crt.sh, urlscan.io), nessuna visita diretta a domini/IP malevoli.
- Nessun campione malware (APK/BAT) scaricato o eseguito — lavoro esclusivamente su IOC e report pubblici già analizzati da terzi.

## Fonti primarie

- CERT-AGID: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
