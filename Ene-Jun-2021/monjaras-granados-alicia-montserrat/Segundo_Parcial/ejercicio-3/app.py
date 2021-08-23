import redis
import json


def cargardatos(ruta):
    # conectarse con redis
    redis_cliente = redis.Redis( host='redis_ej3',port=6379)

    with open(ruta) as contenido:
        resultado = json.load(contenido)
        #print(resultado) trae toda  la informacion
        for persona in resultado:
            key = "{}-{}-{}".format(persona["id"],persona["first_name"],persona["last_name"])# Declarar llave 
            # insertar a redis por persona,
            redis_cliente.set(key, json.dumps(persona)) #el metodo json.dumps nos permite serializar los objetos de Python como un str.
            # obtener valor
            data_fetch = json.loads(redis_cliente.get(key)) # convertir de JSON a Python
            print(data_fetch) 
            #print(redis_cliente.keys())
          

if __name__=='__main__':
    ruta = './mock_data.json'# leer archivo
    cargardatos(ruta)