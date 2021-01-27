from modelsMarvel import *

class querys():

    def __init__(self):
        self.schema={
        'id':"",
        'name':"",
        'image':"",
        'powerstats':{'combat':"", 'durability':"", 'intelligence':"",'power':"",'speed':"",'strength':""},
        'appearance':{'eyeColor':"",'gender':"", 'hairColor':"",'height':"",'race':"",'weight':"" },
        'biography':{'aliases':"",'alignment':"",'alterEgos':"",'firstAppearance':"",'fullName':"",'placeOfBirth':"",'publisher':""},
        'connections':{'groupAffiliation':"",'relatives':""},
        'work':{'base':"",'occupation':""}                    
        }
   
        


    def existId(self,id):# CACHEAR QUERY
        print("from existId Postgres")
        try:          
            hero=heroes.select(heroes.id).where(heroes.id==id) 
            herod=hero.dicts()
            if (len(herod)>0):
                return id
            return 0
        except:
            return 1

    def getIdsSet(self):
        print("from getIdsSet Postgres")
        ids=[]
        try:
            heroesIds=heroes.select(heroes.id)
            heroesd=heroesIds.dicts()
            if (len(heroesd)>0):
                for row in heroesd:
                    for x, y in row.items():
                        ids.append(y)

            return ids
        except:
            print("error")
            return 0    

    def getHeroes1(self): #CACHEAR QUERY
        print("from getHeroes1 Postgres")
        try:
            hero=heroes.select(heroes.id, heroes.name)
            herod=hero.dicts()
            heroesL={}
            if (len(herod)>0):
                for heroi in range(len(herod)):
                    # for x,y in row.items():
                    myHero={}
                    heroesL[herod[heroi]['id']]=herod[heroi]['name']         
                return heroesL
            return 0
        except:
            print("error")
            return 0

    def getHero(self,id): #from database get all in one table
        print("from getHero Postgres")
        if(str(id).startswith('hero:')):
            id=str(id)[5:]
        try:
            hero=heroes.select()
            pwr=powerstats.alias()
            bio=biography.alias()
            her=heroes.alias()
            hero=(heroes
                .select( heroes, powerstats, biography, appearance, connections, work)
                .join(powerstats)
                .switch(heroes)
                .join(biography)
                .switch(heroes)
                .join(appearance)
                .switch(heroes)
                .join(connections)
                .switch(heroes)
                .join(work)
                .where(heroes.id==id))
            herod=hero.dicts()
            if(len(herod)>0):
                len(herod)
                myHero={}
                for key,value in herod[0].items():
                    myHero[key]=value
                return myHero
            return 0
        except:
            print("error")
            return 0        

    def heroToSchema(self,hero):
        schemaR={
        'id':hero['id'],
        'name':hero['name'],
        'image':hero['image'],
        'powerstats': {k:v for (k,v) in hero.items() if k in self.schema['powerstats'] },
        'appearance': {k:v for (k,v) in hero.items() if k in self.schema['appearance'] },
        'biography':  {k:v for (k,v) in hero.items() if k in self.schema['biography'] },
        'connections':{k:v for (k,v) in hero.items() if k in self.schema['connections'] },
        'work':       {k:v for (k,v) in hero.items() if k in self.schema['work'] }           
        }
        return schemaR

