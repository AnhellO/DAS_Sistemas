import time, re, requests, os, errno, json, sqlite3

i=0
ids=[]

db = sqlite3.connect('Cervezas.db')
cursor = db.cursor()

for i in range(0,234):
	ids.append(i)
	i+=1
	
	url = 'https://api.punkapi.com/v2/beers/'+ str(i)
	request = requests.get(url)
	
	id = request.json()[0]['id']
	name=request.json()[0]['name']
	description=request.json()[0]['description']
	image=request.json()[0]['image_url']
	first_brewed=request.json()[0]['first_brewed']
	target_fg=request.json()[0]['target_fg']
	srm=request.json()[0]['srm']
	abv=request.json()[0]['abv']
	ph=request.json()[0]['ph']
	tagline=request.json()[0]['tagline']
	attenuation_level=request.json()[0]['attenuation_level']

	cursor.execute("INSERT INTO CERVEZAS(id,name,description,image,first_brewed,target_fg,srm,abv,ph,tagline,attenuation_level) VALUES(?,?,?,?,?,?,?,?,?,?,?)",(id,name,description,image,first_brewed,target_fg,srm,abv,ph,tagline,attenuation_level))
	db.commit()
	
	print("Cerveza {}".format(name)+ " " + "se insertó correctamente")
print("Listo")

db.close()
