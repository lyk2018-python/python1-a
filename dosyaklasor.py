import os

satir = os.path.abspath("../hebebebebbebse")
print(satir)

if os.path.exists(satir) is False:


    os.mkdir(satir)

print(os.path.exists(satir))
satir2 = os.path.abspath("./seda")
satir3 = os.path.abspath(".")
print(satir2)
print(satir3)

dosya = os.path.join(satir2,"sedan")
print(os.path.dirname(dosya))
print(dosya)
if os.path.exists(dosya):
     os.remove(dosya)
for i in os.listdir(satir3):
    print(i)


for i in os.listdir(satir):
    yeni_path = os.path.join(satir,i)
    print(os.path.isdir(yeni_path))
    print(os.path.isfile(yeni_path))
    print(i)