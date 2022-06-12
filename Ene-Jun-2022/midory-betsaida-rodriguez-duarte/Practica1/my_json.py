import json

with open('sample.json', "r+") as file:
    
    data = json.load(file)
    
    for person in data['person']:
        if int(person["id"]) % 2 != 0:
            print(person)
    
    for person in data["person"]:
        if len(person["company"]) >= 4 and len(person["company"]) <= 6:
            print("\n", person)
    
    for person in data["person"]:
        person["phone_number"] = "XX-XX-XXX"
        print(person)