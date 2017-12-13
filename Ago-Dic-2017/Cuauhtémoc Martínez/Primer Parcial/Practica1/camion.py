# Se importa la clase Vehiculo
from vehiculo import Vehiculo

class Camion(Vehiculo):
    # Definicion de __init__ y atributos de la clase Camion
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, ejes, potencia):
        # Con super se  llama a __init__ de la clase padre y así se establecen los datos
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        # Se inician atributos locales
        self.ejes = ejes
        self.potencia = potencia

    # Metodo getEjes
    def getEjes(self):
        return self.ejes

    # Metodo getPotencia
    def getPotencia(self):
        return self.potencia

    # informeCamion llama a informeVehiculo de la clase padre y se agregan los
    # atributos locales para generar un string con los datos del Camion
    def informeCamion(self):
        return "{}\nExtras: {}\tPotencia: {}".format(self.informeVehiculo(),
                                    self.ejes, self.potencia)
