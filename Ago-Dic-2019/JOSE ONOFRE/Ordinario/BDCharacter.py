import sqlite3
from ClaseCharacter import *

try:
    conexion = sqlite3.connect('BDCharacter.db')
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

#Crear Tabla

    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Personaje(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                status TEXT,
                species TEXT,
                type TEXT,
                gender TEXT,
                origin_name TEXT,
                origin_url TEXT,
                location_name TEXT,
                location_url TEXT,
                image TEXT,
                episode TEXT,
                url TEXT,
                created TEXT
                
                );"""
        cursor.execute(query)
        conexion.commit()
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


 ##Insertar
   
def insertarP(Personaje):
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Personaje VALUES 
                ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(Personaje._id, Personaje._nameCh, Personaje._statusCh, Personaje._speciesCh, Personaje._typeCh, Personaje._genderCh, Personaje._origin_nameCh, Personaje._origin_urlCh, Personaje._location_NameCh, Personaje._location_UrlCh, Personaje._imageCh, Personaje._episodeCh, Personaje._urlCh, Personaje._createdCh)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


# Mostrar datos 
def VisualizarPersonaje():
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Personaje;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nStatus: {}\nSpecies: {}\nType: {}\nGender: {}\nOriginName: {}\nOriginUrl: {}\nLocationName: {}\nLocationUrl: {}\nImage: {}\nEpisode: {}\nUrl: {}\nCreated: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


##################################################


#Crear Tabla Location

    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Loc(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT,
                dimension TEXT,
                residents TEXT,
                url TEXT,
                created TEXT
                
                );"""
        cursor.execute(query)
        conexion.commit()
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


 ##Insertar en Locacion
   
def insertarL(Location):
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Loc VALUES 
                ("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(Location._id, Location._nameLoc, Location._typeLoc, Location._dimensionLoc, Location._residentsLoc, Location._urlLoc, Location._createdLoc)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


# Mostrar datos 
def VisualizarLocacion():
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Loc;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nType: {}\nDimension: {}\nResidents: {}\nUrl: {}\nCreated: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


##################################################


#Crear Tabla Episode

    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Epis(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                airdate TEXT,
                episode TEXT,
                characters TEXT,
                url TEXT,
                created TEXT
                
                );"""
        cursor.execute(query)
        conexion.commit()
        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


 ##Insertar en Epis
   
def insertarE(Episodio):
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Epis VALUES 
                ("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(Episodio._id, Episodio._nameEp, Episodio._airdateEp, Episodio._episodeEp, Episodio._charactersEp, Episodio._urlEp, Episodio._createdEp)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


# Mostrar datos 
def VisualizarEpisode():
    try:
        conexion = sqlite3.connect('BDCharacter.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Epis;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nAirDate: {}\nEpisode: {}\nCharacters: {}\nUrl: {}\nCreated: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()