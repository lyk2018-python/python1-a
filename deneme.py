kisiler = []


while True:
    print("Bir işlem seçiniz")
    print("1 - Yeni kişi ekle")
    print("2 - Kişiyi Düzenle")
    print("3 - Kişiyi Sil")
    print("4 - Programı durdur")

    islem = input("Lütfen Seçiminizi Yapınız :")
    if islem.isnumeric():
        islem = int(islem)


    if islem == 1:
        ad = input("Ad : ")
        soyad = input("soyad : ")
        tel = input("tel : ")
        email = input("e-posta : ")
        kisiler.append({"ad": ad,
                        "soyad": soyad,
                        "tel": tel,
                        "email": email
                        })
        input("İşleminiz gerçekleşti devam \n etmek için bir tuşa basınız")
    elif islem == 2:
        aranacak = input("Aranacak Kelimeyi Giriniz:")
        temp_kisi = None
        for kisi in kisiler:
            for value in kisi.values():
                if aranacak.strip().lower() == value.lower():
                    temp_kisi = kisi

        if temp_kisi is not None:
            kisi_index = kisiler.index(temp_kisi)

            print("Düzenlediğiniz Kişi:\n\nAdı:{ad}\nSoyad: {soyad}\n"
                  "Tel:{tel}\nE-posta: {posta}"
                  "".format(tel=temp_kisi.get("tel"),
                            ad=temp_kisi.get("ad"),
                            soyad=temp_kisi.get("soyad"),
                            posta=temp_kisi.get("email")

                            ))

            ad = input("Ad : ")
            soyad = input("soyad : ")
            tel = input("tel : ")
            email = input("e-posta : ")
            kisiler[kisi_index] = {"ad": ad,
                            "soyad": soyad,
                            "tel": tel,
                            "email": email
                            }
            input("İşleminiz gerçekleşti devam \n etmek için bir tuşa basınız")

        else:
            input("Aradığınız veriden bir eşleşme yok\n"
                  "Lütfen devam etmek için bir tuşa basın")


    elif islem == 3:
        silinecek = input("Aranacak Kelimeyi Giriniz:")
        temp_kisi = None
        for kisi in kisiler:
            for value in kisi.values():
                if aranacak.strip().lower() == value.lower():
                    temp_kisi = kisi

        if temp_kisi is not None:
            kisi_index = kisiler.index(temp_kisi)

    elif islem == 4:
        break