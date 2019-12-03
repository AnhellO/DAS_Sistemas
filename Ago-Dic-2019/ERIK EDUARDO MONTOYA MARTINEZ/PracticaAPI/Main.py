import requests
import sqlite3
from ObjRegistro import Registro

def traerRegistros():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    if r.status_code == 200:
        response = r.json()
        infoReg = []

        for key in response:
            infoReg.append(key)

        for i in response:
            id = i['id']
            name = i['name']
            username = i['username']
            email = i['email']
            address = i['address']
            street = address['street']
            suite = address['suite']
            city = address['city']
            zipcode = address['zipcode']
            address = i['address'].pop('geo')
            lat = address['lat']
            lng = address['lng']
            phone = i['phone']
            website = i['website']
            company = i['company']
            namec = company['name']
            catchPhrase = company['catchPhrase']
            bs = company['bs']
            reg = Registro(id=id, name=name, username=username, email=email, street=street, suite=suite, city=city,zipcode=zipcode, lat=lat, lng=lng, phone=phone, website=website, nameC=namec,catchPhrase=catchPhrase, bs=bs)
            guardarRegistro(reg)
    else:
        print('No se pueden obtener los registros')

def guardarRegistro(registro):
    try:
        conexion = sqlite3.connect('mibd.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO registros VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(registro._id,registro._name,registro._username,registro._email,registro._street,registro._suite,registro._city,registro._zipcode,registro._lat,registro._lng,registro._phone,registro._website,registro._nameC,registro._catchPhrase,registro._bs))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def mostrarRegistro():
    try:
        conexion = sqlite3.connect('mibd.db')
        cursor = conexion.cursor()
        Mostrar = cursor.execute("SELECT * from usuarios").fetchall()
        registros = []

        for u in Mostrar:
            registros.append(Registro(id=u[0], name=u[1], username=u[2], email=u[3], street=u[4], suite=u[5], city=u[6], zipcode=u[7], lat=u[8], lng=u[9], phone=u[10], website=u[11], nameC=u[12], catchPhrase=u[13], bs=u[14]))

        conexion.commit()
        cursor.close()

        for r in registros:
            print(r)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def main():

    mostrarRegistro()

if __name__ == '__main__':
    main()