import json
import redis

varOpen = open("mock_data.json", "r")

varRead = varOpen.read()

#print(varRead)

varJson = json.loads(varRead)

print(len(varJson))
print(varJson[0])
print()
varis = str(varJson[0]) 
print(varis)

#varRedis = redis.Redis(host='redis1', port=6379)

#for keys in varJson:
	#varRedis.set(keys)
