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


mario = Oyuncu(gc=1,vc=2,ismi="Mehmet")
maryonun_ismi_ne = "Mario esittir {}".format(mario)
print(maryonun_ismi_ne)
luigi = Oyuncu()


print("Mario :",mario.get_vurus_gucu())
print("Luigi :",luigi.get_vurus_gucu())
