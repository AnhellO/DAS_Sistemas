import requests
import sqlite3

class RAMApi():
    def getCharacter(self, id):
        # hacemos un request a la api
        url = "https://rickandmortyapi.com/api/character" + "/" + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    def guardarCharacter(self, response, db):
        # obtenemos la información de la api y la guardamos en la base de datos
            name = response['name']
            status = response['status']
            species = response['species']
            type = response['type']
            gender = response['gender']
            image = response['image']
            url = response['url']
            created = response['created']
            db.saveCharacter(name, status, species, type, gender,image, url, created)

    def getLocation(self, id):
        # hacemos un request a la api
        url = "https://rickandmortyapi.com/api/location" + "/" + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    def guardarLocation(self, response, db):
        # obtenemos la información de la api y la guardamos en la base de datos
        name = response['name']
        type = response['type']
        url = response['url']
        created = response['created']
        db.saveLocation(name, type, url, created)

    def getEpisode(self, id):
        # hacemos un request a la api
        url = "https://rickandmortyapi.com/api/episode" + "/" + str(id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    def guardarEpisode(self, response, db):
        # obtenemos la información de la api y la guardamos en la base de datos
        name = response['name']
        url = response['url']
        created = response['created']
        db.saveEpisode(name, url, created)

class sqlite():
    def __init__(self, archivito):
        # Nombre del archivo de la base de datos
        self.conn = sqlite3.connect(archivito)

    def saveCharacter(self, name, status, species, type, gender, image, url, created):
        # Método para insertar character en la base de datos
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO character(name, status, species, type, gender, image, url, created) VALUES
        (?, ?, ?, ?, ?, ?, ?, ?)''',(name, status, species, type, gender,image, url, created))
        self.conn.commit()
    def saveLocation(self, name, type, url, created):
        # Método para guardar location en la base de datos
        cur = self.conn.cursor()
        cur.execute('''INSERT INTO location(name, type, url, created) VALUES
        (?, ?, ?, ?)''',(name, type, url, created))
        self.conn.commit()
    def saveEpisode(self, name, url, created):
        # Método para guardar los episode en la base de datos
        cur = self.conn.cursor()
        cur.execute('INSERT INTO episode(name, url, created) VALUES (?, ?, ?)',(name, url, created))
        self.conn.commit()

    def createTables(self):
        # Método para crear las tablas que tendrá la base de datos
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS character(id INTEGER PRIMARY KEY, name TEXT, status TEXT,
                    species TEXT, type TEXT, gender TEXT, image TEXT, url TEXT, created TEXT)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS location(id INTEGER PRIMARY KEY, name TEXT, type TEXT,
                            url TEXT, created TEXT)""")
        cur.execute("""CREATE TABLE IF NOT EXISTS episode(id INTEGER PRIMARY KEY, name TEXT,
                            url TEXT, created TEXT)""")

def main():
    ramapi = RAMApi() # instancia
    data_base = sqlite('ram.db') # archivo de la base de datos
    data_base.createTables() # creamos las tablas de la base de datos

    for i in range(1,494):
        response = ramapi.getCharacter(i)
        if response != None:
            print("Guardando character con id " + str(i))
            ramapi.guardarCharacter(response, data_base)

    for i in range(1,77):
     response = ramapi.getLocation(i)
     if response != None:
            print("Guardando location con id " + str(i))
            ramapi.guardarLocation(response, data_base)

    for i in range(1,32):
     response = ramapi.getEpisode(i)
     if response != None:
            print("Guardando episode con id " + str(i))
            ramapi.guardarEpisode(response, data_base)

if __name__ == "__main__":
    main()