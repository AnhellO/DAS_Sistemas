import requests
import ubicacion
import database

class obtener_Locacion():
    r = requests.get('https://rickandmortyapi.com/api/location/')
    texto = r.json()
    paginas = texto['info']['pages']
    db = database.basedatos()
    db.crear_tabla_locaciones()

    for i in range(1,paginas+1):
        r = requests.get('https://rickandmortyapi.com/api/location/?page={}'.format(i))
        texto = r.json()
        location = texto['results']
        for locacion in location:
            residentes = []
            res = locacion['residents']
            for j in range(0,len(res)):
                if len(res) != 0:
                    cadena = res[j]
                    
                    parte = ''
                    parte += cadena[42]
                    if len(cadena) >= 44:
                        parte += cadena[43]
                    if len(cadena) == 45:
                        parte += cadena[44]
                    residentes.append(parte)
                else:
                    parte = 'Sin Residentes'
                    residentes.append(parte)
            loc = ubicacion.ubicaciones(locacion['id'],locacion['name'],locacion['type'],locacion['dimension'],locacion['residents'],residentes,locacion['url'])
            db.insertar_locaciones(loc)
            
if __name__ == '__main__':
    obtener_Locacion()