import json

with open('sample.json', "r+") as file:
    
    myjson = json.load(file)
    
    for i in myjson["person"]:
        if int(i["id"]) % 2 != 0:
            print(i)
    
    for i in myjson["person"]:
        if len(i["company"]) >= 4 and len(i ["company"]) <= 6:
            print("\n", i)
    
    for i in myjson["person"]:
        i["phone_nomber"] = "XX-XX-XXX"
        print(i) 