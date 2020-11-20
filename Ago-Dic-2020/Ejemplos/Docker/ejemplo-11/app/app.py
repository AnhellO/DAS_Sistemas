from flask import Flask, request, render_template, jsonify
from models import MyCats

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Pageee'

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.form['name'] if request.method == 'POST' and 'name' in request.form else 'Anonymous'
    return render_template('hello.html', name=name)

@app.route('/my-cats', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        cat = MyCats(nombre=request.form['nombre'], imagen=request.form['imagen'])
        cat.save()
        return {'ID': cat.id, 'nombre': cat.nombre, 'imagen': cat.imagen}

    return jsonify([{'ID': cat.id, 'nombre': cat.nombre, 'imagen': cat.imagen} for cat in MyCats.select()])