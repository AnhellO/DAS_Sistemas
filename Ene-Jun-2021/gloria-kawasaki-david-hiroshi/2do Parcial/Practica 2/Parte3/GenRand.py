import random as randNum
import pymongo
import redis

redis_client = redis.Redis(host="127.0.0.1",port=6379)
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["Numeros"]

nums=[]

for i in range(0,999):
    nums.append(randNum.randint(1000,100000))

_key = 0

for i in nums:
    checker = i%2
    if checker == 0:
        post={"number":i}
        mongo_db.Pares.insert_one(post)
    else:
        redis_client.set(_key,i)
        _key += 1