import sqlite3
from ScrapiReceta import *
from AbstractClassBuilders import *
import sys
#Autor y programador - "Maximiliano García De Santiago"
class SqlCRUDReceta(AbstractProyectReceta):

    def __init__(self):
        self.conexion = sqlite3.connect('ProyectTaco.db')
        self.cursor = self.conexion.cursor()

    def CrearReceta(self, RecetaTaco):
        receta = (RecetaTaco.Id, RecetaTaco.Nombre_Receta, RecetaTaco.Contribuidores, RecetaTaco.Sub_receta_1, RecetaTaco.Sub_receta_2, RecetaTaco.Sub_receta_3, RecetaTaco.Sub_receta_4)
        self.cursor.execute("INSERT INTO Recetas (Id, Nombre_Receta, Contribuidores, Sub_receta_1, Sub_receta_2, Sub_receta_3, Sub_receta_4) VALUES (?,?,?,?,?,?,?)", receta)
        self.conexion.commit()
        RecetaTaco.Id = self.cursor.lastrowid
        print('Receta guardada' )
        return RecetaTaco

    def MostrarListaCompleta(self):
        self.cursor.execute("SELECT * from Recetas")
        for Recetas in self.cursor.fetchall():
            taco = RecetaTaco(Recetas[1], Recetas[2], Recetas[3], Recetas[4], Recetas[5], Recetas[6], Recetas[0])
            print(taco)

    def MostrarListaNombres(self):
        self.cursor.execute("SELECT * from Recetas")
        for Recetas in self.cursor.fetchall():
            taco = RecetaTaco(Recetas[1], Recetas[2], Recetas[3], Recetas[4], Recetas[5], Recetas[6], Recetas[0])
            taco1 = taco.Id
            print(taco1)

    def ConsultarReceta(self, Id):
        self.cursor.execute("SELECT * from Recetas where Id = ?", [Id])
        for Recetas in self.cursor.fetchall():
            taco = RecetaTaco(Recetas[1], Recetas[2], Recetas[3], Recetas[4], Recetas[5], Recetas[6], Recetas[0])
        return print(taco)

    def BorrarReceta(self, Id):
        self.cursor.execute("DELETE from Recetas WHERE Id=?", [Id])
        self.conexion.commit()
        print('Receta borrado')
        return True


if __name__ == "__main__":
    UrlReceta = ScrapTaco()
    crud1 = SqlCRUDReceta()
#    Id = 1
#    MostrarLista = crud.MostrarListaNombres()
#    ConsultarReceta = crud.ConsultarRecet(Id)
#    while Id <= 50:
#        Borrar = crud.BorrarReceta(Id)
#        receta1 = UrlReceta.DatosReceta('http://taco-randomizer.herokuapp.com/', Id)
#        newReceta = crud.CrearReceta(receta1)
#        sleep(1)
#        Id += 1
