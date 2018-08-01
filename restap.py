from urllib.parse import urljoin

import requests


class MyApi():
    main_url = ""
    post_lists = []
    last_start = 0
    last_end = 10

    def __init__(self, url):
        self.main_url = url

    def request_get(self, endpoint):
        yeni_url = urljoin(self.main_url, endpoint)
        return requests.get(yeni_url,headers={"APIKEY":"BLABLA"}).json()

    def next_posts(self):
        next_range = self.last_end - self.last_start
        data = self.post_lists[self.last_end:self.last_end + next_range]

        self.last_start = self.last_end
        self.last_end = self.last_end + next_range
        print("{} to {}".format(self.last_start,self.last_end))
        return data

    def posts(self, start=0, end=10, cache=False):
        self.last_end = end
        self.last_start = start
        get_request = True
        if cache:
            if len(self.post_lists) == 0:
                get_request = True
            else:
                get_request = False

        if get_request:
            self.post_lists = self.request_get("/posts")

        return self.post_lists[start:end]

    def request_post(self, endpoint, data):
        yeni_url = urljoin(self.main_url, endpoint)
        return requests.post(yeni_url, data=data).json()


api = MyApi("https://jsonplaceholder.typicode.com/")
for i in api.posts(0, 5, True):
    print(i.get('title'))

for i in api.next_posts():
    print(i.get('title'))


for i in api.next_posts():
    print(i.get('title'))
