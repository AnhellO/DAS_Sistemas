import pymongo
from flask import Flask, jsonify

# Creamos conexión a MongoDB
client = pymongo.MongoClient("mongodb://root:ejemplo123@mongo_compose:27017/")
db = client["practica"]
coll = db["people"]

# Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/people', methods=["GET"])
def people():
    return jsonify([person for person in coll.find()])

@app.route('/people/<person_id>', methods=["GET"])
def person(person_id):
    return jsonify(coll.find_one({'_id': person_id}))
        