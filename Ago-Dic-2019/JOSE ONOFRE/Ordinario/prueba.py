import requests
import pprint
import ramapi
from ramapi import *
import ClaseCharacter


r = requests.get('https://rickandmortyapi.com/api/episode/')
pprint.pprint(r.json())

ramapi.Base.api_info()
ramapi.Base.schema()

