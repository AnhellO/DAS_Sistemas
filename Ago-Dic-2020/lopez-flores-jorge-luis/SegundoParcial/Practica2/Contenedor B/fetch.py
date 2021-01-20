import requests
import pymongo

client = pymongo.MongoClient("mongodb://db:27017/")
db = client["mi-bd"]

usuarios = []

while len(usuarios) < 100:
	response = requests.get("https://pipl.ir/v1/getPerson")
	data = response.json()
	db.coll.insert_one(data)
	usuarios.append("i")

#db.coll.insert_many(usuarios)