import random
import redis
import pymongo


# Conectarnos con mongo
mongo_cliente = pymongo.MongoClient('mongodb://mongo/')

#print(mongo_cliente.list_database_names())#muestra bases de datos

db = mongo_cliente['Numeros_pares']# crea base de datos
coleccion_var = db['numero'] #crear coleccion

# conectarse con redis
redis_cliente = redis.Redis( host='redis',port=6379 )

for x in range(1000):
    numero = random.randint(1000, 1000000)

    if numero % 2 == 0:

        coleccion = {
            "numero": numero
        }

        coleccion_numero = coleccion_var.insert_one(coleccion)# insertar a mongo
        print(coleccion_numero)

    else:

        redis_cliente.set(x, numero) #insertar a redis
        print(redis_cliente.keys())

