from models import *
from character import *


def main():
    char = Personaje()
    data = char.getCharacter()

    for x in data:
        try:
            raw = x
            if raw:
                person, created = Character.get_or_create(**raw)
                print(f"Character {'Created' if created else 'Existing'}:{person.usr_name}")
        except Exception as error:
            print('Error')

    

if __name__ =='__main__':
    main()
    myDB.close()