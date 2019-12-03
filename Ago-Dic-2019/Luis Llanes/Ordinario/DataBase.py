import sqlite3
import Episodios
import Personaje
import Locaciones


def Crear_Tabla_Personajes():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS personajes(
                fecha_creacion TEXT,
                episodios_apariciones_url TEXT,
                episodios_apariciones_numero TEXT,
                genero TEXT,
                id_personaje TEXT,
                imagen TEXT,
                locacion_name TEXT,
                locacion_url TEXT,
                nombre TEXT,
                origen_name TEXT,
                origen_url TEXT,
                especie TEXT,
                status TEXT,
                tipo TEXT,
                url TEXT PRIMARY KEY,
                foreign key(episodios_apariciones_url) references episodios(url),
                foreign key(locacion_url) references locaciones(url)
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


def Crear_Tabla_Locaciones():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS locaciones(
                fecha_creacion TEXT,
                dimension TEXT ,
                id_locacion TEXT,
                nombre TEXT,
                residentes TEXT,
                tipo TEXT,
                url TEXT PRIMARY KEY
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


def Crear_Tabla_Episodios():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS episodios(
                fecha_lanzamiento TEXT,
                personajes TEXT ,
                fecha_creacion TEXT,
                episodio TEXT,
                id_episodio TEXT,
                nombre TEXT,
                url TEXT PRIMARY KEY
                );"""
        cursor.execute(query)
        
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Agregar_Elemento_Personajes(personaje):
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO personajes VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(personaje._FechaDeCreacion, personaje._EpisodiosDondeAparece, personaje._NumeroEpisodiosDondeAparece, personaje._Genero, personaje._Id_Personaje, personaje._Imagen, personaje._Location_Name, personaje._Location_URL, personaje._Nombre, personaje._Origen_Name, personaje._Origen_URL, personaje._Especie, personaje._Status, personaje._Tipo, personaje._URL)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Agregar_Elemento_Locaciones(locacion):
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO locaciones VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(locacion._FechaCreacion, locacion._Dimension, locacion._Id_Locacion, locacion._Nombre, locacion._Residentes, locacion._Tipo, locacion._URL)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Agregar_Elemento_Episodio(episodio):
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO episodios VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(episodio._FechaLanzamiento, episodio._Personajes, episodio._FechaCreacion, episodio._CodEpisodio, episodio._Id_Episodio, episodio._Nombre, episodio._URL)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Todo_Personajes():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM personajes;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('fecha_creacion: {}\nepisodios_apariciones_url: {}\nepisodios_apariciones_numeros: {}\ngenero: {}\nid_personaje: {}\nimagen: {}\nlocacion_name: {}\nlocacion_url: {}\nnombre: {}\norigen_name: {}\norigen_url: {}\nespecie: {}\nstatus: {}\ntipo: {}\nurl: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


def Ver_Todo_Locaciones():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM locaciones;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('fecha_creacion: {}\ndimension: {}\nid_locacion: {}\nnombre: {}\nresidentes: {}\ntipo: {}\nurl: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Ver_Todo_Episodios():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM episodios;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('fecha_lanzamiento: {}\npersonajes: {}\nfecha_creacion: {}\nepisodio: {}\nid_episodio: {}\nnombre: {}\nurl: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def Eliminar_Tabla_Personajes():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "DELETE FROM personajes"
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valores Eliminados Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

def buscar_Ricks():
    try:
        conexion = sqlite3.connect('Rick&Morty.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = "SELECT * FROM personajes WHERE nombre LIKE '%Rick%';"
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('fecha_creacion: {}\nepisodios_apariciones_url: {}\nepisodios_apariciones_numeros: {}\ngenero: {}\nid_personaje: {}\nimagen: {}\nlocacion_name: {}\nlocacion_url: {}\nnombre: {}\norigen_name: {}\norigen_url: {}\nespecie: {}\nstatus: {}\ntipo: {}\nurl: {}'.format(*row))
            print('-------------------------------')
        
        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

Crear_Tabla_Episodios()
Crear_Tabla_Locaciones()
Crear_Tabla_Personajes()
# buscar_rick()
# Ver_Todo_Locaciones()
# Ver_Todo_Episodios()
# Ver_Todo_Personajes()
# Eliminar_Tabla_Personajes()