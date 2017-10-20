from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)
