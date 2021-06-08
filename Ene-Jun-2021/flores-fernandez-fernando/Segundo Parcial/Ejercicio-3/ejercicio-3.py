import redis
import json

try:
    # conexion con redis container
    redis_client = redis.Redis(host="172.30.0.2", port=6379)

    # trae el json
    with open('mock_data.json') as file:
        data = json.load(file)

    # sacamos los datos de la llave 
    for row in data:
        id = row["id"]
        firstName = row["first_name"]
        lastName = row["last_name"]
        key = str(id) + "-"+firstName+"-"+lastName
        print(key)
        redis_client.set(key, str(data))

    print('Done!')
# encuentra un error
except Exception as e:
    print('Error:\n', e)
