
def hepsinikucult(kelime):
    return kelime.lower()


kelimeler = ["Ahmet","dErYaK","tOLGA"]

kucukkelimer = list(map(hepsinikucult,kelimeler))
print(kucukkelimer)

def dovikuru(para,hangisi):

    if hangisi == 1:

        return para*4.85
    else:
        return para*5.65


paralarim = [54,67,12]
hangisi_euro = [1,0,1]

print(list(map(dovikuru,paralarim,hangisi_euro)))

#################################
######### FILTER ###############

sayilar = [1,2,3,4,5,6,7,8,9,0]
temp = []

for i in sayilar:
    if i%2==1:
        temp.append(i)
print(temp)

def teksayimi(sayi):
    return sayi%2==1
print(sayilar)
print(list(filter(teksayimi,sayilar)))