import redis
import json

try:
    # CONECCION
    redis_client = redis.Redis(host="192.168.144.2",port=6379)

    # NOS LEE LOS DATOS DEL mock_data.json
    with open('mock_data.json') as file:
        data = json.load(file)

    # AÑADIMOS LOS DATOS QUE NOS PIDEN EN LA PRACTICA
    for x in data:
        id = x["id"] 
        frist_name = x["first_name"] 
        last_name = x["last_name"] 
        aux = str(id)+"-"+str(frist_name)+"-"+str(last_name)
        redis_client.set(aux,data)

    print('Done!')
# COMPRUEBA SI HAY ALGUN ERROR
except Exception as e:
    print('Error:\n', e)