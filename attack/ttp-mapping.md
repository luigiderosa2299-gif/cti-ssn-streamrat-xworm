XWorm chain (Windows side)
| Technique ID | Name | Tactic | Behavior | Source |
|---|---|---|---|---|
| T1566.002  | Spearphishing Link | Initial Access | The site delivers a .bat file downloaded by the victim (malware delivery via website) | CERT-AGID A1 |
| T1027.016 | Junk Code Insertion | Stealth | The BAT file contains "fake" code sections (hardware checks that are never executed) to confuse analysis — an obfuscation technique | CERT-AGID A1 |
| T1059.001 | Command and Scripting Interpreter: PowerShell | Execution | The SSN Windows.bat file launches a second PowerShell instance with a hidden window to run the next loader | CERT-AGID, A1 |
| T1036.008 | Masquerading : Masquerade File Type | Stealth | PowerShell downloads a 2.jpg file that actually contains a Base64 string — a technique for hiding the payload inside an apparently harmless format | CERT-AGID A1 |
| T1620 | Reflective code Loading | Stealth | The decoded Base64 code is loaded directly into memory (System.Reflection.Assembly::Load()), without ever writing the final executable to disk | CERT-AGID A1 |
| T1071 | Application Layer Protocol | Command and Control | XWorm (the final RAT) communicates with a command-and-control (C2) server | CERT-AGID A1 |

StreamRat chain (Android side)
| Technique ID | Name | Tactic | Behavior | Source |
|---|---|---|---|---|
| T1476 | Deliver Malicious Application via Other Means | Initial Access | The site offers the download of an APK posing as the official SSN app | CERT-AGID A1 |
| T1406 | Obfuscated Files or Information | Defense Evasion | The APK hides a second payload encrypted with XOR, decoded by a native library | CERT-AGID A1 |
| T1626 | Abuse Elevation Control Mechanism | Privilege Escalation | The app asks the user to enable Android Accessibility services to gain control of the interface | CERT-AGID A1 |
| T1417.002 | Input Capture: GUI Input Capture | Credential Access | The malware uses HTML overlays drawn over other apps to steal data entered by the user | CERT-AGID A1 |
| T1437.001 | Application Layer Protocol: Web Protocols | Command and Control | Communication with the C2 server via WebSocket over TLS | CERT-AGID A1 |
 
