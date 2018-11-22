import time
import re
import requests
import os
import errno
import json
import sqlite3

directorio = 'archivitos-de-html'
url = 'https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke/'


ids = []

parametros = '|'.join([str(id) for id in ids])
db = sqlite3.connect('jokes.db')

cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS joke (
id INTEGER PRIMARY KEY,
type TEXT,
setup TEXT,
punchline TEXT,
path TEXT
)'''
               )

try:
    os.mkdir("./jokes")
except:
    print('No pude crear la carpeta')

for j in range(200):
    request = requests.get(url, params={'ids': parametros})
    ruta = "./jokes/"+str(j)+".json"
    f = open(ruta, "w+")
    f.write(str(request.json()))

    for i in range(0, len(request.json())):
        try:
            cursor.execute(''' INSERT INTO joke VALUES(?,?,?,?,?)''', (request.json()[
                'id'], request.json()['type'], request.json()['setup'], request.json()['punchline'], ruta))
        except:
            print('id repetido')

        print(request.json())
db.commit()
db.close()
