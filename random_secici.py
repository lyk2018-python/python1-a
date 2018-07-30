import time
from random import randint

kisiler = ["Betül Tezel",
           "Orçun",
           "Deryak",
           "Elis",
           "Semiha",
           "Muzaffer",
           "Tolga",
           "Adil",
           "Erkan",
           "İlter",
           "İlter",
           "İlter",
           "Vahit",
           "Furkan",
           "Kadir",
           "Betül",
           "Elif",
           "Mehmet",
           "Seda",
           "Eda",
           "Defne",
           "Esra",
           "Osman",
           "Hayri",
           "Burak",
           "Ertan",
           "İlteriş"
           ]
for i in range(0,10):
    cikan = kisiler[randint(0,len(kisiler)-1)]
    print(cikan)
    time.sleep(1)