from flask import Flask, render_template, jsonify
from mongo import mongo
import json
# from persona import persona
import time
app = Flask(__name__, static_url_path='/static')
cliente=mongo()

peoples=cliente['mydb']['people'].find()

def parsePerson(person):
    return  {
            'id':person['id'],
            'first_name':person['first_name'],
            'last_name':person['last_name'],
            'company':person['company'],
            'email':person['email'],
            'ip_address':person['ip_address'],
            'phone_number':person['phone_number']
    }

def getPeoplesFromDB(peoples):
    x   = []
    for p in peoples:
        x.append(
            parsePerson(p)
        )
    return x

def getPersonFromDB(id):
    person=cliente['mydb']['people'].find_one({"id": str(id)})
    return parsePerson(person)

x=getPeoplesFromDB(peoples)

@app.route('/')
def index():
    return render_template('index.html',personas =x)


@app.route('/people')
def people():
    return jsonify(x)

@app.route('/people/<string:idPerson>')
def heroById(idPerson):
    if(idPerson.isdigit()):
        if(0<int(idPerson)<1001):
            try:
                persona=getPersonFromDB(idPerson)      
                return persona
            except:
                return jsonify({'status':500})
    return jsonify({'status':500})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)