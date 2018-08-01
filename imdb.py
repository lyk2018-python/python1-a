import json

import requests


class Movie():
    title = None
    id = None

    def __init__(self, title, id):
        self.session = requests.session()
        self.title = title
        self.id = id

    def get_info(self):
        try:
            data = self.session.get('https://www.imdb.com/title/{id}/?ref_=nv_sr_1'.format(id=self.id)).content.decode(
                'utf-8')
            return data.split('<span itemprop="ratingValue">')[1].split('<')[0]
        except:
            return "N/A"

    def __str__(self):
        return "{} ({})".format(self.title, self.id)

    def __unicode__(self):
        return "{} ({})".format(self.title, self.id)


class Parser():
    session = None
    search_results = []

    def __init__(self):
        self.session = requests.session()

    def search(self, keyword):
        data = self.session.get(
            'https://v2.sg.media-imdb.com/suggests/{aramailk}/{arama}.json'.format(
                aramailk=keyword[0],
                arama=keyword))
        content = data.content.decode("utf-8")
        suggests_json = content.split('imdb${sup}('.format(sup=keyword))[1][:-1]
        suggests = json.loads(suggests_json)

        for suggest in suggests.get('d'):
            self.search_results.append(Movie(**{
                "title": suggest.get('l'),
                "id": suggest.get('id')
            }))
        return self

    def get_results(self):
        return self.search_results


parse = Parser()
for movie in parse.search("supernat").get_results():
    print(movie, movie.get_info())
