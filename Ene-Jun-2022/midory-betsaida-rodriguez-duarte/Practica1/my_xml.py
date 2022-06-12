import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
data = tree.getroot()
lista_personas = []

for persona in data:
    lista_atributos = [atributo.text for atributo in persona]
    lista_personas.append(lista_atributos)

#Este imprime las personas con ID par.
for persona in lista_personas:
    for id in persona[0]:
        if (int(id) % 2 == 0):
            print(persona)

#Este imprime los correos que tengan .edu o .gov
for persona in lista_personas:
    if persona[4].endswith("edu") or persona[4].endswith("gov"):
        print(persona)

#Cambia la ip_addres 
for persona in lista_personas:
    persona[5] = "127.0.0.1"
    print(persona)

