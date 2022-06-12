import pymongo
import json
import requests
from requests.auth import HTTPBasicAuth

#Creando la conexion a la db y accediendo a la db
client = pymongo.MongoClient("mongodb://root:basedatos@Contenedor_B:27017/")
database = client["Issues"]

#Obtencion de datos
#Isuess open
response =requests.get(f"https://api.github.com/repos/pallets/flask/issues?state=open",auth=HTTPBasicAuth("alfonsoloopez","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"))
dataopen = response.json() # Get a Json

#Creando y poblando la coleccion de Issues open
id = 1
for dato in dataopen:
    dato['_id'] = id
    id +=1
    database.IsuessOpen.insert_one(dato)

#Issues Closed
idO = 1
for i in range(1,94):
    response =requests.get(f"https://api.github.com/repos/pallets/flask/issues?state=closed&page={i}",auth=HTTPBasicAuth("alfonsoloopez","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"))
    dataclosed = response.json() # Get a Json

    #Creando y poblando la coleccion de Isuess closed
    for dato in dataclosed:
        
        dato['_id'] = idO
        idO +=1
        database.IssuesClosed.insert_one(dato)

