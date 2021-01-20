import os
import pymongo

# Environment variables.
user = os.environ["MONGO_INITDB_ROOT_USERNAME"];
password = os.environ["MONGO_INITDB_ROOT_PASSWORD"];
print(user,' ----',password)

client = pymongo.MongoClient("mongodb://{}:{}@mongo:27017".format(user,password))
db = client["mi-db"]

# Obtén un registro
print("Imprime un registro\n", db.pet.find_one(), "\n")

# Obtén todos los registros
print("Imprime todos los registros")
for pet in db.pet.find():
    print(pet)
