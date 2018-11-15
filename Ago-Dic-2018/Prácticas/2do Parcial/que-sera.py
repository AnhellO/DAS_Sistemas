# https://punkapi.com/

import time, re, requests, os, errno, json

directorio = 'archivitos-de-cache'

urls = {
	'https://api.punkapi.com/v2/beers/1',
	'https://api.punkapi.com/v2/beers/68',
	'https://api.punkapi.com/v2/beers/200',
	'https://api.punkapi.com/v2/beers/50',
	'https://api.punkapi.com/v2/beers/28'
}

for url in urls:
	request = requests.get(url)
	nombreArchivo = '{}/{}.html'.format(directorio, request.json()[0]['id'])
	print('Escribiendo archivo {}...'.format(nombreArchivo))

	if not os.path.exists(os.path.dirname(nombreArchivo)):
	    try:
	        os.makedirs(os.path.dirname(nombreArchivo))
	    except OSError as exc:
	        if exc.errno != errno.EEXIST:
	            raise
	
	with open(nombreArchivo, 'w') as archivo:
		archivo.write(request.text)
		archivo.close()
		print('Archivito cacheado :D!')
	
	time.sleep(3)