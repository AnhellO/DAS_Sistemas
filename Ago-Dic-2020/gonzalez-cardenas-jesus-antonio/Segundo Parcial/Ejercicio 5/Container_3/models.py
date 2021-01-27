from peewee import Model, CharField, IntegerField
from db import db

class MyPerson(Model):
    person_id = CharField(primary_key=True)
    balance = CharField()
    age = IntegerField()
    name = CharField()
    company = CharField()
    phone = CharField()
    email = CharField()
    address = CharField()
    about = CharField()
    registered = CharField()

    class Meta:
        database = db
        table_name = 'persons'
