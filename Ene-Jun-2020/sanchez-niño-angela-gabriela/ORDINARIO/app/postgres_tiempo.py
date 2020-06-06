from peewee import *
from playhouse.shortcuts import model_to_dict
from playhouse.postgres_ext import PostgresqlExtDatabase
from time import perf_counter

db = PostgresqlExtDatabase(
    "dc_heroes",
    host = "0.0.0.0",
    user = "postgres",
    password = "postgres", 
    port = 5432
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
inicio = perf_counter()
data = SUPER_HEROE.select().where(SUPER_HEROE.id<100)
fin = perf_counter()
for i in data:
    print(i.name)

print(f"TIEMPO: {fin-inicio}")