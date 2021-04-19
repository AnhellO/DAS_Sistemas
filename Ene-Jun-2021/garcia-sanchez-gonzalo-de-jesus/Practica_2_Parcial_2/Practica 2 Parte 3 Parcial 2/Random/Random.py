import redis
import pymongo

from random import randint

redis_client = redis.Redis(host='redis', port=6379)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mi-db"]

# Name
print("Nombre de la DB: ", db.name)

numeros_aleatorios = [randint(1000, 1000000) for _ in range(100)]

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios)

numeros_pares = filter(lambda n: n % 2 == 0, numeros_aleatorios)

print()
#SE INGRESAN LOS DATOS IMPARES A LA BASE DE DATOS REDIS
print("IMPARES")
print(list(redis_client.get(numeros_impares)))
print()

#SE INGRESAN LOS DATOS IMPARES A LA BASE DE DATOS MONGODB
print()
print("PARES")
print(list(db.pet.insert_many(numeros_pares)))
print()
        

