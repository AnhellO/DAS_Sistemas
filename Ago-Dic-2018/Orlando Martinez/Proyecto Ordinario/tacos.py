from bs4 import BeautifulSoup
import requests
import sqlite3

URL = "http://taco-randomizer.herokuapp.com/"
conexion = sqlite3.connect('Taqueria.db')
cursor =conexion.cursor()

# Realizamos la petición a la web
class Tacos():
    for i in range(1,51):

        req = requests.get(URL)
        soup = BeautifulSoup(req.text, "html.parser")
        Nombre = soup.find('div', {'class': 'ten columns centered'}).h1.text
        Subrecetas=soup.find('div', {'class': 'recipe'}).text
        contribuidores=soup.find('h6', {'class': 'light'}).text
        conexion = sqlite3.connect('Taqueria.db')
        cursor =conexion.cursor()
        cursor.execute("INSERT INTO Tacos (ID_TACO,NOMBRE_TACO,SUBRECETAS,CONTRIBUIDORES) VALUES(?,?,?,?)",(i,Nombre,Subrecetas,contribuidores))
        conexion.commit()
