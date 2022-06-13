#DAS_Ene_Jun
#Practica 1 - Ejercicio 2

import json

def tostring(dude):
    aux="---------------\n"
    aux+="ID: "+str(dude["id"])+"\n"
    aux+="First Name: "+str(dude["first_name"])+"\n"
    aux+="Last Name: "+str(dude["last_name"])+"\n"
    aux+="Company: "+str(dude["company"])+"\n"
    aux+="E-mail: "+str(dude["email"])+"\n"
    aux+="IP Address: "+str(dude["ip_address"])+"\n"
    aux+="Phone Number: "+str(dude["phone_number"])+"\n"
    aux+="---------------\n"
    return aux
    
def odd_id(people):
    print("People with an odd numbered id\n")
    for guy in people:
        if float(guy["id"])%2!=0:
            print(tostring(guy))
    
def company_name(people):
    print("People with a company name between 4 and 6 characters\n")
    for guy in people:
        if len(str(guy["company"]))>4 and len(str(guy["company"]))<6:
            print(tostring(guy))

def change_json(people):
    new=people
    
    for guy in new:
        pn=str(guy["phone_number"])
        aux=pn.replace('-','')
        new_pn="XX-XX-XXX"
        guy["phone_number"]=new_pn
        
    return new
        
if __name__ == "__main__":
    
    file=open("sample.json")
    data=json.load(file)
    file.close()
    
    people=data["people"]["person"]
    new_data=data
    
    odd_id(people)
    company_name(people)
    new_people=change_json(people)
    
    new_data["people"]["person"]=new_people
    with open('updated.json', 'w') as F:
        json.dump(new_data, F, indent=2)
        print("Updated format saved in a json file (updated.json)")


    
    
            
    
    