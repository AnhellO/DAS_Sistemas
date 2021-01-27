import time
from modelslast import *

import lastfmAPI as lastfmAPI

from app.lastfmAPI import artist
from app.modelslast import psql_db, track, playlist, biography


def main():

    COUNT=100
    TRY=0
    LIM_TRY=10
    SEC=10
    api=lastfmAPI()
    while(TRY<LIM_TRY):
        if (thereConnection()==1):    
            print("\n\n"+"*"*60+"\n"+"*"*60+"\n\t\t+++ CONECTION SUCCESSFUL +++\n\n"+"*"*60+"\n"+"*"*60+"\n")    
            createTables()
            for i in range(1, COUNT, 1):
                try:
                    raw_artist = api.getartist(i)

                except:
                    print("ERROR IN GET ARTIST "+str(i))
            TRY=LIM_TRY
        else:
            TRY=TRY+1
            print("\n"+("*"*60)+"\n\t\t>>>  ERROR IN CONNECTION ("+str(TRY)+"/"+str(LIM_TRY)+")\n\t\tTRYING IN "+str(SEC)+" SECONDS <<<\n"+"*"*60+"\n")         
            time.sleep(SEC)

def thereConnection():
    try:
        conn = psql_db.connect()
        return conn
    except:

        return 0
    
   

def createTables():
    try:
        artist.create_table()
        track.create_table()
        playlist.create_table()
        biography.create_table()
        country.create_table()
        print("\n\n"+"*"*60+"\n"+"*"*60+"\n\t\t+++ TABLES CREATION SUCCESSULL +++\n\n"+"*"*60+"\n"+"*"*60+"\n")
        return 1

    except Exception as e:
        print(e)
        print("\n"+"*"*60+"\n\t\t--- TABLES CREATION ERROR ---\n"+"*"*60+"\n")
        return 0

if __name__ == '__main__':
    main()
    psql_db.close()
