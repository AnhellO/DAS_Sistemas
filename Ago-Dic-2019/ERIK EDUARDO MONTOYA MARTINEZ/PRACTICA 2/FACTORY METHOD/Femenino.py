from Persona import Personas

class Femenino(Personas):
    """Esta clase hereda de la clase persona, solo definiremos el constructor"""

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print
        "Hola " + nombre + " su edad es " + str(edad)