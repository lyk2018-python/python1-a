class DataModel():
    veriler = {"ihsan": "erdem", "betul": "tezel", "derya": "karaarslan"}

    def veriyi_modifiyeet(self, veri):
        if type(veri) == str:
            return veri.upper()
        else:
            return veri

    def __setattr__(self, key, value):
        yeni_value = self.veriyi_modifiyeet(value)
        self.veriler.update({key:yeni_value})
        #return object.__setattr__(self, key, yeni_value)

    def __getattr__(self, item):
        print(item)
        if item != "veriler":
            if self.veriler.get(item) is not None:
                return  self.veriler.get(item)

        return object.__getattribute__(self, item)


class DataTable(DataModel):
    pass


data = DataTable()
data.mustafa = "deneme"
print(data.veriler)
print(data.ihsan)
