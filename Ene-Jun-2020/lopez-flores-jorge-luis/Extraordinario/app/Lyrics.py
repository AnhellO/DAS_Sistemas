import json

import requests

artist ='artist'

track ='track'

keywords = {'drink'}

url = 'https://private-21042-lyricsovh.apiary-proxy.com/v1/' + artist+'/' +track

response = requests.get(url)
json_data = json.loads(response.content)
lyrics = json_data['lyrics']

print=(lyrics)