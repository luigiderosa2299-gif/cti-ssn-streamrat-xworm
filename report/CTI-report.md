# CTI Report — Campagna StreamRat/XWorm contro il falso sito SSN

## Executive Summary

Vedi [`executive-summary.md`](executive-summary.md) per la sintesi non tecnica orientata alla decisione.

## Allegato tecnico

### 1. Scenario e fonte primaria

Il 24/09/2026 il CERT-AGID ha pubblicato l'analisi di una campagna malevola che sfrutta un falso sito del Servizio Sanitario Nazionale, consegnando payload diverso in base allo User-Agent del visitatore: **StreamRat** su Android, **XWorm** su Windows.

Fonte primaria: `cert-agid.gov.it/news/falso-sito-del-servizio-sanitario-nazionale-distribuisce-streamrat-su-android-e-xworm-su-windows/`

### 2. Valutazione delle fonti (Admiralty Code)

5 fonti valutate con metodologia Admiralty Code — fonte primaria CERT-AGID (A1 su tutte le affermazioni tecniche dirette), corroborazione indipendente da ThreatFabric (scopritore di StreamRat, A1), contesto generale da Fortinet FortiGuard Labs e da testate giornalistiche italiane (C1, corroborazione senza analisi tecnica propria).

Dettaglio completo: [`../sources/source-evaluation.md`](../sources/source-evaluation.md)

### 3. Indicatori di Compromissione

63 IOC normalizzati (9 MD5, 9 SHA1, 17 SHA256, 10 URL, 14 domini, 3 IP) a partire dai due feed IOCA pubblicati dal CERT-AGID, uniti e deduplicati via script Python.

Arricchimento con VirusTotal (17/17 hash controllati) e ThreatFox (3/3 IP controllati) ha rivelato **almeno 4 famiglie/stadi distinti** nella catena d'infezione, inclusa una famiglia ("Alien", trojan bancario Android) non menzionata nell'articolo CERT-AGID originale.

Dettaglio completo: [`../iocs/iocs.csv`](../iocs/iocs.csv), [`../iocs/ioc-enrichment.md`](../iocs/ioc-enrichment.md)

### 4. Infrastruttura

Pivoting OSINT passivo (Certificate Transparency via Censys) sul dominio radice `v4476.com` ha rivelato un'infrastruttura di phishing **riutilizzata contro almeno 5 paesi** (Italia, Sudafrica, Nuova Zelanda, Regno Unito, Spagna) e brand generici (Google Meet, Crypto.com) — non una campagna costruita su misura per l'Italia, ma un'istanza di un'infrastruttura di distribuzione malware commodity.

Dettaglio completo: [`../infrastructure/pivot-map.md`](../infrastructure/pivot-map.md)

### 5. Tecniche, Tattiche e Procedure (MITRE ATT&CK)

11 tecniche mappate e verificate individualmente sulla fonte ufficiale (6 su matrice Enterprise/Windows per la catena XWorm, 5 su matrice Mobile/Android per la catena StreamRat), ciascuna collegata al comportamento specifico osservato e alla fonte con relativo codice Admiralty.

Dettaglio completo: [`../attack/ttp-mapping.md`](../attack/ttp-mapping.md) — layer ATT&CK Navigator in [`../attack/layer-enterprise.json`](../attack/layer-enterprise.json) e [`../attack/layer-mobile.json`](../attack/layer-mobile.json)

### 6. Contesto normativo (NIS2)

Le tecniche mappate sono state collegate alle misure di gestione del rischio previste dall'Art. 24 del D.Lgs. 138/2024 (recepimento italiano della Direttiva NIS2), con le relative tempistiche di notifica al CSIRT Italia in caso di incidente significativo (24h pre-notifica, 72h notifica, 1 mese relazione finale — Art. 25).

Dettaglio completo: [`../context/nis2-mapping.md`](../context/nis2-mapping.md)

## Metodologia generale

- Nessuna interazione diretta con infrastruttura o campioni malevoli: pivoting esclusivamente passivo tramite servizi terzi (Censys, VirusTotal, ThreatFox)
- Nessun campione malware scaricato o eseguito
- Ogni affermazione tecnica tracciabile a una fonte con relativo codice Admiralty
- Limiti e incertezze dichiarati esplicitamente in ciascun documento di dettaglio, non nascosti
