import requests
import json

class breakingAPI(object):
    def __init__(self):
        self.url = "https://www.breakingbadapi.com/api/characters"
    
    def get_character(self):
        r = requests.get(self.url)
        data = r.json()
        characters = []
        for i in data:
            characters.append({
                "nombre":i.get("name"),
                "fechaNac":i.get("birthday"),
                "ocupacion": [j for j in i.get("occupation")],
                "imagen": i.get("img"),
                "estado": i.get("status"),
                "nickname": i.get("nickname"),
                "apariciones": [j for j in i.get("appearance")],
                "actor": i.get("portrayed"),
                "categoria": i.get("category") 
            })
        return characters
        
    