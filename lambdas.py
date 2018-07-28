import string

# harfler = "abcdefghijklmnoprstuvywxz"
harfler = string.ascii_lowercase

# data = {}
# for i in harfler:
#     data.update({i:harfler.index(i)})

cevrim = {i: harfler.index(i) for i in harfler}
print(cevrim)

isimler = ["mehmet", "deryak", "betul", "iskender", "can"]

print(sorted(isimler, key=lambda x:cevrim.get(x[-1])))
