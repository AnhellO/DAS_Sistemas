from flask import Flask, render_template
from models import *
from pokeapi import PokeAPI
from random import randrange

app = Flask(__name__)
api = PokeAPI()

@app.route('/')
def index():
    # print(Pokemon.select().count())
    pokemon = Pokemon.get(id=randrange(Pokemon.select().count()))
    print(pokemon)

    return render_template('index.html', pokemon=pokemon)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    myDB.close()