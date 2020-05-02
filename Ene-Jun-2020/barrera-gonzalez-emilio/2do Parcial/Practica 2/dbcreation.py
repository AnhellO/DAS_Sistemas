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

class Structures(Model):
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
        db_table = "Structures"

class Civilizations(Model):
    num = CharField(unique=True)
    name = CharField()
    army = CharField()
    expansion= CharField()

    class Meta:
        database = db
        db_table = "Civilizations"

if __name__=='__main__':
    #CONNECTING TO THE DATABASE
    try: #TRY statement, just in case there is an open connection
        db.connect()
        print("Successfully Connected")
    except:
        print("Already Connected")

    #CREATING TABLES
    Unit.create_table() 
    Structures.create_table()
    Civilizations.create_table()

    #DATA INSERTION
    ###Civilization
    civs=api.getCivilizations()
    for i in civs:
        try:
            Civilizations.create(num=i['num'],name=i['name'],army=i['army'],expansion=i['expansion'])
            print(f'row inserted in Civilizations')
        except:
            print(f"can't reuse key '{i['num']}' in 'Civilizations'")
    Civilizations.save()
    ###Units
    uts=api.getUnits()
    for i in uts:
        try:
            Unit.create(num=i['num'],name=i['name'],age=i['age'],wood=i['cost_wood'],gold=i['cost_gold'],food=i['cost_food'],stone=i['cost_stone'],hp=i['hp'],a_range=i['attack_range'],power=i['attack'],armor=i['armor'],accuracy=i['accuracy'])
            print('row inserted in unit')
        except:
            print(f"can't reuse key '{i['num']}' in 'Units'")
    Unit.save()
    ###Structures
    struc=api.getStructures()
    for i in struc:
        try:
            Structures.create(num=i['num'],name=i['name'],age=i['age'],wood=i['cost_wood'],gold=i['cost_gold'],food=i['cost_food'],stone=i['cost_stone'],hp=i['hp'],build_time=i['build_time'],armor=i['armor'])
            print('row inserted in structures')
        except:
            print(f"can't reuse key '{i['num']}' in 'Structures'")
    Structures.save()
    #CLOSING THE CONNECTION
    db.close()