from flask import Flask, render_template, request,url_for, redirect
import database
import sqlite3 as sql

app = Flask(__name__, template_folder='template')
#@app.route('/')
#def temolate():
    #return render_template('buscarPersonajes.html')

@app.route('/Episodio/<dato>')
def traer_episodio(dato):
    con = sql.connect('Ordinario/BaseDatos/rickandmorty.db')
    var = dato
    con.row_factory = sql.Row
    var2 = con.cursor()
    var2.execute('SELECT * FROM episodios WHERE id = {}'.format(var)) 
    lineas = var2.fetchall()
    return render_template('Episodio.html',lineas=lineas)

@app.route('/buscarEpisodio',methods=['GET'])
def episodio():
    if request.method == 'GET':
        dat = request.args.get('Id')
        return redirect(url_for('traer_episodio',dato=dat))


if __name__ == '__main__':
    app.run(debug=True)