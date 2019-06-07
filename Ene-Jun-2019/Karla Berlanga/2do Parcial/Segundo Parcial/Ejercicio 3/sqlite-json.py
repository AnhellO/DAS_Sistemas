import json
import os
from database import DataBase

class User():

    def __init__(self, title, first, last, gender, date,age, phone,email,street, city,state):
        self.title = title
        self.first = first
        self.last = last
        self.gender = gender
        self.date = date
        self.age = age
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state

    def __str__(self):
        return """Name: {} {} {}\nGender: {}\nDate {}\nAge: {}\nContact: Phone: {} | Email: {}\nLocation: Street: {} | City: {} | State: {}""".format(
        self.title,
        self.first,
        self.last,
        self.gender,
        self.date,
        self.age,
        self.phone,
        self.email,
        self.street,
        self.city,
        self.state).strip()

def readJson(ruta):
    #Función que lee un archivo .json desde alguna ruta dada y regresa una lista de objetos tipo User()
    with open(ruta) as file:
        data = json.load(file)
        list = []
        for client in data['results']:
            name = client['name']
            dob = client['dob']
            location = client['location']
            usr = User(name['title'].title(), name['first'].title(), name['last'].title(), client['gender'].lower(), dob['date'], dob['age'], client['phone'], client['email'], location['street'].title(), location['city'].title(), location['state'].title())
            #print(usr)
            list.append(usr)
    return list

def guardarUsuarios():
    #Función que guarda todo los usuarios que se encuentran el archivo json
    ruta = "C:\\Users\\karla\\Documents\\Practicas DAS\\DAS_Sistemas\\Ene-Jun-2019\\Karla Berlanga\\2do Parcial\\Segundo Parcial\\Ejercicio 2\\data.json"
    lista = readJson(ruta)
    db = DataBase('users.db')
    for usr in lista:
        db.SaveUser(usr)

def main():
    guardarUsuarios()



if __name__ == '__main__':
    main()
