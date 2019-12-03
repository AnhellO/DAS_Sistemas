import sqlite3
import pprint

class database_API():

    def __init__(self):
        self.crear_database()
        self.crear_tabla_Characters()
        self.crear_tabla_episodes()
        self.crear_tabla_locations()

    def crear_database(self):
        conexion = sqlite3.connect('database_api.db')
        conexion.close()

    def crear_tabla_Characters(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        query = "CREATE TABLE IF NOT EXISTS characters(id_characters int PRIMARY KEY, name text, status text, species text, gender text, origin text, location text, episode text);"
        cursor.execute(query)
        conexion.commit()
        conexion.close()

    def crear_tabla_locations(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        query = "CREATE TABLE IF NOT EXISTS locations(id_locations int PRIMARY KEY, name text, tipo text, dimension text, residentes text);"
        cursor.execute(query)
        conexion.commit()
        conexion.close()

    def crear_tabla_episodes(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        query = "CREATE TABLE IF NOT EXISTS episodes(id_episodes int PRIMARY KEY, name text, air_date text, episode text, characters text);"
        cursor.execute(query)
        conexion.commit()
        conexion.close()

    def llenar_tabla_characters(self, id_character, name, status, species, gender, origin, location, episode):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO characters (id_characters, name, status, species, gender, origin, location, episode) VALUES(:id_characters, :name, :status, :species, :gender, :origin, :location, :episode)",
        {"id_characters": id_character, "name": name, "status" : status, "species" : species, "gender" : gender, "origin" : origin, "location" : location, "episode" : episode})
        conexion.commit()
        conexion.close()

    def llenar_tabla_locations(self, id_location, name, tipo, dimension, residentes):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO locations (id_locations, name, tipo, dimension, residentes) VALUES (:id_locations, :name, :tipo, :dimension, :residentes)",
        {"id_locations" : id_location, "name" : name, "tipo" : tipo, "dimension" : dimension, "residentes" : residentes})
        conexion.commit()
        conexion.close()

    def llenar_tabla_episodes(self, id_episodes, name, air_date, episode, characters):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO episodes (id_episodes, name, air_date, episode, characters) VALUES (:id_episodes, :name, :air_date, :episode, :characters)",
        {"id_episodes" : id_episodes, "name" : name, "air_date" : air_date, "episode" : episode, "characters" : characters})
        conexion.commit()
        conexion.close()

    def mostrar_tabla_characters(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM characters")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def mostrar_tabla_locations(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM locations")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def mostrar_tabla_episodes(self):
        conexion = sqlite3.connect('database_api.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM episodes")
        rows = cursor.fetchall()
        for row in rows:
            pprint.pprint(row)