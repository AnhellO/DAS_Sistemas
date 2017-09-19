from Vehiculo import Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, sku, carroceria, rendimiento):
        Vehiculo.__init__(self, marca, modelo, color, transmision, sku)
        self.carroceria = carroceria
        self.rendimiento = rendimiento

    def getCarroceria(self):
        return self.carroceria
    def setCarroceria(self):
        self.carroceria = carroceria

    def getRendimiento(self):
        return self.rendimiento
    def setRendimiento(self):
        self.rendimiento = rendimiento

    def atribAuto(self):
        return "Marca: {}\nModelo: {}\nColor: {}\nTransmisión {}\nSKU: {}\nTipo de Carrocería: {}\nRendimiento: {}\n".format(self.marca,
        self.modelo, self.color, self.transmision, self.sku, self.carroceria, self.rendimiento)
