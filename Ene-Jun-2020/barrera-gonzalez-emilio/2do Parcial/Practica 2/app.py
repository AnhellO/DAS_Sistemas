from flask import Flask, render_template
from aoiiapi import aoiiAPI

app=Flask(__name__)
app.config["CACHE_TYPE"] = "null"
api = aoiiAPI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/structures')    
def structures():
    structures=api.getStructures()
    return render_template('structures.html',structures=structures)

@app.route('/units')
def units():
    units=api.getUnits()
    return render_template('units.html',units=units)

@app.route('/civilizations')
def civilizations():
    civilizations=api.getCivilizations()
    return render_template('civilizations.html', civilizations=civilizations)

@app.route('/structure/<num>')    
def structure(num):
    structures=api.getStructure(num)
    return render_template('structures.html',structures=structures)

@app.route('/unit/<num>')
def unit(num):
    units=api.getUnit(num)
    return render_template('units.html',units=units)

@app.route('/civilization/<num>')
def civilization(num):
    civilizations=api.getCivilization(num)
    return render_template('civilizations.html', civilizations=civilizations)

if __name__=='__main__':
    app.run(host="0.0.0.0")

    