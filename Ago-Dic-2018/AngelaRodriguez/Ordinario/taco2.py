from bs4 import BeautifulSoup

import requests
import sqlite3

url="http://taco-randomizer.herokuapp.com/"
conexion = sqlite3.connect('Recetas.db')
cursor = conexion.cursor()


class Tacos():
	for i in range(1,60):
		req = requests.get(url)
		status_code = req.status_code
		if status_code == 200:
			soup = BeautifulSoup(req.text, "html.parser")

		#soup = BeautifulSoup(page.content, 'html.parser')
			receta=soup.find(id="taco-content")
			rec_items=receta.find_all(class_="row")
			recetas =rec_items[0]

#print(recetas.prettify())
		Cont =recetas.find('h6', class_="light").get_text()
		Desc = recetas.find('div', class_="recipe").get_text()
		links = recetas.find('a', href=True)

		cursor.execute("INSERT INTO RECETA (ID_TACO,CONTRIBUIDOR,DESCRIPCION)VALUES(?,?,?)",(i,Cont,Desc))
		conexion.commit()
print("Recetas guardadas")
	#print(Cont)
	#print(Desc)
	#print(links)

conexion.close()
