import redis
import json

try:
    redis_client = redis.Redis(
        host='192.168.128.2',
        port=6379
    )
   
    with open('mock_data.json') as file:
        data = json.load(file)

    for x in data:
        id = x["id"] 
        frist_name = x["first_name"] 
        last_name = x["last_name"] 
        aux = str(id)+"-"+frist_name+"-"+last_name
        redis_client.set(aux,data)

    print('Done!')
except Exception as e:
    print('Error:\n', e)