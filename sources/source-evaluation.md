# Valutazione delle fonti — Admiralty Code

Metodologia: ogni fonte viene valutata su due assi indipendenti — **affidabilità della fonte** (A-F) e **credibilità dell'informazione specifica citata** (1-6). Il codice è assegnato per singola affermazione citata, non per l'intero documento, perché una stessa fonte può contenere informazioni con livelli di certezza diversi.

## Fonte primaria

### CERT-AGID — "Falso sito del Servizio Sanitario Nazionale distribuisce StreamRat su Android e XWorm su Windows"
- **URL**: https://cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/
- **Data**: 24/09/2026
- **Tipo**: CERT governativo italiano (AgID), analisi tecnica diretta (reverse engineering di APK e BAT)

| Affermazione citata | Codice Admiralty | Nota |
|---|---|---|
| Il falso sito distribuisce payload diversi in base allo User-Agent (APK su Android, BAT su Windows) | **A1** | Analisi tecnica diretta del CERT-AGID sul campione |
| StreamRat abusa dei servizi di Accessibilità Android per controllo remoto, overlay HTML, screen capture | **A1** | Confermato da analisi diretta; corroborato indipendentemente da ThreatFabric |
| Il nome "SSN" è solo un'esca, non prova che il bersaglio sia il settore sanitario | **A1** | Dichiarazione esplicita di cautela della fonte stessa — buona pratica di analisi onesta |
| La catena Windows passa da BAT → PowerShell → loader .NET in memoria → XWorm | **A1** | Analisi diretta del campione, inclusi nomi di classe (`myprogram.Homees`, metodo `runss`) |

## Fonti secondarie di corroborazione e contesto

### ThreatFabric — "Uncovering StreamRat: From Meta Ads to Full Device Takeover"
- **URL**: https://www.threatfabric.com/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat
- **Data**: 02/09/2026
- **Tipo**: Laboratorio di ricerca mobile threat intelligence — **scopritore e autore del nome "StreamRat"**

| Affermazione citata | Codice Admiralty | Nota |
|---|---|---|
| StreamRat abusa dei servizi di Accessibilità per VNC/HVNC, overlay, keylogging, screen-blocking | **A1** | Analisi diretta di prima mano, inclusi comandi del bot documentati uno per uno |
| Campagna di distribuzione su Meta/TikTok verso utenti spagnoli (tema streaming TV, ~570.000 impression) | **A1** | Fatto diretto osservato da ThreatFabric — **ma riguarda una campagna diversa da quella SSN italiana**, non applicabile come prova della campagna CERT-AGID |
| StreamRat è distribuito come MaaS (Malware-as-a-Service) dallo stesso attore dietro GodFather e Mirax | **A2** | Inferenza dell'analista basata su somiglianze di codice del control panel — probabilmente vera, non confermata da fonte terza indipendente |

### Fortinet FortiGuard Labs — "Deep Dive into New XWorm Campaign Utilizing Multiple-Themed Phishing Emails"
- **URL**: https://www.fortinet.com/it/blog/threat-research/deep-dive-into-new-xworm-campaign-utilizing-multiple-themed-phishing-emails
- **Data**: 10/02/2026
- **Tipo**: Vendor di sicurezza primario, laboratorio di ricerca minacce proprio

| Affermazione citata | Codice Admiralty | Nota |
|---|---|---|
| XWorm è un RAT commodity attivo dal 2022, distribuito anche via marketplace Telegram, usato da più gruppi distinti | **A1** | Fatto diretto confermato dal proprio laboratorio — utile come contesto generale su XWorm |
| Questa specifica campagna (allegato Excel + CVE-2018-0802) è la stessa osservata da CERT-AGID in Italia | — | **Non applicabile**: vettore di infezione completamente diverso (email/Excel vs sito web/BAT) — non va citata come prova della campagna SSN |

### 2-spyware.com — "XWorm RAT: what it is..."
- **URL**: https://www.2-spyware.com/remove-xworm-rat.html
- **Data**: fatti verificati 25/10/2026
- **Tipo**: Sito di rimozione malware orientato ai consumatori, aggregatore di fonti vendor (Trellix, Gurucul, The Hacker News, Logpoint)

| Affermazione citata | Codice Admiralty | Nota |
|---|---|---|
| XWorm usa bypass AMSI via script e process hollowing in RegSvcs.exe per nascondersi | **B1** | Non è analisi propria, ma riporta correttamente (citando le fonti) analisi di Trellix; corroborato da più vendor citati nello stesso articolo |
| XWorm è distribuito anche tramite builder trojanizzati condivisi su GitHub/Telegram/YouTube | **B2** | Riportato citando The Hacker News, buona trasparenza sulla fonte originale ma informazione di seconda mano |

### Matricedigitale.it — "Falso sito SSN infetta Android e Windows: StreamRAT e XWorm in Italia"
- **URL**: https://www.matricedigitale.it/2026/09/24/falso-sito-ssn-streamrat-android-xworm-windows/
- **Data**: 24/09/2026 (stesso giorno del report CERT-AGID)
- **Tipo**: Testata giornalistica tech/sicurezza italiana, riporta senza analisi tecnica propria

| Affermazione citata | Codice Admiralty | Nota |
|---|---|---|
| StreamRAT su Android, XWorm su Windows, distribuzione differenziata dallo stesso falso sito SSN | **C1** | Coincide esattamente con la fonte primaria CERT-AGID — credibilità massima perché corroborata, affidabilità della fonte più bassa perché non è analisi tecnica originale |
| La campagna si inserisce in un trend di esche a tema sanità/servizi pubblici in Italia nel 2026 (rimborso Fascicolo Sanitario Elettronico, bonus vacanze Agenzia Entrate) | **C2** | Osservazione di contesto plausibile del giornalista, non verificata con dati aggregati propri |

## Sintesi

5 fonti valutate, 1 primaria (CERT-AGID) e 4 secondarie di corroborazione/contesto. Le affermazioni tecniche centrali della campagna (distribuzione differenziata per piattaforma, capacità di StreamRat, catena d'infezione XWorm) raggiungono **A1** grazie a corroborazione indipendente tra CERT-AGID e ThreatFabric. Le fonti Fortinet e matricedigitale sono usate esclusivamente per contesto più ampio (XWorm come malware commodity, trend di campagne italiane a tema pubblico), non come prova diretta di dettagli specifici della campagna SSN.
