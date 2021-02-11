from peewee import *
import time
import json

# Connection.
pg_db = PostgresqlDatabase('postgres_db', user='postgres', password='sudovon', host='postgres', port=5432)

# Metaclass.
class BaseModel(Model):
    class Meta:
        database = pg_db

# Table.
class People(BaseModel):
    first_name = TextField()
    last_name = TextField()
    guid = TextField()
    balance = TextField()
    greeting = TextField()
    eye_color = TextField()
    address = TextField()
    about = TextField()
    registered = TextField()
    company = TextField()

#   If the db isn't up then will try to connect again.
while True:
    try:
        pg_db.connect()
    except Exception:
        time.sleep(1)
        continue
    break

# Create table.
pg_db.create_tables([People])
# Iterate through the json and create a new instance of people that will be pushed to the array.
people_data = []
with open("data.json") as data_file:
    data = json.load(data_file)
    for person_data in data:
        person = People()
        person.first_name = person_data["name"]["first"]
        person.last_name = person_data["name"]["last"]
        person.guid = person_data["guid"]
        person.balance = person_data["balance"]
        person.greeting = person_data["greeting"]
        person.eye_color = person_data["eyeColor"]
        person.address = person_data["address"]
        person.about = person_data["about"]
        person.registered = person_data["registered"]
        person.company = person_data["company"]
        people_data.append(person)
    data_file.close()

# Iterate through the array and store each person in the people table.
for person in people_data:
	person.save()