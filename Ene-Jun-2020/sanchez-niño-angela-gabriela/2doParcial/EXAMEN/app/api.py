import requests
import json
from random import randrange

class PERSONAJE(object):

    def __init__(self):
        self.ENDPOINT = 'https://www.breakingbadapi.com/api/characters'
    
    def get_count(self):
        if self.COUNT:
            return self.COUNT

        r = requests.get(self.ENDPOINT)
        self.COUNT = r.json().get('count', 0)

        return self.COUNT

    def get_personaje(self, x):
        uri = f'{self.ENDPOINT}/{x}'
        r = requests.get(uri)
        data = r.json()

        return {
             'id': json.dumps(num),
            'name':data.get('nombre'),
            'fechaNac':data.get('fechanac'),
            'occupation':data.get('ocupacion'),
            'imagen': data.get('imagen'),
            'status':data.get('estatus'),
            'nickname':data.get('nickname'),
            'apparence':data.get('apariciones'),
            'actor':data.get('actor'),
            'category': data.get('categoria')
}
          



