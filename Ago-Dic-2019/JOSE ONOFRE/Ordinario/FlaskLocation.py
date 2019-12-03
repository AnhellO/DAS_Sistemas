import sqlite3 as sql
from flask import Flask
from flask import g
from flask import render_template, request
from flask import *

########################## Uso de FLask para visualizar dinamicamente##############

app = Flask(__name__, template_folder='template')


@app.route('/locacion/<identificador>')
def location_get(identificador):
        i = identificador
        con = sql.connect("Base.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * from locationp where id={}".format(i))

        rows = cur.fetchall()
        return render_template("locacion.html", rows = rows)

@app.route('/busquedaLocacion', methods = ['GET'])
def buscar():
    if request.method == 'GET':
        user = request.args.get('nm')
        return redirect(url_for('location_get',identificador = user))

if __name__ == "__main__":
    app.run(debug=True)