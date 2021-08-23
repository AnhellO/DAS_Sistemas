import json
import redis

redis_client = redis.Redis(host="172.18.0.2",port=6379)
_key = ""
entri = ""

file = open("mock-data.json",)
data = json.load(file)

for i in data:
    _key += str(i["id"])+"-"
    _key += str(i["first_name"])+"-"
    _key += str(i["last_name"])

    redis_client.set(_key,str(i))    

    _key=""
    pass

"""
redis_client.set(_key,i)
        _key += 1
"""

'''
_key += str(data[0]["id"])

print(_key)
'''