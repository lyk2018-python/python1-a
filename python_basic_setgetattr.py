
class Deneme():
    islem = None
    veri1 = None
    veri2 = None
    def __getattr__(self, item):
        print(item,"Çekildi")
    def __setattr__(self, veritutucu, veri):
        print(veritutucu,"veritutucusuna",veri,"değeri atandı")

    def hesapla(self):
        self.islem = "Toplama"
        self.veri1 = 10
        self.veri2 = 20
        print(self.boy)
    def data(self):
        print(self.__dict__)

dene = Deneme()
dene.boy = 1.76
boyu = dene.boy
dene.hesapla()
print(dene.__dict__)
print(dene.data())
