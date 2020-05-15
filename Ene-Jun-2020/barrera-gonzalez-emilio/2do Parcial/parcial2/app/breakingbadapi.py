import requests
import json

class breaking_bad_API(object):
    
    def __init__(self):
        self.ENDPOINT = "https://www.breakingbadapi.com/api/characters"
    
    def get_characters(self):
        uri = self.ENDPOINT
        r = requests.get(uri)
        data = r.json()
        return_value=[]
        for i in data:
            char_id = i['char_id']
            char_name = i['name']
            char_bd = i['birthday']
            char_oc= ""
            if len(i['occupation'])==0:
                char_oc = "None"
            elif len(i['occupation']) ==1:
                char_oc = i['occupation'][0]
            else: 
                for a in i['occupation']:
                    char_oc += str(a) + ',' 
            char_img = i['img']
            char_status = i['status']
            char_nickname = i['nickname']
            char_appearance= ""
            if len(i['appearance'])==0:
                char_appearance = "None"
            elif len(i['appearance']) ==1:
                char_appearance = i['appearance'][0]
            else:
                for a in i['appearance']:
                    char_appearance += str(a) + ',' 
            char_portrayed = i['portrayed']
            char_category = i['category']
            char_bcs_a=""
            if len(i['better_call_saul_appearance'])==0:
                char_bcs_a = "None"
            elif len(i['better_call_saul_appearance']) ==1:
                char_bcs_a = i['better_call_saul_appearance'][0]
            else:
                for a in i['better_call_saul_appearance']:
                    char_bcs_a += str(a) + ','

            dictionary = {
                'char_id': char_id,
                'char_name': char_name,
                'char_bd': char_bd,
                'char_oc': char_oc,
                'char_img': char_img,
                'char_status': char_status,
                'char_nickname': char_nickname,
                'char_appearance': char_appearance,
                'char_portrayed': char_portrayed,
                'char_category': char_category,
                'char_bcs_a': char_bcs_a 
            }
            return_value.append(dictionary)
        
        return return_value

#TESTS
if __name__ == "__main__":
    api = breaking_bad_API()
    print(api.get_characters())