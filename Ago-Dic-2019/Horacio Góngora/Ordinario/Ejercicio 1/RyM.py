import requests
import sqlite3
from objectRyM import character

def obtenerCharacters():
    rr = requests.get('https://rickandmortyapi.com/api/character/')
    if rr.status_code == 200:
        for a in range(1, 494):
            r = requests.get('https://rickandmortyapi.com/api/character/' + str(a))
            response = r.json()
            infoPersonajes = []
            i = response
            id = i['id']
            name = i['name']
            status = i['status']
            species = i['species']
            tipe = i['type']
            gender = i['gender']
            nameOrigin = i['origin']['name']
            urlOrigin = i['origin']['url']
            nameLocation = i['location']['name']
            urlLocation = i['location']['url']
            image = i['image']
            episodes = i['episode']
            url = i['url']
            created = i['created']
            for x in episodes:
                infoPersonajes.append(str(x))
            cha = character(id=id,name=name,status=status,species=species,tipe=tipe,gender=gender,nameOrigin=nameOrigin, urlOrigin=urlOrigin,nameLocation=nameLocation,urlLocation=urlLocation,image=image,episodes=infoPersonajes,url=url,created=created)
            print(cha._id,cha._name,cha._status,cha._species,cha._tipe,cha._gender,cha._nameOrigin,cha._urlOrigin,cha._nameLocation,cha._urlLocation,cha._image,cha._episodes,cha._url,cha._created)

            try:
                conexion = sqlite3.connect('baseRyM.db')
                cursor = conexion.cursor()

                cursor.execute('INSERT INTO Characters VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(str(id), str(name), str(status), str(species),str(tipe), str(gender), str(nameOrigin),str(urlOrigin),str(nameLocation), str(urlLocation), str(image), episodes, str(url), str(created)))

                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def obtenerLocations():
    resident = ""
    rr = requests.get('https://rickandmortyapi.com/api/location/')
    if rr.status_code == 200:
        for a in range(1, 77):

            r = requests.get('https://rickandmortyapi.com/api/location/' + str(a))
            response = r.json()
            infoResidents = []
            i = response
            id = i['id']
            name = i['name']
            tipe = i['type']
            dimension = i['dimension']
            residents = i['residents']
            url = i['url']
            created = i['created']
            print('id ->', id,
                  '\nname ->', name,
                  '\ntype ->', tipe,
                  '\ndimension ->', dimension,
                  '\nresidents:')
            for x in residents:
                infoResidents.append(x)
                print(f'\t{x}')
            print('url ->', url,
                  '\ncreated', created)

            try:
                conexion = sqlite3.connect('baseRyM.db')
                cursor = conexion.cursor()

                cursor.execute('INSERT INTO Location VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(str(id), str(name), str(tipe), str(dimension),infoResidents,str(url), str(created)))

                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def obtenerEpisodes():
    rr = requests.get('https://rickandmortyapi.com/api/episode/')
    if rr.status_code == 200:
        for a in range(1, 32):

            r = requests.get('https://rickandmortyapi.com/api/episode/' + str(a))
            response = r.json()
            infoEpisodes = []
            i = response
            id = i['id']
            name = i['name']
            air_date = i['air_date']
            episode = i['episode']
            characters = i['characters']
            url = i['url']
            created = i['created']
            print('id ->', id,
                  '\nname ->', name,
                  '\nair_date ->', air_date,
                  '\nepisode ->',episode,
                  '\ncharacters:')
            for x in characters:
                infoEpisodes.append(x)
                print(f'\t{x}')
            print('url ->', url,
                  '\ncreated', created)

            try:
                conexion = sqlite3.connect('baseRyM.db')
                cursor = conexion.cursor()

                cursor.execute('INSERT INTO Episode VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(str(id), str(name), str(air_date), str(episode),infoEpisodes,str(url), str(created)))

                conexion.commit()
                cursor.close()
            except sqlite3.Error as error:
                print('Error con la conexión!', error)

def main():
    obtenerCharacters()
    obtenerLocations()
    obtenerEpisodes()

if __name__ == '__main__':
    main()