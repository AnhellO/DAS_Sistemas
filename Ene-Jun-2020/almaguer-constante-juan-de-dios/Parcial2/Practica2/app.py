from flask import Flask, render_template
from models import civilization,structure,technology,unit
from peewee import *

app = Flask(__name__)

db = SqliteDatabase('ageofempires.db')

civ = civilization()
struct = structure()
tec = technology()
un = unit()

@app.route('/')

def index():
    db.connect()
    civilizations = civ.select()
    structure = struct.select()
    tech = tec.select()
    unit = un.select()
    return render_template('index.html',
                           civilizations=civilizations,
                           structures=structure,
                           techs=tech,
                           units=unit)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
