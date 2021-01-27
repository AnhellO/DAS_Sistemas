import requests
import json

#url ='https://www.breakingbadapi.com/api/characters'
class Personaje(object):
    COUNT = 0

    def getCharacter(self):
        req =requests.get('https://www.breakingbadapi.com/api/characters')
        res = req.json()
        inf = []
        for i in res:
            id = i['char_id']
            name = i['name']
            birthday = i['birthday']
            occupation = i['occupation']
            img = i['img']
            status = i['status']
            nickname = i['nickname']
            portrayed = i['portrayed']
            category = i['category']

            info = {
                'id': id, 'name': name, 
                'birthday': birthday, 'occupation': occupation, 
                'img': img, 'status': status,'nickname': nickname,
                'portrayed': portrayed, 'category': category}       
            inf.append(info)
        return inf

    def countCharacters(self):
        if self.COUNT:
            return self.COUNT

            req =requests.get('https://www.breakingbadapi.com/api/characters')
            self.COUNT = req.json().get('count', 0)
            data = self.COUNT
            return data


char = Personaje()
#print(json.dumps(char.getCharacter(), indent=2))
#print(char.countCharacters())
