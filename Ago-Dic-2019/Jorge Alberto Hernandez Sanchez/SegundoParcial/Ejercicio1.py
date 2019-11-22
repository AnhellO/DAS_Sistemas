import musicbrainzngs
import webbrowser
import requests
import sqlite3
import pprint
class dbartistas():
    #Creando base de datos
    def CreacionTabla():
        try:
            conexion = sqlite3.connect('baseapimusica.db')
            cursor = conexion.cursor()
            print("Conectado a SQLite")
            query = "CREATE TABLE artistas(idartist text, name text, area text, lifespan text, score int, sortname text)"
            cursor.execute(query)
            conexion.commit()
        finally:
            if(conexion):
                conexion.close()
                print("Conexion a SQLite cerrada")


    #rellenando tabla artistas
    def agregar():
        musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
        a = musicbrainzngs.search_artists(artist="xx", area='Los Angeles',country="us",tag=['rock','metal'],limit=100)
        try:
            conexion = sqlite3.connect('baseapimusica.db')
            cursor = conexion.cursor()
            print("Conectado a SQLite")
            j = 0
            for i in a['artist-list']:
                query = "INSERT INTO artistas(idartist, name, area, lifespan, score, sortname) VALUES({},{},{},{},{},{})".format(
                idartist = None,
                nombre = a['artist-list'][j]['area']['name'],
                area = a['artist-list'][j]['area']['type'],
                lifespan = a['artist-list'][j]['life-span'],
                score = a['artist-list'][j]['ext:score'],
                sortname = a['artist-list'][j]['sort-name'])
                j = j + 1
                conexion.execute(query)
                conexion.commit()
        finally:
            if(conexion):
                conexion.close()
                print("Conexion a SQLite cerrada")

    #mostrando datos de la tabla
    def seleccionar():
        try:
            conexion = sqlite3.connect('baseapimusica.db')
            cursor = conexion.cursor()
            print("Conectado a SQLite")
            query = "SELECT * FROM artistas"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        finally:
            if(conexion):
                conexion.close()
                print("Conexion a SQLite cerrada")
#pprint.pprint(a)
#for i in range(0,99):
#    pprint.pprint(b['artist-list'][i]['type'])
#    print("------------------------------------", i)
#print(b)
#pprint.pprint(a)
#pprint.pprint(a['artist-list'][0]['tag-list'])
#print("----------------------------------------------------")
#pprint.pprint(a['artist-list'][1]['tag-list'])
#print("----------------------------------------------------")
#pprint.pprint(a['artist-list'][2]['tag-list'])
#b = musicbrainzngs.search_recordings(country="US", limit= 1)
class dbDiscos():
    def getdiscos(diccionario):
        musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
        a = diccionario
        albums = []
        nombres = get_nombres(a)
        for i in nombres:
            album = musicbrainzngs.search_releases(artist=i, country="us",tag=['rock','metal'],limit=100)
            for k in album['release-list']:
                    albums.append(k["release-group"]["title"])
        return albums

    def get_nombres(diccionario):
        musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
        nombres = []
        for j in range(0,99):
            nombres.append(a['artist-list'][j]['area']['name'])
            return nombres


    def creacion_tabla_discos():
        try:
            conexion = sqlite3.connect('discosapimusica.db')
            cursor = conexion.cursor()
            print("Conectado a SQLite")
            query = "CREATE TABLE discos(iddisco int, nombre_Artista VARCHAR(255), disco VARCHAR(255))"
            cursor.execute(query)
            conexion.commit()
        finally:
            if(conexion):
                conexion.close()
                print("Conexion a SQLite cerrada")

    def agregar_discos(nombres, discos):
        musicbrainzngs.set_useragent('musicbrainzngs', '2.0')
        try:
            conexion = sqlite3.connect('discosapimusica.db')
            cursor = conexion.cursor()
            print("Conectado a SQLite")
            discoss = []
            for i in nombres:
                query = "INSERT INTO discos(iddisco, nombre_Artista, disco) VALUES({},{},{})".format(
                    iddisco = None,
                    nombre_Artisita = nombres[i]
                    for j in range(0, 3):
                        discoss.append(discos[j])
                    disc = str(discoss)
                    conexion.commit()
                    discoss.pop(0)
                    discoss.pop(1)
                    discoss.pop(2)
                )
                cursor.execute(query)
            conexion.commit()
        finally:
            if(conexion):
                conexion.close()
                print("Conexion a SQLite cerrada")

    def seleccionardiscos():
    try:
        conexion = sqlite3.connect('discosapimusica.db')
        cursor = conexion.cursor()
        print("Conectado a SQLite")
        query = "SELECT * FROM discos"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    finally:
        if(conexion):
            conexion.close()
            print("Conexion a SQLite cerrada")

"""
    a = musicbrainzngs.search_artists(artist="xx", area='Los Angeles',country="us",tag=['rock','metal'],limit=100)
    discos.getdiscos(a)
    nombres = get_nombres(a)
    """

class htmlDiscos:
    db = dbDiscos()
    def htmlprint():
        f = open('discos.html', 'w')

        discos = """<html>
        <head></head>
        <body><p>{}</p></body>
        </html>""".format(db.seleccionardiscos())
    f.write(mensaje)
    f.close()
    archivo = "C:\Users\jorge\Documents\Cursos\DAS_Sistemas\Ago-Dic-2019\Jorge Alberto Hernandez Sanchez\SegundoParcial\discosapimusica.db"
    webbrowser.open_new_tab(archivo)

def main():
    dbArt = dbartistas()
    
    dbArt.CreacionTabla()
    dbArt.agregar()
    dbArt.seleccionar()

    dbdisc = dbDiscos()
    dbdisc.creacion_tabla_discos()
    dbdisc.agregar_discos()
    dbdisc.creacion_tabla_discos()
    dbdisc.get_nombres()
    db.getdiscos()

    html = htmlDiscos()
    html.htmlprint()


if __name__ == "__main__":
    main()