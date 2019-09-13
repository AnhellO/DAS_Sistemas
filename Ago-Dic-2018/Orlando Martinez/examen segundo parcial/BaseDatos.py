import time, re, requests, os, errno, json, sqlite3

directorio='2do-parcial/html'
ids=[]
i=0
db = sqlite3.connect('Launch.db')
cursor = db.cursor()
for i in range(0,175):
	ids.append(i)
	i+=1
	urls = 'https://launchlibrary.net/1.3/agency/'+str(i)

	request = requests.get(urls)
	for urls in request.json()['agencies']:
	#print (request.json()['agencies'] request.json()[id])
		id=urls['id']
		nombreArchivo = '{}/{}.JSON'.format(directorio, id)
		name=urls['name']
		countryCode=urls['countryCode']
		abbrev=urls['abbrev']
		infoURL=urls['infoURL']
		direccion=nombreArchivo
		cursor.execute("INSERT INTO Launch(id,name,countryCode,abbrev,infoURL,direccion)VALUES(?,?,?,?,?,?)",(id,name,countryCode,abbrev,infoURL,direccion))
		db.commit()
		print("Agencia: {}".format(name)+ " " + "insertada correctamente")
