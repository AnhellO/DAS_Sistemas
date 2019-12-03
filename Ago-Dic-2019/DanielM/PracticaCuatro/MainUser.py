import requests
import sqlite3
from ObjUsuario import User

def consigoUsuarios():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    if r.status_code == 200:
        response = r.json()
        infoUser = []

        #Aquí metemos a infoUser todos los elements del JSON
        for clave in response:
            infoUser.append(clave)

        #Aquí recorremos cada elemento para ponerlos
        # en objetos, para luego guardarlos.
        for i in response:
            id = i['id']
            name = i['name']
            nombreUsuario = i['username']
            email = i['email']
            direccion = i['address']
            calle = direccion['street']
            suite = direccion['suite']
            city = direccion['city']
            zipcode = direccion['zipcode']
            direccion = i['address'].pop('geo')
            latitud = direccion['lat']
            longitud = direccion['lng']
            phone = i['phone']
            website = i['website']
            compania = i['company']
            nombreComp = compania['name']
            catchPhrase = compania['catchPhrase']
            bs = compania['bs']
            usr = User(id=id, name=name, username=nombreUsuario, email=email, street=calle, suite=suite,
                       city=city, zipcode=zipcode, lat=latitud, lng=longitud, phone=phone, website=website,
                       nameC=nombreComp,catchPhrase=catchPhrase, bs=bs)
            guardarusuario(usr)
    else:
        print('Hay problemas al querer obtener los usuarios :(')

def guardarusuario(usr):
    try:
        conexion = sqlite3.connect('base_de_usuarios.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO usuarios VALUES ('{}','{}','{}','{}',"
            "'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format
            (usr._id,usr._name,usr._username,usr._email,usr._street,usr._suite,
             usr._city,usr._zipcode,usr._lat,usr._lng,usr._phone,usr._website,
             usr._nameC,usr._catchPhrase,usr._bs))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Hay un error en la conexión crack :( ', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def mostrarUsers():

    try:
        conexion = sqlite3.connect('base_de_usuarios.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from usuarios").fetchall()
        users = []

        for u in uMostrar:
            users.append(User(id=u[0], name=u[1], username=u[2], email=u[3], street=u[4], suite=u[5],
                              city=u[6], zipcode=u[7], lat=u[8], lng=u[9], phone=u[10], website=u[11],
                              nameC=u[12], catchPhrase=u[13], bs=u[14]))

        conexion.commit()
        cursor.close()

        for u in users:
            print(u)

    except sqlite3.Error as error:
        print('Hay un error en la conexión crack :( ', error)
    finally:
        if (conexion):
            conexion.close()
def main():
    mostrarUsers()

if __name__ == '__main__':
    main()