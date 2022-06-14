
def make_album(artist_name, album, number_of_tracks=""):
    disc = {'artist': artist_name, 'album': album}
    if number_of_tracks:
        disc['tracks'] = number_of_tracks
    return disc

while True:
    print("please write the artist name: ")
    print("(enter '.' at any time to quit)")


    artist_name_input = input("artist name: "+"\n")
    if artist_name_input == ".":
        break
    album_input = input("album: ")
    if album_input == ".":
        break
    number_of_tracks_input = input("tracks: ")
    if number_of_tracks_input == ".":
        break

    disc = make_album(artist_name_input, album_input, number_of_tracks_input)
    print(disc)
