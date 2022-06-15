import json

def imprimirLista(list : list):
    for i in list:
        print('{')

        for llave, valor in i.items():
            print(f"{llave} : {valor}")

        print('}') 


def listIdImpar(content):
    list = []

    for c in content:
        if (int(c['id']) % 2) == 1:
            list.append(c)

    imprimirLista(list)


def listNombreComañia(content):
    list = []

    for c in content:
        if (len(c['company'])) >= 4 and (len(c['company'])) <=6:
            list.append(c)

    imprimirLista(list)

def updateJSON(contentFile):
    for person in contentFile['people']['person']:
        person['phone_number'] = 'XX-XX-XXX'      

    with open("updated.json", 'w') as file:          
        json.dump(contentFile, file, indent=4)
    

if __name__ == '__main__':
    with open("sample.json", 'r') as file:  
        contentFile = json.load(file)         
    
    content = contentFile['people']['person']
    print(content)

    print('########## Lista personas con id impar ##########')
    listIdImpar(content)
    print('\n########## Lista personas cuya longitud del nombre de la comañia esta entre 4 y 6##########')
    listNombreComañia(content)    
    print('\n########## Haciendo update (creando nuevo archivo)... ##########')    
    updateJSON(contentFile)
    print('Archivo creado !!!!')    