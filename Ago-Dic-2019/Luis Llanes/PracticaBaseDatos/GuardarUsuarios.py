import requests
import sqlite3
import pprint

def Crear_tabla():
    try:
        conexion = sqlite3.connect('usuarios.db')
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
                    companyName TEXT,
                    catchPhrase TEXT,
                    bc TEXT
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



def Insertar(lista):
    try:
        conexion = sqlite3.connect('usuarios.db')
       
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO usuarios VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}')".format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10], lista[11], lista[12], lista[13], lista[14]))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def Buscar_Usuarios():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    response = r.json()

    for i in response:
        lista =[]
        lista.append(i['id'])
        lista.append(i['name'])
        lista.append(i['username'])
        lista.append(i['email'])
        adrs = i['address']
        lista.append(adrs['street'])
        lista.append(adrs['suite'])
        lista.append(adrs['city'])
        lista.append(adrs['zipcode'])
        adrs = i['address'].pop('geo')
        lista.append(adrs['lat'])
        lista.append(adrs['lng'])
        lista.append(i['phone'])
        lista.append(i['website'])
        company = i['company']
        lista.append(company['name'])
        lista.append(company['catchPhrase'])
        lista.append(company['bs'])

        Insertar(lista)
    


def Ver_Todo():
    try:
        conexion = sqlite3.connect('usuarios.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM usuarios;'
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print('------------------------------------------')
            print('Id: {}\nName: {}\nUserName: {}\nEmail: {}\nStreet: {}\nSuite: {}\nCity: {}\nZipCode: {}\nlat: {}\nlng: {}\nPhone: {}\nWebsite: {}\nCompanyName: {}\nCatchPhrase: {}\nbc: {}'.format(*row))
        
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion',error)

    finally:
        if(conexion):
            conexion.close()

if __name__ == '__main__':
    Crear_tabla()
    # Buscar_Usuarios()
    Ver_Todo()

    
