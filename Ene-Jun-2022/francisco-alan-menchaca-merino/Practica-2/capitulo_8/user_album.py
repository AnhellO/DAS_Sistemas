""" 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album's artist and title. Once you have that 
information, call make_album() with the user's input and print the dictionary 
that's created. Be sure to include a quit value in the while loop. """


def make_album(artist_name, album_title, tracks=0):
    album = {"artist": artist_name.title(), "album_name": album_title}
    if tracks:
        album["tracks"] = tracks

    return album


while True:
    print("\nPlease enter the album data")
    print("(Enter 'q' at any time to quit)\n")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    album_title = input("Album name: ")
    if album_title == 'q':
        break

    album_dict = make_album(artist, album_title)
    print(album_dict)

# Please enter the album data
# (Enter 'q' at any time to quit)

# Artist name: Bad Bunny
# Album name: YHLQMDLG
# {'artist': 'Bad Bunny', 'album_name': 'YHLQMDLG'}

# Please enter the album data
# (Enter 'q' at any time to quit)

# Artist name: q
