import sqlite3


conexion=None
cursor=None
#Creo la base de datos

class bddpokeapi():


    conexion=None
    cursor=None
    def __init__(self):

        try:
            self.conexion = sqlite3.connect('pokeapi.db',check_same_thread=False)
            self.cursor = self.conexion.cursor()
            print('Conectado a SQLite')
            self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS pokemones(id TEXT, name TEXT, url TEXT,
            height TEXT, base_exp TEXT, orders TEXT, type TEXT, weight TEXT,
            hp TEXT, defense TEXT, attack TEXT, sprite TEXT)''')

            createTypes='''
            CREATE TABLE IF NOT EXISTS pokemonTypes(
            id TEXT,
            name TEXT,
            url TEXT
            );
            '''
            self.cursor.execute(createTypes)
            self.conexion.commit()

        except sqlite3.Error as error:
            print('Error con la conexión!', error)



    def savePokemon(self,pokemon):
        self.cursor.execute("INSERT INTO pokemones VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(pokemon[0],pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5],pokemon[6],pokemon[7],pokemon[8],pokemon[9],pokemon[10],pokemon[11]))
        self.conexion.commit()

    def saveType(self,type):
        self.cursor.execute("INSERT INTO pokemonTypes VALUES (?,?,?)",(type[0],type[1],type[2]))
        self.conexion.commit()
