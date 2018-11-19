# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import requests, json, sqlite3

url = 'https://api.punkapi.com/v2/beers'

pagina = 1

while pagina <= 3:
	request = requests.get(url, params={'page': str(pagina), 'per_page': 80})
	if request.status_code == 200:

		db = sqlite3.connect('basesita-de-datos')

		cursor = db.cursor()
		cursor.execute('''
			CREATE TABLE IF NOT EXISTS chelas (
				id INTEGER PRIMARY KEY,
				name TEXT,
				tagline TEXT,
				description TEXT,
				image VARCHAR(200),
				abv REAL,
				foodpairing TEXT,
				volume TEXT,
				firstbrewed TEXT,
				brewerstips TEXT
			)'''
		)
		listacheves = request.json()

		for i in range(0, len(listacheves)):
			cursor.execute('''
				INSERT INTO chelas VALUES (
					:id,
					:name,
					:tagline,
					:description,
					:image,
					:abv,
					:foodpairing,
					:volume,
					:firstbrewed,
					:brewerstips
				)''',
				{
				'id': listacheves[i]['id'],
				'name': listacheves[i]['name'],
				'tagline': listacheves[i]['tagline'],
				'description': listacheves[i]['description'],
				'image': listacheves[i]['image_url'],
				'abv': listacheves[i]['abv'],
				'foodpairing': ', '.join(listacheves[i]['food_pairing'][0:]),
				'volume': ' '.join([str(listacheves[0]['volume']['value']), listacheves[0]['volume']['unit']]),
				'firstbrewed': listacheves[i]['first_brewed'],
				'brewerstips': listacheves[i]['brewers_tips']
				}
			)

		cursor.execute('''
			SELECT * FROM chelas

		''')
		queryto = cursor.fetchall()
		for chela in queryto:
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
			print('')

		db.commit()
		db.close()
		pagina+=1
	else:
		print('Request Failed')
