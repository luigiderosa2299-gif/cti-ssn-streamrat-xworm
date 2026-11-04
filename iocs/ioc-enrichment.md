# Arricchimento IOC — VirusTotal e ThreatFox

Metodologia: inizialmente campionati 3 hash SHA256 rappresentativi per tipo di stadio sospettato; dato che il formato IOCA del CERT-AGID non correla esplicitamente MD5/SHA1/SHA256 dello stesso campione (9 MD5, 9 SHA1, ma 17 SHA256 — asimmetria che non permette di assumere relazioni 1:1), l'arricchimento è stato estdato a **tutti i 17 SHA256** disponibili per verificare quanti stadi/famiglie distinte fossero realmente presenti.

## Risultati VirusTotal (17/17 hash controllati)

| Hash SHA256 (troncato) | Detection ratio | Tag principali | Interpretazione |
|---|---|---|---|
| `bd183756...` | **52/71** | Trojan:MSIL/XWorm.c1879efe | **Payload finale Windows** — XWorm, compilato MSIL (.NET), coerente con la catena BAT→PowerShell→loader descritta da CERT-AGID |
| `af46824...` | 5/61 | trojan.base64/bhgd, Trojan.Base64.Reverser | **Loader intermedio** — basso detection perché il contenuto è principalmente offuscamento Base64, non codice malevolo riconoscibile. Probabile corrispondenza con il file `2.jpg` descritto da CERT-AGID |
| `e38a08f7...` | 16/59 | TrojanDropper:Android/Hqwar.cec09aff | **Dropper Android — famiglia Hqwar** (variante 1) |
| `c28f5f55...` | 16/60 | TrojanDropper:Android/Hqwar.85022f23, APK:CRepMalware | **Dropper Android — famiglia Hqwar** (variante 2, hash diverso, stesso tag famiglia) |
| `7b38338d...` | 25/61 | trojan.alien/batagent, Dropper.DR/SNH | **Scoperta non descritta nell'articolo originale** — famiglia "Alien", trojan bancario Android noto, distinto da StreamRat e Hqwar |
| `d3a7938d...` | 15/67 | Android.Trojan.Banker.BCP, Trojan:Win32/Ravartar!rfn | Tag incoerenti tra motori (nome Windows su un probabile file Android) — probabile euristica generica, non conclusivo |
| `492682f8...` | **0/61** | — | File noto a VirusTotal ma **nessun motore lo segnala** — possibile evasione efficace o componente non malevolo di per sé |
| 10 hash rimanenti | nessun risultato | — | Non presenti su VirusTotal — la maggioranza dei file della catena non è mai stata caricata/analizzata pubblicamente |

## Sintesi stadi identificati

Contrariamente all'ipotesi iniziale (3 hash = 3 stadi semplici), l'arricchimento completo rivela **almeno 4 famiglie/stadi distinti**:
1. Dropper Android iniziale — famiglia **Hqwar** (2 campioni)
2. Componente con tag **Alien** (trojan bancario Android) — non menzionato nell'articolo CERT-AGID originale, possibile riuso di tecniche/codice tra famiglie
3. Loader Base64 offuscato (basso detection, consistente con il file `2.jpg` lato Windows)
4. Payload finale **XWorm** (Windows, MSIL/.NET)

Più un componente a detection zero (`492682f8...`) che richiederebbe analisi dinamica per essere classificato con certezza — fuori scope per questo lab (nessuna esecuzione di campioni, solo analisi OSINT passiva).

## Risultati ThreatFox (3/3 IP controllati)

| IP | Risultato |
|---|---|
| Tutti e 3 gli IP della campagna | `no_result` — nessuno dei tre IP è presente nel database ThreatFox |

Interpretazione: l'infrastruttura di rete usata in questa campagna non risulta ripresa da ThreatFox al momento della verifica — possibile indicazione di un'infrastruttura usata in modo mirato/limitato a questa campagna italiana, non ancora (o mai) condivisa con i feed di intelligence internazionali aggregati da abuse.ch.

## Limiti dichiarati

- Il formato IOCA non permette di correlare con certezza quali MD5/SHA1 corrispondano a quali SHA256 dello stesso file.
- Non è stato eseguito nessun campione malware (né scaricato alcun file) — l'analisi si basa esclusivamente su hash/detection ratio pubblici già elaborati da VirusTotal.
- Il componente a 0/61 e i tag incoerenti (Win32 su probabile file Android) richiederebbero analisi dinamica/manuale per essere interpretati con certezza — non eseguita, fuori scope per policy di sicurezza del lab.
