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
stdscr = curses.initscr()


for i in range(0,10):
    cikan = kisiler[randint(0,len(kisiler)-1)]
    stdscr.clear()
    stdscr.addstr(0,0,cikan)
    stdscr.refresh()
    curses.beep()

    if i < 9:
        time.sleep(0.2)
    else:
        time.sleep(2)

stdscr.refresh()
stdscr.addstr(0,0,"Talihlimiz : {}".format(cikan))
stdscr.refresh()
time.sleep(4)
curses.endwin()