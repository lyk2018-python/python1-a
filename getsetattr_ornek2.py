class Insan():
    ozellikler = {"gozu": "Gri"}

    def __setattr__(self, key, value):
        self.ozellikler.update({key: value})

    def __getattr__(self, item):
        if item != "ozellikler":
            if item.endswith("_feet"):
                return self.ozellikler.get(item[:-5]) / 0.3048
            else:
                return self.ozellikler.get(item)

    def save(self):
        print(self.ozellikler)


ihsan = Insan()
ihsan.gozu = "Yeşil"
ihsan.boyu = 1.85
print(ihsan.boyu_feet)
feet = ihsan.boyu_feet
print(feet)
print(ihsan.boyu)
ihsan.ogrenci = True
ihsan.save()