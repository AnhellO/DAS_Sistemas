import json

with open('sample.json', "r+") as file:
    
    myjson = json.load(file)
    
    for i in myjson["Persona"]:
        if int(i["id"]) % 2 != 0:
            print(i)
    
    for i in myjson["Persona"]:
        if len(i["Empresa"]) >= 4 and len(i ["Empresa"]) <= 6:
            print("\n", i)
    
    for i in myjson["Persona"]:
        i["Num_tel"] = "XXX-XXX-XX-XX"
        print(i) 