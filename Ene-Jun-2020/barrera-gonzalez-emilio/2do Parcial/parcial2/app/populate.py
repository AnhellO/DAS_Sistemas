from models import *
from breakingbadapi import breaking_bad_API

def main():
    
    api = breaking_bad_API()
    data = api.get_characters()

    for i in data:
        
        try:
            raw_character = i

            if raw_character:
                charact, created = Characters.get_or_create(**raw_character)
                print(f"Character {'Created' if created else 'Existing'}: {charact.char_name}")
        
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
    myDB.close()