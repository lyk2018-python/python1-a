try:
    deneme = 0/0
except:
    pass

try:
    dememe = 0/0
except Exception as e:
    print(e)

try:
    deneme = 0/0
except ZeroDivisionError as e:
    print(e)

try:
    deneme = "" + 0
except ZeroDivisionError as e:
    print(e)