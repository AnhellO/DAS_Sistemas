import pymongo
import random
import redis

   
client = pymongo.MongoClient('mongodb://mongo/')
db = client['numeros_par']
collection = db['numeros']
   
redis_client = redis.Redis(
    host='redis',
    port=6379
    )

for x in range(1000):
    numero = random.randint(1000, 1000000)

    if numero % 2 == 0:
        document = {
            "numero": numero
        }
        document_id = collection.insert_one(document).inserted_id
        
    else:
        redis_client.set(x, numero)
print('Done!')
