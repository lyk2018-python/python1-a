import os
from pathlib import Path



dosya = Path(".")
sedanin_klasoru = dosya / "seda"
sedanin_klasoru_2 = dosya / "seda" / "eda"
edanin_dosyasi = dosya / "seda" / "eda" / "deneme.txt"

if sedanin_klasoru_2.exists() is False:
    sedanin_klasoru_2.mkdir()
sedanin_dosyasi = dosya / "seda" / "seda_2"

with sedanin_dosyasi.open("w") as file:
    file.write("Burda Text Var")

if edanin_dosyasi.exists() is False:
    with edanin_dosyasi.open("w") as file:
        file.write("Merhaba Dünya!")

deneme_path = os.path.join(os.path.abspath("./"),"seda")
for i in os.listdir(deneme_path):
    if len( i.split(".")) > 1:
        if i.split(".")[1] == "py":
            file_name = os.path.join(deneme_path,i)
            with open(file_name) as file:
                print(file.read())

for i in sedanin_klasoru.glob("*.py"):
    with i.open() as file:
        print(file.read())

for i in range(10):
    yeni_klasor = sedanin_klasoru / "ihsanin_klasoru_{}".format(i)
    if yeni_klasor.exists() is False:
        yeni_klasor.mkdir()

for i in sedanin_klasoru.glob("*.py"):
    i.replace(sedanin_klasoru / "deneme2.py")

    if i.is_file():
        print("Bu bir dosyadır")