import string as sg
import random


class Keepasx():
    file_name = None
    mypasslist = []

    def __init__(self, file_name):
        self.file_name = file_name

    def register_new_pass(self):
        """
        Kullanıcıdan kullanıcı adı , açıklama ve parola ister
        eğer parola boş ise kendisi random bir parola oluşturur
        oluşturulacak parola uzunluğunu da kullanıcıdan isteyeceğiz
        """

    def edit(self):
        """
         verilen index'te olan veriyi değiştirir
        """

    def load(self):
        """
        verdiğimiz dosya isminine bakarak okuma yapacak
        """
        with open(self.file_name) as file:
            file_data = file.read().strip().split("\n")
            for veriler in file_data:
                veri_yigini = veriler.split("@ayrac@")
                self.mypasslist.append(
                    {"username": veri_yigini[0],
                     "password": veri_yigini[1],
                     "description": veri_yigini[2]})

    def list(self):
        """
        parolalarımızı listeleyecek

        """
        for passlist in self.mypasslist:
            print(list(passlist.values()))

    def search(self,keyw):
        """
        vericeğimiz parametreye göre parolalar arasında arama yapacak
        """
        for passlist in self.mypasslist:
            if keyw in list(passlist.values()):
                print(list(passlist.values()))

    def save(self):
        """
        dosyaya kayit yapacak
        """
        data = ""
        for i in self.mypasslist:
            data += "{username}@ayrac@{passw}@ayrac@{desc}\n".format(username=i.get('username'),passw=i.get('password'),desc=i.get('description'))
        with open(self.file_name,"w") as file:
            file.write(data)

    def generate_pass(self, length):
        string_data = sg.printable
        return ''.join([string_data[random.randint(0, len(string_data) - 1)] for i in range(0, length)])


kep = Keepasx()
print(kep.generate_pass(10))
