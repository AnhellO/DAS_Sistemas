import json
import pymongo
import requests
from requests.auth import HTTPBasicAuth

client = pymongo.MongoClient("mongodb://root:Parc@BaseDeDatos:27017/")
database = client["Issues"]
id = 1
for dato in dataopen:
    dato['_id'] = id
    id +=1
    database.Open.insert_one(dato)

    for dato in dataclosed:

        dato['_id'] = id
        id +=1
        database.Closed.insert_one(dato)
