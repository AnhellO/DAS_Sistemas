import requests
from peewee import *

db = SqliteDatabase('AoEII.db')


# ********************************************************
# Creamos Modelos
# ********************************************************

class civilization(Model):
    id = CharField(primary_key=True)
    name = CharField()
    expansion = CharField()
    army_type = CharField()

    class Meta:
        database = db
        db_table = 'civilization'


class structure(Model):
    id = CharField(primary_key=True)
    name = CharField()
    age = CharField()
    build_time = CharField()
    armor = CharField()

    class Meta:
        database = db
        db_table = 'structure'


class unit(Model):
    id = CharField(primary_key=True)
    name = CharField()
    age = CharField()
    expansion = CharField()
    attack = CharField()
    armor = CharField()

    class Meta:
        database = db
        db_table = 'unit'


class technology(Model):
    id = CharField(primary_key=True)
    name = CharField()
    expansion = CharField()
    age = CharField()
    build_time = CharField()

    class Meta:
        database = db
        db_table = 'technology'


# conexion a la base de datos
db.connect()
# print("Conectado! :v")

# ********************************************************
# Obtenemos info de la API
# ********************************************************

def getCivilizations():
    data_civ = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations').json()

    for civ in data_civ['civilizations']:

        id = civ['id']
        name = civ['name']
        expansion = civ['expansion']
        army_type = civ['army_type']

        civilization.insert(id=id, name=name, expansion=expansion, army_type=army_type).execute()


def getUnits():
    data_units = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units').json()
    for uni in data_units['units']:
        id = uni['id']
        name = uni['name']
        age = uni['age']
        expansion = uni['expansion']
        try:
            attack = uni['attack']
        except:
            attack = '-'
        armor = uni['armor']

        unit.insert(id=id, name=name, age=age, expansion=expansion, attack=attack, armor=armor).execute()


def getStructures():
    data_struct = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/structures').json()

    for struct in data_struct['structures']:

        id = struct['id']
        name = struct['name']
        age = struct['age']
        build_time = struct['build_time']
        armor = struct['armor']

        structure.insert(id=id, name=name, age=age, build_time=build_time, armor=armor).execute()


def getTechnologies():
    data_techs = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/technologies').json()
    for techs in data_techs['technologies']:
        id = techs['id']
        name = techs['name']
        expansion = techs['expansion']
        age = techs['age']
        build_time = techs['build_time']

        technology.insert(id=id, name=name, expansion=expansion, age=age, build_time=build_time).execute()


# ********************************************************
# Creamos Tablas
# ********************************************************
# print('Creando tablas...')

civilization.create_table()
unit.create_table()
structure.create_table()
technology.create_table()

# ********************************************************
# Inserta registros en la BD
# ********************************************************
# print('Insertando información a la BD...')

if __name__ == '__main__':
    getCivilizations()
    getUnits()
    getStructures()
    getTechnologies()

# print('Listo!')
