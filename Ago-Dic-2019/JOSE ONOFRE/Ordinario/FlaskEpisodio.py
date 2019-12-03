import sqlite3 as sql
from flask import Flask
from flask import g
from flask import render_template, request
from flask import *

########################## Uso de FLask para visualizar dinamicamente##############

##NOTA: se envia desde el html de busqueda el dato para mostrar los
#resultado en el localhost:5000

app = Flask(__name__, template_folder='template')


@app.route('/locacion/<identificador>')
def episodio_get(identificador):
        i = identificador
        con = sql.connect("Base.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * from episodep where id={}".format(i))

        rows = cur.fetchall()
        return render_template("episodio.html", rows = rows)

@app.route('/busquedaEpisodio', methods = ['GET'])          
def buscar():
    if request.method == 'GET':
        user = request.args.get('nm')
        return redirect(url_for('episodio_get',identificador = user))

if __name__ == "__main__":
    app.run(debug=True)