from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,ejes,potencia):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku)
        self.ejes = ejes
        self.potencia = potencia

    def setEjes(self,ejes):
        self.ejes = ejes
    def getEjes(Self):
        return self.ejes

    def setPotencia(self,potencia):
        self.potencia = potencia
    def getPotencia(self):
        return self.potencia
