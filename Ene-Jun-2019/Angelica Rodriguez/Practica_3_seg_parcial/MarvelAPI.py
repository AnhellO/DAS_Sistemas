import hashlib
import requests
import sqlite3

class MarvelAPI():
    def conexionAPI(self, id_movie):
        # Nos conectamos a la API y extraemos la información
        public_key = '2eebb4cf7d11d924d000c50dce4b6fd8'
        private_key = 'cd1a18752fc1885fdf638d106f7fc56a480128ad'
        ts = id_movie
        # Creamos el hash
        hash = hashlib.md5((ts + private_key + public_key).encode()).hexdigest()
        # url
        base = 'https://gateway.marvel.com/v1/public/'
        comics = requests.get(base + 'events/' + ts , params={'apikey': public_key, 'ts': ts, 'hash': hash})
        if comics.status_code != 200:  # si no nos pudimos conectar
            return None
        else:
            return comics.json()  # conexión exitosa

    def verificarResultadoAPI(self, result):
        # Función para verificar resultado de la API
        if result is not None:  # si no hubo error, mandar el resultado
            return result
        else:  # si hubo error, notificar al usuario del error
            print("Ha ocurrido un error. Comprueba tu conexión a Internet")
            return None

    def guardarInformacion(self, dictionary):
        # Método para guardar la información en la base de datos
        data_base = sqlite('db_marvel.db')  # archivo de la base de datos
        for i in dictionary['data']['results']:  # extraemos información
            id_movie = i['id']
            title = i['title']
            description = i['description']
            data_base.saveMovie(id_movie, title, description) # Guardamos película
            characters = i['characters']['items']
            for character in characters:
                id_character = character['resourceURI'].split('/')[-1]
                name_character = character['name']
                data_base.saveCharacter(id_character, name_character) # guardamos personajes
                # Guardamos las relaciones entre la película y el personaje
                data_base.saveRelationships(id_movie, id_character)



class sqlite():
    def __init__(self, archivo):
        # Nombre del archivo de la base de datos
        self.conn = sqlite3.connect(archivo)

    def saveMovie(self, id, name, description):
        # Método para insertar películas en base de datos
        cur = self.conn.cursor()
        cur.execute('INSERT OR IGNORE INTO MOVIES (id, movie, description) VALUES ({}, "{}", "{}")'.format(id, name, description))
        self.conn.commit()

    def saveCharacter(self, id, name):
        # Método para guardar personajes en la base de datos
        cur = self.conn.cursor()
        cur.execute('INSERT OR IGNORE INTO CHARACTERS (id, character) VALUES ({}, "{}")'.format(id, name))
        self.conn.commit()

    def saveRelationships(self, id_movie, id_character):
        # Método para guardar la relación del personaje con la película en la que aparece
        cur = self.conn.cursor()
        cur.execute("INSERT INTO RELATIONSHIPS(movie_id, character_id) VALUES ({}, {})".format(id_movie, id_character))
        self.conn.commit()

    def getCharactersInMovie(self, movie):
        # Función que regresa la relación entre personajes y películas a las que pertenecen
        cur = self.conn.cursor()
        characters = cur.execute("""SELECT m.movie, c.character FROM RELATIONSHIPS r
                                    left join CHARACTERS c on c.id = r.character_id
                                    left join MOVIES m on m.id = r.movie_id
                                    WHERE r.movie_id = """ + movie + " order by m.movie asc").fetchall()
        return characters

    def createTables(self):
        # Método para crear las tablas que tendrá la base de datos
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS MOVIES(id INTEGER PRIMARY KEY, movie TEXT, description TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS CHARACTERS(id INTEGER PRIMARY KEY, character TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS RELATIONSHIPS(movie_id INTEGER, character_id INTEGER)")


def main():
    marvel = MarvelAPI()  # creamos instancia de la clase MarvelAPI
    data_base = sqlite('db_marvel.db')  # instancia de clase sqlite
    data_base.createTables() # creamos tablas de la base de datos
    search_movies = ['234', '314', '29'] # id de las películas a buscar
    for movie in search_movies:
        result = marvel.conexionAPI(movie) # buscamos película
        verificacion = marvel.verificarResultadoAPI(result) # verificamos resultado
        if verificacion is not None: # si el resultado fue correcto, lo guardamos en la base de datos
            print("Guardando en base de datos película con id " + movie)
            marvel.guardarInformacion(verificacion)
        else: # si no hubo resultado, marcamos error
            print("ERROR")
    # Imprimimos las películas con los personajes que aparecen en cada una de ellas
    print("Películas y personajes que hay en la base de datos:\n")
    for movie in search_movies:
        characters = data_base.getCharactersInMovie(movie)
        if characters: # si hay personajes guardados, imprimirlos
            for character in characters:
                print(character)
            print("\n")
        else: # si no hay personajes, indicar que no existen registros
            print("No hay registros de la película con el id " + movie)


if __name__ == "__main__":
    main()
