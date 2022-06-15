import json

with open('favorite_number.json') as f:
    number = json.load(f)

print("Tu numero favorito es: " + str(number))