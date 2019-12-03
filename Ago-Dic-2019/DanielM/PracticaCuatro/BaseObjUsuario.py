import sqlite3

#Creo la base de datos
try:
    conexion = sqlite3.connect('base_de_usuarios.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = 'SELECT sqlite_version();'
    cursor.execute(query)
    rows = cursor.fetchall()
    print('Version de SQLite: ', rows)
    cursor.close()
except sqlite3.Error as error:
    print('Hay un error en la conexión crack :( ', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')

#Creo la tabla de usuarios
try:
    conexion = sqlite3.connect('base_de_usuarios.db')
    cursor = conexion.cursor()
    print('Conectado a SQLite')

    query = '''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                email TEXT,
                street TEXT,
                suite TEXT,
                city TEXT,
                zipcode TEXT,
                lat TEXT,
                lng TEXT,
                phone TEXT,
                website TEXT,
                nameC TEXT,
                catchPhrase TEXT,
                bc TEXT
            );'''

    cursor.execute(query)
    conexion.commit()
    print('La tabla fue creada con éxito :v ')
    cursor.close()
except sqlite3.Error as error:
    print('Hay un error en la conexión crack :( ', error)
finally:
    if (conexion):
        conexion.close()
        print('Conexión a SQLite cerrada\n')