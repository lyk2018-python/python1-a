import siniflar2
from kisayollar import kisayol1, kisayol2
from random import randint


class Canli():
    dogumu = ""
    kilosu = 0
    tokluk = 0
    susuzluk = 0
    enerji = 100
    yasiyormu = True

    def __init__(self, dogumu, kilosu, tokluk, susuzluk):
        self.dogumu = dogumu
        self.kilosu = kilosu
        self.tokluk = tokluk
        self.susuzluk = susuzluk

    def enerji_hesapla(self):
        kalan_tokluk = 100 - self.tokluk
        enerji_carpani = kalan_tokluk * 0.1
        return enerji_carpani

    def haraket(self, mesafe):

        self.tokluk -= mesafe
        self.enerji -= mesafe * self.enerji_hesapla()
        if self.enerji <= 0:
            self.kilosu -= 1
            if self.kilosu <= 0:
                self.yasiyormu = False

    def beslenir(self, nekadar):
        if self.tokluk < 100:
            self.tokluk += nekadar
        else:
            self.enerji += nekadar


class Kedigiller(Canli):

    def kuyruk(self):
        print("Kuyruk Haraket Etti")

    def biyik(self):
        print("Bıyıklarını oynattı")


class Kediler(Kedigiller):
    cinsi = "Tekir"
    rengi = ""

    def __str__(self):
        return "Miyawwww"


class Cezve(Kediler):
    def __init__(self):
        Kediler.__init__(self, "20 Ocak 2015", 3, 100, 100)
        self.rengi = "Siyah"
        self.cinsi = "Bombay"

    def oyna(self):
        oyunlar = ["Kendi Kuyruğumu Kovalarım",
                   "Sigara paketini at getir oynarım"]
        return oyunlar[randint(0, len(oyunlar))]


if __name__ == '__main__':
    kedim = Cezve()
    print("cinsi", kedim.cinsi)
    print("rengi", kedim.rengi)
    print("enerji", kedim.enerji)
    kedim.haraket(10)
    print("enerji", kedim.enerji)
    print("tokluk", kedim.tokluk)
