from bs4 import BeautifulSoup
import requests
import sqlite3
url="https://randomuser.me/api/"
ids=[]
i=0
db = sqlite3.connect('Taqueria.db')
cursor = db.cursor()
class cliente():
    for i in range(0,51):
        ids.append(i)
        i+=1
        urls = 'https://randomuser.me/api/'
        request = requests.get(urls)
        for urls in request.json()['results']:
            nombre=urls['name']['first']
            genero=urls['gender']
            direccion=urls['location']['street']
            celular=urls['cell']
            cursor.execute("INSERT INTO Clientes(ID_CLIENTE,NOMBRE_CLIENTE,GENERO,DIRECCION,CELULAR)VALUES(?,?,?,?,?)",(i,nombre,genero,direccion,celular))
            db.commit()
