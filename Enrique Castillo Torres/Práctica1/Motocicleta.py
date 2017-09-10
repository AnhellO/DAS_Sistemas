from Vehiculo import Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, sku, tipo, cc):
        Vehiculo.__init__(self, marca, modelo, color, transmision, sku)
        self.tipo = tipo
        self.cc = cc

    def getTipo(self):
        return self.tipo
    def setTipo(self):
        self.tipo = tipo

    def getCc(self):
        return self.cc
    def setCc(self):
        self.cc = cc

    def atribMoto(self):
        return "Marca: {}\nModelo: {}\nColor: {}\nTransmisión {}\nSKU: {}\nTipo: {}\nCC: {}\n".format(self.marca,
        self.modelo, self.color, self.transmision, self.sku, self.tipo, self.cc)
