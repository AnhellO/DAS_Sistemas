import requests
import json
import sqlite3


def get_paises(archivo_bd = 'countries.db'):
    con = sqlite3.connect(archivo_bd)
    cursor = con.cursor()
    respuesta = requests.get('https://restcountries.eu/rest/v2/all')
    if respuesta.status_code == 200:
        respuesta_json = json.loads(respuesta.text)
        for pais in respuesta_json:
            string_lenguajes = ','.join(lenguaje['iso639_2'] for lenguaje in pais['languages'])
            cursor.execute('insert into country values ("{}", "{}", "{}", "{}", "{}")'.format(pais['name'],
            string_lenguajes, pais['region'], pais['capital'], pais['timezones'][0]))
        con.commit()
    con.close()


def main():
    get_paises()


if __name__ == '__main__':
    main()