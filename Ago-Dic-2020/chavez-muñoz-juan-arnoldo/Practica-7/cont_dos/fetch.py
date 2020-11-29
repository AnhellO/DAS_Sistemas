import requests
from random import randrange
import pymongo as mo

client = mo.MongoClient("mongodb://localhost:27017/")
db = client["mi-db"]

#Name
print("Nombre de la DB: ", db.name)

def insert_fake_users():
    lista = []
    for i in range(100):
        r = requests.get('https://pipl.ir/v1/getPerson')
        data = r.json()
        name = str(data['person']['personal'].get('name'))
        email = str(data['person']['online_info'].get('email'))
        position = str(data['person']['work'].get('position'))
        datos = {f"name": name, "email": email, "position": position}
        #lista.append(datos)
        db.Persons.insert_one(datos)  
    return "Se insertaron :D"
    # client = mo.MongoClient("mongodb://localhost:27017/")
    # db = client["mi-db"]
    # print("Nombre de la DB: ", db.name)
    # for thing in lista:
    #     db.Persons.insert_one(thing)   
    # return "Se insertaron :D"
    
# Obtiene un registro aleatoprio dependiendo del id
# def get_rand_registro(number:int):
#     print("Imprime todos los registros de las fake Persons: ")
#     count = 1
#     for person in db.Persons.find():
#         if count == number:
#             return person
#         else:
#             count += 1
        
if __name__ == "__main__":
    print(insert_fake_users())
  