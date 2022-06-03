#DAS_Ene_Jun
#Practica 1 - Ejercicio 3

import yaml

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

def id_divby3(source):
    print("People whose id is a multiple of 3\n")
    for person in source["people"]["person"]:
        if int(person['id'])%3==0:
            print(tostring(person))

def print_5name(source):
    print("People whose name or last name have exactly 5 letters\n")
    for person in source["people"]["person"]:
        if len(person['first_name'])==5 or len(person['last_name'])==5:
            print(tostring(person))
            
def updt_email(source):
    new=source
    for person in new["people"]["person"]:
        person["email"]="---"
        
    with open("updated.yml", "w") as file:
        source=yaml.dump(new, file)
    print("Updated data saved in a yaml file (updated.yml)")

if __name__ == "__main__":
    
    with open("sample.yml") as f:
        source=yaml.load(f, Loader=yaml.FullLoader)
        
    #id_divvy3(source)
    #print_5name(source)
    updt_email(source)
    