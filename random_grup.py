import curses
import os
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
           "Ertan"]


for z in range(0,4):
    grup = []

    print("GRUP",z,"#"*100)
    for i in range(0,6):
        cikan = kisiler[randint(0,len(kisiler)-1)]
        grup.append(cikan)
        kisiler.remove(cikan)

        if i < 9:
            time.sleep(0.2)
        else:
            time.sleep(0.1)
    print(grup)
