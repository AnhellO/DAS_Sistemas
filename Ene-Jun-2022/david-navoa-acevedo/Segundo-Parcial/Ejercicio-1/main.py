
import requests
from flask import Flask, jsonify, request

try: 
    from pymongo import mongo_client
except ImportError:
    raise ImportError('pymongo is not installed...')

class MongoDB(object):
    #database_name = Flask, collection_name = issues
    def __init__(self, host='localhost', port=27017, database_name=None, collection_name=None):
        try:
            self._connection = mongo_client(host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def insert(self, lista):
        # add/append/new single record
        post_id = self._collection.insert_many([lista])
        return post_id

def insert(dicc):
    mongo_db = MongoDB(database_name='Flask', collection_name='issues')
    dic = {}
    listilla = []
    for item in dicc:
            for key, value in item.items():
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        dic.update({ckey2:value2})
                else:
                    dic.update({key:value})
            listilla.append(dic)
            dic = {}
    for lista in listilla:
            print(mongo_db.insert(lista))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["GET"])
def issues():
    url = "https://api.github.com/repos/pallets/flask/issues"
    response = requests.get(url).json()
    insert(response)

