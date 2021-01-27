import requests
import json
import random
from random import randrange

class PokeAPI(object):
    def __init__(self):
        #self.ENDPOINT = 'https://pokeapi.co/api/v2/pokemon-form'
        self.ENDPOINT='https://pokeapi.co/api/v2/pokemon'

    def getPokemon(self, x):
        payload = {}
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        data = r.json()
        
        abilities = [ability['ability'] for ability in data.get('abilities')]
        name_abilities = [ability['name'] for ability in abilities]
        
        moves = [move['move'] for move in data.get('moves')]
        name_moves = [move['name']for move in moves]
        
        items = [item['item'] for item in data.get('held_items')]
        name_items = [item['name'] for item in items]
        
        return {
            'name': data.get('name'),
            'id' : data.get('id'),
            'base_experience' : data.get('base_experience'),
            'weight': data.get('weight'),
            'height': data.get('height'),
            'order': data.get('order'),
            'location_area_encounters':data.get('location_area_encounters'),      
            'moves': str(random.sample(name_moves, k=5)).strip('[]'),
            'abilities' : str(name_abilities).strip('[]'),
            'items': str(name_items).strip('[]'),
            'type': data.get('species', {}).get('url'),
            'image': data.get('sprites', {}).get('front_default')
        }

#api = PokeAPI()
#print(json.dumps(api.getPokemon(randrange(807)), indent=2))