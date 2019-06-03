import json
import os
import sqlite3

class DataBase:
    def __init__(self, archivo):
        # creamos archivo donde guardaremos base de datos
        self.conn = sqlite3.connect(archivo)

    def readFile(self):
        # abrimos archivo donde esta el json
        with open('users.json') as file:
            data = json.load(file)
            resultados_api = data['results']
            # guardamos cada resultado en la base de datos
            for i in resultados_api:
                self.store(i['gender'], i['name']['title'], i['name']['first'], i['name']['last'], i['email'],
                i['location']['street'], i['location']['city'], i['location']['state'], i['location']['postcode'],
                i['location']['coordinates']['latitude'], i['location']['coordinates']['longitude'],
                i['login']['username'], i['login']['password'])

    # método para guardar datos en base de datos
    def store(self, gender, title, first_name, last_name, email, street, city, state, postcode, latitude, longitude, username, password):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO USUARIOS (gender, title, first_name, last_name, email, street, city, state, postcode, latitude, longitude, username, password) VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(gender, title, first_name, last_name, email, street, city, state, postcode, latitude, longitude, username, password))
        self.conn.commit()

    # Método para crear tabla de base de datos
    def createTables(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE USUARIOS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                             gender TEXT,
                                             title TEXT,
                                             first_name TEXT,
                                             last_name TEXT,
                                             email TEXT,
                                             street TEXT,
                                             city TEXT,
                                             state TEXT,
                                             postcode TEXT,
                                             latitude TEXT,
                                             longitude TEXT,
                                             username TEXT,
                                             password TEXT)""")

def main():
    db = DataBase('users.db')
    print("Creando base de datos...")
    db.createTables()
    db.readFile()


if __name__ == "__main__":
    main()
