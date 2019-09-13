import time, re, requests, os, errno, json, sqlite3
ids=[]
i=0
db = sqlite3.connect('Cerveza.db')
cursor = db.cursor()
for i in range(0,234):
	ids.append(i)
	i+=1
	urls = 'https://api.punkapi.com/v2/beers/'+str(i)

	request = requests.get(urls)
	id = request.json()[0]['id']
	name=request.json()[0]['name']
	description=request.json()[0]['description']
	image_url=request.json()[0]['image_url']
	abv=request.json()[0]['abv']
	ph=request.json()[0]['ph']
	attenuation_level=request.json()[0]['attenuation_level']
	first_brewed=request.json()[0]['first_brewed']
	contributed_by=request.json()[0]['contributed_by']
	tagline=request.json()[0]['tagline']
	target_og=request.json()[0]['target_og']
	cursor.execute("INSERT INTO CERVEZAS(id,name,description,image_url,abv,ph,attenuation_level,first_brewed,contributed_by,tagline,target_og)VALUES(?,?,?,?,?,?,?,?,?,?,?)",(id,name,description,image_url,abv,ph,attenuation_level,first_brewed,contributed_by,tagline,target_og))
	db.commit()
	print ("cerveza: {}".format(name)+ " " + "La cerveza fue insertada correctamente")
print("Fin de la lista!!")
db.close()