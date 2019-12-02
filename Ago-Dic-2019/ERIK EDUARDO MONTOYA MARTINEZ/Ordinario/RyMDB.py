import sqlite3
try:
    conexion = sqlite3.connect('RyMDB.db')
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


try:
    conexion = sqlite3.connect('RyMDB.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')
#creadno tabla de personajes
    tablaper = '''CREATE TABLE IF NOT EXISTS Personajes (
                id TEXT,
                name TEXT,
                status TEXT,
                species TEXT,
                type TEXT,
                gender TEXT,
                OriginName TEXT,
                OriginUrl TEXT,
                LocationName TEXT,
                LocationUrl TEXT,
                image TEXT,
                episodes TEXT,
                url TEXT,
                created TEXT
            );'''
#creando tabla de locaciones
    tablaloc = '''CREATE TABLE IF NOT EXISTS Locaciones (
                id TEXT,
                name TEXT,
                type TEXT,
                dimension TEXT,
                residents TEXT,
                url TEXT,
                created TEXT
            );'''
#creando tabla de episodios
    tablaepi = '''CREATE TABLE IF NOT EXISTS Episodios (
                id TEXT,
                name TEXT,
                air_date TEXT,
                episode TEXT,
                characters TEXT,
                url TEXT,
                created TEXT
            );'''

    cursor.execute(tablaper)
    cursor.execute(tablaloc)
    cursor.execute(tablaepi)
    conexion.commit()
    print('Tabla creada con éxito')
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión!', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')