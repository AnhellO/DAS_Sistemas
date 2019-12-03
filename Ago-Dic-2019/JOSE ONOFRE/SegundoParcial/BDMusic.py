import sqlite3
import ClaseArtista
import ClaseDisco
try:
    conexion = sqlite3.connect('BDMusic.db')
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
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Artist(
                id TEXT PRIMARY KEY,
                Artista TEXT NOT NULL,
                Area TEXT,
                Score TEXT,
                Inicio TEXT
                
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

#Crear Tabla 2

    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Discos(
                id TEXT PRIMARY KEY,
                Artista TEXT NOT NULL,
                Pais TEXT,
                Fecha TEXT,
                Estado TEXT
                
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


# Insertar los datos a la tabla Discos
def insertarD(Disco):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Discos VALUES 
                ('{}', '{}', '{}', '{}', '{}')""".format(Disco._id, Disco._artista, Disco._pais, Disco._fecha, Disco._estado)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()




# Insertar los datos a la BD
def insertar(Artista):
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Discos VALUES 
                ('{}', '{}', '{}', '{}', '{}')""".format(Artista._id, Artista._artista, Artista._area, Artista._score, Artista._begin)
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
def Visualizar():
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Artist;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nArea: {}\nScore: {}\nComienzo: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


# Mostrar datos 2 
def VisualizarD():
    try:
        conexion = sqlite3.connect('BDMusic.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Discos;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nArtista: {}\nPais: {}\nFecha: {}\nEstado: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()