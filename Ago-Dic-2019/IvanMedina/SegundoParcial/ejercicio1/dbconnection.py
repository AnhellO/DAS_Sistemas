from artist import artist
from disk import disk
import sqlite3


class dbconnection():

    con=None
    cur=None

    def __init__(self,namedb):
        try:
           print(namedb)
           self.con = sqlite3.connect(namedb)
           self.cur = self.con.cursor()
           print("Conectado a SQLite")
           query ="CREATE TABLE IF NOT EXISTS artist (area text, date text, nombre text, gender text, type text, text score, id INTEGER PRIMARY KEY AUTOINCREMENT);"
           self.cur.execute(query)
           query="CREATE TABLE IF NOT EXISTS disk (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, aritst TEXT, country TEXT);"
           self.cur.execute(query)
           self.con.commit()

        except:
           if(self.con):
               self.con.close()
               print("SQL Connection error")



    def storeArtist(self,artistList):
        try:
            for artist in artistList:
                self.cur.execute("INSERT INTO artist VALUES (?,?,?,?,?,?,?)",(artist.area,artist.date,artist.name,artist.gender,artist.type,artist.score,None))
            self.con.commit()
        except:
            print("Error trying store ")

    def storeDisk(self,disktList):
        # try:
        for disk in disktList:
            print(disk)
            self.cur.execute("INSERT INTO disk VALUES (?,?,?,?)",(None,disk.name,disk.artist,disk.country))
        self.con.commit()
        # except:
        #     print("Error trying store ")

    def getArtistFromDB(self):
        try:

            showArtists = self.cur.execute("SELECT * from artist").fetchall()
            print(showArtists)
            artists = []
            i = 0
            for t in showArtists:
                artists.append(artist(t[0], t[1], t[2], t[3], t[4],t[5]))
                i+=1
            if len(artists)>0:
                return artists

            print("Nada que mostrar")
            return 1
        except:
            print("Error en consulta de playlist")
            return 1


    def getDiskFromDB(self):
        try:

            showDisk = self.cur.execute("SELECT * from disk").fetchall()
            disks = []
            i = 0
            for t in showDisk:
                disks.append(disk(t[0], t[1], t[2]))
                i+=1
            if len(disks)>0:
                return disks

            print("Nada que mostrar")
            return 1
        except:
            print("Error en consulta de playlist")
            return 1

    def printBDD(self,artists): #imprimir playlist desde la bdd
        if len(artists)<1:
            print("Nada en tu lista")
            return 1
        play_String=""
        i=0
        for t in artists:
            if i==len(artists)-1:
                play_String+="{["+str(i)+"]"+str(t)+"}"
            else:
                play_String+="{["+str(i)+"]"+str(t)+"}\n"
                i=i+1
        return play_String
