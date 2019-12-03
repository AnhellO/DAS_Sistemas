import musicbrainzngs
import pprint
import bandas
import basedatos

def buscar_bandas():
    musicbrainzngs.set_useragent('musicbrainzngs','2.0')

    req = musicbrainzngs.search_artists(area='Los Angeles', tag=['Rock','Metal'], country='US',limit=100)

    for artista in req['artist-list']:
        if 'type' in artista:
            tipo = artista['type']
        else:
            tipo='Group'
        banda = bandas.bandas(artista['id'],artista['name'],tipo,'banda',artista['area']['name'])
        #print('------------------------------')
        #print(banda)
        basedatos.agregar_artista(banda)


if __name__ == '__main__':
    #basedatos.crear_base_datos()
    #basedatos.crear_tabala_artistas()
    #buscar_bandas()
    basedatos.Ver_Todos_Artistas()
    
    