catena XWorm (lato Windows)
| ID tecnica | Nome | Tattica | Comportamento | Fonte |
|---|---|---|---|---|
| T1566.002  | Spearphishing Link | Initial Access | Il sito consegna un file .bat scaricato dalla vittima (consegna del malware tramite sito web) | CERT-AGID A1 |
| T1027.016 | Junk Code Insertion | Stealth | Il file BAT contiene sezioni di codice "finte" (controlli hardware mai eseguiti) per confondere l'analisi — tecnica di offuscamento | CERT-AGID A1 |
| T1059.001 | Command and Scripting Interpreter: PowerShell | Execution | Il file SSN Windows.bat avvia una seconda istanza di PowerShell con finestra nascosta per eseguire il loader successivo | CERT-AGID, A1 |
| T1036.008 | Masquerading : Masquerade File Type | Stealth | PowerShell scarica un file 2.jpg che in realtà contiene una stringa Base64 — tecnica di occultamento del payload dentro un formato apparentemente innocuo | CERT-AGID A1 |
| T1620 | Reflective code Loading | Stealth | Il codice Base64 decodificato viene caricato direttamente in memoria (System.Reflection.Assembly::Load()), senza mai scrivere l'eseguibile finale su disco | CERT-AGID A1 |
| T1071 | Application Layer Protocol | Command and Control | XWorm (il RAT finale) comunica con un server di comando e controllo (C2) | CERT-AGID A1 |

catena StreamRat (lato Android)
| ID tecnica | Nome | Tattica | Comportamento | Fonte |
|---|---|---|---|---|
| T1476 | Deliver Malicious Application via Other Means | Initial Access | Il sito propone il download di un APK che si finge l'app ufficiale SSN | CERT-AGID A1 |
| T1406 | Obfuscated Files or Information | Defense Evasion | L'APK nasconde un secondo payload cifrato con XOR, decodificato da una libreria nativa | CERT-AGID A1 |
| T1626 | Abuse Elevation Control Mechanism | Privilege Escalation | L'app richiede l'abilitazione dei servizi di Accessibilità di Android per ottenere controllo dell'interfaccia | CERT-AGID A1 |
| T1417.002 | Input Capture: GUI Input Capture | Credential Access | Il malware usa overlay HTML sovrapposti alle altre app per rubare dati inseriti dall'utente | CERT-AGID A1 |
| T1437.001 | Application Layer Protocol: Web Protocols | Command and Control | Comunicazione con il server C2 tramite WebSocket su TLS | CERT-AGID A1 |
 
