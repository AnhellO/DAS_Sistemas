
from peewee import *
import requests

db = SqliteDatabase('ageofempires.db')

#creación de modelos
class civilization(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    expansion = CharField()
    army_type = CharField()
    team_bonus = CharField()

    class Meta:
        database = db
        db_table = 'civilization'

class structure(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    expansion = CharField()
    age = CharField()
    cost = IntegerField()

    class Meta:
        database = db
        db_table = 'structure'

class unit(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    description =  CharField()
    expansion = CharField()
    age = CharField()

    class Meta:
        database = db
        db_table = 'units'

class technology(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    description = CharField()
    expansion = CharField()
    age = CharField()
    cost = CharField()

    class Meta:
        database = db
        db_table = 'technology'

#conexion a la base de datos
db.connect()

def get_civs():
    civs = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations').json()
    for civ in civs['civilizations']:
        id = civ['id']
        name = civ['name']
        expansion = civ['expansion']
        army_type = civ['army_type']
        team_bonus = civ['team_bonus']

        civilization.insert(id=id,
                            name=name,
                            expansion=expansion,
                            army_type=army_type,
                            team_bonus=team_bonus).execute()

def get_structs():
    structs = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/structures').json()
    for struc in structs['structures']:
        id = struc['id']
        name = struc['name']
        expansion = struc['expansion']
        age = struc['age']
        cost = struc['cost']
        structure.insert(
            id=id,
            name=name,
            expansion=expansion,
            age=age,
            cost=cost
        ).execute()


def get_units():
    units = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units').json()
    for uni in units['units']:
        id = uni['id']
        name = uni['name']
        description = uni['description']
        expansion = uni['expansion']
        age = uni['age']

        unit.insert(
            id=id,
            name=name,
            description=description,
            expansion=expansion,
            age=age).execute()

def get_techs():
    techs = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/technologies').json()
    for tech in techs['technologies']:
        id = tech['id']
        name = tech['name']
        description = tech['description']
        expansion = tech['expansion']
        age = tech['age']
        dic_cost = tech['cost']

        #Obtiene diccionarios de los costos
        for k,v in dic_cost.items():
            cost = f'{k}:{v}'
        technology.insert(
            id=id,
            name=name,
            description=description,
            expansion=expansion,
            age=age,
            cost=cost
        ).execute()

#inserta registros en las entidades de la BD

if __name__ == '__main__':
    get_civs()
    get_structs()
    get_units()
    get_techs()