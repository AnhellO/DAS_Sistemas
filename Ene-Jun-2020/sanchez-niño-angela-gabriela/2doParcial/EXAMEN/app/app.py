from flask import Flask, render_template
from models import *
from api import PERSONAJE

app = Flask(__name__)
@app.route('/')
def index():
     api = PERSONAKE.select()
     personaje = [perso.nombre for perso in api]
     return render_template('index.html',personaje = personaje)

@app.route('/character/<ID>')
def get_char(ID):
     api = PERSONAJE.select().where(PERSONAJE.id == ID)
     for chars in api:
          personaje = {
          "id": chars.id,
          "nombre":chars.nombre,
          "fechaNac":chars.fechaNac,
          "ocupacion":chars.ocupacion,
          "imagen": chars.imagen,
          "estado":chars.estado,
          "nickname":chars.nickname,
          "apariciones":chars.apariciones,
          "actor":chars.actor,
          "categoria": chars.categoria
        }
     return render_template('character.html',personaje = personaje)
     
if __name__ == '__main__':
     app.run(host= "0.0.0.0")
    