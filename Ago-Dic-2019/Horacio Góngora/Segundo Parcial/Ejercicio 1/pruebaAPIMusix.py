import sqlite3
import musicbrainzngs
import json
import pprint
from objArtBand import artista

def buscarArt():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
    art = musicbrainzngs.search_artists(area='Los Angeles', tag='[rock,metal]', country="US", limit=100)

    ii = 0
    for i in art['artist-list']:
        area = art['artist-list'][ii]['area']['name']
        id = art['artist-list'][ii]['id']
        sort = art['artist-list'][ii]['sort-name']
        extScore = art['artist-list'][ii]['ext:score']
        nombre = art['artist-list'][ii]['name']
        typeC = art['artist-list'][ii]['area']['type']
        ii = ii+1
        ar = artista(id=ii,area=area,typeC=typeC,nombre=nombre,sort=sort,idd=id,extScore=extScore)
        guardarArt(ar)

def buscarDisco():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
    nombres = mostrarNombres()
    x = 0
    di = []
    for i in nombres:
        disco = musicbrainzngs.search_releases(artist=i, country='US', limit=5)
        for disc in disco['release-list']:
            discoss = disc['release-group']['title']
            di.clear()
            di.append(discoss)
        x=x+5
        cadena = " ".join(di)
        guardarDisco(x, i, cadena)

def guardarDisco(id, nombre, disco):
    try:
        conexion = sqlite3.connect('baseBandas.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO discos VALUES ('{}','{}','{}')".format(id,nombre,disco))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def guardarArt(artt):
    try:
        conexion = sqlite3.connect('baseBandas.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO artistas VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(artt._id,artt._area,artt._typeC,artt._nombre,artt._sort,artt._idd,artt._extScore))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión a SQLite cerrada\n')

def mostrarNombres():
    try:
        conexion = sqlite3.connect('baseBandas.db')
        cursor = conexion.cursor()
        uMostrar = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for u in uMostrar:
            u = artista(id=u[0],area=u[1],typeC=u[2],nombre=u[3],sort=u[4],idd=u[5],extScore=u[6])
            art.append(u._nombre)
        conexion.commit()
        cursor.close()

        return art

    except sqlite3.Error as error:
        print('Error con la conexión!', error)
    finally:
        if (conexion):
            conexion.close()

def main():
    #buscarArt()
    buscarDisco()

if __name__ == '__main__':
    main()