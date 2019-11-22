import sqlite3

#Obtener los datos de todos los artistas
def Obtener_Datos_Artistas():
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

#Obtener los datos de uno o varios artistas
def Obtener_Datos_Artistas_Especificos(nombre):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM artistas where nombre='{}';".format(nombre)
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

#Obtener todos los discos de un artistas
def Ver_Albums_Artista(Artista):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM albums where artista = '{}';".format(Artista)
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

#Obtener discos específicos de uno o varios artistas por medio de:
# id
# título del disco

def Ver_Albums_Especifico(Id_Album = '', titulo= '', Artista =''):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')
        if Id_Album == '' and titulo == '' and Artista == '':
            query = 'SELECT * FROM albums;'
        elif Id_Album != '':
            query = "SELECT * FROM albums where artista = '{}' and id = '{}';".format(Artista, Id_Album)
        elif titulo != '':
            query = "SELECT * FROM albums where artista = '{}' and titulo = '{}';".format(Artista, titulo)
        else:
            query = "SELECT * FROM albums where artista = '{}';".format(Artista)
        
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

#Contar cuantos artistas existen en la base de datos
def Ver_Cantidad_Artistas():
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

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

#Contar cuantos discos tiene X artista
def Ver_Cantidad_Albums_Artista(Artista):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM albums where artista = '{}';".format(Artista)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

#Obtener todos los artistas cuyos tags incluyan un tag en específico pasado como parámetro, es decir parameter_tag in tags
def Obtener_Artistas_Tags(Tags):
    try:
        conexion = sqlite3.connect('musicBrainz.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM artistas where tags = '{}';".format(Tags)
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


# Obtener_Datos_Artistas()
# Obtener_Datos_Artistas_Especificos('Xzibit')
# Ver_Albums_Artista('Xzibit')
# Ver_Albums_Especifico(titulo='40 Dayz & 40 Nightz',Artista='Xzibit')
# Ver_Cantidad_Artistas()
# Ver_Cantidad_Albums_Artista('Xzibit')
# Obtener_Artistas_Tags('rock or metal')
