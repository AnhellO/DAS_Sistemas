from Vehiculo import Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, sku, ejes, potencia):
        Vehiculo.__init__(self, marca, modelo, color, transmision, sku)
        self.ejes = ejes
        self.potencia = potencia

    def getEjes(self):
        return self.Ejes
    def setEjes(self):
        self.Ejes = Ejes

    def getPotencia(self):
        return self.potencia
    def setPotencia(self):
        self.potencia = potencia

    def atribCamion(self):
        return "Marca: {}\nModelo: {}\nColor: {}\nTransmisión {}\nSKU: {}\nNúmero de ejes: {}\nPotencia del motor: {}\n".format(self.marca,
        self.modelo, self.color, self.transmision, self.sku, self.ejes, self.potencia)
