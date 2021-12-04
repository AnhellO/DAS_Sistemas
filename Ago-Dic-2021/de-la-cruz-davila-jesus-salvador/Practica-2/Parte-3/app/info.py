import redis
import json

cliente_redis = redis.Redis(host='redis_db', port=6379)

with open('mock_data.json') as archivo_json:
    data = json.load(archivo_json)

for i in range(0, 99):
    cliente_redis.set('id{}'.format(data[i]['id']), 'first_name{}'.format(data[i]['first_name']), 'last_name{}'.format(data[i]['last_name']), 'email{}'.format(
        data[i]['email']), 'gender{}'.format(data[i]['gender']), 'ip_address{}'.format(data[i]['ip_address']), 'school_number{}'.format([i]['school_number']))
