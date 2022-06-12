import json
import pymongo
import requests
from requests.auth import HTTPBasicAuth

#Creando la conexion a la db y accediendo a la db
client = pymongo.MongoClient("mongodb://root:examen123@BaseDeDatos:27017/")
database = client["Issues"]

#Obtencion de datos
#Isuess open
response =requests.get(f"https://api.github.com/repos/pallets/flask/issues?state=open",auth=HTTPBasicAuth("midoryduarte","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"))
dataopen = response.json() # Get a Json

#Creando y poblando la coleccion de Issues open
id = 1
for dato in dataopen:
    dato['_id'] = id
    id +=1
    database.Open.insert_one(dato)

#Issues Closed
for i in range(1,94):
    response =requests.get(f"https://api.github.com/repos/pallets/flask/issues?state=closed&page={i}",auth=HTTPBasicAuth("midoryduarte","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"))
    dataclosed = response.json() # Get a Json

    #Creando y poblando la coleccion de Isuess closed
    for dato in dataclosed:
        
        dato['_id'] = id
        id +=1
        database.Closed.insert_one(dato)
