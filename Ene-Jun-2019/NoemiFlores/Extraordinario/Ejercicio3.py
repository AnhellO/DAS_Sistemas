from abc import ABC, abstractmethod
import requests
import json

#Se crean objetos que representen a los paises
class Paises():
    def __init__(self, id, numericCode, name, nativeName, capital, region, subregion, languages):
        self.id = id
        self.numericCode = numericCode
        self.name = name
        self.nativeName = nativeName
        self.capital = capital
        self.region = region
        self.subregion = subregion
        self.languages = languages

    def __str__(self):
        return """- Id: {}\n- Codigo: {}\n- Nombre: {}\n- Nombre nativo: {}\n- Capital: {}\n- Region: {}\n- Subregion: {}\n- Lenguajes: {}\n
        """.format(
        self.id,
        self.numericCode,
        self.name,
        self.nativeName,
        self.capital,
        self.region,
        self.subregion,
        self.languages,
        ).strip()


#Interfaz de la conexión a la API
class APIConnection():
    @abstractmethod
    def makeGet(self):
        pass


class getPaises(APIConnection):

    def __init__(self):
        self.url = 'https://restcountries.eu/rest/v2/all'

    def makeGet(self):
        solicitud = requests.get(self.url)
        if solicitud.status_code != 200:
            return "Ocurrió un error"
        else:
            elements = []
            data = solicitud.json()
            for element in data['top']:
                obj = Paises(element['id'],element['numericCode'], element['name'],element['nativeName'], element['Capital'],
                element['region'], element['subregion'], element['languages'])
                elements.append(obj)
        return elements

if __name__ == '__main__':
    pass
