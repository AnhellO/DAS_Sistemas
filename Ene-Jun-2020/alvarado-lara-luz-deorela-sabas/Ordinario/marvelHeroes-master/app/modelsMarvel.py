from peewee import *
from playhouse.shortcuts import model_to_dict

#psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='localhost', password='marvel123')
psql_db = PostgresqlDatabase('marvelHeroes', user='postgres', host='marvelDB_A', password='marvel123')

class BaseModel(Model):
    class Meta:
       database = psql_db

class heroes(BaseModel):
    id = PrimaryKeyField(null=False)  
    name = CharField()
    image = CharField()


class powerstats(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    combat = CharField(null=True, max_length=10)
    durability = CharField(null=True, max_length=10)
    intelligence = CharField(null=True, max_length=10)
    power = CharField(null=True, max_length=10)
    speed = CharField(null=True, max_length=10)
    strength = CharField(null=True, max_length=10)

class work(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    base =  TextField(null=True)
    occupation = TextField(null=True)

class connections(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    groupAffiliation = TextField(null=True)
    relatives = TextField(null=True)

class biography(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    aliases = TextField(null=True)
    alignment = TextField(null=True)
    alterEgos = TextField(null=True)
    firstAppearance = TextField(null=True)
    fullName = TextField(null=True)
    placeOfBirth = TextField(null=True)
    publisher = TextField(null=True)

class appearance(BaseModel):
    id =ForeignKeyField(heroes, primary_key=True)
    eyeColor = CharField(null=True)
    gender = CharField(null=True)
    hairColor = CharField(null=True)
    height = CharField(null=True)
    race = CharField(null=True)
    weight = CharField(null=True)

