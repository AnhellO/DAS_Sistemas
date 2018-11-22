import re, requests, os, errno, json, sqlite3

def getDatos(url,i):
	ids=[]
	print ('Buscando datos...')
	ids.append(i)
	urls = url + str(i)
	request = requests.get(urls)
    #Variables
	name = request.json()['name']
	birth = request.json()['birth_year']
	gender = request.json()['gender']
	mass = request.json()['mass']
	home = request.json()['homeworld']
	#Creacion del JSON
	for url in urls:
		directorio = 'json'
		JSONFILE ='{}/{}.json'.format(directorio, request.json()['name'])
		print('Escribiendo archivo {}...'.format(JSONFILE))
		if not os.path.isfile(os.path.dirname(JSONFILE)):
			try:
				os.makedirs(os.path.dirname(JSONFILE))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
		with open(JSONFILE, 'w') as archivo:
			archivo.write(request.text)
			archivo.close()
			print('Json creado.')
		js= os.path.dirname(JSONFILE)
		qery = setDatos(name,birth,gender,mass,home,js)
		return('Guardando Datos...')

def setDatos(name,birth,gender,mass,homeworld,js):
	conn = sqlite3.connect(':memory:')
	conn = sqlite3.connect("Characters.db")
	cursor = conn.cursor()

	if not os.path.isfile("Characters.db"):
		conn = sqlite3.connect("Characters.db")
	else:
		pass

	cursor.execute('''
		CREATE TABLE IF NOT EXISTS Personajes (
			Nombre TEXT PRIMARY KEY,
			Fecha_de_Nacimiento TEXT,
			Sexo TEXT,
			Masa TEXT,
			Planeta_de_Origen TEXT,
			JSONPATH TEXT
		)'''
	)
	conn.commit()
	cursor.execute(''' INSERT INTO Personajes VALUES (?,?,?,?,?,?)''', (name,birth,gender,mass,homeworld,js))
	conn.commit()

	conn.close()
	return('Valores Insertados.')

if __name__ == '__main__':
	url = 'https://swapi.co/api/people/'
	i=0
	j=0
	#POR MUY RARO QUE PAREZCA, MI API NO TIENE EL NÚMERO 17. Y está fea.
	for i in range(1,17):
		qery = getDatos(url,i)

		if qery:
			print(" {}.- Datos almacenados.".format(i))
		else:
			print("Fallo, la tabla está vacía.")
		i+=1
	for j in range(18,89):
		qery1 = getDatos(url,j)

		if qery1:
			print(" {}.- Datos almacenados.".format(j))
		else:
			print("Fallo, la tabla está vacía.")
		j+=1
	print("Listo.")
