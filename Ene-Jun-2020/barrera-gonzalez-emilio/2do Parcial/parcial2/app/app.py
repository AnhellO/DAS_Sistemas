from flask import Flask, render_template
from models import *
from breakingbadapi import breaking_bad_API

app = Flask(__name__)
api = breaking_bad_API()

@app.route('/')
def index():
    chars = Characters.select()
    
    return render_template('index.html',chars=chars)

@app.route('/<int:char_id>')
def specific(char_id):
    
    char = Characters.get(char_id=char_id)
    return render_template('specific.html',char=char)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    myDB.close()