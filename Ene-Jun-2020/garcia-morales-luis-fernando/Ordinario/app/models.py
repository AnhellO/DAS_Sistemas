from peewee import *
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(
    "dc_heroes",
    host = "dc_db",
    user = "postgres",
    password = "postgres", 
    )

class SUPER_HEROE(Model):
    id = IntegerField()
    name = TextField()
    full_name = TextField()
    alter_egos = TextField()
    aliases = TextField()
    place_of_birth = TextField()
    first_appearance = TextField()
    publisher = TextField()
    alignment = TextField()
    gender = TextField()
    race = TextField()
    height = TextField()
    weight = TextField()
    eye_color = TextField()
    hair_color = TextField()
    occupation = TextField()
    base = TextField()
    group_affiliation = TextField()
    relatives = TextField()
    image = TextField ()

    class Meta:
        database = db
        db_table = "SUPER_HEROE"

class SUPERHEROES_STATS(Model):
    id =IntegerField()
    intelligence = CharField()
    strength = CharField()
    speed = CharField()
    durability = CharField()
    power = CharField()
    combat = CharField()

    class Meta:
        database = db
        db_table = "SUPERHEROES_STATS" 


