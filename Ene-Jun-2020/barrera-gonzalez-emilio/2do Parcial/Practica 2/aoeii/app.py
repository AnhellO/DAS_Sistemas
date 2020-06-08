from flask import Flask, render_template
from aoiiapi import aoiiAPI
from peewee import *
from dbcreation import *

#Defining the database
db = SqliteDatabase('AgeOfEmpiresII.db')
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/structures')    
def structures():
    db.connect()
    structures=Structure.select()
    db.close()
    print(structures)
    return render_template('structures.html',structures=structures)

@app.route('/units')
def units():
    db.connect()
    units=Unit.select()
    db.close()
    return render_template('units.html',units=units)

@app.route('/civilizations')
def civilizations():
    db.connect()
    civilizations=Civilization.select()
    db.close()
    return render_template('civilizations.html', civilizations=civilizations)

@app.route('/tech')
def tech():
    db.connect()
    tech=Technology.select()
    db.close()
    return render_template('tech.html', tech=tech)


if __name__=='__main__':
    app.run(host="0.0.0.0")    