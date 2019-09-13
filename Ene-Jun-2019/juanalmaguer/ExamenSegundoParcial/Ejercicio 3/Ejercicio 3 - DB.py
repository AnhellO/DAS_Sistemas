import json
import sqlite3
import urllib.request

conexion = sqlite3.connect('Users1.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE USUARIOS
(NOMBRE TEXT NOT NULL,
APELLIDO TEXT NOT NULL,
GENERO TEXT NOT NULL,
DIRECCION TEXT NOT NULL,
EMAIL TEXT NOT NULL)''')

with open('RandomUsers.json') as json_file:
    str_file = json_file.read()
    data = json.loads(str_file)
    acumulador = 0
    for result in data['results']:
        acumulador += 1
        if result['gender'] == 'female':
            cursor.execute(
                "insert into Users values ('{}', '{}', 'F', '{}', '{}')".format(acumulador, result['name']['first'],
                                                                                    result['name']['last'],
                                                                                    result['location']['street'],
                                                                                    result['email']))
        else:
            cursor.execute(
                "insert into Users values ('{}', '{}', 'M', '{}', '{}')".format(acumulador, result['name']['first'],
                                                                                    result['name']['last'],
                                                                                    result['location']['street'],
                                                                                    result['email']))

conexion.commit()
conexion.close()