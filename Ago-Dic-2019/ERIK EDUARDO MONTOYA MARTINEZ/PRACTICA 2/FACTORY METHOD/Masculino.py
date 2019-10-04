from Persona import Personas

class Masculino(Personas):
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print
        "Hola " + nombre + " su edad es " + str(edad)
