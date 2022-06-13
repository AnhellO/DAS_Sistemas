#10.11

import json

numero = input("Cual es tu numero favorito? ")

with open('favorite_number.json', 'w') as f:
    json.dump(numero, f)
    print("gracias! lo recordare.")
