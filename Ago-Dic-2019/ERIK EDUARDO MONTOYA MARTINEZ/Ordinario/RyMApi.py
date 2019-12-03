import sqlite3
from objectRyM import personaje
import requests


def traerPersonajes():
    rr = requests.get('https://rickandmortyapi.com/api/character/')
    if rr.status_code == 200:
        for a in range(1, 494):
            r = requests.get('https://rickandmortyapi.com/api/character/' + str(a))
            response = r.json()
            listPersonajes = []
            i = response
            id = i['id']
            name = i['name']
            status = i['status']
            species = i['species']
            tipe = i['type']
            gender = i['gender']
            OriginName = i['origin']['name']
            OriginUrl = i['origin']['url']
            LocationName = i['location']['name']
            LocationUrl = i['location']['url']
            image = i['image']
            episodes = i['episode']
            url = i['url']
            created = i['created']
            for x in episodes:
                    listPersonajes.append(str(x))
            p = personaje(id=id,name=name,status=status,species=species,tipe=type,gender=gender,OriginName=OriginName,
                           OriginUrl=OriginUrl,LocationName=LocationName,LocationUrl=LocationUrl,image=image,episodes=listPersonajes,url=url,created=created)
            print(p._id,p._namepa._status,p._species,p._type,p._gender,p._nameOrigin,p._urlOrigin,p._nameLocation,p._urlLocation,p._image,p._episodes,p._url,p._created)

            try:
                conexion = sqlite3.connect('RyMDB.db')
                cursor = conexion.cursor()
                cursor.execute('INSERT INTO Personajes VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'
                               .format(str(id), str(name), str(status), str(species),str(type), str(gender), str(OriginName ),str(OriginUrl),str(LocationName), str(LocationUrl), str(image), episodes, str(url), str(created)))
                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def traerLocaciones():
    resident = ""
    rr = requests.get('https://rickandmortyapi.com/api/location/')
    if rr.status_code == 200:
        for a in range(1, 77):
            r = requests.get('https://rickandmortyapi.com/api/location/' + str(a))
            response = r.json()
            i = response
            list_residents=[]
            id = i['id']
            name = i['name']
            tipe = i['type']
            dimension = i['dimension']
            residents = i['residents']
            url = i['url']
            created = i['created']
            print('id: ', id,'\nname: ', name,'\ntype:  ', type,'\ndimension: ', dimension,'\nresidents:')
            for x in residents:
                list_residents.append(x)
                print(f'\t{x}')
            print('url ->', url,'\ncreated', created)
            try:
                conexion = sqlite3.connect('RyMDB.db')
                cursor = conexion.cursor()
                cursor.execute('INSERT INTO Locaciones VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(str(id), str(name), str(type), str(dimension),list_residents,str(url), str(created)))
                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def traeEpisodio():
    rr = requests.get('https://rickandmortyapi.com/api/episode/')
    if rr.status_code == 200:
        for a in range(1, 32):
            r = requests.get('https://rickandmortyapi.com/api/episode/' + str(a))
            response = r.json()
            i = response
            list_episodio = []
            id = i['id']
            name = i['name']
            air_date = i['air_date']
            episode = i['episode']
            characters = i['characters']
            url = i['url']
            created = i['created']
            print('id ->', id,'\nname:  ', name,'\nair_date: ', air_date,'\nepisode:  ',episode,'\ncharacters:')
            for x in characters:
               list_episodio.append(x)
            print(f'\t{x}')
            print('url ->', url,'\ncreated', created)
            try:
                conexion = sqlite3.connect('RyMDB.db')
                cursor = conexion.cursor()
                cursor.execute('INSERT INTO Episodios VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(str(id), str(name), str(air_date), str(episode),list_episodio,str(url), str(created)))
                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def main():
    traeEpisodio()
    traerLocaciones()
    traerPersonajes()

if __name__ == '__main__':
    main()