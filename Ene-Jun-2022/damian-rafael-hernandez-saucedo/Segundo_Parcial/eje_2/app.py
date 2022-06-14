import pymongo
from flask import Flask,session,render_template,request,redirect,url_for
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/', methods=['GET','POST'])
def index():
    di=[]
    client = pymongo.MongoClient("mongodb://hola:hola123@mongo:27017/")
    db  = client["traba"]
    columna = db['trabajo']
    for x in columna.find():
        x['_id'] = str(x['_id'])
        di.append(x)
    
    if request.method == 'POST':  
        for dic in di:
            dic['_id'] = str(dic['_id'])
            if str(dic['number']) == request.form['in']:
                session['infor'] = dic
                return redirect(url_for('informacion'))
            
    return render_template('index.html',diccionario=di)


@app.route('/informacion')
def informacion():
    return render_template('informacion.html',diccionario=session['infor'])


def main():
    app.run(debug=True,host="0.0.0.0")

if __name__=="__main__":
    main()
    









