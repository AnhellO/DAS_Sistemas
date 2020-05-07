from flask import Flask, render_template
from peewee import *
from models import Pokemon
from pokeapi import PokeAPI
from random import randrange

app = Flask(__name__)
api = PokeAPI()

@app.route('/')
def index():
    pokemon = api.get_pokemon(randrange(api.get_count()))
    print(pokemon)
    return render_template('index.html', pokemon=pokemon)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
