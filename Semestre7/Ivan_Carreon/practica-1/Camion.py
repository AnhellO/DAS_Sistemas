from Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,ejes,potencia):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia)
        self.ejes = ejes
        self.potencia = potencia

    def setEjes(self,ejes):
        self.ejes = ejes
    def getEjes(self):
        return self.ejes

    def setPotencia(self,potencia):
        self.potencia = potencia
    def getPotencia(self):
        return self.potencia

camion1 = Camion('Mercedez Benz','Zetros','Rojo','OM 926 LA','6','113.146 €','Actros 12.0 V6 de 320 caballos','0300','3','2ejes','240 kW (326 CV)')
camion2 = Camion('Scania ','P280','Blanco','Allison 4500PR,6 Speed Automatic ','6','$2,133,820','Euro 5 280 CV','0301','2','1eje','280 CV')
