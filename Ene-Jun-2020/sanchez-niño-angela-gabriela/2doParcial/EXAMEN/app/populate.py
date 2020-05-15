from models import *
from api import PERSONAJE
import logging


def main():
    api = PERSONAJE()
    
    for i in range(1, api.get_count(), 1):
        try:
            raw_perso = api.get_personaje(i)
            
            if raw_perso:
                perso, created = Personaje.get_or_create(**raw_perso)
                print(f"Personaje {'Created' if created else 'Existing'}: {personaje.nombre}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
    myDB.close()