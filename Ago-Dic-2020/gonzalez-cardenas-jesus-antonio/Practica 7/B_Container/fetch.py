import requests
import pprint
import json
import pymongo

api_url = 'https://pipl.ir/v1/getPerson'
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["persons"]

def get_some_data():
    r= requests.get(api_url)
    data = r.content
    actual_json = json.loads(data)
    return actual_json

def insert_some_data(_data:list):
    db.persons.insert_many(_data)
    

def export_data_to_file(_data:list):
    file = open("data_in_db.json","w+")
    for x in range(len(_data)):
        file.write(json.dumps(_data[x],indent=2))
    file.close()

def main():
    amount = 100
    data_list = []
    for x in range(amount):
        data_list.append(get_some_data())
    
    insert_some_data(data_list)
    # export_data_to_file(data_list)
    # pprint.pprint(get_some_data())

if __name__ == "__main__":
    main()

