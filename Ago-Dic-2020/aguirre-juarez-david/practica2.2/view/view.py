from flask import Flask, render_template
import pymongo as mo
import random as rand

app = Flask(__name__)

@app.route("/")
def get_random_user():
	c = mo.MongoClient("mongodb://db:27017/")
	db = c["mo-data"]

	index = rand.randint(0, db.users.count() - 1)

	return render_template("index.html", **db.users.find_one({ "position": index }))
