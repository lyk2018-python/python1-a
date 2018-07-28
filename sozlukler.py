"""
veri yerine herşey gelebilir örneğin:
string
integer
dict
list
float
tuple
class
function
"""

sozluk = {"anahtar": "veri"}

print(sozluk)

sozluk = {1:2,
          "anahtar": "veri",
          "anahtar1":1,
          "anahtar2": {"icanahtar":"icveri"},
          "anahtar3":[1,"asd","444"]}

print(sozluk)
for eleman in sozluk.items():
    print(eleman[0],eleman[1])

for anahtar in sozluk.keys():
    print(anahtar)


print("Values'ı ekrana basıyoruz")
print(sozluk.values())
print("Ekrana basma bitti")

for veri in sozluk.values():
    if type(veri) == dict:
        for icveri in veri.values():
            print("{} bu ic veri".format(icveri))
    elif type(veri) == list:
        for iclist in veri:
            print("{} bu da içteki list".format(iclist))


sozluk_updates = {"adilcan":1}
sozluk.update(sozluk_updates)
print(sozluk)
sozluk_updates = {"adilcan":11}
sozluk.update(sozluk_updates)
print(sozluk)
print(sozluk.get("adilcan","yok"))
print(sozluk.get("orcun","yok"))
print(sozluk.get("orcun"))

keyne = None
verine = 11
for i in sozluk.items():
    if i[1] == verine:
        keyne = i[0]

print(keyne)
print(dict.fromkeys({"deneme":1}))

print(sozluk.pop("adilcan"))
print(sozluk.get("anahtar2").pop('icanahtar'))
print(sozluk)
print(sozluk.clear())
print(sozluk)
