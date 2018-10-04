class InstrumentoMusical(object):
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def setNombre(nom):
        self.nombre = nom
    def getNombre():
        return self.nombre
    def setColor(col):
        self.color = col
    def getColor():
        return self.color

class Guitarra(InstrumentosMusicales):
    def __init__(self, nombre, color, tipo):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo
    def setTipo(self, tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def gritar(self):
        print("{} ESTO ES...GENIAAAAAAAAAL!".format(self.nombre))

    def __str__(self):
        return "Nombre: {} \nColor: {} \nTipo: {}".format(self.nombre, self.color, self.tipo)
class Bateria(InstrumentosMusicales):
    def __init__(self, nombre, color, marca):
        self.nombre = nombre
        self.color = color
        self.marca = marca
    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def TocaR(self):
        print("{} VENGA MEXICOOOOOOO!".format(self.nombre))

    def __str__(self):
        return "Nombre: {} \nColor: {} \nMarca: {}".format(self.nombre, self.color, self.marca)
if __name__ == "__main__":
    guitarra = Guitarra("La morena", "negra", "Electrica")
    guitarra2 = Guitarra("Normal", "rojo", "Acústica")
    print(guitarra)
    print(guitarra2)
    bateria = Bateria("Bate Bate", "Blanca","Sonor")
    bateria2 = Bateria("Como de que rock", "Dorada","Pearl Road")
    print(bateria)
    print(bateria2)