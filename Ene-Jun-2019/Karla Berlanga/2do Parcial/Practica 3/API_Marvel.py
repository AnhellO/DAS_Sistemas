from datetime import datetime
import hashlib
import requests
import json

class Character(object):

    def __init__(self, clave, name, description, url_detail, url_wiki, movie):
        self.clave = clave
        self.name = name
        self.description = description
        self.url_detail = url_detail
        self.url_wiki = url_wiki
        self.movie = movie

    def __str__(self):
        movie = ''
        if self.movie == 1:
            movie = "The Avengers"
        elif self.movie == 2:
            movie = "The Avengers: Age of Ultron"
        elif self.movie == 3:
            movie = "The Avengers: Infinity War"
        return """- Id: {}\n- Name: {}\n- Description: {}\n- URL - detail: {}\n- URL - wiki: {}\n- Movie: {}\n----------------------
        """.format(
        self.clave,
        self.name,
        self.description,
        self.url_detail,
        self.url_wiki,
        movie
        ).strip()


def makeGet(movie):
    apikey = '9d6bb1185f419ca5b8c19885b63d408e'
    apikey_private = 'd9a1863fd64ca42c043a8b714447d1821c9b127b'
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))
    cadena = str(timestamp)+apikey_private+apikey

    #Se crea el md5
    h = hashlib.md5()
    h.update(cadena.encode('utf-8'))
    md5 = h.hexdigest()

    if movie == 1:
        event = 234
    elif movie == 2:
        event = 314
    elif movie == 3:
        event = 29
    else:
        return "No coincide con la tetralogía de Avengers"

    url = 'http://gateway.marvel.com/v1/public/characters?events='+str(event)+'&limit=20&ts='+str(timestamp)+'&apikey='+apikey+'&hash='+md5
    solicitud = requests.get(url)
    if solicitud.status_code != 200:
        return "Ocurrió un error"
    else:
        characters=[]
        data = solicitud.json()
        for character in data['data']['results']:
            c = Character(character['id'],character['name'],character['description'],character['urls'][0]['url'],character['urls'][1]['url'], movie)
            characters.append(c)
        return characters


if __name__ == '__main__':
    pass
