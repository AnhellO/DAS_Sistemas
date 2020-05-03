from peewee import *
from aoiiapi import aoiiAPI
#DEFINING OUR DATABASE(in which we will put the data)
db = SqliteDatabase('AgeOfEmpiresII.db')
#DEFINING THE API (from which we will be pulling the data)
api = aoiiAPI()

#DEFINING THE MODELS FOR THE DATABASE
class Unit(Model):
    num = CharField(unique=True)
    name = CharField()
    wood = CharField()
    gold = CharField()
    food = CharField()
    stone = CharField()
    hp = CharField()
    a_range = CharField()
    power = CharField()
    armor = CharField()
    accuracy = CharField()

    class Meta:
        database = db
        db_table =  'Unit'

class Structure(Model):
    num = CharField(unique=True)
    name = CharField()
    wood = CharField()
    gold = CharField()
    food = CharField()
    stone = CharField()
    hp = CharField()
    build_time = CharField()
    armor = CharField()

    class Meta:
        database = db
        db_table = "Structure"

class Civilization(Model):
    num = CharField(unique=True)
    name = CharField()
    army = CharField()
    expansion= CharField()

    class Meta:
        database = db
        db_table = "Civilization"

class Technology(Model):
    num = CharField(unique=True)
    name = CharField()
    age = CharField()
    wood = CharField()
    food = CharField()
    gold = CharField()
    stone = CharField()
    build_time = CharField()
    class Meta:
        database = db
        db_table = "Technology"

if __name__=='__main__':
    #CONNECTING TO THE DATABASE
    try: #TRY statement, just in case there is an open connection
        db.connect()
        print("Successfully Connected")
    except:
        print("Already Connected")

    #CREATING TABLES
    Unit.create_table() 
    Structure.create_table()
    Civilization.create_table()
    Technology.create_table()

    #DATA INSERTION
    ###Civilization
    civs = api.getCivilizations()
    for i in civs:
        try:
            Civilization.create(num=i['num'],name=i['name'],army=i['army'],expansion=i['expansion'])
            print(f'row inserted in Civilization')
        except:
            print(f"can't reuse key '{i['num']}' in 'Civilization'")
    ###Units
    uts = api.getUnits()
    for i in uts:
        try:
            Unit.create(num=i['num'],name=i['name'],age=i['age'],wood=i['cost_wood'],gold=i['cost_gold'],food=i['cost_food'],stone=i['cost_stone'],hp=i['hp'],a_range=i['attack_range'],power=i['attack'],armor=i['armor'],accuracy=i['accuracy'])
            print('row inserted in Unit')
        except:
            print(f"can't reuse key '{i['num']}' in 'Units'")
    ###Structures
    struc = api.getStructures()
    for i in struc:
        try:
            Structure.create(num=i['num'],name=i['name'],age=i['age'],wood=i['cost_wood'],gold=i['cost_gold'],food=i['cost_food'],stone=i['cost_stone'],hp=i['hp'],build_time=i['build_time'],armor=i['armor'])
            print('row inserted in structure')
        except:
            print(f"can't reuse key '{i['num']}' in 'Structure'")
    ###Tech
    tech = api.getTech()
    for i in tech:
        try:
            Technology.create(num=i['num'],name=i['name'],age=i['age'],wood=i['wood'],food=i['food'],gold=i['gold'],stone=i['stone'],build_time=i['build_time'])
            print('row inserted in Technology')
        except:
            print(f"can't reuse key '{i['num']}' in 'Technology'")

    #CLOSING THE CONNECTION
    db.close()