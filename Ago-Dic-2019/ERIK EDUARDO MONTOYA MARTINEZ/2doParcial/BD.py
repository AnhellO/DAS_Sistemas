import sqlite3

#Creo la base de datos
try:
    conexion = sqlite3.connect('musicbrainzDB.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de SQLite: ', rows)
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')

#Creo la tabla de usuarios
try:
    conexion = sqlite3.connect('musicbrainzDB.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS Artistas (
                id TEXT,
                area TEXT,
                typeC TEXT,
                name TEXT,
                sort TEXT,
                id2 TEXT,
                extScore TEXT
            );'''

    cursor.execute(query)
    conexion.commit()
    print('Tabla creada con éxito')
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')


def InserArt(art):
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = """INSERT INTO Artistas VALUES ('{}', '{}', '{}', '{}', '{}', '{}',{})""".format(art._id, art._area, art._typeC, art._name, art._sort, art._id2, art._extScore)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Inserts OK', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!',error)

    finally:
        if(conexion):
            conexion.close()


def ShowAllArt():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT * FROM Artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Num de Registros: ', len(rows))

        for r in rows:
            print('Id: {}\nTipoC: {}\nNombre: {}\nArea: {}\nSortName: {}\nextScore: {}'.format(*rows))
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!', error)

    finally:
        if (conexion):
            conexion.close()
def DropArtistas():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'DROP TABLE Artistas;'
        cursor.execute(query)

        print('Se elimino la tabla artistas')

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!', error)

    finally:
        if (conexion):
            conexion.close()

            

def Discos():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = """CREATE TABLE IF NOT EXISTS Discos(
                id TEXT,
                nameArt TEXT ,
                Title TEXT,
                Status TEXT,
                Type TEXT
                );"""
        cursor.execute(query)

        print('Tabla creada con exito!')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!', error)

    finally:
        if (conexion):
            conexion.close()

def InsertDiscos(discos):
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = """INSERT INTO discos VALUES ('{}', '{}', '{}', '{}', '{}')""".format(discos._id, discos._nameArt, discos._Title, discos._Status, discos._Type)
        r = cursor.execute(query)
        conexion.commit()
        print('inserts OK', r)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!',error)

    finally:
        if(conexion):
            conexion.close()


def ShowAllDiscos():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT * FROM Discos;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))
        for r in rows:
            print('Id: {}\nArtista: {}\nTitle: {}\nStatus: {}\nType: {}'.format(*rows))
        print('Total de registros: ', len(rows))
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexion!', error)

    finally:
        if (conexion):
            conexion.close()


def DropDiscos():
    try:
        conexion = sqlite3.connect('musicBrainzDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'DROP TABLE Discos;'
        cursor.execute(query)

        print('Se elimino la tabla!')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion!', error)

    finally:
        if (conexion):
            conexion.close()



