
from dis import dis


def make_album(artist_name, album, number_of_tracks=""):
    disc = {'artist': artist_name, 'album': album}
    if number_of_tracks:
        disc['tracks'] = number_of_tracks
    return disc

album = make_album('Santiago Benavides', 'Modo de Vida')
print(album)
album = make_album('System of a Down', 'toxicity')
print(album)
album = make_album('Jose Luis Perales', 'Como es el')
print(album)
album = make_album('cricri', 'la fuente', '12')
print(album)