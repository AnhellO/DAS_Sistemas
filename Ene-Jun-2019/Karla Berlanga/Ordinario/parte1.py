from abc import ABC, abstractmethod
import requests
import json

#Se crean objetos que representen Animes, Mangas y Personajes
class Anime():
    def __init__(self, id, title, rank, url, image_url, type, episodes, start_date, end_date, members, score):
        self.id = id
        self.title = title
        self.rank = rank
        self.url = url
        self.image_url = image_url
        self.type = type
        self.episodes = episodes
        self.start_date = start_date
        self.end_date = end_date
        self.members = members
        self.score = score

    def __str__(self):
        return """- Id: {}\n- Title: {}\n- Rank: {}\n- URL - detail: {}\n- URL - Image: {}\n- Type: {}\n- Episodes: {}\n- Start Date: {}\n- End Date: {}\n- Members: {}\n- Score: {}\n----------------------
        """.format(
        self.id,
        self.title,
        self.rank,
        self.url,
        self.image_url,
        self.type,
        self.episodes,
        self.start_date,
        self.end_date,
        self.members,
        self.score
        ).strip()

class Manga():
    def __init__(self, id, title, rank, url, image_url, type, volumes, start_date, end_date, members, score):
        self.id = id
        self.title = title
        self.rank = rank
        self.url = url
        self.image_url = image_url
        self.type = type
        self.volumes = volumes
        self.start_date = start_date
        self.end_date = end_date
        self.members = members
        self.score = score

    def __str__(self):
        return """- Id: {}\n- Title: {}\n- Rank: {}\n- URL - detail: {}\n- URL - Image: {}\n- Type: {}\n- Volumes: {}\n- Start Date: {}\n- End Date: {}\n- Members: {}\n- Score: {}\n----------------------
        """.format(
        self.id,
        self.title,
        self.rank,
        self.url,
        self.image_url,
        self.type,
        self.volumes,
        self.start_date,
        self.end_date,
        self.members,
        self.score
        ).strip()

class Character():
    def __init__(self, id, title, name_kanji, rank, url, image_url):
        self.id = id
        self.title = title
        self.name_kanji = name_kanji
        self.rank = rank
        self.url = url
        self.image_url = image_url


    def __str__(self):
        return """- Id: {}\n- Title: {}\n- Name Kanji: {}\n- Rank: {}\n- URL - detail: {}\n- URL - Image: {}\n----------------------
        """.format(
        self.id,
        self.title,
        self.name_kanji,
        self.rank,
        self.url,
        self.image_url
        ).strip()

#Interfaz de la conexión a la API
class APIConnection():
    @abstractmethod
    def makeGet(self):
        pass

"""Aplicando los conocimientos de patrones de diseño, se aplica el metodo de Factory"""

class getAnimes(APIConnection):

    def __init__(self):
        self.url = 'https://api.jikan.moe/v3/top/anime/1'

    def makeGet(self):
        solicitud = requests.get(self.url)
        if solicitud.status_code != 200:
            return "Ocurrió un error"
        else:
            elements = []
            data = solicitud.json()
            for element in data['top']:
                obj = Anime(element['mal_id'],element['title'], element['rank'], element['url'],
                element['image_url'], element['type'], element['episodes'], element['start_date'],
                element['end_date'], element['members'], element['score'])
                elements.append(obj)
        return elements

class getMangas(APIConnection):

    def __init__(self):
        self.url = 'https://api.jikan.moe/v3/top/manga/1'

    def makeGet(self):
        solicitud = requests.get(self.url)
        if solicitud.status_code != 200:
            return "Ocurrió un error"
        else:
            elements = []
            data = solicitud.json()
            for element in data['top']:
                obj = Manga(element['mal_id'],element['title'], element['rank'], element['url'],
                element['image_url'], element['type'], element['volumes'], element['start_date'],
                element['end_date'], element['members'], element['score'])
                elements.append(obj)
        return elements

class getCharacters(APIConnection):

    def __init__(self):
        self.url = 'https://api.jikan.moe/v3/top/characters/1'

    def makeGet(self):
        solicitud = requests.get(self.url)
        if solicitud.status_code != 200:
            return "Ocurrió un error"
        else:
            elements = []
            data = solicitud.json()
            for element in data['top']:
                obj = Character(element['mal_id'],element['title'],element['name_kanji'],
                element['rank'], element['url'],element['image_url'])
                elements.append(obj)
        return elements


class APIFactory():

    @staticmethod
    def apiType(tipo):
        types = {
        'anime': getAnimes,
        'manga': getMangas,
        'characters': getCharacters
        }
        return types[tipo.lower()]()


def main():
    animes = APIFactory.apiType('anime')
    mangas = APIFactory.apiType('manga')
    characters = APIFactory.apiType('characters')

    print("****************Animes********************")
    print(*animes.makeGet(), sep='\n')
    print("****************Mangas********************")
    print(*mangas.makeGet(), sep='\n')
    print("****************Characters********************")
    print(*characters.makeGet(), sep='\n')



if __name__ == '__main__':
    main()
