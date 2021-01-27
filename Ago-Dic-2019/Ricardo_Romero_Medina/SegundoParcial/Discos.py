import musicbrainzngs
import pprint
import basedatos
import ClaseDiscos

def buscar_discos():
    musicbrainzngs.set_useragent('musicbrainzngs','2.0')

    lista=basedatos.Ver_Artista()

    #print(lista)

    for i in range(0,len(lista)):
        req = musicbrainzngs.search_releases(artist=lista[i],country='US',limit=5)
        #pprint.pprint(req)
        for disco in req['release-list']:
            if 'status' in disco:
                status = disco['status']
            else:
                status = 'No Official'
            if 'country' in disco:
                country = disco['country']
            else:
                country = 'US'
            disco = ClaseDiscos.discos(disco['id'],disco['artist-credit'][0]['name'],disco['release-group']['title'],country,status)
            #print(disco)
            basedatos.agregar_discos(disco)


if __name__ == '__main__':
    #basedatos.crear_base_datos()
    #basedatos.crear_tabala_discos()
    #buscar_discos()
    basedatos.Ver_Todos_Discos()