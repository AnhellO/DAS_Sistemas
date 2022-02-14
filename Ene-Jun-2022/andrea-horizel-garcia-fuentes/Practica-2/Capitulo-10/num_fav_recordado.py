import json

try:
    with open('favorite_number.json') as filenombre:
        numero = json.load(filenombre)
except FileNotFoundError:
    numero = input("Cual es tu numero favorito? ")
    with open('favorite_number.json', 'w') as filenombre:
        json.dump(numero, filenombre)
    print("gracias!, Lo recordare.")
else:
    print("recuerdo tu numero favorito " + str(numero) + ".")