import musicbrainzngs
import pprint
import BD
import DiscosObj
import ObjetoArtista




def getArt():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')

    results = musicbrainzngs.search_artists(area='Los Angeles', country="us", tag=['rock', 'metal'], limit=100)
    for Art in results['artist-list']:
        if 'type' in Art:
            Type = Art['type']
        else:
            Type = 'Group'
        Art1 = Art.Artista(Art['id'], Art["name"], 'Lost', Art['area']['name'], Art['ext:score'],
                                 Type)

        BD.InsertArt(Art1)

def getDiscos():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')

    list = BD.showNames()
    for i in range(0, len(list)):
        results = musicbrainzngs.search_releases(artist=list[i], country="us", limit=5)

        for Art in results['release-list']:
            if 'Status' in Art:
                Status = Art['Status']
            else:
                Status = 'Official'

            if 'Type' in Art['release-group']:
                Type = Art['release-group']['type']
            else:
                Type = 'Other'

            Disco1 = DiscosObj.Discos(Art['id'], Art['artist-credit'][0]['name'],
                                        Art['release-group']['title'], Status, Type)
            BD.Add(Disco1)


if __name__ == '__main__':
    BD.Artistas()
    BD.Discos()
    BD.ShowAllArt()
