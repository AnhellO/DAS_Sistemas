from peewee import *
from playhouse.shortcuts import model_to_dict
from modelsMarvel import *
from marvelAPI import marvelAPI
import time

def main():

    COUNT=735
    TRY=0
    LIM_TRY=10
    SEC=10
    api=marvelAPI()
    while(TRY<LIM_TRY):
        if (thereConnection()==1):    
            print("\n\n"+"*"*60+"\n"+"*"*60+"\n\t\t+++ CONECTION SUCCESSFUL +++\n\n"+"*"*60+"\n"+"*"*60+"\n")    
            createTables()
            for i in range(1, COUNT, 1):
                try:
                    raw_hero = api.getHero(i)         
                    if raw_hero:
                        if (raw_hero['biography']['publisher']=='Marvel Comics' or raw_hero['biography']['publisher']=='Captian Marvel'):
                            hero, created = heroes.get_or_create(id=raw_hero['id'], name=raw_hero['name'], image=raw_hero['image'])
                            if created:
                                powerstats.create(id=hero.id, **raw_hero['powerstats'])
                                work.create(id=hero.id, **raw_hero['work'])
                                connections.create(id=hero.id, groupAffiliation=raw_hero['connections']['group-affiliation'], relatives=raw_hero['connections']['relatives'])
                                biography.create(id=hero.id,  **raw_hero['biography'], alterEgos=raw_hero['biography']['alter-egos'], fullName=raw_hero['biography']['full-name'],
                                firstAppearance=raw_hero['biography']['first-appearance'], placeOfBirth=raw_hero['biography']['place-of-birth'])
                                appearance.create(id=hero.id, **raw_hero['appearance'], eyeColor=raw_hero['appearance']['eye-color'], hairColor=raw_hero['appearance']['hair-color'])
                            print(f"Hero {'Created' if created else 'Existing'}: {raw_hero['name']}")
                except:
                    print("ERROR IN GET HERO "+str(i))
            TRY=LIM_TRY
        else:
            TRY=TRY+1
            print("\n"+("*"*60)+"\n\t\t>>>  ERROR IN CONNECTION ("+str(TRY)+"/"+str(LIM_TRY)+")\n\t\tTRYING IN "+str(SEC)+" SECONDS <<<\n"+"*"*60+"\n")         
            time.sleep(SEC)

def thereConnection():
    try: 
        conn=psql_db.connect()
        return conn
    except:
     
        return 0
    
   

def createTables():
    try:
        heroes.create_table()
        powerstats.create_table()
        work.create_table()
        connections.create_table()
        biography.create_table()
        appearance.create_table()    
        print("\n\n"+"*"*60+"\n"+"*"*60+"\n\t\t+++ TABLES CREATION SUCCESSULL +++\n\n"+"*"*60+"\n"+"*"*60+"\n")
        return 1

    except Exception as e:
        print(e)
        print("\n"+"*"*60+"\n\t\t--- TABLES CREATION ERROR ---\n"+"*"*60+"\n")
        return 0

if __name__ == '__main__':
    main()
    psql_db.close()
