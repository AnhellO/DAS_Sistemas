import pymongo as mongo
import redis
import random

client_redis = redis.Redis(host="127.0.0.1",port=6379)
client_mongo = mongo.MongoClient("mongodb://localhost:27017/")
mongo_db = client_mongo["Numeros"]

numbers=[]

for i in range(0,999):
    numbers.append(random.randint(1000,100000))

_key = 0

for i in numbers:
    checker = i%2
    if checker == 0:
        post={"number":i}
        mongo_db.Pares.insert_one(post)
    else:
        client_redis.set(_key,i)
        _key = _key + 1
