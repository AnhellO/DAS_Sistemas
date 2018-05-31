from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, tipo, cc):
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        self.tipo = tipo
        self.cc = cc

    def getTipo(self):
        return self.tipo

    def getCC(self):
        return self.cc
