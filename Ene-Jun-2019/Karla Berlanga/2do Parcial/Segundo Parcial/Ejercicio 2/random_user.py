import requests
import json
import os

def makeGet():
    #Función que se conecta a una API que genera usuarios random y regresa un diccionario con 100 usuarios
    url = 'https://randomuser.me/api/?results=100'
    solicitud = requests.get(url)
    if solicitud.status_code != 200:
        print("Ocurrió un error")
    else:
        data = solicitud.json()
        return data

def createJson(data):
    #Función que recibe un diccionario y lo sobreescribe en un archivo con extensión .json
    fname = "data.json"
    if os.path.isfile(fname):
        os.remove(fname)

    with open(os.path.join(fname), 'w',encoding='utf-8') as file:
        json.dump(data, file)

def main():
    #Se hace la consulta a la API
    data = makeGet()
    #Se manda el diccionarop obtenido en la consulta anterior y se guarda en el archivo .json
    createJson(data)

if __name__ == '__main__':
    main()
