import yaml
import json

def imprimirLista(list : list):
    for i in list:
        print('{')

        for llave, valor in i.items():
            print(f"{llave} : {valor}")

        print('}') 


def listIdMultiplo3(content):
    list = []

    for c in content:
        if (int(c['id']) % 3) == 0:
            list.append(c)

    imprimirLista(list)


def listNombreApellido(content):
    list = []

    for c in content:
        if (len(c['first_name'])) == 5 or (len(c['last_name'])) == 5:
            list.append(c)

    imprimirLista(list)

def updateYAML(contentFile):
    for person in contentFile['people']['person']:
        person['email'] = '---'      

    with open("updated.yml", 'w') as file:          
        yaml.dump(contentFile, file)
    

if __name__ == '__main__':
    with open("sample.yml", 'r') as file:  
        contentFile = yaml.load(file, Loader=yaml.FullLoader)         
    
    content = contentFile['people']['person']    

    print('########## Lista personas cuyo id es multiplo de 3 ##########')
    listIdMultiplo3(content)    
    print('\n########## Lista personas cuya longitud del nombre o apellido es igual a5 ##########')
    listNombreApellido(content)    
    print('\n########## Haciendo update (creando nuevo archivo)... ##########')    
    updateYAML(contentFile)
    print('Archivo creado !!!!')    