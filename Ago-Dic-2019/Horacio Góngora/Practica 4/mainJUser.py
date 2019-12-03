import requests
import sqlite3
from ObjetoUser import User

def conseguirUsers():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    if r.status_code == 200:
        response = r.json()
        infoUser = []

        #Lleno infoUser con todos los elementos del JSON
        for clave in response:
            infoUser.append(clave)

        #Recorro cada elemento uno por uno y lo pongo en unos objetos y los guardo
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
            usr = User(id=id, name=name, username=username, email=email, street=street, suite=suite, city=city,zipcode=zipcode, lat=lat, lng=lng, phone=phone, website=website, nameC=namec,catchPhrase=catchPhrase, bs=bs)
            guardarUser(usr)
    else:
        print('Problemas al obtener los Usuarios')

def guardarUser(usr):
    try:
        conexion = sqlite3.connect('baseUser.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO usuarios VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(usr._id,usr._name,usr._username,usr._email,usr._street,usr._suite,usr._city,usr._zipcode,usr._lat,usr._lng,usr._phone,usr._website,usr._nameC,usr._catchPhrase,usr._bs))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def mostrarUsers():
    try:
        conexion = sqlite3.connect('baseUser.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from usuarios").fetchall()
        users = []

        for u in uMostrar:
            users.append(User(id=u[0], name=u[1], username=u[2], email=u[3], street=u[4], suite=u[5], city=u[6], zipcode=u[7], lat=u[8], lng=u[9], phone=u[10], website=u[11], nameC=u[12], catchPhrase=u[13], bs=u[14]))

        conexion.commit()
        cursor.close()

        for u in users:
            print(u)

        #return users
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def main():
    #conseguirUsers()
    mostrarUsers()

if __name__ == '__main__':
    main()