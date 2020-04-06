from flask import Flask, render_template
from pokeapi import PokeAPI
from random import randrange

app = Flask(__name__)
api = PokeAPI()

@app.route('/')
def index():

    pokemon = api.getPokemon(randrange(807))
    return render_template('index.html', pokemon=pokemon)
"""
@app.route('/<pokemn>')
def param(pokemn):
    pokemon=api.getPokemon(pokemn)
    return render_template('index.html', pokemn=pokemon)
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
