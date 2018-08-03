import json
import requests
import logging
FORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
logging.basicConfig(filename="hata2.log",format=FORMAT,level=logging.DEBUG)
class Movie():
    title = None
    id = None

    def __init__(self, title, id):
        logging.info('Movie Sınıfı {title}, {id} parametreleri ile Oluşturuldu'.format(title=title,id=id))

        self.session = requests.session()
        self.title = title
        self.id = id

    def get_info(self):
        logging.info('{title}, {id} infosu istendi'.format(title=self.title, id=self.id))

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
        logging.info('Parser Sınıfı Oluşturuldu')

    def search(self, keyword):
        logging.info('{key} sözcüğü ile arama yapıldı'.format(key=keyword))

        data = self.session.get(
            'https://v2.sg.media-imdb.com/suggests/{aramailk}/{arama}.json'.format(
                aramailk=keyword[0],
                arama=keyword))
        content = data.content.decode("utf-8")

        suggests_json = content.split('imdb${sup}('.format(sup=keyword))[1][:-1]
        suggests = json.loads(suggests_json)
        logging.info('Data başarılı bir şekilde çekildi')

        for suggest in suggests.get('d'):
            self.search_results.append(Movie(**{
                "title": suggest.get('l'),
                "id": suggest.get('id')
            }))
        logging.info('Kendimi return ettim')

        return self

    def get_results(self):
        logging.info('Result istendi')

        return self.search_results


parse = Parser()
for movie in parse.search("supernat").get_results():
    print(movie, movie.get_info())

try:
    d = 0/0
except ZeroDivisionError as e:
    logging.exception("Sıfıra bölünme",exc_info=e)