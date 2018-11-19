# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import time, re, requests, os, errno, json, sqlite3

directorio = 'comprobacion-bd-llena'
url = 'https://api.punkapi.com/v2/beers'

ids = range(1,235)
ids1 = list(ids)

db = sqlite3.connect(':memory:')
db = sqlite3.connect('basesita-de-datos.db')

cursor = db.cursor()
cursor.execute('''
	CREATE TABLE IF NOT EXISTS chelas (
		id INTEGER PRIMARY KEY,
		name TEXT,
		description TEXT,
		image_url VARCHAR(200),
        abv TEXT,
        food_pairing TEXT,
        tagline TEXT,
        first_brewed TEXT,
        ph TEXT,
        ingredients TEXT,
        attenuation_level TEXT
	)'''
)

for id in ids1:
    request = requests.get('https://api.punkapi.com/v2/beers', params={'ids':str(id)})
    datos = request.json()
    db = sqlite3.connect(':memory:')
    db = sqlite3.connect('basesita-de-datos.db')

    cursor = db.cursor()
    if cursor.execute('''
        INSERT INTO chelas VALUES (
        :id, :name, :description, :image_url, :abv, :food_pairing,
        :tagline, :first_brewed, :ph, :ingredients, :attenuation_level)''',
        {'id':datos[0].get("id"), 'name':datos[0].get("name"), 'description':datos[0].get("description"), 'image_url':datos[0].get("image_url"), 'abv':datos[0].get("abv"), 'food_pairing':', '.join(datos[0].get("food_pairing")),
        'tagline':datos[0].get("tagline"), 'first_brewed':datos[0].get("first_brewed"), 'ph':datos[0].get("ph"), 'ingredients':', '.join(datos[0].get("ingredients")), 'attenuation_level':datos[0].get("attenuation_level") }) :
        print("Chela agregada a la bd")
    else:
        print("NO se agregó")

    db.commit()
    time.sleep(10)

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
			<br/><br/>
			<a href="{}">Imagen</a>
            <br/><br/>
            <h4>Abv: {}</h4>
            <h4>Food pairing: {}</h4>
            <h4>Tagline: {}</h4>
            <h4>First brewed: {}</h4>
            <h4>Ph: {}</h4>
            <h4>Ingredients: {}</h4>
            <h4>Attenuation level: {}</h4>
		</p>

        <em>Mostrando registro #{}</em>
		'''.format(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[0])

		archivo.write(waGuardar)
		archivo.close()
		print('Archivito cacheado :D!')

db.close()
