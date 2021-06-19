from random import randrange
import pymongo
import redis

conn = pymongo.MongoClient("mongodb://localhost:8081/")
mydb = conn["numeroPares"]
mycol = mydb["pares"]

contador=0
while contador<1001:
    diccionario={"numero":randrange(0,1000000,2)}
    x=mycol.insert_one(diccionario)
    contador=contador+1

redis_client = redis.Redis(host='redis', port=6379)

contador=0
while contador<1001:
    diccionario={"numero":randrange(0,1000000,2)}
    redis_client.set('numero',diccionario['numero'])
    contador=contador+1