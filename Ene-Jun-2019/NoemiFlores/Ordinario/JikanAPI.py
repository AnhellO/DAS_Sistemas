import requests
import json
import sqlite3

class JikanAPI():
    @staticmethod
    def Anime():
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in range(10):
            response = requests.get('https://api.jikan.moe/v3/anime/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Anime VALUES ({}, '{}', '{}', '{}')".format(id, response_json['title'], response_json['title_japanese'], response_json['video_url']))
                conn.commit()
        conn.close()

    @staticmethod
    def Manga():
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in range(10):
            response = requests.get('https://api.jikan.moe/v3/manga/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Manga VALUES ({}, '{}', '{}', '{}')".format(id, response_json['url'], response_json['image_url'], response_json['name']))
                conn.commit()
        conn.close()

    @staticmethod
    def Characters():
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in range(10):
            response = requests.get('https://api.jikan.moe/v3/character/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Character VALUES ({}, '{}', '{}', '{}')".format(id, response_json['name'], response_json['name_kanji'], response_json['url']))
                conn.commit()
        conn.close()

def main():
    JikanAPI.Anime()
    JikanAPI.Manga()
    JikanAPI.Characters()

if __name__ == '__main__':
    main()