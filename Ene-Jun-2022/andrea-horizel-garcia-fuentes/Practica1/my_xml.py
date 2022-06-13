import xml.etree.ElementTree as ET


tree = ET.parse('sample.xml')


data = tree.getroot()


people = []

for persona in data:
    
    lista_atributos = [atributo.text for atributo in persona]

    
    people.append(lista_atributos)

for i in people:
    for id in i[0]:
        if (int(id) % 2 == 0):
            print(i)

for i in people:
    for correo in i[4]:
        if persona[4].endswith(".edu") or persona[4].endswith(".gov"):
            print(persona)

