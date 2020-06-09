from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
	'personajes',
	host='serie_db',
	port=3306,
	user='root',
	passwd='root'
)

class Personaje(Model):
    name= CharField()
    fechanac = CharField()
    imagen = CharField()
    occupation = CharField()
    status = CharField()
    nickname = CharField()
    apparence = CharField()
    actor = CharField()
    category = CharField()

    class Meta:
        database = myDB