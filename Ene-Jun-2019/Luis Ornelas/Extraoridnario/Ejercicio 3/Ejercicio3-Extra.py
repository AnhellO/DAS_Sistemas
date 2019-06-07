import requests
import json
import sqlite3

def get_paises(archivo_bd = 'Paises.db'):
    conexion = sqlite3.connect(archivo_bd)
    cursor = conexion.cursor()
    response = requests.get('https://restcountries.eu/rest/v2/all')
    if response.status_code == 200:
        response_json = json.loads(response.text)
        for pais in response_json:
            all_lenguajes = ','.join(lenguaje['iso639_2'] for lenguaje in pais['languages'])
            cursor.execute('INSERT INTO Paises VALUES ("{}", "{}", "{}", "{}", "{}")'.format(pais['name'], pais['capital'], pais['region'], all_lenguajes, pais['flag']))
        conexion.commit()
    conexion.close()

def main():
    get_paises()

if __name__ == '__main__':
    main()
