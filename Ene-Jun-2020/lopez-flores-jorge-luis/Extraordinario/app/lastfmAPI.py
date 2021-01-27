import os
import sys

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "3438d479a2065875b8f422a8bbf50cf2"  # this is a sample key
API_SECRET = "d95841d5489c8646213335aec1fd4bc8"

# In order to perform a write operation you need to authenticate yourself
username = "jorgelof"
password_hash = pylast.md5("chatolds12!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# Now you can use that object everywhere
artist = network.get_top_artists(limit=100)
for artists in artist:
 print(artists.item)


def track_and_timestamp(track):
    return f"{track.playback_date}\t{track.track}"


def print_track(track):
    print(track_and_timestamp(track))

TRACK_SEPARATOR = " - "


def split_artist_track(artist_track):
    artist_track = artist_track.replace(" – ", " - ")
    artist_track = artist_track.replace("“", '"')
    artist_track = artist_track.replace("”", '"')

    (artist, track) = artist_track.split(TRACK_SEPARATOR)
    artist = artist.strip()
    track = tracks.strip()
    print("Artist:\t\t'" + artist + "'")
    print("Track:\t\t'" + track + "'")


    # Validate
    if len(artist) == 0 and len(track) == 0:
        sys.exit("Error: Artist and track are blank")
    if len(artist) == 0:
        sys.exit("Error: Artist is blank")
    if len(track) == 0:
          sys.exit("Error: Track is blank")

    return (artist, track)