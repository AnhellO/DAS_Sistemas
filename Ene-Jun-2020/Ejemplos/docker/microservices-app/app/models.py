from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
	'pokedex',
	host='pokepy_db',
	port=3306,
	user='root',
	passwd='root'
)

class Pokemon(Model):
    nombre = CharField()
    tipos = CharField()
    imagen = CharField()

    class Meta:
        database = myDB