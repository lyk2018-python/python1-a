from pprint import pprint


class Oyuncu(object):
    gucu = None
    vurus_carpanimiz = None
    oyuncu_ismi = ""

    def __init__(self,ismi="İsimsiz", gc=10, vc=1.3):
        self.gucu = gc
        self.oyuncu_ismi = ismi
        self.vurus_carpanimiz = vc
        print('Ben Çalıştım')

    def set_vurus_carpani(self, carpan):
        self.vurus_carpanimiz = carpan

    def set_gucu(self, guc):
        self.gucu = guc

    def get_vurus_gucu(self):
        return self.get_gucu() * self.vurus_carpanimiz

    def get_gucu(self):
        return self.gucu

    def __str__(self):
        return "Oyuncu {}".format(self.oyuncu_ismi)


class Mario(Oyuncu):
    def mario_musun(self):
        return True


class Luigi(Oyuncu):
    def mario_musun(self):
        return False

    def get_vurus_gucu(self):
        return self.gucu * 100

    @staticmethod
    def hiz_hesapla(ivme_katsayisi, max_hiz):
        print(ivme_katsayisi, max_hiz)

    def hiz(self):
        Luigi.hiz_hesapla(99, 666)

class PayerTwo(Oyuncu):
    def __init__(self):
        Oyuncu.__init__(self)


class PlayerOne(Oyuncu):
    ac_dc = None
    def __init__(self,ismi="İsixxxmsiz", gc=10, vc=1.3, acdc=1000):
        super().__init__(gc=10,ismi=ismi)
        self.ac_dc = acdc


    def hiz(self, a, b):
        Luigi.hiz_hesapla(a, b)


print(__name__)
if __name__ == '__main__':

    # mario = Mario(gc=1,vc=2,ismi="Mehmet")
    # print(mario.mario_musun())

    player_one = PlayerOne()
    player_two = PayerTwo()
    print(player_two)
    print(player_one)


    # luigi = Luigi()
    # print(luigi.mario_musun())


    # print("Mario :",mario.get_vurus_gucu())
    # # print("Luigi :",luigi.get_vurus_gucu())
    # Luigi.hiz_hesapla(15, 20)
    # player_one.hiz(7, 8)
