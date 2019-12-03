import musicbrainzngs
import pprint
import ClaseArtista
import BDMusic
musicbrainzngs.set_useragent('musicbrainzngs','2.0')

r = musicbrainzngs.search_artists(area="Los Angeles", type = "group", country="United States",limit= 50, tag = ['rock','metal'])



for artist in r['artist-list']:

    if 'isni-list' in artist:
        isn = artist['isni-list']
        
    else:
        isn = ['00000000']
        
    
    if 'begin' in artist['life-span']:
        beg = artist['life-span']['begin']
    else:
        beg = 'Unknown'

    item = ClaseArtista.Artista(id = artist['id'],name = artist['name'],area = artist['area']['name'],extscore = artist['ext:score'],ilist = isn,begin = beg)
    #print("id: {}\nname: {}\narea: {}\next:score {}\nisni-list: {}\nbegin: {}".format(artist['id'], artist['name'], artist['area']['name'], artist['ext:score'], isn, beg))
    #print(item._islist)
    #BDMusic.insertar(item)

    
BDMusic.Visualizar()



#pprint.pprint(r)