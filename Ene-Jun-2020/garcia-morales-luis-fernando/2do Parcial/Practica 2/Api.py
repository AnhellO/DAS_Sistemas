import requests
import json

class API(object):
    
    def __init__(self):
        self.ENDPOINT = 'https://age-of-empires-2-api.herokuapp.com/api/v1'

    def getCiv(self):
        civ = f'{self.ENDPOINT}/civilizations'
        r = requests.get(civ)
        data = r.json()
        civilizaciones = []
        for i in data.get("civilizations"):
            civilizaciones.append({
                "nombre":i.get("name"),
                "expansion": i.get("expansion"),
                "tipo": i.get("army_type")
            })
        return civilizaciones
    
    def getUni(self):
        uni = f'{self.ENDPOINT}/units'
        r = requests.get(uni)
        data = r.json()
        unidades = []
        for i in data.get("units"):
            unidades.append({
                "nombre":i.get("name"),
                "descripcion": i.get("description"),
                "expansion": i.get("expansion"),
                "edad": i.get("age"),
                "rango": i.get("range"),
                "ataque": i.get("attack")
            })
        return unidades
    
    def getEst(self):
        est = f'{self.ENDPOINT}/structures'
        r = requests.get(est)
        data = r.json()
        estructuras = []
        for i in data.get("structures"):
            estructuras.append({
                "nombre": i.get("name"),
                "expansion": i.get("expansion"),
                "edad": i.get("age"),
                "tiempo": i.get("build_time")
            })
        return estructuras
    
    def getTec(self):
        tec = f'{self.ENDPOINT}/technologies'
        r= requests.get(tec)
        data = r.json()
        tecnologias = []
        for i in data.get("technologies"):
            tecnologias.append({
                "nombre": i.get("name"),
                "descripcion": i.get("description"),
                "expansion": i.get("expansion"),
                "edad": i.get("age")
            })
        return tecnologias
