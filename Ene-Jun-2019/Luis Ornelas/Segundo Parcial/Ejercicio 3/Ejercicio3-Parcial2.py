import json
import sqlite3

conexion = sqlite3.connect('Users1.db')
cursor = conexion.cursor()

with open('RandomUsers.json') as json_file:
    data = json.load(json_file)
    for result in data['results']:
        if result['gender'] == 'female':
            cursor.execute("insert into Users values ('{}', '{}', 'F', '{}', '{}')".format(result['First'], result['Last'], result['Location'], result['Email']))
        else:
            cursor.execute("insert into Users values ('{}', '{}', 'M', '{}', '{}')".format(result['First'], result['Last'], result['Location'], result['Email']))

conexion.commit()
conexion.close()
