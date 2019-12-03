"""Crea un script en Python que consuma datos de la siguiente API https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2
Deberás de leer la documentación de la API para saber como funciona y como utilizarla
Ejemplo de endpoint de la API -> http://musicbrainz.org/ws/2/artist/020bfbb4-05c3-4c86-b372-17825c262094?fmt=json

Los datos consumidos deberán de ser guardados en una base de datos de SQLite. Los datos que deberás de obtener son los siguientes:
Todas las bandas cuyo area.name = "Los Angeles"
Las bandas deben de tener tags con la palabra rock y/o metal incluído en el name del tag
Debes de almacenar al menos 5 campos extras aparte del nombre de la banda en una tabla llamada artistas o similar
Guarda al menos 100 artistas diferentes en la base de datos
Para cada una de las bandas deberás de almacenar los discos que lanzaron exclusivamente en los US (country = "US"),
en otra tabla por separado a la de artistas"""

import sqlite3
import musicbrainzngs
import pprint
from arttista import artista
import json


def buscarArtista():
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
        art = artista(id=ii,area=area,typeC=typeC,nombre=nombre,sort=sort,idd=id,extScore=extScore)
        guardarArtista(art)

def guardarArtista(artt):
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO artistas VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(artt._id,artt._area,artt._typeC,artt._nombre,artt._sort,artt._idd,artt._extScore))

        conexion.commit()
        cursor.close()
    except sqlite3.Error as error:
        print('Error con la conexión', error)
    finally:
        if (conexion):
            conexion.close()
            print('Conexión cerrada\n')

def viewNombres():
    try:
        conexion = sqlite3.connect('bandas.db')
        cursor = conexion.cursor()
        viewnom = cursor.execute("SELECT * from artistas").fetchall()
        art = []

        for u in viewnom:
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

def buscarDisco():
    musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
    nombres = viewNombres()
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
        conexion = sqlite3.connect('bandas.db')
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
            print('Conexión cerrada\n')

def main():
    buscarArtista()
    buscarDisco()
if __name__ == '__main__':
    main()