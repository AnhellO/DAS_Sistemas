import json
import redis

cliente = redis.Redis(host="[TU IP]",port=6379)
llave = ""

file = open("mock-data.json",)
data = json.load(file)

for i in data:
    llave = str(i["id"])+"-"+str(i["first_name"])+"-"+str(i["last_name"])
    cliente.set(llave,str(i))    
    llave=""