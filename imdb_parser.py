import json
import requests
kullanici_girdisi = input("Aramak istediginizi giriniz :")
data = requests.get('https://v2.sg.media-imdb.com/suggests/{aramailk}/{arama}.json'.format(aramailk=kullanici_girdisi[0],arama=kullanici_girdisi))
content = data.content.decode("utf-8")
suggests_json = content.split('imdb${sup}('.format(sup=kullanici_girdisi))[1][:-1]
suggests = json.loads(suggests_json)
number = 0
for i in suggests.get("d"):
    number +=1
    print(number,i.get('l'))
secim = input("Lütfen Seçim Yapım :")
if secim.isnumeric():
    secim = int(secim)
    sectigin_element = suggests.get("d")[secim]
    sectigim_sayfa = requests.get('https://www.imdb.com/title/{id}/?ref_=nv_sr_1'.format(id=sectigin_element.get('id')))
    
#
# for i in suggests:
#     print(i)