from datetime import datetime, timedelta
import calendar

"""
Pzt Sal Çar Per Cum Cmt Pzr
1   2   3   4   5   6   7
8   9   10  11  12  13  14
15  16  17  18  19  20  21
"""
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30,31]

month = 3

inital_array = []
for day in range(0,month_days[month]):
    day_text = str(day+1)
    if len(day_text) == 1:
        day_text = "0{d}".format(d=day_text)
    day_object = datetime.strptime("2018-{month}-{day}".format(month=month,
                                                               day=day_text),
                                   "%Y-%m-%d")
    print(day_object.weekday())

print(datetime.date(datetime.now()).isocalendar())
