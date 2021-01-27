import os
import pymongo

# Environment variables.
user = os.environ["MONGO_INITDB_ROOT_USERNAME"];
password = os.environ["MONGO_INITDB_ROOT_PASSWORD"];
print(user,' ----',password)

client = pymongo.MongoClient("mongodb://{}:{}@mongo:27017".format(user,password))
db = client["mi-db"]

# Name
print("Nombre de la DB: ", db.name)

# Crea colección e inserta un registro
print(db.pet.insert_many([
    {
        "name": "firulais",
        "owner": "jahir",
        "specie": "perro"
    },
    {
        "name": "taco",
        "owner": "jonathan",
        "specie": "perro"
    },
    {
        "name": "garfield",
        "owner": "erick",
        "specie": "gato"
    },
    {
        "name": "charlotte",
        "owner": "juan daniel",
        "specie": "araña"
    },
    {
        "name": "solovino",
        "owner": "jorge",
        "specie": "perro"
    },
]))
