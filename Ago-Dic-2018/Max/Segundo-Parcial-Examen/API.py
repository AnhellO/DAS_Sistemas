import time, re, requests, os, errno, json, sqlite3

num = 1
url = 'https://anapioficeandfire.com/api/characters/' + str(num)

self.conexion = sqlite3.connect('IceandFire.db')
self.cursor = self.conexion.cursor()

while num <= 100:

    REQ = requests.get(url)

    if REQ.status_code == 200:
        requests = REQ.json()
#        print(datos)
	for i in request:
		cursor.execute(''' INSERT INTO ICEANDFIRE VALUES (?,?,?,?,?)''', (request.json()[i]['url'], request.json()[i]['name'], request.json()[i]['grender'], request.json()[i]['culture'], request.json()[i]['born']))

    num += 1

db.commit()
db.close()
