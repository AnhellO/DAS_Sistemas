import pymongo
import random
import redis

try:
    
    client = pymongo.MongoClient('mongodb://mongo/')
    db = client['pair-numbers']
    collection = db['numbers']
   
    redis_client = redis.Redis(
        host='redis',
        port=6379
    )

    for x in range(1000):
        number = random.randint(1000, 1000000)

        if number % 2 == 0:

            document = {
                "number": number
            }

            document_id = collection.insert_one(document).inserted_id
        
        else:
            redis_client.set(x, number)

    print('Done!')

except Exception as e:
    print('Error:\n', e)