import redis
import json

with open('mock_data.json') as json_file:
    data=json.load(json_file)

redis_client = redis.Redis(host='redis_db', port=6379)

for i in data:
    redis_client.set("id":i['id'],"first_name":i['first_name'],"last_name":i['last_name'],"email":i['email'],"gender":i['gender'],"ip_address":i['ip_address'],"school_number":i['school_number'])
