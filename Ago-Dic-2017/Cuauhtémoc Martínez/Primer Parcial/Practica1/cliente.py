# Se importa la clase Persona
from persona import Persona

class Cliente(Persona):
    # Definicion de __init__ y atributos de la clase Cliente
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        # Con super se  llama a __init__ de la clase padre y así se establecen los datos
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)

    # informeCliente llama a informePersona de la clase padre
    # para generar un string con los datos del Cliente
    def informeCliente(self):
        return self.informePersona()
