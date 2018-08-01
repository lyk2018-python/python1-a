import time
import requests


def login_miyiz():
    xdata = session_request.get("http://192.168.1.108:5000/").content.decode("utf-8")
    return xdata


session_request = requests.session()
session_request.headers = {"User-Agent": "Mozilla 5.0", "Naper": "Seda", "Seda": "Zeda"}

while True:
    if login_miyiz().find("İYİ Kİ DOĞDUN SEMİHA") > -1:
        print('loginiz')
        time.sleep(5)
    else:
        kullanici_adi = input('Kullanıcı Adı Giriniz : ')
        parola = input('Parola Giriniz : ')
        data = session_request.post("http://192.168.1.108:5000/", data={"email": kullanici_adi,
                                                                        "password": parola}).content.decode("utf-8")
        print(data)
