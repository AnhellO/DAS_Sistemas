from flask import Flask,render_template
from main import *
from random import randrange
from peewee import *

app = Flask(__name__)
main()
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/civilizations/')
def civilizaciones():
    query = CIVILIZACIONES.select().where(CIVILIZACIONES.id == randrange(17))
    for civs in query:
        civilizacion = {
            "id": civs.id,
            "nombre":civs.nombre,
            "expansion":civs.expansion,
            "tipo": civs.tipo
        }
    return render_template('civilizations.html', civilizacion = civilizacion)

@app.route('/units/')
def Unidades():
    query = UNIDADES.select().where(UNIDADES.id == randrange(104))
    for unis in query:
        unidad = {
            "id": unis.id,
            "nombre":unis.nombre,
            "descripcion":unis.descripcion,
            "expansion": unis.expansion,
            "edad": unis.edad,
            "rango": unis.rango,
            "ataque": unis.ataque
        }
    return render_template('units.html', unidad=unidad)

@app.route('/structures/')
def Estructuras():
    query = ESTRUCTURAS.select().where(ESTRUCTURAS.id == randrange(59))
    for estrucs in query:
        estructura = {
            "id": estrucs.id,
            "nombre":estrucs.nombre,
            "edad": estrucs.edad,
            "tiempo": estrucs.tiempo
        }
    return render_template('structures.html', estructura=estructura)

@app.route('/technologies/')
def Tecnologias():
    query = TECNOLOGIAS.select().where(TECNOLOGIAS.id == randrange(140))
    for tecs in query:
        tecnologia = {
            "id": tecs.id,
            "nombre":tecs.nombre,
            "descripcion": tecs.descripcion,
            "expansion": tecs.expansion,
            "edad": tecs.edad
        }
    return render_template('technologies.html', tecnologia = tecnologia)
db.close()
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    

