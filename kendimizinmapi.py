from functools import reduce

eski_filter = filter
eski_map = map


def filter(func, liste):
    sonuc = []
    for i in liste:
        if func(i):
            sonuc.append(i)
    return sonuc


def map(func, liste):
    sonuc = []
    for i in liste:
        sonuc.append(func(i))
    return sonuc


def abudikgubidikfonksiyon(gubidik):
    return gubidik * 1200


def hello(name):
    return "Hello {}".format(name)


def twist(dansci):
    if dansci == "Deryak":
        return True
    else:
        return False


def birlestir(birinci, ikinci):
    return birinci + " " + ikinci


def ucuc(rakam1, rakam2):
    return rakam1 * rakam2


rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(reduce(ucuc, rakamlar))

kisiler = ["Mustafa", "Ahmed", "İhsan", "Tolga", "Deryak"]

print(reduce(birlestir, kisiler))

print(list(filter(twist, kisiler)))
# print(list(map(hello,kisiler)))
# print(list(eski_map(hello,kisiler)))
#
# sayilar = [1,2,3,4]
#
# print(list(map(abudikgubidikfonksiyon,sayilar)))
