@@ -0,0 +1,80 @@
# https://punkapi.com/
# http://docs.python-requests.org/en/master/
import time, re, requests, os, errno, json, sqlite3
def getDatos(url,i):
	directorio = 'archivitos-de-cache'
	ids=[]
	print ('Buscando datos...')
	ids.append(i)
	urls = url + str(i)
	request = requests.get(urls)
	id = request.json()[0]['id']
	name = request.json()[0]['name']
	description = request.json()[0]['description']
	image_url = request.json()[0]['image_url']
	abv= request.json()[0]['abv']
	target_fg = request.json()[0]['target_fg']
	tagline = request.json()[0]['tagline']
	first_brewed = request.json()[0]['first_brewed']
	ibu = request.json()[0]['ibu']
	ph = request.json()[0]['ph']
	qery = setDatos(id,name,description,image_url,abv,target_fg,tagline,first_brewed,ibu,ph)
    return(qery)
def setDatos(id,name,description,image_url,abv,target_fg,tagline,first_brewed,ibu,ph):
	#ids = [1, 68, 28, 50, 200]
	#parametros = '|'.join([str(id) for id in ids])
	conn = sqlite3.connect(':memory:')
	conn = sqlite3.connect("refrigerador.db")
	cursor = conn.cursor()
    if not os.path.isfile("refrigerador.db"):
		conn = sqlite3.connect("refrigerador.db")
    else:
	    pass
 	cursor.execute('''
		CREATE TABLE IF NOT EXISTS chelas (
			id INTEGER PRIMARY KEY,
			name TEXT,
			description TEXT,
			image_url TEXT,
			abv TEXT,
			target_fg TEXT,
			tagline TEXT,
			first_brewed TEXT,
			ibu TEXT,
			ph TEXT
		)'''
	)
	conn.commit()
	cursor.execute(''' INSERT INTO chelas VALUES (?,?,?,?,?,?,?,?,?,?)''', (id,name,description,image_url,abv,target_fg,tagline,first_brewed,ibu,ph))
	conn.commit()
 	queryto = cursor.execute('''
		SELECT * FROM chelas
		ORDER BY name''')
	qery= show(queryto)
	conn.close()
    return(qery)
def show(queryto):
    for row in queryto:
        return('\nID: {} \nNombre: {} \nDescripcion {} \nImagen: {} \nAbv: {} \nTarget: {} \nTag: {} \nFirst Brewed: {} \nIbu: {} \nPH: {} '\
		 .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
if __name__ == '__main__':
	url = 'https://api.punkapi.com/v2/beers/'
	i=0
    for i in range(1,235):
		#Rango de 235 para que se repita 234 veces, que es el número de cervezas que hay.
		qery = getDatos(url,i)
        if qery:
			print(" {}.- Datos almacenados.".format(i))
	    else:
			print("Fallo, la tabla está vacía.")
		#print(qery)
		#Imprimir qery trae los datos del select en el orden que se vayan almacenando.
		i+=1
	print("Listo.")
