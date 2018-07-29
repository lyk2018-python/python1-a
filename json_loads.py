import json

data = {"polisiye": ["Sherlock", "Behzat Ç."],
        "fantastik": ["Silmarillion",
                      "Cüce Derinlikleri Ejderhaları",
                      "İkizlerin Savaşı",
                      "İkizlerin Sınavı",
                      "Otostopçunun ...",
                      "Harry Potter"],
        "klasikler": ["Beyaz Zambaklar Ülkesi",
                      "Sefiller",
                      "Yeraltından Notlar"]}


try:
    with open("kitaplar.txt", "w") as dosya:
        json.dump(data, dosya)
except Exception(IOError) as hata:
    print(hata)


try:
    with open("kitaplar.txt") as dosya:
        data = json.load(dosya)
        print(data)
        print(type(data))
        print(data.values())
except Exception(IOError) as hata:
    print(hata)

# temp_liste = ["1","2","3","4","5"]

# try:
#     with open("yeni_kitaplar.txt", "w") as dosya:
#         for i in temp_liste:
#             dosya.write(i)
# except IOError as hata:
#     print(hata)

