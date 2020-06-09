from flask import Flask, render_template
from zc_das_pract2_.api_n_databs import *
from peewee import *

app = Flask(__name__)

db = SqliteDatabase('AoEII.db')

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
    return render_template('Information.html',
                           civilizations=civilizations,
                           structures=structure,
                           techs=tech,
                           units=unit)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
