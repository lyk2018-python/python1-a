import string

# harfler = "abcdefghijklmnoprstuvywxz"
harfler = string.ascii_lowercase

cevrim = {i: harfler.index(i) for i in harfler}

isimler = ["mehmet", "deryak", "betul", "iskender", "can"]

print(sorted(isimler, key=lambda x:cevrim.get(x[-1])))
