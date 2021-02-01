import random
import time
import redis
from pymongo import MongoClient

def generar_enteros_random(start,stop, n):
    randomlist = random.sample(range(start, stop), n)
    return randomlist

def par(num):
    return num%2


#        print("primo")
#generar_enteros_random(1000,1000000,1000)
#print(par(5))





def main():
    lista_enteros=generar_enteros_random(1000,1000000,1000)
    # creando client_mongo
    client_mongo=MongoClient('mongodb://%s:%s@mongodb' % ("generador", "generador"))
    db = client_mongo["numeros"]
    col=db["pares"]

    client_redis = redis.StrictRedis(host="redisdb", port=6379, db=0, charset="utf-8", decode_responses=True)

    for numero in lista_enteros:
        if par(numero):
            print("redis")
            with client_redis:
                client_redis.sadd("impares",numero)
        else:
            print("mongo")
            with client_mongo:
                col.insert_one({"value":numero})

if __name__ == '__main__':
    main()

