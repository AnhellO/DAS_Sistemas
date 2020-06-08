from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase(
    'breakingbad',
    host = 'breakingbad_db',
    port = 3306,
    user = 'root',
    passwd = 'root'
)

class Characters(Model):
    char_id = IntegerField(primary_key=True)
    char_name = CharField()
    char_bd = CharField()
    char_oc = CharField()
    char_img = CharField()
    char_status = CharField()
    char_nickname = CharField()
    char_appearance = CharField()
    char_portrayed = CharField()
    char_category = CharField()
    char_bcs_a = CharField()

    class Meta:
        database = myDB
        db_table = 'characters'