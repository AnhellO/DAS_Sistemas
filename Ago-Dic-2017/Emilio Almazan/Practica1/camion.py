from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, ejes, potencia):
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        self.ejes = ejes
        self.potencia = potencia

    def getEjes(self):
        return self.ejes

    def getPotencia(self):
        return self.potencia
