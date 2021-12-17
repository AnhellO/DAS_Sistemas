from flask import Flask, jsonify
from app import appDB

#creamos un objeto flask en el objeto
app = Flask(__name__)

apk = appDB('user','pass1234','localhost','prueba','3306')
response = apk.imprimir()

#definimos la ruta
@app.route('/', methods=['GET'])
def get_user():
    for i in range(len(response)):
        return jsonify({"hola":"hahahah"})
    #if request.method == "GET":
    #return jsonify(response[int(id)]) #utilizamos el webscraping

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)