# Se importa la clase Persona
from persona import Persona

class Vendedor(Persona):
    # Definicion de __init__ y atributos de la clase Vendedor
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono, numVendedor):
        # Con super se  llama a __init__ de la clase padre y así se establecen los datos
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)
        # Se inician atributos locales
        self.numVendedor = numVendedor

    # Metodo getNumVendedor
    def getNumVendedor(self):
        return self.numVendedor

    # informeVendedor llama a informePersona de la clase padre y se agregan los
    # atributos locales para generar un string con los datos del Vendedor    
    def informeVendedor(self):
        return "#Vendedor: {0}\n{1}".format(self.numVendedor,self.informePersona())
