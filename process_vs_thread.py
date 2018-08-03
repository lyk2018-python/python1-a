
import requests
import time
from multiprocessing.pool import ThreadPool

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}


def download_site(page):
    response = requests.get("https://eksisozluk.com/python--109286?p={}".format(page), headers=user_agent)
    return response.text

thread_havuzu = ThreadPool(69)
data = []
baslangic = time.time()
data = thread_havuzu.map(download_site, range(1, 70))
bitis = time.time()
print(bitis-baslangic)