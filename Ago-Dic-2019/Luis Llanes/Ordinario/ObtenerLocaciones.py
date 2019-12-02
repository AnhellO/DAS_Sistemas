import requests
# import pprint
import Locaciones
import DataBase

def Obtener_Locaciones():
    r = requests.get("https://rickandmortyapi.com/api/location")
    results = r.json()

    numeroPaginas = results['info']['pages']
    # pprint.pprint(results)
    for i in range(1, (numeroPaginas+1)):
        r = requests.get("https://rickandmortyapi.com/api/location?page={}".format(i))
        results = r.json()
        for locacion in results['results']:
            gengibre = Locaciones.locacion(locacion['created'], locacion['dimension'], locacion['id'], locacion['name'], locacion['residents'], locacion['type'], locacion['url'])
            # print(locacion['created'])
            # print(locacion['dimension'])
            # print(locacion['id'])
            # print(locacion['name'])
            # print(locacion['residents'])
            # print(locacion['type'])
            # print(locacion['url'])
            # print(gengibre)
            # print('---------------------------------')
            DataBase.Agregar_Elemento_Locaciones(gengibre)

if __name__ == '__main__':
    Obtener_Locaciones()

"""
FechaDeCreacion
Dimension
Id_Locacion
Nombre
Residentes
Tipo
url

"""