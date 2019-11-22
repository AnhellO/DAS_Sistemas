import musicbrainzngs
import pprint
import sqlite3
import ClaseDisco
import BDMusic
musicbrainzngs.set_useragent('musicbrainzngs','2.0')

#r = musicbrainzngs.search_artists(query='area.name:Los Angeles',limit=5)

r = musicbrainzngs.search_releases(type = "group", country = 'US', tag=['rock','metal'],limit= 100)

for discos in r['release-list']:

    if 'status' in discos:
        stat = discos['status']
        
    else:
        stat = 'Unofficial'

    disc = ClaseDisco.Disc(id = discos['artist-credit'][0]['artist']['id'],name = discos['artist-credit'][0]['artist']['name'], country = discos['country'], date = discos['date'], status = stat)
    #pprint.pprint(discos['artist-credit'][0]['artist']['id'])
    #pprint.pprint(discos['artist-credit'][0]['artist']['name'])
    #pprint.pprint(discos['country'])
    #pprint.pprint(discos['date'])
    #pprint.pprint(discos['status'])
    print(disc)

#BDMusic.insertarD(disc)

BDMusic.VisualizarD

#pprint.pprint(r)



