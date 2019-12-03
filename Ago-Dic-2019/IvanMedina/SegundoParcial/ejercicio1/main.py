import requests
import musicbrainzngs
import dbconnection
from artist import artist
from disk import disk
from apiconnection import apiconnection
from dbconnection import dbconnection



if __name__ == '__main__':
    musicbrainzngs.set_useragent('musicrainzngs','2.0')
    bdd=dbconnection("database.db")
    api=apiconnection()
    print("\nobteniendo 100 artistas diferentes de 'Los Angeles' 'Metal' o 'Rock' ... <<<<<<<<<< \n")
    result=api.searach_Artist_in_Area("Los Angeles","us",['rock','metal'],100)
    artists=api.resultToArtistObj(result)
    print("\nobtenido, Limpiando base de datos.. <<<<<<<<<< \n ")
    bdd.cur.execute("DELETE FROM disk;")
    bdd.cur.execute("DELETE FROM artist;")
    bdd.con.commit()
    print("\nLimpia y almacenando.. <<<<<<<<<< \n")
    bdd.storeArtist(artists)
    print("\nAlmacenados <<<<<<<<<< \n")
    print("\nobteniendo de la base de datos e imprimiendo... <<<<<<<<<< \n" )
    print(bdd.printBDD(bdd.getArtistFromDB()))
    print("\nobteniendo (5) discos para cada artista (solo de eu) ... <<<<<<<<<< \n")
    diskera=[]
    for disks in artists:
        diskera.append(musicbrainzngs.search_releases(artist=disks.name, country='us', limit=5))
    print("\nobtenida, imprimiendo ... <<<<<<<<<< \n")
    disks=api.resultToDiscObj(diskera)
    print("\nguardando en base de datos ... <<<<<<<<<< \n")
    bdd.storeDisk(disks)
    print("\n>Almacenado, imprimiendo ... <<<<<<<<<< \n")
    bdd.getDiskFromDB()
    print(bdd.printBDD(bdd.getDiskFromDB()))
    print("\n>Fin ejercicio 1 ... <<<<<<<<<< \n")
