import requests
import json
import sqlite3

class P1_Jikan():
    @staticmethod
    def AnimesG():
        anime_list = [1, 5, 6, 7, 8, 20, 30, 50, 60, 80, 90, 45, 17, 97, 14, 79, 87, 84]
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in anime_list:
            response = requests.get('https://api.jikan.moe/v3/anime/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Anime VALUES ({}, '{}', '{}', '{}')".format(id, response_json['title'], response_json['episodes'], response_json['status']))
                conn.commit()
        conn.close()

    @staticmethod
    def MangaG():
        manga_list = [1, 2, 3, 4, 7, 8, 9, 10, 80, 90, 100, 74, 78, 89, 12, 11, 63, 88, 99]
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in manga_list:
            response = requests.get('https://api.jikan.moe/v3/manga/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Manga VALUES ({}, '{}', '{}', '{}')".format(id, response_json['title'], response_json['chapters'], response_json['status']))
                conn.commit()
        conn.close()

    @staticmethod
    def CharactersG():
        characters_list = [1, 2, 3, 4, 5, 6, 7, 50, 60, 89, 86, 52, 15, 96, 16, 69, 13, 27, 21]
        conn = sqlite3.connect('Jikan.db')
        cur = conn.cursor()
        for id in characters_list:
            response = requests.get('https://api.jikan.moe/v3/character/{}'.format(id))
            if response.status_code == 200:
                response_json = json.loads(response.text)
                cur.execute("INSERT INTO Character VALUES ({}, '{}', '{}')".format(id, response_json['name'], response_json['image_url']))
                conn.commit()
        conn.close()

def main():
    P1_Jikan.AnimesG()
    P1_Jikan.MangaG()
    P1_Jikan.CharactersG()

if __name__ == '__main__':
    main()
