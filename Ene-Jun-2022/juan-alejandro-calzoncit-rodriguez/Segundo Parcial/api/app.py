import pymongo
from flask import Flask, jsonify, request, render_template

# Creamos conexión a MongoDB
client = pymongo.MongoClient("mongodb://root:contrasena123@mongo_compose:27017/")
db = client["parcial"]
coll = db["issues"]

# Aplicación de flask
app = Flask(__name__, template_folder='template')

# Ruta principal (muestra todas las issues junto con su id, titulo y el link a su propia 'ruta')
@app.route("/")
def issues():
    issues = [issue for issue in coll.find()]
    return render_template('tableIssues.html',title='Issues Table',issues = issues)    

# Ruta para cada issue (muestra todo el contenido de cada uno)
@app.route("/<int:number>")
def issue(number):
    issue = coll.find_one({'_id': number})   
    return render_template('tableIssue.html',title=f'Issue {number}',issue = issue)                

if __name__ == "__main__":
    app.run(debug=True)