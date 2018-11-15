# https://punkapi.com/
# http://docs.python-requests.org/en/master/

import time, re, requests, os, errno, json, sqlite3

directorio = 'archivitos-de-cache'
url = 'https://api.punkapi.com/v2/beers'

ids = [1, 68, 28, 50, 200]
parametros = '|'.join([str(id) for id in ids])

request = requests.get(url, params={'ids': parametros})

db = sqlite3.connect(':memory:')
db = sqlite3.connect('basesita-de-datos.db')

cursor = db.cursor()
cursor.execute('''
	CREATE TABLE chelas (
		id INTEGER PRIMARY KEY,
		name TEXT
	)'''
)

db.close()
# nombreArchivo = '{}/{}.json'.format(directorio, 'resultado')
# print('Escribiendo archivo {}...'.format(nombreArchivo))
#
# if not os.path.exists(os.path.dirname(nombreArchivo)):
# 	try:
# 		os.makedirs(os.path.dirname(nombreArchivo))
# 	except OSError as exc:
# 		if exc.errno != errno.EEXIST:
# 			raise
#
# with open(nombreArchivo, 'w') as archivo:
# 	archivo.write(request.text)
# 	archivo.close()
# 	print('Archivito cacheado :D!')
