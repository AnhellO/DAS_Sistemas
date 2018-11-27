import sqlite3
from BeerAPI import *
from AbstractBeer import *
import sys

class SqlCRUD(AbstractPunk):
    def __init__(self):
        self.conexion = sqlite3.connect('BeerDB.db')
        self.cursor = self.conexion.cursor()

    def CrearCerveza(self, Cerveza):
        cerv = (Cerveza.id, Cerveza.name, Cerveza.descripcion, Cerveza.image, Cerveza.abv, Cerveza.ibu, Cerveza.ebc, Cerveza.food_pairing, Cerveza.first_brewed, Cerveza.ph, Cerveza.attenuation_level)
        self.cursor.execute("INSERT INTO Beer (Id, Name, Descripcion, Image, Abv, Ibu, Ebc, Food_pairing, First_brewed, Ph, Attenuation_level) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", cerv)
        self.conexion.commit()
        Cerveza.id = self.cursor.lastrowid

    def MostrarLista(self):
        self.cursor.execute("SELECT * from Beer")
        for Beef in self.cursor.fetchall():
            cerv = Cerveza(Beer[1], Beer[2], Beer[3], Beer[4], Beer[5], Beer[6], Beer[7], Beer[8], Beer[9], Beer[10], Beer[11])
            print(cerv)

    def ConsultarCerveza(self, id):
        self.cursor.execute("SELECT * from Beer where Id = ?", [id])
        for Summoner in self.cursor.fetchall():
            cerv = Cerveza(Beer[1], Beer[2], Beer[3], Beer[4], Beer[5], Beer[6], Beer[7], Beer[8], Beer[9], Beer[10], Beer[11])
        return print(cerv)

if __name__ == "__main__":
    pagina = ApiBeer()
    crud = SqlCRUD()
    IDS = 1
    while IDS <= 234:
        datos = pagina.DatosBeer('https://api.punkapi.com/v2/beers/' +str(IDS) )
#        print(datos)
        sleep(1)
        IDS += 1

        newCerveza = crud.CrearCerveza(datos)
        lista = crud.MostrarLista()
