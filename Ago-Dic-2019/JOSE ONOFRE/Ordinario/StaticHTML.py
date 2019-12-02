import peewee
import sqlite3
import Peewee
import PeeweeLocation
import PeeweeEpisode
import pprint
import ClaseCharacter
import ClaseLocation
import ClaseEpisode
## Generar HTMLS Estaticos para visualizar la informacion ##

def get_personajes():
    char = Peewee.CharacterP.select(Peewee.CharacterP.id,Peewee.CharacterP.name,Peewee.CharacterP.status,Peewee.CharacterP.species,Peewee.CharacterP.type,Peewee.CharacterP.gender,Peewee.CharacterP.origin_name,Peewee.CharacterP.origin_url,Peewee.CharacterP.location_name,Peewee.CharacterP.location_url,Peewee.CharacterP.image,Peewee.CharacterP.episode,Peewee.CharacterP.url,Peewee.CharacterP.created)
    lista = []

    for c in char:
        objetoper = ClaseCharacter.Personaje(c.id,c.name,c.status,c.species,c.type,c.gender,c.origin_name,c.origin_url,c.location_name,c.location_url,c.image,c.episode,c.url,c.created)
        lista.append(objetoper)
    
    return lista
    #print(lista[0])



##Crear HTML PERSONAJE
def CrearHTML():
    Ch = []
    Ch = get_personajes()
    for nini in range(0,len(Ch)):
        #print(nini)
        character = Ch[nini]
        content='''<p>Id: {}</p>
                    <p>Name: {}</p>
                    <p>Status: {}</p>
                    <p>Species: {}</p>
                    <p>Type: {}</p>
                    <p>Gender: {}</p>
                    <p>OriginName: {}</p>
                    <p>OriginUrl: {}</p>
                    <p>LocationName: {}</p>
                    <p>LocationUrl: {}</p>
                    <p>Image: {}</p>
                    <p>Episode: {}</p>
                    <p>Url: {}</p>
                    <p>Created: {}</p>
        '''.format(character._id, character._nameCh, character._statusCh, character._speciesCh, character._typeCh, character._genderCh, character._origin_nameCh, character._origin_urlCh, character._location_NameCh, character._location_UrlCh, character._imageCh, character._episodeCh, character._urlCh, character._createdCh)
        #print(character)
        fill = open('staticHtml/Characters/CharactersAccess/Personaje_{}.html'.format(nini+1),'w',encoding='utf-8') #Abrir archivo para ser escrito
        fill.write(content)
        fill.close()


##########################################################

##########################################################


def get_locations():
    loc = PeeweeLocation.LocationP.select(PeeweeLocation.LocationP,PeeweeLocation.LocationP.name,PeeweeLocation.LocationP.type,PeeweeLocation.LocationP.dimension,PeeweeLocation.LocationP.residents,PeeweeLocation.LocationP.url,PeeweeLocation.LocationP.created)
    listaL = []

    for l in loc:
        objetoloc = ClaseLocation.Locacion(l.id,l.name,l.type,l.dimension,l.residents,l.url,l.created)
        listaL.append(objetoloc)
        #print(listaL)
    return listaL
    #print(len(listaL))
    



##Crear HTML PERSONAJE
def CrearHTMLLocations():
    Liist = []
    Liist = get_locations()
    for nil in range(0,len(Liist)):
        #print(nini)
        location = Liist[nil]
        content='''<p>Id: {}</p>
                    <p>Name: {}</p>
                    <p>Type: {}</p>
                    <p>Dimension: {}</p>
                    <p>Residents: {}</p>
                    <p>Url: {}</p>
                    <p>Created: {}</p>
        '''.format(location._id, location._nameLoc, location._typeLoc, location._dimensionLoc, location._residentsLoc,location._urlLoc, location._createdLoc)
        #print(character)
        fill = open('staticHtml/Locations/LocationsAccess/Location_{}.html'.format(nil+1),'w',encoding='utf-8') #Abrir archivo para ser escrito
        fill.write(content)
        fill.close()
        print(len(Liist))


##########################################################

##########################################################


def get_episodes():
    ep = PeeweeEpisode.EpisodeP.select(PeeweeEpisode.EpisodeP.id,PeeweeEpisode.EpisodeP.name,PeeweeEpisode.EpisodeP.airdate,PeeweeEpisode.EpisodeP.episode,PeeweeEpisode.EpisodeP.characters,PeeweeEpisode.EpisodeP.url,PeeweeEpisode.EpisodeP.created)
    listaE = []

    for e in ep:
        objetoep = ClaseEpisode.Episodio(e.id,e.name,e.airdate,e.episode,e.characters,e.url,e.created)
        listaE.append(objetoep)
        #print(listaE)
    return listaE
    
    

##Crear HTML PERSONAJE
def CrearHTMLEpisodio():
    Liste = []
    Liste = get_episodes()
    for nile in range(0,len(Liste)):
        #print(nini)
        episode = Liste[nile]
        content='''<p>Id: {}</p>
                    <p>Name: {}</p>
                    <p>Airdate: {}</p>
                    <p>Episode: {}</p>
                    <p>Characters: {}</p>
                    <p>Url: {}</p>
                    <p>Created: {}</p>
        '''.format(episode._id, episode._nameEp, episode._airdateEp, episode._episodeEp, episode._charactersEp, episode._urlEp, episode._createdEp)
        #print(character)
        fill = open('staticHtml/Episodes/EpisodesAccess/Episode_{}.html'.format(nile+1),'w',encoding='utf-8') #Abrir archivo para ser escrito
        fill.write(content)
        fill.close()
        #print(len(Liste))

#get_episodes()
#get_locations()
#CrearHTMLLocations()
#CrearHTML()
CrearHTMLEpisodio()
#get_personajes()