import requests
import json
import sqlite3

class jikan_sqlite():
    @staticmethod
    def get_anime():
        anime_recommendations = [1535, 1575, 14719, 30276, 31964, 1, 2001, 10087, 5114, 5081, 23273, 17265, 31478, 33352, 33255]
        connection = sqlite3.connect('AniManga.db')
        cursor = connection.cursor()
        for id in anime_recommendations:
            response = requests.get('https://api.jikan.moe/v3/anime/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cursor.execute("insert into Anime values ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id, response_json['title'], response_json['episodes'], response_json['duration'], response_json['rating'], response_json['url'], response_json['image_url'], response_json['trailer_url']))
                connection.commit()
        connection.close()

    @staticmethod
    def get_manga():
        manga_recommendations = [86337, 48399, 81669, 31499, 2, 642, 14790, 44, 98720, 12994, 90125, 67617, 45757, 88930, 60553]
        connection = sqlite3.connect('AniManga.db')
        cursor = connection.cursor()
        for id in manga_recommendations:
            response = requests.get('https://api.jikan.moe/v3/manga/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cursor.execute("insert into Manga values ({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(id, response_json['title'], response_json['type'], response_json['volumes'], response_json['chapters'], response_json['url'], response_json['image_url']))
                connection.commit()
        connection.close()

    @staticmethod
    def get_chara():
        featured_characters = [125056, 90291, 417, 71, 22037, 2075, 24596, 41402, 4004, 85, 77605, 118739, 148622, 81367, 138441]
        connection = sqlite3.connect('AniManga.db')
        cursor = connection.cursor()
        for id in featured_characters:
            response = requests.get('https://api.jikan.moe/v3/character/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cursor.execute("insert into Characters values ({}, '{}', '{}')".format(id, response_json['name'], response_json['image_url']))
                connection.commit()
        connection.close()

def main():
    jikan_sqlite.get_anime()
    jikan_sqlite.get_manga()
    jikan_sqlite.get_chara()

if __name__ == '__main__':
    main()
    # response = requests.get('https://api.jikan.moe/v3/anime/1535')
    # print(response.status_code)
    # episodes = duration = rating = synopsis = '0'
    # if response.status_code == 200:
    #     response_json = json.loads(response.text)
    #     title = response_json['title']
    #     episodes = response_json['episodes']
    #     duration = response_json['duration']
    #     rating = response_json['rating']
    #     synopsis = response_json['synopsis']
    #     print('1\n{}\n{}\n{}\n{}\n{}'.format(title, episodes, duration, rating, synopsis))
