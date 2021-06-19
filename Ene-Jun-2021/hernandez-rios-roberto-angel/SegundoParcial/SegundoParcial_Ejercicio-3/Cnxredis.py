import redis
import json

archivo=open("mock_data.json", 'r').read()
archivo=archivo.replace("[", "").replace("]", "").split(',\n')
lineas=[]
for linea in archivo:
    lineas.append(json.loads(linea))

llaves=[]
for llave in range(len(lineas)):
    string = '{}-{}-{}'.format(lineas[llave].get("id"),lineas[llave].get("first_name"),lineas[llave].get("last_name"))
    llaves.append(string)

r = redis.Redis(host='redis', port=6379)

for set in range(len(lineas)):
    r.set(llaves[set], str(lineas[set]))
