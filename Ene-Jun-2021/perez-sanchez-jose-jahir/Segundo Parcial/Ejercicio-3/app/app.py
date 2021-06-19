import redis
import json

redis_client = redis.Redis(host='redis', port=6379)
with open('monk-data.json') as contenido:
    data = json.load(contenido)

for dato in data:
    key =dato.get('id'),dato.get('first_name'),dato.get('last_name')
    redis_client.set(key,dato)


print(redis_client.keys())