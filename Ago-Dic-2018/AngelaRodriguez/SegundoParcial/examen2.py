
import time, re, requests, os, errno, json, sqlite3
ids=[]
i=0
db = sqlite3.connect('NBA.db')
cursor = db.cursor()
for i in range(0,63):
	ids.append(i)
	i+=1
	urls = 'https://any-api.com/nba_com/nba_com/docs/_boxscore/' + str(i)	  
	

	request = requests.get(urls)

	id = request.json()['id']
	name=request.json()['name']
	gameId=request.json()['gameId']
	eventName=request.json()['eventName']
	points=request.json()['points']
	teamId=request.json()['teamId']

	cursor.execute("INSERT INTO nba2(name,gameId,eventName,points,teamId)VALUES(?,?,?,?,?)",(name,gameId,eventName,points,teamId))
	db.commit()
	print ("dato: {}".format(name)+ " " + "el dato fue insertado correctamente")
print("Fin de la lista!!")
db.close()