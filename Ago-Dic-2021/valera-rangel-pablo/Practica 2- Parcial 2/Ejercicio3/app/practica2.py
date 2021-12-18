from redis import *
from json import *

red = redis.Redis(host='redis_db', port=6379, decode_responses=True)
file = open('Practica 2- Parcial 2\Ejercicio 3\mock_Load.json')
Load = json.load(file)

for i in range(0, 99):
    red.set('id{}'.format(Load[i]['id']),
            'first_name{}'.format(Load[i]['first_name']),
            'last_name{}'.format(Load[i]['last_name']),
            'email{}'.format(Load[i]['gender']),
            'ip_address{}'.format(Load[i]['ip_address']),
            'school_numer{}'.format(Load[i]['school_number']))
            
"""
    ({"id":1,
    "first_name":"Adelice",
    "last_name":"Castillon",
    "email":"acastillon0@intel.com",
    "gender":"Male",
    "ip_address":"110.188.66.73",
    "school_number":"ca2bae7e-c200-4c5b-97ba-f14407cb19c5"})
    """