import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
data = tree.getroot()
Gente = []

for Persona in data:
    
    lista_atributos = [atributo.text for atributo in Persona]  
    Gente.append(lista_atributos)

for i in Gente:
    for id in i[0]:
        if (int(id) % 2 == 0):
            print(i)

for i in Gente:
    for correo in i[4]:
        if Persona[4].endswith(".edu") or Persona[4].endswith(".gov"):
            print(Persona)