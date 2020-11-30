from peewee import Model, CharField, IntegerField
from db import db

class CEOs(Model):
    idceos = CharField()
    index = CharField()
    nombre = CharField()
    age = CharField()
    picture = CharField()

    class Meta:
	    database = db
	    table_name = 'ceos'

class Companies(Model):
    idceos = CharField()
    nombre = CharField()
    email = CharField()
    phone = CharField()
    about = CharField()
    direccion = CharField()
    registered = CharField()
    latitude = CharField()
    longitude = CharField()

    class Meta:
	    database = db
	    table_name = 'companies'