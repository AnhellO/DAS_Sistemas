class Album():

    def __init__(self, titulo, cancion, genero, artista, año):
        self.titulo = titulo
        self.cancion= cancion
        self.genero = genero
        self.artista = artista
        self.año = año 

    def get_titulo(self):
        return "Informacion: \nTitulo: {} \ncancion: {} \ngenero: {} \nartista: {}\naño: {}\n".format(self.titulo, self.cancion, self.genero, self.artista, self.año)

    def get_cancion(self):
        return"resumen: \ncancion: {}, \ngenero: {}, \nartista: {} \n".format(self.cancion, self.genero, self.artista)
    
class Cancion(Album):
    
    def __init__(self, titulo, cancion, genero, artista, año, Nombre, pista, duracion):
        Album.__init__(self, titulo, cancion, genero, artista, año)
        self.Nombre= Nombre
        self.pista= pista
        self.duracion= duracion
    
    def get_pista(self):
        return "Informacion de la cancion: \nNombre: {}, \npista: {}, \nduracion \n".format(self.Nombre, self.pista, self.duracion)

    def get_Nombre(self, Nombre):
        self.Nombre = Nombre

Alter_Bridge=Album('One Day Remains','Open Your Eyes', 'Rock', 'Alter Bridge','2004')
print(Alter_Bridge.get_titulo())
print(Alter_Bridge.get_cancion())

open=Cancion('One Day Remains','Open Your Eyes','Rock','Alter Bridge','2004','Metalingus','5','4.19 min')
print(open.get_pista())