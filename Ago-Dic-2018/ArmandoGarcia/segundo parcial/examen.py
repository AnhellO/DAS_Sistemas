
import requests
import json
import sqlite3
from random import randrange
from random import choice
import os
import re
import errno
#escogi la api de los perritso que venia hasta arriba espero no haya problema
db = sqlite3.connect('basdeperritos.db')
cur = db.cursor()
directorio = 'html'
cur.execute('''
CREATE TABLE IF NOT EXISTS perritos (
id INTEGER PRIMARY KEY,
name TEXT,
status TEXT,
image_url VARCHAR(200),
age INTEGER
)''')
db.commit()
for i in range(1 ,101):
    url = "https://dog.ceo/api/breeds/image/random"
    request = requests.get(url)
    ad=request.json()
    imagen=ad['message']
    status=ad['status']
    print('Dato insertado')
    cur.execute('''
    INSERT INTO perritos (
    id,
    name,
    status,
    image_url,
    age
    )
    VALUES (?,?,?,?,?);''',(i,choice(["Pluto","Pongo","Coronel","Lucky","Scooby-Doo","Golfo","Toby ","Chase"]),imagen,status,randrange(10)
    ))
    db.commit()

    archivo=open("perrito{}.json".format(str(i)),"a")
    archivo.write(request.text)
    archivo.close()
queryto = cur.execute('''
SELECT * FROM perritos
ORDER BY id
''')

for row in queryto:
    nombreArchivo = '{}/{}.html'.format(directorio, row[0])
    print('Escribiendo archivo {}...'.format(nombreArchivo))

    if not os.path.exists(os.path.dirname(nombreArchivo)):
    	try:
    		os.makedirs(os.path.dirname(nombreArchivo))
    	except OSError as exc:
    		if exc.errno != errno.EEXIST:
    			raise

    with open(nombreArchivo, 'w') as archivo:
    	waGuardar = '''
    	<h1>{}</h1>
    	<p>
    		{}
    		<br/>
    		<a href="{}">Imagen</a>
    	</p>
    	<em>Mostrando registro #{}</em>
    	'''.format(row[1], row[2], row[4], row[0],row[3])

    	archivo.write(waGuardar)
    	archivo.close()
    	print('Archivito cacheado :D!')

db.close()
