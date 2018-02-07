def make_album(artist, title, tracks=0):
    album_dict = {
        'artista': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = "\nCual album es? "
artist_prompt = "Quien es el artista? "

print("Ingresar salir en cualquier momento para detener")

while True:
    title = input(title_prompt)
    if title == 'salir':
        break
    
    artist = input(artist_prompt)
    if artist == 'salir':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks!")

