import requests
import sqlite3
from user import User

def getUsers():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    if r.status_code == 200:
        response = r.json()
        Usuarios = []

        for l in response:
            Usuarios.append(l)

        for i in response:
            id = i['id']
            name = i['name']
            username = i['username']
            email = i['email']
            adrs = i['address']
            street = adrs['street']
            suite = adrs['suite']
            city = adrs['city']
            zipcode = adrs['zipcode']
            adrs = i['address'].pop('geo')
            lat = adrs['lat']
            lng = adrs['lng']
            phone = i['phone']
            website = i['website']
            company = i['company']
            namec = company['name']
            catchPhrase = company['catchPhrase']
            bs = company['bs']
            usuario = User(id=id, name=name, username=username, email=email, street=street, suite=suite, city=city,
                       zipcode=zipcode, lat=lat, lng=lng, phone=phone, website=website, nameC=namec,
                       catchPhrase=catchPhrase, bs=bs)
            guardarUsuario(usuario)
    else:
        print('Problemas al obtener los Usuarios')


def guardarUsuario(usuario):
    try:
        conexion = sqlite3.connect('user.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO usuarios VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                usuario.id, usuario.name, usuario.username, usuario.email, usuario.street, usuario.suite, usuario.city, usuario.zipcode,
                usuario.lat, usuario.lng, usuario.phone, usuario.website, usuario.nameC, usuario.catchPhrase, usuario.bs))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')


def viewUsers():
    try:
        conexion = sqlite3.connect('user.db')
        cursor = conexion.cursor()
        view = cursor.execute("SELECT * from usuarios").fetchall()
        users = []

        for u in view:
            users.append(
                User(id=u[0], name=u[1], username=u[2], email=u[3], street=u[4], suite=u[5], city=u[6], zipcode=u[7],
                     lat=u[8], lng=u[9], phone=u[10], website=u[11], nameC=u[12], catchPhrase=u[13], bs=u[14]))

        conexion.commit()
        cursor.close()

        for u in users:
            print(u)

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()


def main():
    # getUsers()
    viewUsers()


if __name__ == '__main__':
    main() 