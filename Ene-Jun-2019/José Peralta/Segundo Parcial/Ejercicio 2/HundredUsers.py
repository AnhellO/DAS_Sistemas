import requests
import json

if __name__ == '__main__':
    response = requests.get('https://randomuser.me/api/?results=100')
    if response.status_code == 200:
        response_json = json.loads(response.text)
        results = response_json['results']

        with open('RandomUsers.json', 'w') as fp:
            json.dump({'results':results}, fp)
