# https://randomuser.me/
# http://docs.python-requests.org/en/master/

import requests, json, sqlite3, os, errno

url = 'https://randomuser.me/api/?results=100'

request = requests.get(url)
db = sqlite3.connect('BaseDatos.db')

cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS usuarios (
		gender TEXT,
		name TEXT,
		lastName TEXT,
		address TEXT,
		age INTEGER,
		dob TEXT,
		ruta_json TEXT

	)'''
)

for i in range(0, len(request.json()['results'])):
	rutaJson = "json/{}.json".format(request.json()['results'][i]['name']['first'])
	if not os.path.exists(os.path.dirname(rutaJson)):
		try:
			os.makedirs(os.path.dirname(rutaJson))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise
	with open(rutaJson, "w") as archivo:
		archivo.write(str(request.json()['results'][i]))
		archivo.close()
		print('Aquí esta mi Json xD')


	cursor.execute('''
		INSERT INTO usuarios VALUES (
			?,
			?,
			?,
			?,
			?,
			?,
			?
		)''',#Parseando el json :3
		(request.json()['results'][i]['gender'],
		request.json()['results'][i]['name']['first'],
		request.json()['results'][i]['name']['last'],
		request.json()['results'][i]['location']['street'],
		request.json()['results'][i]['dob']['date'],
		request.json()['results'][i]['dob']['age'],
		rutaJson)
	)


queryto = cursor.execute('''
	SELECT * FROM usuarios
	ORDER BY name
''')#Comprobando que se guardaron >.<
db.commit()
db.close()


rutaHtml = 'html/Users.html'

if not os.path.exists(os.path.dirname(rutaHtml)):
	try:
		os.makedirs(os.path.dirname(rutaHtml))
	except OSError as exc:
		if exc.errno != errno.EEXIST:
			raise

with open(rutaHtml, 'w') as archivo:
	miHtml = '''
	<!DOCTYPE html>

	<html>
		<head>
			<style>
				table {
					font-family: arial, sans-serif;
					border-collapse: collapse;
					width: 100%;
				}

				td, th {
					border: 1px solid #dddddd;
					text-align: left;
					padding: 8px;
				}

				tr:nth-child(even) {
					background-color: #dddddd;
				}
			</style>
		</head>
		<body>
			<h2>Items de la Base de Datos</h2>
			<table>
				<tr>
					<th>gender</th>
					<th>name</th>
					<th>lastName</th>
					<th>address</th>
					<th>age</th>
					<th>dob</th>
					<th>ruta_json</th>
				</tr>
				<tr> ... </tr>
			</table>
		</body>
	</html>
	'''

	archivo.write(miHtml)
	archivo.close()
	print('Cacheando mi archivo xD')
