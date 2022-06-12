import json

with open('favorite_number.json') as filenombre:
    numero = json.load(filenombre)

print("Recuerdo tu numero favorito! " + str(numero) + ".")