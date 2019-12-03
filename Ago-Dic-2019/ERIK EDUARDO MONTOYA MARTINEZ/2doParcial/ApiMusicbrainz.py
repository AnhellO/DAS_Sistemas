import sqlite3
import pprint
import musicbrainzngs
from ObjetoArtista import Artista


def search():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
    Art = musicbrainzngs.search_artists(area='Los Angeles', tag='[rock,metal]', country="US", limit=100)
    j = 0
    for i in Art['artist-list']:
        id2 = Art['artist-list'][j]['id']
        nombre = Art['artist-list'][j]['name']
        area = Art['artist-list'][j]['area']['name']
        sortname = Art['artist-list'][j]['sort-name']
        eScore = Art['artist-list'][j]['ext:score']
        tipoC = Art['artist-list'][j]['area']['type']
        j = j+1
        art = search(id=j,nombre=nombre,area=area,sort=sortname,id2=id2,eScore=eScore,tipoC=tipoC)

        save(art)

def save(arti):
    try:
        conexion = sqlite3.connect('musicbrainzDB.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO Artistas VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(arti._id,arti._nombre,arti._area,arti._sortname,arti._eScore,arti._tipoC,arti._id2))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def main():
    search()

if __name__ == '__main__':
    main()