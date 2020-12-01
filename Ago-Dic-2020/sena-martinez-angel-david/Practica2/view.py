from flask import Flask, render_template
import pymongo
import random

app = Flask(__name__)

@app.route('/')
def mostrar_usuario():
	client = pymongo.MongoClient("mongodb://db:27017/")
	db = client["mi-bd"]

	personas = []
	for x in db.coll.find():
		personas.append(x)
	persona = personas[random.randint(0, len(personas) - 1)]

	return render_template('usuariorandom.html', **persona)