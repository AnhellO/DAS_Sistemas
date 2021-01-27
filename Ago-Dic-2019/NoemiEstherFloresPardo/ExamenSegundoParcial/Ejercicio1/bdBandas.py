import sqlite3

try:
    conexion = sqlite3.connect('bandas.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de SQLite: ', rows)
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión cerrada\n')

try:
    conexion = sqlite3.connect('bandas.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS artistas (
                id TEXT,
                area TEXT,
                typeC TEXT,
                name TEXT,
                sort TEXT,
                idd TEXT,
                extScore TEXT
            );'''

    cursor.execute(query)
    conexion.commit()

    query = '''CREATE TABLE IF NOT EXISTS discos (
                    id Text,
                    name TEXT,
                    discos TEXT
                );'''

    cursor.execute(query)
    conexion.commit()
    print('Tabla creada con éxito')
    cursor.close()
except sqlite3.Error as error:
    print('Error con la conexión', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')