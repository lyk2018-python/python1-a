class BenimSinifim(object):
    pass

sinifim = BenimSinifim()
sinifim.masasayisi = 15
sinifim.ogrencisayisi = 30
sinifim.kalemsayisi = 90
deneme = sinifim.__dict__
deneme.update({"ogrencisayisi":99})
print(sinifim.ogrencisayisi)
print(sinifim.__dict__)