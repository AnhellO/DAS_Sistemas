import requests
import json


class marvelAPI():

    def __init__(self):    
        self.TOKEN='10220039278206178'
        self.ENDPOINT = 'https://www.superheroapi.com/api.php/'+self.TOKEN+'/'
        self.ID =0

    def getHero(self, x):
        r = requests.get(self.ENDPOINT+str(x))
        if r.status_code != 200:
            raise Exception(f"Hero {self.ENDPOINT}/{x} doesn't exist in the API :(")

        data = r.json()   
        id=data.get('id')
        name=data.get('name')
        image=data.get('image').get('url')
        powerstats=self.getPowerstats(data.get('powerstats'))
        appearance=self.getAppearance(data.get('appearance'))
        biography=self.getBiography(data.get('biography'))
        work=self.getWork(data.get('work'))
        connections=self.getConnections(data.get('connections'))        
        return {'id':id, 'name':name , 'image': image,'powerstats':powerstats,'appearance':appearance, 'biography':biography,'work':work, 'connections':connections }
    
    def getPowerstats(self, powerstats):
        combat=powerstats.get('combat')
        durability=powerstats.get('durability')
        intelligence=powerstats.get('intelligence')
        power=powerstats.get('power')
        speed=powerstats.get('speed')
        strength=powerstats.get('strength')
        return {'combat':combat , 'durability': durability, 'intelligence':intelligence,'power':power, 'speed':speed, 'strength':strength}
    
    
    def getAppearance(self, apparance):
        eyeColor=apparance.get('eye-color') 
        gender=apparance.get('gender')
        hairColor=apparance.get('hair-color')
        height=str(apparance.get('height'))
        race=apparance.get('race')
        weight=str(apparance.get('weight'))
        return {'eye-color':eyeColor , 'gender': gender, 'hair-color':hairColor, 'height':height, 'race':race, 'weight':weight}
    
    def getBiography(self, biography):
        aliases=str(biography.get('aliases'))
        alignment=biography.get('alignment')
        alterEgos=str(biography.get('alter-egos'))
        firstAppearance=biography.get('first-appearance')
        fullName=biography.get('full-name')
        placeOfBirth=biography.get('place-of-birth')
        publisher=biography.get('publisher')
        return {'aliases':aliases , 'alignment': alignment, 'alter-egos':alterEgos, 'first-appearance':firstAppearance, 'full-name':fullName, 'place-of-birth':placeOfBirth,'publisher':publisher}
    
    def getWork(self, work):
        base=work.get('base')
        occupation=work.get('occupation')
        return {'base':base , 'occupation': occupation}
    
    def getConnections(self,connections):
        groupAffiliation=str(connections.get('group-affiliation'))
        relatives=connections.get('relatives')
        return {'group-affiliation':groupAffiliation , 'relatives': relatives}
    

