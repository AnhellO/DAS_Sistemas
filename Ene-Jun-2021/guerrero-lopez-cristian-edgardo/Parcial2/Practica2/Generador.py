import pymongo
import redis
import random

r_client = redis.Redis(host="127.0.0.1",port=6379)
m_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = m_client["Numeros"]

numeros=[]

for i in range(0,999):
    numeros.append(random.randint(1000,100000))

_key = 0

for i in numeros:
    checker = i%2
    if checker == 0:
        post={"number":i}
        mongo_db.Pares.insert_one(post)
    else:
        r_client.set(_key,i)
        _key += 1