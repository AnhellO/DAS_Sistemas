import sqlite3
from API_Marvel import Character

class DataBase():

    def __init__(self, file):
        self.connection = sqlite3.connect(file)

    def CreateTable(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
            cursor.execute("""CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      clave int,
                                      name text,
                                      description text,
                                      url_detail text,
                                      url_wiki text,
                                      movie int
                                )""")
            return ("LA TABLA characters SE CREÓ EXITOSAMENTE")

        except sqlite3.OperationalError:
            return ("OCURRIÓ UN ERROR")

        self.connection.commit()


    def SaveCharacter(self, character):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos

        cursor.execute('''SELECT clave,movie FROM characters WHERE clave = "{}" and movie = "{}"'''.format(character.clave, character.movie))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        resultados = cursor.fetchone()


        if resultados is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'CLAVE':character.clave,
            'NAME': character.name,
            'DESCRIPTION':character.description,
            'URL_DETAIL': character.url_detail,
            'URL_WIKI':character.url_wiki,
            'MOVIE':int(character.movie)}
            try:
                cursor.execute( "INSERT INTO characters (id, clave, name, description, url_detail, url_wiki, movie) VALUES(null,:CLAVE,:NAME,:DESCRIPTION,:URL_DETAIL,:URL_WIKI,:MOVIE);", parametros)
                print("EL PERSONAJE: {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(character.name))
            except:
                return("ERROR AL INSERTAR EL PERSONAJE A LA BASE DE DATOS")

            self.connection.commit()
            cursor.execute("""SELECT * FROM characters WHERE clave = :CLAVE """, {'CLAVE': character.clave})
            consulta = cursor.fetchall()
            list_characters = []
            for c in consulta:
                character = Character(c[1], c[2], c[3], c[4], c[5], c[6])
                list_characters.append(character)
            return list_characters
            self.connection.commit()
        else:
            return "EL PERSONAJE {} YA EXISTE EN LA BASE DE DATOS".format(character.name)

    def ShowCharacters(self, movie):
            # Se hace la conexión a la base de datos
            cursor = self.connection.cursor()
            list = []

            # Se hace la consulta de los libros que se mostrará para ver si hay registros
            cursor.execute("""SELECT * FROM characters where movie={}""".format(movie))
            registros = cursor.fetchall()
            if registros == []:
                return "NO HAY REGISTROS EN LA BASE DE DATOS"

            cursor.execute("""SELECT * FROM characters where movie={}""".format(movie))
            consulta = cursor.fetchall()

            for c in consulta:
                character = Character(c[1], c[2], c[3], c[4], c[5], c[6])
                list.append(character)
            return list


if __name__ == '__main__':
    db = DataBase('avengers.db')
    #print(db.CreateTable())
    #print(db.ShowCharacters(1))
    pass
