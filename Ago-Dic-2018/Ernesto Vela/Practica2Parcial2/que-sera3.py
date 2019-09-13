# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import time, re, requests, os, errno, json, sqlite3

directorio = 'archivitos-de-html'
url = 'https://api.punkapi.com/v2/beers'

for i in range(1, 4):
	request = requests.get(url, params={'page': i, 'per_page':80})

	db = sqlite3.connect(':memory:')
	db = sqlite3.connect('basesita-de-datos.db')

	cursor = db.cursor()
	cheves = request.json()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS chelas (
			id INTEGER PRIMARY KEY,
			name TEXT,
			description TEXT,
			image_url VARCHAR(200),
			abv REAL,
			food_pairing BLOB,
			ibu INTEGER,
			ebc INTEGER,
			srm INTEGER,
			ph REAL
		)'''
	)
	if i == 3:
		for o in range(0, 74):
			cursor.execute('''
				INSERT INTO chelas (
				id,
				name,
				description,
				image_url,
				abv,
				food_pairing,
				ibu,
				ebc,
				srm,
				ph
				)
				VALUES (
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
					);''',(cheves[o]['id'], cheves[o]['name'], cheves[o]['description'], cheves[o]['image_url'], cheves[o]['abv'], str(cheves[o]['food_pairing']), cheves[o]['ibu'], cheves[o]['ebc'], cheves[o]['srm'], cheves[o]['ph'])
				)
	else:
		for o in range(0, 80):
			cursor.execute('''
				INSERT INTO chelas (
				id,
				name,
				description,
				image_url,
				abv,
				food_pairing,
				ibu,
				ebc,
				srm,
				ph
				)
				VALUES (
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
					);''',(cheves[o]['id'], cheves[o]['name'], cheves[o]['description'], cheves[o]['image_url'], cheves[o]['abv'], str(cheves[o]['food_pairing']), cheves[o]['ibu'], cheves[o]['ebc'], cheves[o]['srm'], cheves[o]['ph'])
				)


	queryto = cursor.execute('''
		SELECT * FROM chelas
	''')
	print(queryto.fetchall())



db.close()
