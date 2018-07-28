def menu():
    print("Lütfen seçiminizi yapınız")
    print("     1 - Toplama işlemi")
    print("     2 - Çıkartma işlemi")
    print("     3 - Çarpma işlemi")
    print("     4 - Bölme işlemi")
    islem = input('İşlem :')
    if islem.isnumeric():
        return int(islem)
    else:
        print("Hatalı girdi")
        return menu()


def sayigirisi():
    sayilar = []
    print("Lütfen sayı giriniz. İşeminizi tamamlamak için = tuşuna basabilirsiniz")
    while True:
        sayi = input("Girdi :")
        if sayi.isnumeric():
            sayilar.append(int(sayi))
        elif sayi.strip() == "=":
            return sayilar

while True:
    menu_secimi = menu()
    sayilar = sayigirisi()
    if menu_secimi == 1:
        print(sum(sayilar))
    elif menu_secimi == 2:
        ""



