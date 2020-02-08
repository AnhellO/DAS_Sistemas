# "select count(Nombre) from Paises where Nombre = Nombre"
#
# "select * from Paises where Nombre = 'Mexico'"
#
# "select Lenguajes from Paises where Id = Id"
#
# "select Nombre from Paises where Continente = 'Europe'"

import requests
import json
import sqlite3

# originalmente planeaba usar 'iso639_1', pero en el caso de Malasia (Malaysia), me
# daba problemas, así que decidí cambiar a 'iso639_2'
def obtener_paises(archivo_bd = 'paises.db'):
    conexion = sqlite3.connect(archivo_bd)
    cursor = conexion.cursor()
    respuesta = requests.get('https://restcountries.eu/rest/v2/all')
    if respuesta.status_code == 200:
        respuesta_json = json.loads(respuesta.text)
        for pais in respuesta_json:
            string_lenguajes = ','.join(lenguaje['iso639_2'] for lenguaje in pais['languages'])
            cursor.execute('insert into Paises values ("{}", "{}", "{}", "{}", "{}")'.format(pais['name'],
            string_lenguajes, pais['region'], pais['capital'], pais['timezones'][0]))
        conexion.commit()
    conexion.close()

def main():
    # respuesta = requests.get('https://restcountries.eu/rest/v2/all')
    # if respuesta.status_code == 200:
    #     response_json = json.loads(respuesta.text)
    #     for i in response_json:
    #         print(i)
    #####################################################
    # respuesta = requests.get('https://restcountries.eu/rest/v2/name/canada')
    # if respuesta.status_code == 200:
    #     respuesta_json = json.loads(respuesta.text)
    #     print(','.join(i['iso639_1'] for i in respuesta_json[0]['languages']))
    #     # for i in respuesta_json[0]['languages']:
    #     #     print(i['iso639_1'])
    #####################################################
    # respuesta = requests.get('https://restcountries.eu/rest/v2/name/malaysia')
    # if respuesta.status_code == 200:
    #     respuesta_json = json.loads(respuesta.text)
    #     print(respuesta_json[0]['languages'])
    #     pais = respuesta_json[0]
    #     string_lenguajes = ','.join(lenguaje['iso639_2'] for lenguaje in pais['languages'])
    #     print("insert into Paises values {}, '{}', '{}', '{}', '{}', {}, {}".format(1,
    #     pais['name'], string_lenguajes, pais['region'], pais['topLevelDomain'][0], pais['latlng'][0],
    #     pais['latlng'][1]))
    #####################################################
    obtener_paises()

if __name__ == '__main__':
    main()
