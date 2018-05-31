# Se importa la clase Vehiculo
from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    # Definicion de __init__ y atributos de la clase Motocicleta
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, tipo, cc):
        # Con super se  llama a __init__ de la clase padre y así se establecen los datos
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        # Se inician atributos locales
        self.tipo = tipo
        self.cc = cc

    # Metodo getTipo
    def getTipo(self):
        return self.tipo

    # Metodo getCC
    def getCC(self):
        return self.cc

    # informeMotocicleta llama a informeVehiculo de la clase padre y se agregan los
    # atributos locales para generar un string con los datos de la Motocicleta
    def informeMotocicleta(self):
        return "{}\nExtras: Tipo: {}\t\tCentimetros Cubicos: {}".format(self.informeVehiculo(),
                                    self.tipo, self.cc)
