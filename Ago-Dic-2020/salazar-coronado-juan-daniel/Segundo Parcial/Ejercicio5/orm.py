from peewee import *

db = PostgresqlDatabase(
    'postgres',
    user='daniel',
    password='dm16',
    host='localhost',
    port=5432
)

class Description(Model):
	id = CharField()
	index = IntegerField()
	guid = CharField()
	isactive = BooleanField()
	balance = CharField()
	picture = CharField()
	age = IntegerField()
	eyeColor = CharField()
	name = ArrayField()

	class Meta:
		database = db
		table_name = 'person_description'

class Information(Model):
	company = CharField()
	email = CharField()
	phone = CharField()
	address = CharField()
	about = TextField()
	registered = CharField()
	latitude= CharField()
	longitude = CharField()
	tags = ArrayField()

	class Meta:
		database = db
		table_name = 'person_information'

class InformationExtra(Model):
	range = ArrayField()
	friends = ArrayField()
	greeting = CharField()
	favoritefruit = CharField()

	class Meta:
		database = db
		table_name = 'person_informationextra'

db.connect()
db.create_tables([Description, Information, InformationExtra])
db.close()