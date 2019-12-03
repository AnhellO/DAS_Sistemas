import requests
import pprint
import ramapi
from ramapi import *
import ClaseEpisode
import BDCharacter
#r = requests.get('https://rickandmortyapi.com/api/character/')

ramapi.Base.api_info()
ramapi.Base.schema()


for n in range(1,3):
    r = requests.get('https://rickandmortyapi.com/api/episode/?page={}'.format(n))
    #pprint.pprint(r.json())
    cosa = r.json()
    for episodio in cosa['results']:

        item = ClaseEpisode.Episodio(id = episodio['id'],name = episodio['name'],airdate = episodio['air_date'],episode = episodio['episode'], characters = episodio['characters'], url = episodio['url'], created = episodio['created'])
        print("-------------Inicio de Episodio--------------\n")
        #print(item)
        BDCharacter.insertarE(item)
        print("-------------Final de Episodio--------------\n")

BDCharacter.VisualizarEpisode()