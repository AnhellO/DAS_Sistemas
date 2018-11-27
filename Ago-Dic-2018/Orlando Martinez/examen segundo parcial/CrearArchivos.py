import time, re, requests, os, errno, json, sqlite3

directorio='2do-parcial/html'
ids=[]
i=0
for i in range(0,175):
	ids.append(i)
	i+=1
	urls = 'https://launchlibrary.net/1.3/agency/'+str(i)

	request = requests.get(urls)
	for urls in request.json()['agencies']:
	#print (request.json()['agencies'] request.json()[id])
		id=urls['id']

		nombreArchivo = '{}/{}.JSON'.format(directorio, id)
		print('Creando archivo{}'.format(nombreArchivo))
		print(request.json()['agencies'])
		if not os.path.exists(os.path.dirname(nombreArchivo)):
			try:
				os.makedirs(os.path.dirname(nombreArchivo))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise

		with open(nombreArchivo, 'w') as archivo:
			archivo.write(request.text)
			archivo.close()
			print('Archivo creado')
		time.sleep(3)
