import sqlite3
from parte1 import Anime, Manga, Character

class DataBase():

    def __init__(self, file):
        self.connection = sqlite3.connect(file)

    def CreateTables(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
            cursor.execute("""CREATE TABLE IF NOT EXISTS animes (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      clave int,
                                      title text,
                                      rango int,
                                      url text,
                                      url_image text,
                                      type int,
                                      episodes int,
                                      start_date text,
                                      end_date text,
                                      members int,
                                      score real
                                )""")

            cursor.execute("""CREATE TABLE IF NOT EXISTS mangas (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      clave int,
                                      title text,
                                      rango int,
                                      url text,
                                      url_image text,
                                      type int,
                                      volumes int,
                                      start_date text,
                                      end_date text,
                                      members int,
                                      score real
                                )""")

            cursor.execute("""CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      clave int,
                                      title text,
                                      name_kanji text,
                                      rango int,
                                      url text,
                                      url_image text
                                )""")

            return ("LA TABLA animes, mangas y characters SE CREÓ EXITOSAMENTE")

        except sqlite3.OperationalError:
            return ("OCURRIÓ UN ERROR")

        self.connection.commit()


    def saveAnime(self,data):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos
        cursor.execute('''SELECT clave FROM animes WHERE clave = "{}"'''.format(data.id))

        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'CLAVE':data.id,
            'TITLE': data.title,
            'RANGO': int(data.rank),
            'URL': data.url,
            'URL_IMAGE':data.image_url,
            'TYPE':data.type,
            'EPISODES': data.episodes,
            'START': data.start_date,
            'FIN': data.end_date,
            'MEMBERS': int(data.members),
            'SCORE': float(data.score)
            }
            try:
                cursor.execute( "INSERT INTO animes (id, clave, title, rango, url, url_image,type, episodes, start_date, end_date, members, score) VALUES(null,:CLAVE,:TITLE,:RANGO,:URL,:URL_IMAGE,:TYPE, :EPISODES, :START, :FIN,:MEMBERS, :SCORE);", parametros)
                self.connection.commit()
                return("EL ANIME: {} SE INSERTÓ EXITOSAMENTE A LA TABLA animes".format(data.title))
            except:
                return("ERROR AL INSERTAR EL ANIME A LA BASE DE DATOS")


        else:
            return "EL ANIME {} YA EXISTE EN LA TABLA animes".format(data.title)

    def showAnimes(self):
            # Se hace la conexión a la base de datos
            cursor = self.connection.cursor()
            list = []

            # Se hace la consulta de los libros que se mostrará para ver si hay registros
            cursor.execute("""SELECT * FROM animes""")
            registros = cursor.fetchall()
            if registros == []:
                return "NO HAY REGISTROS EN LA TABLA animes"
            else:
                for e in registros:
                    element = Anime(e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11])
                    list.append(element)
                return list


    def saveManga(self,data):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos
        cursor.execute('''SELECT clave FROM mangas WHERE clave = "{}"'''.format(data.id))

        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'CLAVE':data.id,
            'TITLE': data.title,
            'RANGO': int(data.rank),
            'URL': data.url,
            'URL_IMAGE':data.image_url,
            'TYPE':data.type,
            'VOLUMES': data.volumes,
            'START': data.start_date,
            'FIN': data.end_date,
            'MEMBERS': int(data.members),
            'SCORE': float(data.score)
            }
            try:
                cursor.execute( "INSERT INTO mangas (id, clave, title, rango, url, url_image,type, volumes, start_date, end_date, members, score) VALUES(null,:CLAVE,:TITLE,:RANGO,:URL,:URL_IMAGE,:TYPE, :VOLUMES, :START, :FIN,:MEMBERS, :SCORE);", parametros)
                self.connection.commit()
                return("LA MANGA: {} SE INSERTÓ EXITOSAMENTE A LA TABLA mangas".format(data.title))
            except:
                return("ERROR AL INSERTAR LA MANGA A LA BASE DE DATOS")


        else:
            return "LA MANGA {} YA EXISTE EN LA TABLA mangas".format(data.title)

    def showMangas(self):
            # Se hace la conexión a la base de datos
            cursor = self.connection.cursor()
            list = []

            # Se hace la consulta de los libros que se mostrará para ver si hay registros
            cursor.execute("""SELECT * FROM mangas""")
            registros = cursor.fetchall()
            if registros == []:
                return "NO HAY REGISTROS EN LA TABLA mangas"
            else:
                for e in registros:
                    element = Manga(e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8], e[9], e[10], e[11])
                    list.append(element)
                return list

    def saveCharacter(self,data):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos
        cursor.execute('''SELECT clave FROM characters WHERE clave = "{}"'''.format(data.id))

        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'CLAVE':data.id,
            'TITLE': data.title,
            'NAME': data.name_kanji,
            'RANGO': int(data.rank),
            'URL': data.url,
            'URL_IMAGE':data.image_url
            }
            try:
                cursor.execute( "INSERT INTO characters (id, clave, title, name_kanji, rango, url, url_image) VALUES(null,:CLAVE,:TITLE,:NAME,:RANGO,:URL,:URL_IMAGE);", parametros)
                self.connection.commit()
                return("EL PERSONAJE: {} SE INSERTÓ EXITOSAMENTE A LA TABLA characters".format(data.title))
            except:
                return("ERROR AL INSERTAR EL PERSONAJE A LA BASE DE DATOS")


        else:
            return "EL PERSONAJE {} YA EXISTE EN LA TABLA characters".format(data.title)

    def showCharacters(self):
            # Se hace la conexión a la base de datos
            cursor = self.connection.cursor()
            list = []

            # Se hace la consulta de los libros que se mostrará para ver si hay registros
            cursor.execute("""SELECT * FROM characters""")
            registros = cursor.fetchall()
            if registros == []:
                return "NO HAY REGISTROS EN LA TABLA characters"
            else:
                for e in registros:
                    element = Character(e[1], e[2], e[3], e[4], e[5], e[6])
                    list.append(element)
                return list


if __name__ == '__main__':
    db = DataBase('AnimeMangaCharacter.db')
    #print(db.CreateTables())
