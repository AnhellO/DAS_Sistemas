import time, re, requests, os, errno, json, sqlite3

ids=[]
i=0
j=0
db = sqlite3.connect('Tvmaze.db')
cursor = db.cursor()

#Angel la API que agarré estaba super mal
#Incluso ni pude crear los archivos de json.
#Tenía muchos id que no tenían contenido
#Por eso agregue la lista de esa forma
list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1000,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,1001,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,1002,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
for i in list:


	i+=1
	url = 'http://api.tvmaze.com/shows/'+str(i)
	request = requests.get(url)
	id = request.json()['id']
	name=request.json()['name']
	runtime=request.json()['runtime']
	weight=request.json()['weight']
	officialSite=request.json()['officialSite']
	status=request.json()['status']
	cursor.execute("INSERT INTO TVMAZE(id,name,runtime,weight,officialSite,status)VALUES(?,?,?,?,?,?)",(id,name,runtime,weight,officialSite,status))
	db.commit()
	print("TvMaze {}".format(name)+ " " + "se insertó correctamente")
	print("Listo")
