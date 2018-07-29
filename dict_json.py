import json

bir_sozluk = {"meyvalar":{"yazmeyveleri":["karpuz","kavun","şeftali"],
                          "kismeyveleri":["portakal","mandalina","greyfurt"]}}

print(type(bir_sozluk),bir_sozluk)
str_sozluk = json.dumps(bir_sozluk)
print(type(str_sozluk),str_sozluk)
str_2 = '[{"meyvalar": {"kismeyveleri": ["portakal", "mandalina", "greyfurt"], "yazmeyveleri": ["karpuz", "kavun", "\u015feftali"]}}]'
iki_sozluk = json.loads(str_2)
print(type(iki_sozluk),iki_sozluk)
dede_list = '[1,2,3,4,5,6]'
rere = json.loads(dede_list)
print(type(rere))
