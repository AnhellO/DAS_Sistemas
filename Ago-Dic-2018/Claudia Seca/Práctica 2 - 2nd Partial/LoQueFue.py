# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import requests, json, sqlite3

url = 'https://api.punkapi.com/v2/beers'

for i in range(1, 4):
	request = requests.get(url, params={'page': i, 'per_page': 80})
	db = sqlite3.connect('basecita_de_datos.db')

	cursor = db.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS chelas (
			id INTEGER PRIMARY KEY,
			name TEXT,
			ibu REAL,
			description TEXT,
			image VARCHAR(200),
			abv REAL,
			foodpairing TEXT,
			tagline TEXT,
			ph REAL,
			yeast TEXT
		)'''
	)

	for i in range(0, len(request.json())):
		cursor.execute('''
			INSERT INTO chelas VALUES (
				?,
				?,
				?,
				?,
				?,
				?,
				?,
				?,
				?,
				?
			)''',#Parseando el json :3
			(request.json()[i]['id'],
			request.json()[i]['name'],
			request.json()[i]['ibu'],
			request.json()[i]['description'],
			request.json()[i]['image_url'],
			request.json()[i]['abv'],
			', '.join(request.json()[i]['food_pairing'][0:2]),
			request.json()[i]['tagline'],
			request.json()[i]['ph'],
			request.json()[i]['ingredients']['yeast'])
		)


	queryto = cursor.execute('''
		SELECT * FROM chelas
		ORDER BY name
	''')#Comprobando que las cheves se guardaron >.<
	[print(row[0:], print('')) for row in queryto]
	"""for chela in queryto:
		print('Id: {}'.format(chela[0]))
		print('Name: {}'.format(chela[1]))
		print('TagLine: {}'.format(chela[2]))
		print('Description: {}'.format(chela[3]))
		print('Image: {}'.format(chela[4]))
		print('Alcohol By Volume: {}'.format(chela[5]))
		print('Food Pairing: {}'.format(chela[6]))
		print('Volume: {}'.format(chela[7]))
		print('First Brewed: {}'.format(chela[8]))
		print('Brewers Tips: {}'.format(chela[9]))
		print('')"""

	db.commit()
	db.close()
