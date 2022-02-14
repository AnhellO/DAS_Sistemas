""" 8-7. Album: Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an artist name and an 
album title, and it should return a dictionary containing these two pieces of 
information. Use the function to make three dictionaries representing different 
albums. Print each return value to show that the dictionaries are storing the 
album information correctly.
Add an optional parameter to make_album() that allows you to store the number
of tracks on an album. If the calling line includes a value for the number of
tracks, add that value to the album's dictionary. Make at least one new function
call that includes the number of tracks on an album. """


def make_album(artist_name, album_title, tracks=0):
    album = {"artist": artist_name.title(), "album_name": album_title}
    if tracks:
        album["tracks"] = tracks

    return album


album_dict = make_album("Imagine Dragons", "Origins")
print(album_dict)
# {'artist': 'Imagine Dragons', 'album_name': 'Origins'}

album_dict = make_album("The Weeknd", "Starboy", 18)
print(album_dict)
# {'artist': 'The Weeknd', 'album_name': 'Starboy', 'tracks': 18}

album_dict = make_album(artist_name="Bad Bunny",
                        album_title="YHLQMDLG", tracks=20)
print(album_dict)
# {'artist': 'Bad Bunny', 'album_name': 'YHLQMDLG', 'tracks': 20}
