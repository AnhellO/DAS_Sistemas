import requests
import json
import os

class RandomUserApi():
    def getRandomUser(self):
        response = requests.get(url = "https://randomuser.me/api/?results=130")
        return response.json()

    def createJson(self, data):
        file_name = "users.json"
        if os.path.isfile(file_name):
            os.remove(file_name)

        with open(os.path.join(file_name), 'w', encoding='utf-8') as file:
            json.dump(data, file)

def main():
    rnd_user = RandomUserApi()
    response = rnd_user.getRandomUser()
    rnd_user.createJson(response)

if __name__ == "__main__":
    main()
