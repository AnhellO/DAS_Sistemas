# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import time, re, requests, os, errno, json, sqlite3

directorio = 'archivitos-de-html'
url = 'https://api.punkapi.com/v2/beers'

ids = [1, 68, 28, 50, 200]
parametros = '|'.join([str(id) for id in ids])

request = requests.get(url, params={'ids': parametros})

db = sqlite3.connect(':memory:')
db = sqlite3.connect('basesita-de-datos.db')

cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS chelas (
		id INTEGER PRIMARY KEY,
		name TEXT,
		description TEXT,
		image VARCHAR(200)
	)'''
)

queryto = cursor.execute('''
	SELECT * FROM chelas
	ORDER BY name
''')

for row in queryto:
	nombreArchivo = '{}/{}.html'.format(directorio, row[1])
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
		'''.format(row[1], row[2], row[3], row[0])

		archivo.write(waGuardar)
		archivo.close()
		print('Archivito cacheado :D!')

db.close()
