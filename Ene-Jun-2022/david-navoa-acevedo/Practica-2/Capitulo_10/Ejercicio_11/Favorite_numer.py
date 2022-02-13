import json

favorite_number = input("Whats your favorite number? :")
favorite_number_json = 'Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_11/wild_json.json'

with open(favorite_number_json, 'w') as opened_file:
    json.dump(favorite_number, opened_file)
    print("Done :3, thanks!")