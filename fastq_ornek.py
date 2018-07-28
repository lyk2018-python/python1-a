"""
1 - Class oluştur dosyayı parametre olarak ver
2 - Class a bir fonksiyon oluştur onda da bir parametre olsun ve verdiğimiz parametre
ile dosyamız içerisindeki okuma bloklarında arama yapsın
3 - 2. bir fonksiyonumuz olsun bulunan okuma sayısını versin
4 - 3. bir fonksiyonumuz olsun bulunan satırları versin

"""


# class ParseFASTQ():
#     file_data = []
#     filtered_data = []
#     filter_keyword = None
#     def __init__(self, file_name):
#
#         with open(file_name) as file_data:
#             self.file_data = file_data.read().split("+\n")
#
#     def filter(self, data):
#         if data.find(self.filter_keyword) > -1:
#             return True
#         else:
#             return False
#
#     def find(self, keyword):
#         self.filter_keyword = keyword
#         self.filtered_data = list(filter(self.filter, self.file_data))
#
#     def count(self):
#         return len(self.filtered_data)
#
#     def result(self):
#         return self.filtered_data
#
# parsed_file = ParseFASTQ("Brca1Reads_7.2.fastq")
# parsed_file.find("GGG")
# print(parsed_file.count())
#
# def filtrele(data):
#     if data.find("#") > -1:
#         return True
#     return False
#
#
# with open("Brca1Reads_7.2.fastq") as file:
#     data = file.read().split("+\n")
#     hepsi = list(filter(filtrele, data))
#     for i in hepsi:
#         print(i)


# def fonk(param1, param2):
#     return param1 + param2
#
#
# print(fonk(2, 4))

# fonk = lambda param1, param2 : param1 + param2
#
# print(fonk(2,4))














