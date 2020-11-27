import peewee
import time
import json

db = peewee.PostgresqlDatabase(
	"users",
	user="postgres",
	host="postgres",
	port=5432
)

class Person(peewee.Model):
	first_name = peewee.CharField()
	last_name = peewee.CharField()
	balance = peewee.CharField()
	age = peewee.IntegerField()
	eye_color = peewee.CharField()
	company = peewee.CharField()
	email = peewee.CharField()
	phone = peewee.CharField()
	address = peewee.CharField()
	registered = peewee.CharField()

	class Meta:
		database = db

# read json file
persons = []
with open("data.json") as json_file:
	data = json.load(json_file)

	for k in data:
		p = Person()
		p.first_name = k["name"]["first"]
		p.last_name = k["name"]["last"]
		p.balance = k["balance"]
		p.age = k["age"]
		p.eye_color = k["eyeColor"]
		p.company = k["company"]
		p.email = k["email"]
		p.phone = k["phone"]
		p.address = k["address"]
		p.registered = k["registered"]

		persons.append(p)
	
	json_file.close()

# try to connect to DB
while True:
	try:
		db.connect()
	except Exception:
		time.sleep(1)
		continue

	break

db.create_tables([Person])

# save all
for p in persons:
	p.save()