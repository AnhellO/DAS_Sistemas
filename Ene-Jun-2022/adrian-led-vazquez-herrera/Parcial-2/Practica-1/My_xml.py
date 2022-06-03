#DAS_Ene_Jun
#Practica 1 - Ejercicio 1
from xml.etree import ElementTree

def tostring(dude):
    aux="---------------\n"
    aux+="ID: "+str(dude.find("./id").text)+"\n"
    aux+="First Name: "+str(dude.find("first_name").text)+"\n"
    aux+="Last Name: "+str(dude.find("last_name").text)+"\n"
    aux+="Company: "+str(dude.find("company").text)+"\n"
    aux+="E-mail: "+str(dude.find("email").text)+"\n"
    aux+="IP Address: "+str(dude.find("ip_address").text)+"\n"
    aux+="Phone Number: "+str(dude.find("phone_number").text)+"\n"
    aux+="---------------\n"
    return aux

def even_id(people):
    print("People with an even numbered id\n")
    for person in people:
        if int(person.find("./id").text)%2==0:
            print(tostring(person))
            
def spec_email(people):
    print("People whose email ends with '.gov' or '.edu'\n")
    for person in people:
        email=person.find("./email").text
        if str(email[-4:])==".gov" or str(email[-4:])==".edu":
            print(tostring(person))

def change_ip(root):
    new=root
    for ip in new.iter("ip_address"):
        ip.text="127.0.0.1"
    new_xml=ElementTree.ElementTree(new)
    with open("updated.xml", "wb") as f:
        new_xml.write(f)
    print("Updated data saved in a xml file (updated.xml)")

if __name__ == "__main__":
    
    with open('sample.xml', 'rt') as f:
        tree = ElementTree.parse(f)
    
    root=tree.getroot()
    people=root.findall("./person")
    
    
    even_id(people)
    spec_email(people)
    change_ip(root)
    
    