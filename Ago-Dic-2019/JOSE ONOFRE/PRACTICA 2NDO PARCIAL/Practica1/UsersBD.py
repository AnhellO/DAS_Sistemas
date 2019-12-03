import sqlite3
from ClaseUsers import *

try:
    conexion = sqlite3.connect('BDUsuarios.db')
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
        conexion = sqlite3.connect('BDUsuarios.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS Users(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                username TEXT,
                email TEXT,
                address TEXT,
                addressgeo TEXT,
                phone TEXT,
                website TEXT,
                company TEXT
                
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
   
def insertarUsuario(usuario):
    try:
        conexion = sqlite3.connect('BDUsuarios.db')
        cursor = conexion.cursor()
        print('Conectado')
        query = """INSERT INTO Users VALUES 
                ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(usuario._id, usuario._name, usuario._username, usuario._email, usuario._address, usuario._addressgeo, usuario._phone, usuario._website, usuario._company)
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
def VisualizarUsuarios():
    try:
        conexion = sqlite3.connect('BDUsuarios.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM Users;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nUsername: {}\nEmail: {}\nAddress: {}\nAddresGeo: {}\nPhone: {}\nWebsite: {}\nCompany: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()


# Borrar un registro


def EliminarUsuario(id):
    try:
        conexion = sqlite3.connect('BDUsuarios.db')
        cursor = conexion.cursor()
        print('conectado')

        query = 'DELETE from Users where id={}'.format(id)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Eliminado Correctamente', resultado)
        cursor.close()
    
    except sqlite3.Error as error:
            print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

# Mostrar datos 
def VisualizarUsuarioPorId(id):
    try:
        conexion = sqlite3.connect('BDUsuarios.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT id,name,username,email,address,addressgeo,phone,website,company from Users where id={}'.format(id)
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print('Id: {}\nName: {}\nUsername: {}\nEmail: {}\nAddress: {}\nAddresGeo: {}\nPhone: {}\nWebsite: {}\nCompany: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()
