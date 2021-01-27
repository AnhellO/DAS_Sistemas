import abc
from abc import ABCMeta, abstractmethod

class Pista (metaclass=abc.ABCMeta):
    @abstractmethod

    def __init__(self, name, fav, duracion, artista):
        self.name = name
        self.fav = fav
        self.duracion = duracion
        self.artista = artista
        
        def getName(self):
            return self.name
        def getFav(self):
            return self.fav
        def getDuracion(self):
            return self.duracion
        def getArtista(self):
            return self.artista

        def main():
            rolita1 = Pista('El sapito', 'si', '2', 'Ghost')
            rolita2 = Pista('Ramito de violetas', 'no', '3', 'Pesado')
            rolita3 = Pista('pumped up kids', 'no', '4', 'Caloncho')

        print("\nLista: " + self.rolita1() + "\n" + self.rolita2() + "\n" + self.rolita3())

        def addAño(self):
            pass


class Reproductor(Pista):
    def disco(self):
        print("\nNombre: " +self.getName()+"\nFavorito:"+self.getFav()+"\nDuracion:"+self.getDuracion()+"\nArtista:"+self.getArtista())

archivo = open("Ej1.csv","a")

name = input("Nombre de la rolita: ")
fav = input("Es de tu agrado?: ")
duracion = input("Cuanto dura? (numero entero): ")
artista = input("Quien la canta: ")

print ("Se han capturado: " +name + "," +fav + "," +duracion + "," + artista )


archivo.write("\n")
archivo.write(name)
archivo.write("\n")
archivo.write(duracion)
archivo.write("\n")
archivo.write(artista)
archivo.write("\n")
if  fav=="si":
    archivo.write(fav)
else:
    archivo = open("Ej1.csv", "a")
    archivo.truncate()

archivo.close()

print ("Disco de favoritos\n")
archivo = open("Ej1.csv")

print(archivo.read())

archivo.close()