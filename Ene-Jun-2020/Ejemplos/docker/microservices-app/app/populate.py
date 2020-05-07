from models import *
from pokeapi import PokeAPI

def main():
    myDB.connect()
    myDB.create_tables([Pokemon])
    api = PokeAPI()
    
    for i in range(1, api.get_count(), 1):
        try:
            raw_pokemon = api.get_pokemon(i)
            
            if raw_pokemon:
                pokemon, created = Pokemon.get_or_create(**raw_pokemon)
                print(f"Pokemon {'Created' if created else 'Existing'}: {pokemon.nombre}")
        except Exception as e:
            print(e)

    myDB.close()

if __name__ == '__main__':
    main()