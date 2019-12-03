import musicbrainzngs
import pprint
import artista
import disquillos
import DataBase

def obtener_artistas():
    musicbrainzngs.set_useragent('musicbrainzngs','2.0')

    results = musicbrainzngs.search_artists(area='Los Angeles',country="us",tag=['rock','metal'],limit=100)
    # q = musicbrainzngs.search_works(query='artist.name:Ozzy Osbourne',type='album')
    # q = musicbrainzngs.search_releases(artist='Ozzy Osbourne', country="us", limit=3)
    # pprint.pprint(q)
    # pprint.pprint(results)
    # i=0
    for artist in results['artist-list']:
        if 'type' in artist:
            tipo = artist['type']
        else:
            tipo = 'Group'
        bolillo = artista.artist(artist['id'],artist["name"],'atun',artist['area']['name'],artist['ext:score'],tipo)
        # print('-------------------------------')
        # print(bolillo)
        # print(i,'===',artist['id'], artist["name"], artist['area']['name'], artist['ext:score'],artist['type'])
        # i+=1
        DataBase.Agregar_Elemento_Artista(bolillo)

def obtener_discos():
    musicbrainzngs.set_useragent('musicbrainzngs','2.0')
    # results = musicbrainzngs.search_releases(artist='Ozzy Osbourne', country="us", limit=10)
    # pprint.pprint(results)
    # for artist in results['release-list']:
    #     print(artist['id'], artist['artist-credit'][0]['name'], artist['release-group']['title'], artist['status'], artist['release-group']['type'])

    listilla= DataBase.Ver_Nombres()
    for i in range(0,len(listilla)):
        results = musicbrainzngs.search_releases(artist=listilla[i], country="us", limit=5)
        
        for artist in results['release-list']:
            if 'status' in artist:
                status = artist['status']
            else:
                status = 'Unofficial'

            if 'type' in artist['release-group']:
                tipo = artist['release-group']['type']
            else:
                tipo = 'Other'
            
            panecito = disquillos.album(artist['id'], artist['artist-credit'][0]['name'], artist['release-group']['title'], status, tipo)
            DataBase.Agregar_Elemento_Album(panecito)
            # print(artist['id'], artist['artist-credit'][0]['name'], artist['release-group']['title'], status, tipo)
            # print('--------------------')
        

if __name__ == '__main__':
    DataBase.Crear_Tabla_Artistas()
    DataBase.Crear_Tabla_Albums()
    # obtener_artistas()
    DataBase.Ver_Todo_Artistas()
    # obtener_discos()
    # DataBase.Ver_Todo_Albums()
    # DataBase.borrar_tabla_albums()
    # DataBase.borrar_tabla_Artistas()