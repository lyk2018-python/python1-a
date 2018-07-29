import string as sg
import random
import json


class Keepasx():
    file_name = None
    mypasslist = []

    def __init__(self, file_name):
        self.file_name = file_name
        while True:
            menu = self.input_control_error("""
            Lütfen İşlem seçiniz:
            1 - Yeni parola oluştur
            2 - Parolaları listele
            3 - Parola ara
            """, is_numeric=True)
            if menu == 1:
                self.register_new_pass()
            elif menu == 2:
                self.list()
            elif menu == 3:
                key = self.input_control_error("Arama Kriteri :")
                self.search(key)
            else:
                print('Hatalı Girdi')

    def input_control_error(self, text, is_numeric=False):
        while True:
            input_data = input(text)
            if input_data.strip() != "":
                if is_numeric:
                    if input_data.isnumeric():
                        return int(input_data)
                    else:
                        print('Geçersiz girdi')
                else:
                    return input_data
            else:
                print('Geçersiz girdi')

    def register_new_pass(self):
        """
        Kullanıcıdan kullanıcı adı , açıklama ve parola ister
        eğer parola boş ise kendisi random bir parola oluşturur
        oluşturulacak parola uzunluğunu da kullanıcıdan isteyeceğiz
        """
        username = self.input_control_error("Lütfen Kullanıcı adı giriniz :")
        password = input("Lütfen parolanızı giriniz:")
        if password.strip() == "":
            password_length = self.input_control_error('Lütfen parola uzunluğu giriniz', is_numeric=True)
            password = self.generate_pass(password_length)
        aciklama = self.input_control_error("Lütfen açıklama giriniz :")

        self.mypasslist.append({"username": username, "password": password, "description": aciklama})
        self.save()

    def edit(self,text,is_numeric=False):
        """
         verilen index'te olan veriyi değiştirir
        """
        print('Edit çağrıldı')



    def load(self):
        """
        verdiğimiz dosya isminine bakarak okuma yapacak
        """
        with open(self.file_name) as file:
            print(file.read())
            file_data = file.read().strip().split("\n")
            for veriler in file_data:
                veri_yigini = veriler.split("@ayrac@")
                self.mypasslist.append(
                    {"username": veri_yigini[0],
                     "password": veri_yigini[1],
                     "description": veri_yigini[2]})
        # with open(self.file_name) as file:
        #     file_data = json.load(file)
        #     print(file_data)
    def list(self):
        """
        parolalarımızı listeleyecek

        """
        for passlist in self.mypasslist:
            print(list(passlist.values()))

    def search(self, keyw):
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
        # data = ""
        # for i in self.mypasslist:
        #     data += "{username}@ayrac@{passw}@ayrac@{desc}\n".format(username=i.get('username'),
        #                                                              passw=i.get('password'), desc=i.get('description'))
        # with open(self.file_name, "w") as file:
        #     file.write(data)


        with open(self.file_name, "w") as file:
            json.dump(self.mypasslist, file)

    def generate_pass(self, length):
        string_data = sg.printable
        return ''.join([string_data[random.randint(0, len(string_data) - 1)] for i in range(0, length)])


kep = Keepasx("passfile.txt")
print(kep.generate_pass(10))
print(kep.load())