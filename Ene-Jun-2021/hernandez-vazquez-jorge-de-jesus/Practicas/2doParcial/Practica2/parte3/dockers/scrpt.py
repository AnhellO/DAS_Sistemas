import redis
import pymongo
import random

myclient = pymongo.MongoClient("mongodb://mongo/")
mydb = myclient["numeros_pares"]
mycol = mydb["mongonumbers"]

rediss = redis.Redis(host='redis',port=6379)


for numbers in range(1000):
    n = random.randint(1000, 1000000)
    if numbers % 2 == 0:
        colleccion = {
            "numbers":numbers
        }
        cllction_num = mycol.insert_one(colleccion)
        print(cllction_num)

    else:
        rediss.set(numbers, n)
        print(rediss.keys())