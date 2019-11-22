"""En un archivo de Python por separado crea una clase llamada ORM, la cual nos permita acceder a cualquiera de las tablas creadas a partir
del ejercicio anterior. La clase ORM nos debe de dar la posibilidad de llevar a cabo las siguientes rutinas;
1. Obtener los datos de todos los artistas
2. Obtener los datos de uno o varios artistas
3. Obtener todos los discos de uno o varios artistas
4.Obtener discos específicos de uno o varios artistas por medio de:
    id
    título del disco
5.Contar cuantos artistas existen en la base de datos
6.Contar cuantos discos tiene X artista
7.Obtener todos los artistas cuyos tags incluyan un tag en específico pasado como parámetro, es decir parameter_tag in tags
8.Deberás de demostrar la funcionalidad de las rutinas requeridas anteriomente a través de la función main"""

import sqlite3

def getDatosTodosArtistas():
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT * FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        for row in rows:
            print('Id: {}\nNombre: {}\nOtro Nombre: {}\nTipo Ciudad: {}\nExtScore: {}'.format(*row))

        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def getDatosUnoVariosArtistas(nombre):
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = "SELECT * FROM artistas where nombre='{}';".format(nombre)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        for row in rows:
            print('Id: {}\nNombre: {}\nOtro Nombre: {}\nTipo Ciudad: {}\nExtScore: {}'.format(*row))
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def cantidadArtistas():
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = 'SELECT * FROM artistas;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def CantidadAlbumsArtista(nombre):
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = "SELECT * FROM discos where artista = '{}';".format(nombre)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

# getDatosTodosArtistas()
# getDatosUnoVariosArtistas()
# cantidadArtistas()
# CantidadAlbumsArtista()