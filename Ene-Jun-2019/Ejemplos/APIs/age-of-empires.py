import requests
import sqlite3

url = 'https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations'

r = requests.get(url)

db = sqlite3.connect(':memory:')
db = sqlite3.connect('aoe.db')
cursor = db.cursor()

for civilization in r.json()['civilizations']:
    if civilization['expansion'] == 'The Conquerors':
        query = '''
        INSERT INTO civiliceichons (id, name, expansion)
        VALUES (?, ?, ?)
        '''
        cursor.execute(query, (civilization['id'], civilization['name'], civilization['expansion']))


db.commit()        
print(cursor.fetchall())
db.close()
