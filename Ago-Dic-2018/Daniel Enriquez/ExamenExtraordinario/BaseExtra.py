import time, re, requests, os, errno, json, sqlite3

i=0
#conexion con la base
db = sqlite3.connect('Cervecitas.db')
cursor = db.cursor()
#Mediante este ciclo se trae una cerveza  a la vez de la API desde la posicion 0 a la 50
for i in range(0,50):
    i+=1

    url = 'https://api.punkapi.com/v2/beers/'+ str(i)
    request = requests.get(url)
#Elementos extraidos del Jason de la API
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

#Se insertan en las tablas ya creadas en el archivo base.py a la vez que se hace cada ciclo for
    cursor.execute("INSERT INTO INFOPRINCIPAL(id,name,description) VALUES(?,?,?)",(id,name,description))
    db.commit()
    cursor.execute("INSERT INTO INFOSECUNDARIA(id,image,first_brewed,target_fg) VALUES(?,?,?,?)",(id,image,first_brewed,target_fg))
    db.commit()
    cursor.execute("INSERT INTO INFOEXTRA(id,srm,abv,ph,tagline,attenuation_level) VALUES(?,?,?,?,?,?)",(id,srm,abv,ph,tagline,attenuation_level))
    db.commit()
#Extrae el nombre de la cerveza para poder apreciar la insercion de cada elemnto
    print("Cerveza {}".format(name)+ " " + "se insertó correctamente")

db.close()
