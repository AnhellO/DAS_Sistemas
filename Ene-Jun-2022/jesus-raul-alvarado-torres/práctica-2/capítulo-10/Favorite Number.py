import json

number = input("¿Cual es tu numero favorito? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Gracias, lo recordaré.")