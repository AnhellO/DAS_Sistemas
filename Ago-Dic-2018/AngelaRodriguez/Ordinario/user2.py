import time, re, requests, os, errno, json, sqlite3

db = sqlite3.connect('Recetas.db')
cursor = db.cursor()
#urls = 'https://randomuser.me/api/ '
urls = 'https://randomapi.com/api/6de6abfedb24f889e0b5f675edc50deb?fmt=raw&sole' 

class Usuario():
	for i in range(1,50):
		request = requests.get(urls)
		status_code = request.status_code
		if status_code == 200:
			#id = request.json()[0]['id']
			first=request.json()[0]['first']
			last=request.json()[0]['last']
			email=request.json()[0]['email']
			address=request.json()[0]['address']
			balance=request.json()[0]['balance']
			cursor.execute("INSERT INTO USUARIOS(id,first,last,email,address,balance)VALUES(?,?,?,?,?,?)",(i,first,last,email,address,balance))
			db.commit()
print("usuarios guardados!!")
db.close()