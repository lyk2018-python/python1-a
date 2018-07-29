
try:
    with open("deneme.xtxr") as file:
        data = file.read()
    deneme = 0/0
except FileNotFoundError:
    with open('deneme.xtxr',"w") as file:
        print("Dosya oluşturuldu")
        file.write("x")
except ZeroDivisionError:
    deneme = 0




class BenimExce(Exception):
    pass



deneme = "ismail"

if deneme != "mustafa":
    raise BenimExce("Dememe mustafa olmalı")