def make_album(artista, titulo, tracks=0):
    #8.7
    album_dict = {
        'artista': artista.title(),
        'titulo': titulo.title(),
        }
    if tracks:
        album_dict['canciones'] = tracks
    return album_dict

album = make_album('Justin Bieber', 'Changes')
print(album)

album = make_album('The goo goo dolls', 'A boy name goo')
print(album)

album = make_album('Siddhartha', 'unicos')
print(album)

album = make_album('Keane', 'Bedshaped', tracks=10)
print(album)