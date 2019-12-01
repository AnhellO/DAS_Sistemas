import sqlite3

def crear_tabla():
    try:
        conexion = sqlite3.connect('Apis/usuariosDB.db')
        cursor = conexion.cursor()
        print('Conectado a SQLite')

        query = '''CREATE TABLE IF NOT EXISTS users (
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
                    companyName TEXT,
                    catchPhrase TEXT,
                    bs TEXT
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

def Insertar(usua):
    try:
        conexion = sqlite3.connect('Apis/usuariosDB.db')

        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO users VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(usua._Id,usua._Nombre,usua._NombreUsuario,usua._Email,usua._Calle,usua._Suite,usua._Ciudad,usua._CodigoZip,usua._Latitud,usua._Longitud,usua._Telefono,usua._WebSite,usua._CompañiaNombre,usua._CatchPhrase,usua._Bs))

        conexion.commit()
        print('Valor Insertado Correctamente')
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def Ver_Todos_Usuarios():
    try:
        conexion = sqlite3.connect('Apis/usuariosDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM users;'
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            
            print('Id: {}\nNombre: {}\nNombre Usuario: {}\nE-mail: {}\nCalle: {}\nSuite: {}\nCiudad: {}\nCodigo Zip: {}\nLatitud: {}\nLongitud: {}\nTelefono: {}\nSitio Web: {}\nCompañia: {}\nCatch Phrase: {}\nBs: {}'.format(*row))
            print('------------------------------------------')

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def Ver_Un_Usuario(Id):
    try:
        conexion = sqlite3.connect('Apis/usuariosDB.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM users WHERE id = {};'.format(Id)
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            
            print('Id: {}\nNombre: {}\nNombre Usuario: {}\nE-mail: {}\nCalle: {}\nSuite: {}\nCiudad: {}\nCodigo Zip: {}\nLatitud: {}\nLongitud: {}\nTelefono: {}\nSitio Web: {}\nCompañia: {}\nCatch Phrase: {}\nBs: {}'.format(*row))
            print('------------------------------------------')

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')