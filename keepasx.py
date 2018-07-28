import string as sg
import random


class Keepasx():
    def __init__(self):
        """init"""
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
    def list(self):
        """
        parolalarımızı listeleyecek
        """
    def search(self):
        """
        vericeğimiz parametreye göre parolalar arasında arama yapacak
        """
    def save(self):
        """
        dosyaya kayit yapacak
        """
    def generate_pass(self,length):
        string_data =sg.printable
        return ''.join([string_data[random.randint(0,len(string_data)-1)] for i in range(0,length)])

kep = Keepasx()
print(kep.generate_pass(10))