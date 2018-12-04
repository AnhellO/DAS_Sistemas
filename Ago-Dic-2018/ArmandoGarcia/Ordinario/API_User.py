import requests
from abstractUsuario import *
import json
class API_User(AbstracUsers):
    def get_user(self,url):
        request = requests.get(url)
        r = request.json()
        name=r['results'][0]['name']['first']
        email=r['results'][0]['email']
        phone=r['results'][0]['phone']
        picture=r['results'][0]['picture']['medium']
        location=r['results'][0]['location']['street']
        return Users(name,email,phone,picture,location)

if __name__ == '__main__':
    x=API_User()
    urs = x.get_user('https://randomuser.me/api/')
    print(urs.picture)
