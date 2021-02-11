import requests
import json
import sqlalchemy
from sqlalchemy.dialects import mysql


def obtener_paises(archivo_bd = 'paises.db'):
    conexion = mysql.connect(archivo_bd)
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
    obtener_paises()

if __name__ == '__main__':
    main()