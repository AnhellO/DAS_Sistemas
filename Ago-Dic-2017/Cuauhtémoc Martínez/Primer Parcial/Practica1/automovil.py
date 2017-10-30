# Se importa la clase Vehiculo
from vehiculo import Vehiculo

class Automovil(Vehiculo):
    # Definicion de __init__ y atributos de la clase Automovil
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, puertas, equipado, kmL):
        # Con super se  llama a __init__ de la clase padre y así se establecen los datos
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        # Se inician atributos locales
        self.puertas = puertas
        self.equipado = equipado
        self.kmL = kmL

    # Metodo getPuertas
    def getPuertas(self):
        return self.puertas

    # Metodo getEquipado
    def getEquipado(self):
        return self.equipado

    # Metodo getKmL
    def getKmL(self):
        return self.kmL

    # informeAutomovil llama a informeVehiculo de la clase padre y se agregan los
    # atributos locales para generar un string con los datos del Automovil
    def informeAutomovil(self):
        return "{}\nExtras: {}\t{}\tRendimiento: {}".format(self.informeVehiculo(),
                                    self.puertas, self.equipado, self.kmL)
