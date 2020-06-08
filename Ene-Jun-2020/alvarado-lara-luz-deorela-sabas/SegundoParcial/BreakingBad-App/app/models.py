from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
    'characters',
    port = 3306,
    user = 'root',
    passwd = 'root'
)

class Character(Model):
    usr_id = CharField()
    usr_nombre = CharField()
    usr_birthday = CharField()
    usr_occupation = CharField()
    usr_img = CharField()
    usr_status = CharField()
    usr_nickname = CharField()
    usr_portrayed = CharField()
    usr_category = CharField

    class Meta:
        database = myDB
