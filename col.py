from collections import Counter

data = ["ahmet","mehmet","ahmet","cihan","ihsan","ziya","ziya","ziya"]
data2 = ["ahmet","mehmet","ahmet","cihan","ihsan","ziya","ziya","ziya","derya"]

data = Counter(data)
data2 = Counter(data2)
data.subtract(data2)
print(dict(data))

print(list(data))
print(data.most_common(2))
z = Counter(a=1,b=2,ihsan=9)
print(list(z.elements()))
data3 = Counter("mustafa")
print(data3.most_common(2))
print(list(z))
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(dict(c))