from Peewee import *
#Creacion de la tabla Episode usando Peewee
class EpisodeP(BaseModel):
    id = TextField(unique=True)
    name = TextField()
    airdate = TextField()
    episode = TextField()
    characters = TextField()
    url = TextField()
    created = TextField()

#db.connect()
db.create_tables([EpisodeP])

#Insertar datos Episode
def InsertarEpisode(Episode): 
    EpisodeP.create( #Insertamos los datos usando metodo create() de peewee
        id = Episode._id,
        name = Episode._nameEp,
        airdate = Episode._airdateEp,
        episode = Episode._episodeEp,
        characters = Episode._charactersEp,
        url = Episode._urlEp,
        created = Episode._createdEp
    )
    
def MostrarEpisode():
    for episode in EpisodeP.select():
        print('\n----------Episodio----------\n')
        print('Id: {}\nName: {}\nAirDate: {}\nEpisode: {}\nCharacters: {}\nUrl: {}\nCreated: {}'.format(episode.id, episode.name, episode.airdate, episode.episode, episode.characters, episode.url, episode.created))