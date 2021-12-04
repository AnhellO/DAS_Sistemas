import redis
import json

print("SE EJECUTO CORRECTAMENTE LA APP")

r = redis.Redis(host='redis_db', port=6379, decode_responses=True) #Docker
file = open('mock_data.json')
data = json.load(file)

for i in range(0, 99):
    r.set('id{}'.format(data[i]['id']), 'first_name{}'.format(data[i]['first_name']), 'last_name{}'.format(data[i]['last_name']), 'email{}'.format(data[i]['gender']), 'ip_address{}'.format(data[i]['ip_address']), 'school_numer{}'.format(data[i]['school_number']))