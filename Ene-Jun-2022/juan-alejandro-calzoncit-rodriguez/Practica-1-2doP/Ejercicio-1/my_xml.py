import xml.etree.ElementTree as ET

def imprimirLista(list : list):
    for i in list:
        print('{')
        for j in range(len(i)):
            print(f"{i[j].tag} : {i[j].text}")
        print('}') 

def listaIdImpar(root):
    list = []
    for person in root:
        if (int(person[0].text) % 2) == 0:            
            list.append(person)

    imprimirLista(list)           

def listaDominio(root):
    list = []
    for person in root:
        if (person[4].text).count('.gov') or (person[4].text).count('.edu'):
            list.append(person)

    imprimirLista(list)           
    
def updateXML(tree):
    address = '127.0.0.1'
    for person in tree.findall('person'):
        person[5].text = address
    
    tree.write('update.xml')

if __name__ == "__main__":
    tree = ET.parse('sample.xml')
    root = tree.getroot()

    print('########## Lista personas con id par ##########')
    listaIdImpar(root)
    print('\n########## Lista personas con con dominio .gov ó .edu ##########')
    listaDominio(root)
    print('\n########## Haciendo update (creando nuevo archivo)... ##########')
    updateXML(tree)
    print('Archivo creado !!!!')