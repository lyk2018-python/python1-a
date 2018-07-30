import pprint
import re

with open("Brca1Reads_7.2.fastq") as f:
    dosya_icerigi = f.read()

sonuc = re.findall("^@chr(\d+):(\d+):([FR]):-?\d+\/\d+$",
                   dosya_icerigi,
                   flags=re.IGNORECASE|re.MULTILINE)

listem = []
for chrom, pos, direction in sonuc:
    ham_pozisyon = int(pos)
    if direction == "R":
        ham_pozisyon = ham_pozisyon * -1
    listem.append((int(chrom), ham_pozisyon))

pprint.pprint(sorted(listem))