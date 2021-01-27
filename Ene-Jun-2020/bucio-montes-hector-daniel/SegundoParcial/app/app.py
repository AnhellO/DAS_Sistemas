from flask import Flask, render_template
from Models import *
from CharsApi import BB_Chars_API

app = Flask(__name__)
api = BB_Chars_API()


@app.route('/')
def index():
    characters = Characters.select()
    return render_template('index.html', api=characters)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
    myDB.close()
