import time, re, requests, os, errno, json, sqlite3


ids=[]
i=0
db = sqlite3.connect('Chelas.db')
cursor = db.cursor()
for i in range(0,234):
	ids.append(i)
	i+=1
	urls = 'https://api.punkapi.com/v2/beers/'+str(i)
	request = requests.get(urls)
	id = request.json()[0]['id']
	name=request.json()[0]['name']
	description=request.json()[0]['description']
	image=request.json()[0]['image_url']
	abv=request.json()[0]['abv']
	target_fg=request.json()[0]['target_fg']
	tagline=request.json()[0]['tagline']
	srm=request.json()[0]['srm']
	ph=request.json()[0]['ph']
	attenuation_level=request.json()[0]['attenuation_level']
	cursor.execute("INSERT INTO CHELAS(id,name,description,image,abv,target_fg,tagline,srm,ph,attenuation_level)VALUES(?,?,?,?,?,?,?,?,?,?)",(id,name,description,image,abv,target_fg,tagline,srm,ph,attenuation_level))
	db.commit()
	print("cervaza {}".format(name)+ " " + "insertada correctamente")
print("Terminado!!")





db.close()
