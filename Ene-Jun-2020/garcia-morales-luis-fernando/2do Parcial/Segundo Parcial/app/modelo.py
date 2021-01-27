from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
	'BreakingDb',
	host='breaking_db',
	port=3306,
	user='root',
	passwd='root'
)

class PERSONAJES(Model):
    nombre = CharField()
    fechaNac = CharField()
    ocupacion = CharField()
    imagen = CharField()
    estado = CharField()
    nickname = CharField()
    apariciones = CharField()
    actor = CharField()
    categoria = CharField()

    class Meta:
        database = myDB