import pymongo
from flask import Flask, jsonify, request

# Creamos conexión a MongoDB
client = pymongo.MongoClient("mongodb://root:ejemplo123@mongo_compose:27017/")
db = client["practica"]
coll = db["people"]

# Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello_world():
    return """
        <p>Hello, World!<br /></p>
        <p>Go to the API <a href="/people">here</a><br /></p>
    """

@app.route('/people', methods=["GET", "POST"])
def people():
    # Para debuggear la información
    app.logger.warning(request.data)
    app.logger.warning(request.json)
    if request.method == "GET":
        return jsonify([person for person in coll.find()])
    
    if request.method == "POST":
        p = create_person(request)
        result = coll.insert_one(p)
        return jsonify({
            'message': f'Resource created with ID: {result.inserted_id}',
            'result': p
        }), 201

@app.route('/people/<person_id>', methods=["GET"])
def person(person_id):
    p = coll.find_one({'_id': person_id})
    
    if p == None:
        return jsonify({'message': 'Resource does not exist'}), 404
    
    return jsonify(p)

def create_person(request):
    return {
        '_id': request.json['id'],
        'company': request.json['company'],
        'email': request.json['email'],
        'first_name': request.json['first_name'],
        'ip_address': request.json['ip_address'],
        'last_name': request.json['last_name'],
        'phone_number': request.json['phone_number']
    }