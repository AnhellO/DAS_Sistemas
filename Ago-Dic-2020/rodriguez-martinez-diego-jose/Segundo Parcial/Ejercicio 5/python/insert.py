import json
from peewee import *

from models import CEOs, Companies, db

with open('data.json') as f:
  data = json.load(f)

for i in data:
    CEO_data = {
            "index": i["index"],
            "nombre": i["name"]["first"],
            "age": i["age"],
            "picture": i["picture"]
        }

    company_data = {
                "nombre": i["company"],
                "email": i["email"],
                "phone": i["phone"],
                "about": i["about"],
                "direccion": i["address"],
                "registered": i["registered"],
                "latitude": i["latitude"], 
            "longitude": i["longitude"] 
            }
    
    CEO = CEOs.create(**CEO_data)
    company = Companies.create(**company_data)

    CEO.save()
    company.save()

