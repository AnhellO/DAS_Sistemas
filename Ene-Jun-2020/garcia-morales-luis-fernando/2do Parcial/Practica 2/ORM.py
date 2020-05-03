from peewee import *
import requests
db = SqliteDatabase('AOE2.db')

class CIVILIZACIONES(Model):
    nombre = CharField()
    expansion = CharField()
    tipo = CharField()
    
    class Meta:
        database = db

class UNIDADES(Model):
    nombre = CharField()
    descripcion = CharField()
    expansion = CharField()
    edad = CharField()
    rango = IntegerField()
    ataque = IntegerField()

    class Meta:
        database = db

class ESTRUCTURAS(Model):
    nombre = CharField()
    expansion = CharField()
    edad = CharField()
    tiempo = FloatField()

    class Meta:
        database = db

class TECNOLOGIAS(Model):
    nombre = CharField()
    descripcion =CharField()
    expansion = CharField()
    edad = CharField()

    class Meta:
        database = db