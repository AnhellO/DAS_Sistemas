import requests
import json


class BB_Chars_API(object):

    def __init__(self):
        self.ENDPOINT = "https://www.breakingbadapi.com/api/characters"

    def get_characters(self):
        uri = self.ENDPOINT
        r = requests.get(uri)
        data = r.json()
        information = []
        for i in data:
            id = i['char_id']
            name = i['name']
            birthday = i['birthday']
            occupation = ""
            if len(i['occupation']) == 0:
                occupation = "None"
            elif len(i['occupation']) == 1:
                occupation = i['occupation'][0]
            else:
                for a in i['occupation']:
                    occupation += str(a) + '-'
            img = i['img']
            status = i['status']
            nickname = i['nickname']
            appearance = ""
            if len(i['appearance']) == 0:
                appearance = "None"
            elif len(i['appearance']) == 1:
                appearance = i['appearance'][0]
            else:
                for a in i['appearance']:
                    appearance += str(a) + '-'
            portrayed = i['portrayed']
            category = i['category']

            dictionary = {
                'id': id, 'name': name, 'birthday': birthday, 'occupation': occupation, 'img': img,
                'status': status, 'nickname': nickname, 'appearance': appearance, 'portrayed': portrayed,
                'category': category,
            }
            information.append(dictionary)

        return information


if __name__ == "__main__":
    api = BB_Chars_API()
    print(json.dumps(api.get_characters(), indent=2))
