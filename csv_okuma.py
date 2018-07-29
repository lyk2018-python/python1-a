import csv

sayilar = []
with open("test.csv") as dosya:
    rows = csv.reader(dosya,delimiter=";",quotechar='"')
    for row in list(rows)[1:]:
        if row[3].isnumeric():
            sayi = int(row[3])
            sayilar.append(sayi)
    print("max",max(sayilar))
    print("min",min(sayilar))


