from flask import Flask, render_template
from modelo import *
from breakingApi import breakingAPI

app = Flask(__name__)
@app.route('/')
def index():
     query = PERSONAJES.select()
     personaje = [perso.nombre for perso in query]
     return render_template('index.html',personaje = personaje)

@app.route('/character/<ID>')
def get_char(ID):
     query = PERSONAJES.select().where(PERSONAJES.id == ID)
     for chars in query:
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
     app.run(debug=True , host= "0.0.0.0")
    