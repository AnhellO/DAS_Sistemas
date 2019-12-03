import requests
import episodio
import database

class obtener_episodio():
    r = requests.get('https://rickandmortyapi.com/api/episode/')
    texto = r.json()
    paginas = texto['info']['pages']
    db = database.basedatos()
    db.crear_tabla_Episodios()


    for i in range(1,paginas+1):
        r = requests.get('https://rickandmortyapi.com/api/episode/?page={}'.format(i))
        texto = r.json()
        episode = texto['results']
        for episodes in episode:
            char = []
            character = episodes['characters']
            for j in range(0,len(character)):
                cadena = character[j]
                
                parte = ''
                parte += cadena[42]
                if len(cadena) >= 44:
                    parte += cadena[43]
                if len(cadena) == 45:
                    parte += cadena[44]
                char.append(parte)
            epi = episodio.episodios(episodes['id'],episodes['name'],episodes['air_date'],episodes['episode'],episodes['characters'],char,episodes['url'])
            db.insertar_episodios(epi)

if __name__ == '__main__':
    obtener_episodio()