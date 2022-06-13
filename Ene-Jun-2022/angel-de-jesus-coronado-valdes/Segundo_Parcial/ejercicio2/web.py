import pymongo
import json
from flask import Flask,session,render_template,request,redirect,url_for
import os

# conexion a la base de datos
class Conexion:
    def __init__(self,client):
        self.client = client
    
    def Mostrar_Datos(self):
        lista = []
        db  = self.client["prueba"]
        print("Nombre de la DB: ",db.name)
        print("**************************************************************+")
        col = db['pet']
        for x in col.find():
            x['_id'] = str(x['_id'])
            print(x['_id'])
            lista.append(x)
        return lista


app = Flask(__name__)
app.secret_key = os.urandom(24)


# se realiza la redirección de la pagina si no se ah hecho el post
@app.route('/', methods=['GET','POST'])
def index():
    diccionario=[]
    client = pymongo.MongoClient("mongodb://root:root123@mongo_DB:27017/")
    con = Conexion(client)
    diccionario = con.Mostrar_Datos()
    
    if request.method == 'POST':  
        for dic in diccionario:
            dic['_id'] = str(dic['_id'])
            if str(dic['number']) == request.form['h2']:
                session['infor'] = dic
                return redirect(url_for('layout'))
            
    return render_template('index.html',diccionario=diccionario)


# si la session contiene dato se redirecciona a layout
# si no se mantiene en index
@app.route('/layout')
def layout():
    return render_template('layout.html',diccionario=session['infor'])


def main():
    app.run(debug=True,host="0.0.0.0")

if __name__=="__main__":
    main()
    









