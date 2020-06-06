import requests
import json
from random import randrange

class PokeAPI(object):

    COUNT = 0

    def __init__(self):
        self.ENDPOINT = 'https://pokeapi.co/api/v2/pokemon'

    def get_count(self):
        if self.COUNT:
            return self.COUNT

        r = requests.get(self.ENDPOINT)
        self.COUNT = r.json().get('count', 0)

        return self.COUNT

    def get_pokemon(self, x):
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        
        if r.status_code != 200:
            raise Exception(f"Pokemon {self.ENDPOINT}/{x} doesn't exist in the API :(")
        
        data = r.json()
        types = ','.join(list(filter(lambda x: x != '', [_type.get('type', {}).get('name', '') for _type in data.get('types', [])])))

        return {
            'nombre': data.get('name'),
            'tipos': json.dumps(types),
            'imagen': data.get('sprites', {}).get('front_default'),
        }