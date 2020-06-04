from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = PostgresqlDatabase(
    'pokedex',
    host='postgres',
    user='postgres',
    password='postgres'
)

class Pokemon(Model):
    nombre = CharField()
    tipos = CharField()
    imagen = CharField()

    class Meta:
        database = myDB