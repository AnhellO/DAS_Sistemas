from flask import Flask
from db import Db
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    person = Db().get_random_person()
    return render_template('index.html', person=person)

if __name__ == "__main__":
    print("Iniciando servidor de Flask...")
    app.run(host="0.0.0.0", debug=True)
    print("Servidor corriendo en:\n0.0.0.0")

