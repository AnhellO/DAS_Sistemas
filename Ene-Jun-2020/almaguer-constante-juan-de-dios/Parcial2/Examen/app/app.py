from flask import Flask, render_template
from populate import characters, myDB
from peewee import *
app = Flask(__name__)


@app.route('/')
def index():
    chars = characters.select()
    return render_template('login.html',characters=characters)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    myDB.close()