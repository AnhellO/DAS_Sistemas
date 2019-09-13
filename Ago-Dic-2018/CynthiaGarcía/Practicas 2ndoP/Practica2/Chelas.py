# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import time
import re
import requests
import os
import errno
import json
import sqlite3

directorio = 'archivitos-de-html'
url = 'https://api.punkapi.com/v2/beers/'


ids = []

parametros = '|'.join([str(id) for id in ids])
#db = sqlite3.connect(':memory:')
db = sqlite3.connect('basesita-de-datos.db')

cursor = db.cursor()
"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS chelas (
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT,
image_url VARCHAR(200),
abv real,
food_pairing real,
ibu real,
ph real,
first_brewed text,
ebc real,
attenuation_level text

)'''
               )
"""               


for i in range(90):
    request = requests.get(url + str(i+1), params={'ids': parametros})

    for i in range(0, len(request.json())):
        cursor.execute(''' INSERT INTO chelas VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (request.json()[i]['id'], request.json()[i]['name'], request.json()[i]['description'], request.json()[i]['image_url'], request.json()[i]['abv'], str(request.json()[i]['food_pairing']), request.json()[i]['ibu'], request.json()[i]['ph'], request.json()[i]['first_brewed'], request.json()[i]['ebc'], request.json()[i]['attenuation_level']))

"""
    queryto = cursor.execute('''
		SELECT * FROM chelas
		ORDER BY name ''')

    print(queryto.fetchall())
"""    
db.commit()
db.close()
