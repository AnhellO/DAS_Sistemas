import sqlite3 as sql
from flask import Flask
from flask import g
from flask import render_template, request
from flask import *

########################## Uso de FLask para visualizar dinamicamente##############

app = Flask(__name__, template_folder='template')


@app.route('/')
def new_character():
    con = sql.connect("Base.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from characterp")

    rows = cur.fetchall()
    return render_template('index.html', rows = rows)



#@app.route('/personaje')
#def character():
#    
#    con = sql.connect("Base.db")
#    con.row_factory = sql.Row
#
#    cur = con.cursor()
#    cur.execute("select * from characterp where id=1")
#
#    rows = cur.fetchall()
#    return render_template('personaje.html', rows = rows)

#METODOS PARA BUSCAR UN PERSONAJE DESDE LA VENTANA DEL NAVEGADOR
# Es necesario abrir 'busqueda.html' para poder visualizar

@app.route('/personaje/<identificador>')
def character_get(identificador):
        i = identificador
        con = sql.connect("Base.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * from characterp where id={}".format(i))

        rows = cur.fetchall()
        return render_template("personaje.html", rows = rows)

@app.route('/busqueda', methods = ['GET'])
def buscar():
    if request.method == 'GET':
        user = request.args.get('nm')
        return redirect(url_for('character_get',identificador = user))


###################################

@app.route('/locacion/<identa>')
def locacion_get(identa):
        n = identa
        net = sql.connect("Base.db")
        net.row_factory = sql.Row
        cur = net.cursor()
        cur.execute("SELECT * from locationp where id={}".format(n))

        rows = cur.fetchall()
        return render_template("location.html", rows = rows)

@app.route('/busquedaLocacion', methods = ['GET'])
def buscarloc():
    if request.method == 'GET':
        loca = request.args.get('nm')
        return redirect(url_for('locacion_get',identa = loca))

#@app.route('/success/<name>')
#def success(name):
#   return 'welcome %s' % name


#@app.route('/busqueda',methods = ['POST', 'GET'])
#def login():
#   if request.method == 'POST':
#      user = request.form['nm']
#      return redirect(url_for('success',name = user))
#   else:
#      user = request.args.get('nm')
#      return redirect(url_for('success',name = user))



if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
        



