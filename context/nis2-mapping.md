# Dai TTP ai requisiti NIS2 (D.Lgs. 138/2024)

Metodologia: le misure NIS2 derivano direttamente dalle tecniche ATT&CK mappate nella Fase 4 (non da un'organizzazione fittizia) — per ogni tecnica, la mitigazione raccomandata da MITRE viene collegata alla categoria di misura corrispondente prevista dall'**Articolo 24** del D.Lgs. 138/2024 (recepimento italiano della Direttiva NIS2 — attenzione: la numerazione italiana **non coincide** con quella della direttiva UE, dove le misure di sicurezza sono all'Art. 21; nel decreto italiano sono all'**Art. 24**).

## Tabella TTP → Mitigazione → Misura NIS2

| Tecnica ATT&CK | Mitigazione (da MITRE) | Misura NIS2 Art. 24 | Confidenza collegamento |
|---|---|---|---|
| T1566.002 (Spearphishing Link) | User Training, Network Intrusion Prevention | Formazione e igiene informatica di base; policy di sicurezza della posta elettronica | Alta — collegamento diretto e consolidato in letteratura |
| T1027.016 (Junk Code Insertion) | Antivirus/Antimalware comportamentale | Gestione delle vulnerabilità; rilevamento e risposta (EDR) | Media — l'offuscamento è difficile da mitigare preventivamente, serve detection comportamentale più che prevenzione |
| T1059.001 (PowerShell) | Disable or Remove Feature or Program; Execution Prevention (AppLocker/WDAC); Logging PowerShell (ScriptBlock Logging) | Controllo degli accessi; policy di hardening dei sistemi; logging e monitoraggio | Alta — mitigazioni specifiche e ben documentate (restrizione dell'uso di PowerShell non necessario) |
| T1036.008 (Masquerade File Type) | User Training; Restrict File and Directory Permissions | Formazione del personale; policy di sicurezza sui download/allegati | Media — mitigazione principalmente comportamentale/umana, difficile da bloccare tecnicamente al 100% |
| T1620 (Reflective Code Loading) | Behavior Prevention on Endpoint (EDR); Restrict file and directory permissions | Gestione degli incidenti (rilevamento); soluzioni di rilevamento e risposta avanzate (EDR) | Media — tecnica difficile da prevenire, principalmente rilevabile a runtime |
| T1071 (Application Layer Protocol) | Network Intrusion Prevention; Filtraggio/monitoraggio del traffico di rete; SSL/TLS Inspection | Monitoraggio della rete; segmentazione; gestione degli incidenti | Alta — collegamento diretto, controllo di rete è categoria esplicita in NIS2 |
| T1476 (Deliver Malicious App via Other Means) | User Training; Restrict installazione da fonti non autorizzate (MDM) | Formazione e igiene informatica; policy di gestione dei dispositivi mobili | Alta |
| T1406 (Obfuscated Files or Information, Mobile) | Application Vetting | Gestione del rischio della catena di approvvigionamento (se tramite app store); controllo delle applicazioni installabili | Media |
| T1626 (Abuse Elevation Control Mechanism) | User Guidance; Use Recent OS Version | Formazione del personale; gestione delle patch/aggiornamenti | Alta — mitigazione MITRE esplicitamente di tipo formativo, coerente con Art. 24 |
| T1417.002 (GUI Input Capture / overlay) | Use Recent OS Version (restrizioni overlay Android 12+) | Gestione delle patch; policy di gestione dei dispositivi mobili (MDM) | Media |
| T1437.001 (Application Layer Protocol: Web Protocols, Mobile) | Network Intrusion Prevention | Monitoraggio della rete; gestione degli incidenti | Alta |

## Tempistiche di notifica (Art. 25, D.Lgs. 138/2024)

Se un dispositivo di un soggetto NIS (essenziale o importante) venisse compromesso da questa catena d'attacco (XWorm su Windows o StreamRat su Android) e l'incidente fosse classificato come **significativo** (grave perturbazione operativa, o perdite materiali/immateriali considerevoli per terzi), scatterebbero i seguenti obblighi verso il CSIRT Italia:

1. **Entro 24 ore** dalla conoscenza dell'incidente — pre-notifica, con indicazione se l'incidente sembra derivare da atti malevoli e se ha un possibile impatto transfrontaliero
2. **Entro 72 ore** — notifica con aggiornamento delle informazioni, valutazione iniziale di gravità/impatto, e IoC disponibili (qui entrerebbero in gioco esattamente gli IOC raccolti nella Fase 2 di questo lab)
3. **Su richiesta del CSIRT** — relazione intermedia sugli aggiornamenti
4. **Entro 1 mese** dalla notifica — relazione finale con descrizione dettagliata, causa, misure di attenuazione adottate

Nota: l'obbligo di notifica decorre dal 1° gennaio 2026; le notifiche volontarie (anche di minacce o quasi-incidenti, non solo incidenti significativi) sono possibili fin da subito (Art. 26).

## Perimetro di Sicurezza Nazionale Cibernetica (nota distintiva)

Il Perimetro di Sicurezza Nazionale Cibernetica (PSNC, introdotto dal D.L. 105/2019, distinto da NIS2) è un regime normativo **separato**, rivolto esclusivamente a soggetti pubblici e privati che erogano **funzioni o servizi essenziali per lo Stato** (non tutte le aziende NIS2 rientrano nel Perimetro — è un sottoinsieme più ristretto e più critico). Una PMI generica soggetta a NIS2 non rientrerebbe automaticamente nel Perimetro, a meno di operare in settori/infrastrutture di rilevanza strategica nazionale esplicitamente individuati.

## Limiti dichiarati

- Le misure NIS2 elencate non derivano da un elenco ufficiale e completo delle "41 misure di sicurezza" previste dalla determinazione ACN (non reperito nella ricerca OSINT condotta) — sono categorie generali citate esplicitamente nell'Art. 24 e nelle fonti secondarie consultate, non la lista tecnica completa e numerata.
- Il collegamento "tecnica → misura" riflette un ragionamento analitico personale, non una mappatura ufficiale pubblicata da ACN o MITRE — va trattato come ipotesi di lavoro ragionevole, non come riferimento normativo certificato.
