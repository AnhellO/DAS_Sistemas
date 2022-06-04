import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
print(r.json())