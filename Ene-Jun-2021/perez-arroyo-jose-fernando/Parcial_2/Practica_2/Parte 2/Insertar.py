import pymongo
import json
from pymongo import MongoClient
from MHConsulter import *

client = MongoClient("localhost", 27017)
db = client["mi-db"]

# Name
print("Nombre de la DB: ", db.name)
print(client.list_database_names())

resultado = MHConsulter()
resultado.setItemAilments()
resultado.setAilmentId("6")
resultado.construirPeticion()
resultado.ejecutarPeticion()
resultado.transformText()

prueba = resultado.serializationJson()
prueba = json.dumps(prueba)
prueba2 = json.loads(resultado.serializationJson())

# Crea colección e inserta un registro
print(db.pet.insert_many([prueba2]))