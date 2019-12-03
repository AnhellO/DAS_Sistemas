import peewee
import sqlite3
import Peewee
import PeeweeLocation
import PeeweeEpisode
import pprint
import ClaseCharacter
import ClaseLocation
import ClaseEpisode


def get_personajes():
    char = Peewee.CharacterP.select(Peewee.CharacterP.id,Peewee.CharacterP.name,Peewee.CharacterP.status,Peewee.CharacterP.species,Peewee.CharacterP.type,Peewee.CharacterP.gender,Peewee.CharacterP.origin_name,Peewee.CharacterP.origin_url,Peewee.CharacterP.location_name,Peewee.CharacterP.location_url,Peewee.CharacterP.image,Peewee.CharacterP.episode,Peewee.CharacterP.url,Peewee.CharacterP.created)
    lista = []

    for c in char:
        objetoper = ClaseCharacter.Personaje(c.id,c.name,c.status,c.species,c.type,c.gender,c.origin_name,c.origin_url,c.location_name,c.location_url,c.image,c.episode,c.url,c.created)
        lista.append(objetoper)
    
    return lista

##Crear HTML PERSONAJE
def CrearHTMLIndex():
    Ch = []
    Ch = get_personajes()
    v = ''
    for nini in range(0,len(Ch)):
        #print(nini)
        character = Ch[nini]
        content='''<p>Id: {}</p>
                    <p>Name: <a href='file:///C:/Users/Eduardo-PC/Desktop/OrdinarioDAS/staticHtml/Characters/CharactersAccess/Personaje_{}.html'>{}</a></p>
        '''.format(character._id,nini+1, character._nameCh)
        v += content
        #print(character)
    fill = open('staticHtml/Characters/Personajes.html','w',encoding='utf-8') #Abrir archivo para ser escrito
    fill.write(v)
    fill.close()

############################################




def get_locations():
    loc = PeeweeLocation.LocationP.select(PeeweeLocation.LocationP,PeeweeLocation.LocationP.name,PeeweeLocation.LocationP.type,PeeweeLocation.LocationP.dimension,PeeweeLocation.LocationP.residents,PeeweeLocation.LocationP.url,PeeweeLocation.LocationP.created)
    listaL = []

    for l in loc:
        objetoloc = ClaseLocation.Locacion(l.id,l.name,l.type,l.dimension,l.residents,l.url,l.created)
        listaL.append(objetoloc)
        #print(listaL)
    return listaL
    #print(len(listaL))
    

##Crear HTML Locations
def CrearHTMLIndexLocation():
    Liist = []
    Liist = get_locations()
    v = ''
    for nil in range(0,len(Liist)):
        #print(nini)
        location = Liist[nil]
        content='''<p>Id: {}</p>
                    <p>Name: <a href="file:///C:/Users/Eduardo-PC/Desktop/OrdinarioDAS/staticHtml/Locations/LocationsAccess/Location_{}.html">{}</a></p>
        '''.format(location._id,nil+1, location._nameLoc)
        #print(character)
        v+=content
    fill = open('staticHtml/Locations/Locations.html','w',encoding='utf-8') #Abrir archivo para ser escrito
    fill.write(v)
    fill.close()
        #print(len(Liist))



##########################################################


def get_episodes():
    ep = PeeweeEpisode.EpisodeP.select(PeeweeEpisode.EpisodeP.id,PeeweeEpisode.EpisodeP.name,PeeweeEpisode.EpisodeP.airdate,PeeweeEpisode.EpisodeP.episode,PeeweeEpisode.EpisodeP.characters,PeeweeEpisode.EpisodeP.url,PeeweeEpisode.EpisodeP.created)
    listaE = []

    for e in ep:
        objetoep = ClaseEpisode.Episodio(e.id,e.name,e.airdate,e.episode,e.characters,e.url,e.created)
        listaE.append(objetoep)
        #print(listaE)
    return listaE
    
    

##Crear HTML Episode
def CrearHTMLEpisodioIndex():
    Liste = []
    Liste = get_episodes()
    v = ''
    for nile in range(0,len(Liste)):
        #print(nini)
        episode = Liste[nile]
        content='''<p>Id: {}</p>
                    <p>Name: <a href="file:///C:/Users/Eduardo-PC/Desktop/OrdinarioDAS/staticHtml/Episodes/EpisodesAccess/Episode_{}.html">{}</a></p>
        '''.format(episode._id,nile+1, episode._nameEp)
        v += content
        #print(character)
    fill = open('staticHtml/Episodes/Episodes.html','w',encoding='utf-8') #Abrir archivo para ser escrito
    fill.write(v)
    fill.close()

#CrearHTMLIndex()
#CrearHTMLIndexLocation()
CrearHTMLEpisodioIndex()