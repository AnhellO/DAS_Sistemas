from peewee import *
import Peewee
import sqlite3
import ClaseCharacter
import pprint
db = SqliteDatabase('Base.db')
#Creando la tabla Character usando Peewee
class BaseModel(Model):
    class Meta:
        database = db


class CharacterP(BaseModel):
    id = TextField(unique=True)
    name = TextField()
    status = TextField()
    species = TextField()
    type = TextField()
    gender = TextField()
    origin_name = TextField()
    origin_url = TextField()
    location_name = TextField()
    location_url = TextField()
    image = TextField()
    episode = TextField()
    url = TextField()
    created = TextField()
    
db.connect()
#db.create_tables([CharacterP])

#Insertar datos Character
def InsertarCharacter(Personaje):
    CharacterP.create(
        id = Personaje._id,
        name = Personaje._nameCh,
        status = Personaje._statusCh,
        species = Personaje._speciesCh,
        type = Personaje._typeCh,
        gender = Personaje._genderCh,
        origin_name = Personaje._origin_nameCh,
        origin_url = Personaje._origin_urlCh,
        location_name = Personaje._location_NameCh,
        location_url = Personaje._location_UrlCh,
        image = Personaje._imageCh,
        episode = Personaje._episodeCh,
        url = Personaje._urlCh,
        created = Personaje._createdCh
    )
    
def MostrarCharacter():
    for character in CharacterP.select():
        print('\n----------Personaje----------\n')
        print('Id: {}\nName: {}\nStatus: {}\nSpecies: {}\nType: {}\nGender: {}\nOriginName: {}\nOriginUrl: {}\nLocationName: {}\nLocationUrl: {}\nImage: {}\nEpisode: {}\nUrl: {}\nCreated: {}'.format(character.id, character.name, character.status, character.species, character.type, character.gender, character.origin_name, character.origin_url, character.location_name, character.location_url, character.image, character.episode, character.url, character.created))
        


####################################

