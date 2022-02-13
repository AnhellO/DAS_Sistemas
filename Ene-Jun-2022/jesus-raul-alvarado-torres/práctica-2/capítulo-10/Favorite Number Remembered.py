import json

try:
    with open('favorite_number.json') as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("¿Cual es tu numero favorito? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Gracias, lo recordaré.")
else:
    print("Tu numero favorito es: " + str(number))