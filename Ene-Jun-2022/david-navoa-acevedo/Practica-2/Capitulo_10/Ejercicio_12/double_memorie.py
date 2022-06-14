import json

favorite_numbers = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_12/wild_json.json"

try:
    
    with open(favorite_numbers) as opened_file_0:
        number = json.load(opened_file_0)
    
except Exception:
    number = input("tell me your favorite number: ")

    with open(favorite_numbers, 'w') as opened_file_1:
        current_json = json.dump(number, opened_file_1)
        print("Done :3, thanks!")
else:

    print("I know your favorite number! Its " + number + " where is my cookie? :3")