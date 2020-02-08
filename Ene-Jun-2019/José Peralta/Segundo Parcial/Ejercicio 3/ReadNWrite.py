import json
import sqlite3
# Las consultas del ejercicio 4 las hice cargando datos en la base de manera manual
class Person():
    def __init__(self, nombre, apellido, genero, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return '{}\n{}\n{}\n{}\n{}\n'.format(self.nombre, self.apellido, self.genero, self.direccion, self.correo)

if __name__ == '__main__':
    con = sqlite3.connect('RandomUsers.db')
    cur = con.cursor()
    people = []
    with open('RandomUsers.json') as json_file:
        data = json.load(json_file)
        for result in data['results']:
            name = result['name']['first']
            last_name = result['name']['last']
            address = result['location']['street']
            email = result['email']
            gender = ''
            if result['gender'] == 'female':
                gender = 'F'
            else:
                gender = 'M'
            people.append(Person(name, last_name, gender, address, email))
    for person in people:
        cur.execute("insert into Users values ('{}', '{}', '{}', '{}', '{}')".format(person.nombre, person.apellido, person.genero, person.direccion, person.correo))
    con.commit()
    con.close()
