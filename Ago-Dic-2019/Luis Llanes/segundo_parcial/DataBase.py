import sqlite3
from artista import artist
from disquillos import album

def Crear_Tabla_Artistas():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS artistas(
                id TEXT,
                nombre TEXT ,
                tags TEXT,
                area TEXT,
                ExtScore TEXT,
                tipo TEXT
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


def Agregar_Elemento_Artista(artist):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO artistas VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(artist._id, artist._name, artist._tags, artist._area, artist._extScore, artist._type)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Todo_Artistas():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nNombre: {}\nTags: {}\nArea: {}\nExtScore: {}\nTipo: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Nombres():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT nombre FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')
        lista = []
        for row in rows:
            lista.append(row[0])
        
        print('Total de registros: ', len(rows))
        
        cursor.close()
        

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
        return lista

def Crear_Tabla_Albums():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS albums(
                id TEXT,
                artista TEXT ,
                titulo TEXT,
                status TEXT,
                type TEXT
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Agregar_Elemento_Album(album):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO albums VALUES ('{}', '{}', '{}', '{}', '{}')""".format(album._id, album._artista, album._titulo, album._status, album._type)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Todo_Albums():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM albums;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nTitulo: {}\nStatus: {}\nType: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def borrar_tabla_albums():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'DROP TABLE albums;'
        cursor.execute(query)
        
        print('registros eliminados')

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def borrar_tabla_Artistas():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'DROP TABLE artistas;'
        cursor.execute(query)
        
        print('registros eliminados')

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()