from crypt import methods
import pymongo
from flask import Flask

client = pymongo.MongoClient("mongodb://root:Parc@BaseDeDatos:32569/")

db = client["Issues"]
closed = db["Closed"]

open = db["Open"]

app = Flask(__name__)
app.config["Debug"] = True

@app.route('/', methods=["get"])

def PAge():
    pagina = ""
    PagSup = "<table><tr><td>Id</td><td>State</td><td>Title</td>"
    for opens in open.find():
        pagina+= f"<tr><td>{opens['_id']}</td><td>{opens['state']}</td><td><a href='/Open/{opens['_id']}'>{opens['title']}</a></td>"
    for close in closed.find():
        pagina+= f"<tr><td>{close['_id']}</td><td>{close['state']}</td><td><a href='/Closed/{close['_id']}'>{close['title']}</a></td>"
    pagina = pagina +"</table>"
    contenido = PagSup + pagina
    return contenido

@app.route('/Open/<int:id>')
def mostrarOpen(id):
    pag = "<table border: 1px solid black>"
    result = open.find_one({'_id': id})
    result = dict(result)
    for key, value in result.items():
        pag += f"<tr><td>{key}</td><td>{value}</td></tr>"
    pag += "</table>"
    return pag

@app.route('/Closed/<int:id>')
def mostrarClosed(id):
    pag = "<table border: 1px solid black>"
    result = closed.find_one({'_id': id})
    result = dict(result)
    for key, value in result.items():
        pag += f"<tr><td>{key}</td><td>{value}</td></tr>"
    pag += "</table>"
    return 