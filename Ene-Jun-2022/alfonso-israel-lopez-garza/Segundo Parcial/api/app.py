from crypt import methods
import pymongo
from flask import Flask, jsonify,json, Response, render_template

#Creando la conexion a la db y accediendo a la db
client = pymongo.MongoClient("mongodb://root:basedatos@Contenedor_B:27017/")
database = client["Issues"]
IssClosed = database["IssuesClosed"]
IssOpen = database["IsuessOpen"]
#Flask
app = Flask(__name__)
app.config["DEBUG"] = True

# Creando la ruta principal
@app.route('/')
def git():
    return """
    <h1>Issues </h1>
    <p> <a href="/IssuesOpen">Abiertos <-- Click aqui para ver los Issues con state:open</a></p>
    <p> <a href="/IssuesClosed">Cerrados <-- Click aqui para ver los Issues con state:closed</a></p>
    """

#Creando la pagina que muestra en una tabla los Issues cerrados (Id, titulo, url del repositorio, link para ver datos completos)
@app.route('/IssuesClosed', methods=["GET"])
def IssuresClosed():
    pagina = f"<h1>Cerrados<h1><table><tr style='background-color: #96D4D4;'><td>Id</td><td>Titulo</td><td>Url</td><td>Link</td></tr>"
    for closed in IssClosed.find():
        pagina+= f"<tr><td>{closed['_id']}</td><td>{closed['title']}</td><td>{closed['html_url']}</td>"
        pagina += f"<td><a href='/mostrarclosed/{closed['_id']}'>Mostrar Completo</a></td></tr>"
    pagina+= "</table>"
    return pagina


#Creando la pagina que muestra los datos completos del Issue seleccionado)
@app.route('/mostrarclosed/<int:id>')
def mostrar_issueclosed(id):
    pagina = f"<h1>Descripcion Completa</h1><table border: 1px solid black>"
    result = IssClosed.find_one({'_id': id})
    result = dict(result)
    for key, value in result.items():
        pagina += f"<tr><td style='background-color: #D1F2EB;>{key}</td><td>{value}</td></tr>"
    pagina += "</table>"
    return pagina


#Creando la pagina que muestra en una tabla los Issues abiertos (Id, titulo, url del repositorio, link para ver datos completos)
@app.route('/IssuesOpen', methods=["GET"])
def IssuresOpen():
    pagina = f"<h1>Abiertos<h1><table><tr style='background-color: #FAD7A0;'><td>Id</td><td>Titulo</td><td>Url</td><td>Link</td></tr>"
    for open in IssOpen.find():
        pagina += f"<tr><td>{open['_id']}</td><td>{open['title']}</td><td>{open['html_url']}</td>"
        pagina += f"<td><a href='/mostraropen/{open['_id']}'>Mostrar Completo</a></td></tr>"
    pagina+= "</table>"
    return pagina


#Creando la pagina que muestra los datos completos del Issue seleccionado)
@app.route('/mostraropen/<int:id>')
def mostrar_issueopen(id):
    pagina = f"<h1>Descripcion Completa</h1><table border: 1px solid black>"
    result = IssOpen.find_one({'_id': id})
    result = dict(result)
    for key, value in result.items():
        pagina += f"<tr><td style='background-color: #FAE5D3;>{key}</td><td>{value}</td></tr>"
    pagina += "</table>"
    return pagina