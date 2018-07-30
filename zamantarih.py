import datetime
import locale
import time

date = datetime.datetime
print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.today().hour)
print(date.today().minute)
print(date.today().microsecond)
print(date.utcnow())
yenitarih = date.today() + datetime.timedelta(days=7,minutes=30)
print(yenitarih.minute)
print(yenitarih.ctime())
print(yenitarih.isoformat())
print(date.fromtimestamp(time.time()))
print(yenitarih.strftime("%A %d-%m-%Y %H:%M"))
print(date.now() - yenitarih)

