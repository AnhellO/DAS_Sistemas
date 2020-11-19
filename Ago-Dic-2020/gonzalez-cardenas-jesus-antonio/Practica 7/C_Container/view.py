import pymongo
import json
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Index():
    client = pymongo.MongoClient("mongodb://mongo:27017/")
    db = client["persons"]  
    some_persons = db.persons.find()
    some_person = some_persons[random.randrange(100)]
    some_person = format_data(some_person)
    return render_template('index.html', person = some_person)

def format_data(data_person:dict):
    person_info = {
    'user_name' : data_person.get('person').get('online_info').get('username'),
    'e_mail': data_person.get('person').get('online_info').get('email'),
    'name':data_person.get('person').get('personal').get('name'),
    'last_name':data_person.get('person').get('personal').get('last_name'),
    'age':data_person.get('person').get('personal').get('age'),
    'number':data_person.get('person').get('personal').get('cellphone'),
    'country':data_person.get('person').get('personal').get('country')
    }
    return person_info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)