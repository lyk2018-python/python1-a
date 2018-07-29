import json

data = {"polisiye": ["Sherlock", "Behzat Ç."], "fantastik": ["Silmarillion",
                                                             "Cüce Derinlikleri Ejderhaları",
                                                             "İkizlerin Savaşı",
                                                             "İkizlerin Sınavı",
                                                             "Otostopçunun ..."]}



with open("kitaplar.txt","w") as dosya:
    json.dump(data,dosya)

with open("kitaplar.txt") as dosya:
    data = json.load(dosya)
    print(data)
