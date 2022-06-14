import json

json_file = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_11/wild_json.json"

with open(json_file) as opened_file:
    number = json.load(opened_file)

    print("I know your favoritenumber! Its " + number + " where is my cookie? :3")