
import pylast
from lastfmapi import lastfm_network, print_it

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
from app.lastfmAPI import artist
from app.modelslast import track

API_KEY = "3438d479a2065875b8f422a8bbf50cf2"  # this is a sample key
API_SECRET = "d95841d5489c8646213335aec1fd4bc8"

# In order to perform a write operation you need to authenticate yourself
username = "jorgelof"
password_hash = pylast.md5("chatolds12!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

tracks = artist.get_top_tracks(limit=5)
for tracks in track:
    print(tracks.item)

members = artist.get_band_members()
print(members)

biography = artist.get_bio_summary()
print(biography)
