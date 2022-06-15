def make_album(artist_name, album_title):
    album = {'Artist name' : artist_name, 'Album title' : album_title}
    return album

while True:

    print("(Enter ':q' at any time to quit)")

    artist = input("Name of the artist : ")
    if artist == ':q':
        break
    album = input("Name of the artist : ")
    if album == ':q':
        break

    print(make_album(artist, album))