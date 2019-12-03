import requests
# import pprint
import Episodios
import DataBase

def Obtener_Episodios():
    r = requests.get('https://rickandmortyapi.com/api/episode')
    results = r.json()

    numeroPaginas = results['info']['pages']

    # pprint.pprint(results)
    for i in range(1, numeroPaginas+1):
        r = requests.get('https://rickandmortyapi.com/api/episode?page={}'.format(i))
        results = r.json()

        for episodios in results['results']:
            Cafecito = Episodios.episodio(episodios['air_date'], episodios['characters'], episodios['created'], episodios['episode'], episodios['id'], episodios['name'], episodios['url'])
            # print(Cafecito)
            DataBase.Agregar_Elemento_Episodio(Cafecito)


if __name__ == '__main__':
    Obtener_Episodios()

"""
FechaLanzamiento
Personajes
FechaCreacion
Episodio
Id_Episodio
Nombre
Url"""