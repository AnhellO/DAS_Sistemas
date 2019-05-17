import requests
import json

def main():
    response = requests.get('https://randomuser.me/api/?results=100')
    if response.status_code == 200:
        response_json = json.loads(response.text)
        results = response_json['results']
        for answer in results:
            with open('RandUser.json', 'a') as fp:
                json.dump(answer, fp)
        print(results)
if __name__ == '__main__':
    main()
