import pymongo
import redis
import random as rand

nums=[]
clientemongo = pymongo.MongoClient("mongodb://localhost:27017/")
clienteredis = redis.Redis(host="127.0.0.1",port=6379)
database = clientemongo["Numeros"]

for i in range(0,999):
    nums.append(rand.randint(1000,100000))

aux = 0

for i in nums:
    checker = i%2
    if checker == 0:
        post={"number":i}
        database.Pares.insert_one(post)
    else:
        clienteredis.set(aux,i)
        aux += 1

      

