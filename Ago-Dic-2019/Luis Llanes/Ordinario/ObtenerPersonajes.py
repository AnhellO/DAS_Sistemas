import requests
# import pprint
import Personaje
import DataBase


def Obtener_Personajes():
    r = requests.get("https://rickandmortyapi.com/api/character")
    results = r.json()

    numeroPaginas = results['info']['pages']

    # pprint.pprint(results)
    for i in range(1, (numeroPaginas+1)):
        r = requests.get("https://rickandmortyapi.com/api/character/?page={}".format(i))
        results = r.json()
        
        for personajes in results['results']:
            eps = []
            episodios = personajes['episode']
            for j in range(0, len(episodios)):
                cadena = episodios[j]
                cap = ''
                cap += cadena[40]
                if len(cadena) == 42:
                    cap += cadena[41]
                eps.append(cap)
            Panecito = Personaje.personaje(personajes['created'], personajes['episode'], eps, personajes['gender'], personajes['id'], personajes['image'], personajes['location']['name'], personajes['location']['url'], personajes['name'], personajes['origin']['name'], personajes['origin']['url'], personajes['species'], personajes['status'], personajes['type'], personajes['url'])
            # print(personajes['created'])
            # print(personajes['episode'])
            # print(personajes['gender'])
            # print(personajes['id'])
            # print(personajes['image'])
            # print(personajes['location']['name'])
            # print(personajes['location']['url'])
            # print(personajes['name'])
            # print(personajes['origin']['name'])
            # print(personajes['origin']['url'])
            # print(personajes['species'])
            # print(personajes['status'])
            # print(personajes['type'])
            # print(personajes['url'])
            # print('---------------------')
            # print(Panecito)
            DataBase.Agregar_Elemento_Personajes(Panecito)

if __name__ == '__main__':
    Obtener_Personajes()

"""
Resultados:
    FechaDeCreacion
    EpisodioDondeAparece
    Genero
    Id
    Image
    Location
        Name
        url
    Name
    Origin
        Name
        url
    especie
    status
    type
    url


"""