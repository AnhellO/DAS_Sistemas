from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
    'Characters',
    host='BreakBad_db',
    port=3306,
    user='root',
    passwd='root'
)


class Characters(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    birthday = CharField()
    occupation = CharField()
    img = CharField()
    status = CharField()
    nickname = CharField()
    appearance = CharField()
    portrayed = CharField()
    category = CharField()

    class Meta:
        database = myDB
        db_table = 'Personajes'
