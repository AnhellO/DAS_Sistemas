import pymongo # https://pypi.org/project/pymongo/
import redis # https://pypi.org/project/redis/
from random import randrange

# Crea los 1000 números aleatorios
random_nums = [randrange(1000, 1000000) for i in range(0, 1000)]

###############################################################################################
#
#                               L Ó G I C A   D E   M O N G O
#
###############################################################################################

# Conectate al contenedor de Mongo: docker run --name mongo -d -p 27017:27017 mongo
myclient = pymongo.MongoClient("mongodb://mongo:27017/")
# Crea la base de datos en Mongo
mydb = myclient["numbers"]
# Crea la colección en Mongo
mycol = mydb["even"]

# Inserta solamente los números pares en la colección
for item in random_nums:
    if item % 2 == 0:
        result = mycol.insert_one({"number": item})
        print(result)

# Obtén todos los registros existentes en la colección
for item in mycol.find():
    print(item)

###############################################################################################
#
#                               L Ó G I C A   D E   R E D I S
#
###############################################################################################

# Conectate al contenedor de Redis: docker run --name redis -d -p 6379:6379 redis
r = redis.Redis(host='redis', port=6379)

# Inserta solamente los números impares en el storage de Redis
for i in range(0, len(random_nums)):
    if random_nums[i] % 2:
        r.set(i, random_nums[i])

# Imprime todos los números existentes
for key in r.keys():
    print(r.get(key))