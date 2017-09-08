from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,tipo,cenCub):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku)
        self.tipo = tipo
        self.cenCub = cenCub

    def getTipo(self):
        return self.tipo
    def getCenCub(self):
        return self.cenCub

    def setTipo(self,tipo):
        self.tipo = tipo
    def setCenCub(self,cenCub):
        self.cenCub = cenCub
