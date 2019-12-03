import requests
import personaje
import database

def obtener_personaje():

    r = requests.get('https://rickandmortyapi.com/api/character/')
    texto = r.json()
    paginas = texto['info']['pages']
    db = database.basedatos()
    db.crear_tabla_personajes()

    for i in range(1,paginas+1):
        r = requests.get('https://rickandmortyapi.com/api/character/?page={}'.format(i))
        texto = r.json()
        character = texto['results']
        for persona in character:
            epis = []
            episo = persona['episode']
            for j in range(0,len(episo)):
                cadena = episo[j]
                parte = ''
                parte += cadena[40]
                if len(cadena) == 42:
                    parte += cadena[41]
                epis.append(parte)
            locati = []
            loca = persona['location']['url']
            if len(loca) != 0:
                cad = loca
                part = ''
                part += cad[41]
                if len(cad) == 43:
                    part += cad[42]
                locati.append(part)
            else:
                part = 'Sin Localizar'
                locati.append(part)
            per = personaje.characters(persona['id'],persona['name'],persona['status'],persona['species'],persona['type'],persona['origin']['name'],persona['location']['name'],locati,persona['episode'],epis,persona['url'])
            db.insertar_personajes(per)

if __name__ == '__main__':
    obtener_personaje()