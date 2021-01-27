from peewee import *

#psql_db = PostgresqlDatabase('playlist', user='postgres', host='localhost', password='pylast123')
psql_db = PostgresqlDatabase('playlist', user='postgres', host='pylastDB_A', password='pylast123')

class BaseModel(Model):
    class Meta:
       database = psql_db

class artist(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField()
    image = CharField()


class playlist(BaseModel):
    id =ForeignKeyField(artist, primary_key=True)

class track(BaseModel):
    id =ForeignKeyField(artist, primary_key=True)

class biography(BaseModel):
    id =ForeignKeyField(artist, primary_key=True)
    fullName = TextField(null=True)
    track = TextField(null=True)
    country = TextField(null=True)
