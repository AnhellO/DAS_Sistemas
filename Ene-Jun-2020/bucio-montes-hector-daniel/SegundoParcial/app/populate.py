from CharsApi import BB_Chars_API
from Models import *


def main():
    api = BB_Chars_API()
    data = api.get_characters()

    for i in data:

        try:
            rawPers = i

            if rawPers:
                charact, created = Characters.get_or_create(**rawPers)
                print(f"Character {'Created' if created else 'Existing'}: {charact.char_name}")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
    myDB.close()
