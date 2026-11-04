import json
import csv

with open ("iocs/raw/StreamRAT-XWorm-24-09-2026.json") as f:
    dati1 = json.load(f)
evento1 = list(dati1.values())[0]
ioc1 = evento1["ioc_list"]

with open("iocs/raw/StreamRAT-XWorm-25-09-2026.json") as f :
    dati2 = json.load(f)
evento2 = list(dati2.values())[0]
ioc2 = evento2["ioc_list"]

md5_uniti = set(ioc1["md5"]) | set(ioc2["md5"])
sha1_uniti = set(ioc1["sha1"]) | set(ioc2["sha1"])
domain_uniti = set(ioc1["domain"]) | set(ioc2["domain"])
url_uniti = set(ioc1["url"]) | set(ioc2["url"])
ipv4_uniti = set(ioc1["ipv4"]) | set(ioc2["ipv4"])
sha256_uniti = set(ioc1["sha256"]) | set(ioc2["sha256"])



print(f" MD5 unici: {len(md5_uniti)}")
print(f" sha1 unici: {len(sha1_uniti)}")
print(f" domain unici: {len(domain_uniti)}")
print(f" ipv4 unici: {len(ipv4_uniti)}")
print(f" url unici: {len(url_uniti)}")
print(f" sha256 unici: {len(sha256_uniti)}")

with open ("iocs/iocs.csv", "w", newline="") as f :
        writer = csv.writer(f)
        writer.writerow(["tipo", "valore"])
        for valore in md5_uniti:
             writer.writerow(["md5", valore])
        for valore in sha1_uniti:
                writer.writerow(["sha1", valore])
        for valore in sha256_uniti:
                writer.writerow(["sha256", valore])
        for valore in url_uniti:
                writer.writerow(["url", valore])
        for valore in domain_uniti:
                writer.writerow(["domain", valore]) 
        for valore in ipv4_uniti:
                writer.writerow(["ipv4", valore]) 








