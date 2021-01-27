from flask import Flask, render_template, request,url_for, redirect
import database
import sqlite3 as sql

app = Flask(__name__, template_folder='template')
#@app.route('/')
#def temolate():
    #return render_template('buscarPersonajes.html')

@app.route('/Personaje/<dato>')
def traer_personaje(dato):
    con = sql.connect('Ordinario/BaseDatos/rickandmorty.db')
    var = dato
    con.row_factory = sql.Row
    var2 = con.cursor()
    var2.execute('SELECT * FROM personajes WHERE id = {}'.format(var)) 
    lineas = var2.fetchall()
    return render_template('Personaje.html',lineas=lineas)

@app.route('/buscarPersonaje',methods=['GET'])
def personaje():
    if request.method == 'GET':
        dat = request.args.get('Id')
        return redirect(url_for('traer_personaje',dato=dat))


if __name__ == '__main__':
    app.run(debug=True)