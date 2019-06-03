import requests
import sqlite3

class CosasOtakus():
    def getRequest(self, endpoint, id):
        # hacemos un request a la api de jikan
        url = "https://api.jikan.moe/v3/" + endpoint + "/" + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def guardarInformacion(self, endpoint, response, db):
        # obtenemos la información de la api y la guardamos en la base de datos
        if endpoint == "anime":
            title = response['title']
            episodes = response['episodes']
            duration = response['duration']
            rating = response['rating']
            synopsis = response['synopsis']
            image_url = response['image_url']
            status = response['status']
            db.saveAnime(title, episodes, duration, rating, synopsis, image_url, status)
        elif endpoint == "manga":
            title = response['title']
            status = response['status']
            image_url = response['image_url']
            synopsis = response['synopsis']
            chapters = response['chapters']
            db.saveManga(title, status, image_url, synopsis, chapters)
        elif endpoint == "character":
            name = response['name']
            about = response['about']
            image_url = response['image_url']
            db.saveCharacters(name, about, image_url)


class sqlite():
    def __init__(self, archivo):
        # Nombre del archivo de la base de datos
        self.conn = sqlite3.connect(archivo)

    def saveAnime(self, title, episodes, duration, rating, synopsis, image_url, status):
        # Método para insertar animes en la base de datos
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO ANIME (title, episodes, duration, rating, synopsis, image_url, status) VALUES
        (?, ?, ?, ?, ?, ?, ?)''',(title, episodes, duration, rating, synopsis, image_url, status))
        self.conn.commit()

    def saveManga(self, title, status, image_url, synopsis, chapters):
        # Método para guardar mangas en la base de datos
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO MANGA (title, status, image_url, synopsis, chapters) VALUES
        (?, ?, ?, ?, ?)''', (title, status, image_url, synopsis, chapters))
        self.conn.commit()

    def saveCharacters(self, name, about, image_url):
        # Método para guardar los personajes en la base de datos
        cur = self.conn.cursor()
        about = about.encode("unicode_escape").decode("utf-8")
        cur.execute('INSERT INTO CHARACTERS(name, about, image_url) VALUES (?, ?, ?)',(name, about, image_url))
        self.conn.commit()

    def createTables(self):
        # Método para crear las tablas que tendrá la base de datos
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS ANIME(id INTEGER PRIMARY KEY, title TEXT, episodes INTEGER,
                    duration TEXT, rating TEXT, synopsis TEXT, image_url TEXT, status TEXT)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS MANGA(id INTEGER PRIMARY KEY, title TEXT, status TEXT,
                    image_url TEXT, synopsis TEXT, chapters INTEGER)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS CHARACTERS(id INTEGER PRIMARY KEY, name TEXT, about TEXT,
                    image_url TEXT)""")


def main():
    otaku = CosasOtakus() # instancia
    data_base = sqlite('db_otaku.db') # archivo de la base de datos
    data_base.createTables() # creamos las tablas de la base de datos
    endpoints = ['anime', 'manga', 'character'] # endpoints a utilizar
    for endpoint in endpoints:
        for i in range(1, 30):
            response = otaku.getRequest(endpoint, i)
            if response != None:
                print("guardando " + endpoint + " con id " + str(i))
                otaku.guardarInformacion(endpoint, response, data_base)



if __name__ == "__main__":
    main()
