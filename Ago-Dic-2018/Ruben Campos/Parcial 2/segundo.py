# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import requests, json, sqlite3, os, errno

url = 'https://api.jikan.moe/v3/anime/20/episodes/1'

request = requests.get(url)
if request.status_code == 200:

	db = sqlite3.connect('database')

	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS capitulosnaruto (
			id INTEGER PRIMARY KEY,
			title TEXT,
			titlejapanese TEXT,
			aired TEXT,
			videourl VARCHAR(200),
			rutajson TEXT
		)'''
	)
	listacapitulos = request.json()

	for i in range(0, 100):
		archivojson = "jsons/{}.json".format(listacapitulos['episodes'][i]['episode_id'])
		if not os.path.exists(os.path.dirname(archivojson)):
			try:
				os.makedirs(os.path.dirname(archivojson))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise

		with open(archivojson, 'w') as archivo:
			archivo.write(str(listacapitulos['episodes'][i]))
			archivo.close()
			print('Json Creado!')

		cursor.execute('''
			INSERT INTO capitulosnaruto VALUES (
				:id,
				:title,
				:titlejapanese,
				:aired,
				:videourl,
				:rutajson
			)''',
			{
			'id': listacapitulos['episodes'][i]['episode_id'],
			'title': listacapitulos['episodes'][i]['title'],
			'titlejapanese': listacapitulos['episodes'][i]['title_japanese'],
			'aired': listacapitulos['episodes'][i]['aired']['string'],
			'videourl': listacapitulos['episodes'][i]['video_url'],
			'rutajson': archivojson
			}
		)
		db.commit()

	cursor.execute('''
		SELECT * FROM capitulosnaruto

	''')
	queryto = cursor.fetchall()
	print(queryto[0][0])
	archivohtml = 'html/Tabla.html'

	if not os.path.exists(os.path.dirname(archivohtml)):
		try:
			os.makedirs(os.path.dirname(archivohtml))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise

	with open(archivohtml, 'w') as archivo:
		Guardar = '''
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
				<table id="myTable">
					<tr>
						<th>Id</th>
						<th>Title</th>
						<th>TitleJapanese</th>
						<th>Aired</th>
						<th>VideoUrl</th>
						<th>RutaJSON</th>
					</tr>
					<tr>{}</tr>
					<tr>{}</tr>
					<tr>{}</tr>
					<tr>{}</tr>
					<tr>{}</tr>
					<tr>{}</tr>
				</table>
			</body>
		</html>
		'''

		archivo.write(Guardar)
		archivo.close()
	print('Html creado!')

	db.commit()
	db.close()
else:
	print('Request Failed')
