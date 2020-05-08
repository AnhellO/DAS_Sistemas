from models import *
from pokeapi import PokeAPI
import logging

# logger = logging.getLogger('peewee')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

def main():
    api = PokeAPI()
    
    for i in range(1, api.get_count(), 1):
        try:
            raw_pokemon = api.get_pokemon(i)
            
            if raw_pokemon:
                pokemon, created = Pokemon.get_or_create(**raw_pokemon)
                print(f"Pokemon {'Created' if created else 'Existing'}: {pokemon.nombre}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
    myDB.close()