import json

with open('data.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(f"ID: {p['_id']}")
        print(f"First Name: {p['name']['first']}")
        print(f"Last Name: {p['name']['last']}")
        print(f"Age: {p['age']}")
        print()