import requests
import pymongo

id_persona = 0
def fake_data():
    global id_persona
    URI = "https://pipl.ir/v1/getPerson"
    r = requests.get(URI)
    data = r.json()
    
    id_persona += 1
    return {
            'id': id_persona,
            'Name': data.get('person').get('personal').get('name'),
            'Education': data.get('person').get("education"),
            'Personal': data.get('person').get("personal"),
            'Work': data.get('person').get("work")
            }


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://mongo:27017/")
    db = client["mi-db"]

    db.person.insert_many([fake_data() for i in range(100)])