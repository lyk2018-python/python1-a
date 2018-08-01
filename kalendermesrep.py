import calendar
kalender = calendar.Calendar()
kalender.setfirstweekday(1)
print(calendar.weekday(2018,8,4))
print(list(kalender.itermonthdates(2018,8)))
print(list(kalender.iterweekdays()))