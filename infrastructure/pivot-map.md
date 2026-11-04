# Infrastructure Pivoting — dominio v4476.com

## Punto di partenza

Tutti gli URL e domini elencati negli IOC del CERT-AGID (Fase 2) condividono lo stesso dominio radice: **`v4476.com`**. Il pivoting OSINT parte da qui, con l'obiettivo di capire se questa infrastruttura è dedicata esclusivamente alla campagna italiana o condivisa con altri bersagli.

## Metodo

Ricerca passiva tramite **Certificate Transparency log** (Censys), nessuna visita diretta al dominio.

Primo tentativo (fallito): query generica `names: v4476.com` — risultato rumoroso, ha trovato domini completamente estranei che contengono per coincidenza la sottostringa `4476.com` (es. `teamcity-9163-4476.com`, infrastrutture aziendali legittime senza alcuna relazione con la campagna). Lezione: una ricerca per sottostringa libera non equivale a una ricerca per sottodominio esatto.

Query corretta, con match esatto sul suffisso: **`cert.names: ".v4476.com"`** — 3 risultati, tutti genuinamente riferiti all'infrastruttura in esame.

## Risultati

| Host | Validità certificato | CA | Confidenza |
|---|---|---|---|
| `panel.v4476.com` | 24/09/2026 → 23/12/2026 | Let's Encrypt (CN=YE2) | A1 — osservazione diretta da log di trasparenza dei certificati |
| `panel.v4476.com` (cert. precedente) | 22/09/2026 → 21/12/2026 | Let's Encrypt (CN=YE1) | A1 |
| `panel.v4476.com` (cert. precedente) | 23/09/2026 → 22/12/2026 | Let's Encrypt (CN=YE1) | A1 |

Validità di ~90 giorni e emissione automatizzata (Let's Encrypt) in rapida sequenza (3 certificati in meno di 48 ore) — coerente con un'infrastruttura automatizzata e "usa e getta", tipica di toolkit di phishing/malware-as-a-service.

## Scoperta principale: riuso multi-paese dell'infrastruttura

Gli stessi certificati elencano, come **Subject Alternative Names (SAN)**, nomi host riferiti a enti di **almeno 5 paesi diversi**, oltre all'Italia:

| Sottodominio SAN | Ente impersonato |
|---|---|
| `salute.gov.it.v4476.com` | Ministero della Salute / SSN — Italia (campagna documentata da CERT-AGID) |
| `health.gov.za.v4476.com` | Ministero della Sanità — Sudafrica |
| `health.govt.nz.v4476.com` | Ministero della Sanità — Nuova Zelanda |
| `met.police.uk.v4476.com` | Metropolitan Police — Regno Unito |
| `ad.gob.es.v4476.com`, `ministeriosanidad.com.v4476.com` | Enti governativi/sanitari — Spagna |
| `crypto.com.v4476.com`, `meet.google.com.v4476.com`, `google.com.v4476.com` | Brand generici ad alta fiducia (non enti pubblici) |
| `panel.v4476.com` | Probabile pannello di controllo centrale dell'infrastruttura |

**Interpretazione (confidenza: alta, A2)**: `v4476.com` non è un'infrastruttura costruita su misura per colpire l'Italia, ma una piattaforma di phishing/distribuzione malware **riutilizzabile e multi-bersaglio**, in cui il tema dell'esca (sanità, polizia, servizi generici) viene intercambiato a seconda della campagna. Questo corrobora direttamente quanto osservato da ThreatFabric sul malware StreamRat: *"gli attaccanti possono cambiare bersaglio senza modificare o ridistribuire il malware"* — qui lo stesso principio si osserva anche a livello di infrastruttura di distribuzione, non solo del malware stesso.

**Cautela dichiarata**: non è possibile stabilire con certezza se tutte queste istanze (Italia, Sudafrica, Nuova Zelanda, UK, Spagna) fossero attive simultaneamente o distribuite nel tempo — i tre certificati osservati sono relativi allo stesso breve periodo (settembre 2026), ma la presenza nel SAN non implica necessariamente una campagna attiva contemporanea per ciascun ente elencato.
