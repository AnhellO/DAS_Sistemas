from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,puertas,equipado,kmlitros):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku)
        self.puertas = puertas
        self.equipado = equipado
        self.kmlitros = kmlitros

    def setPuertas(self,puertas):
        self.puertas = puertas
    def getPuertas(self):
        return self.puertas

    def setEquipado(self,equipado):
        self.equipado = equipado
    def getEquipado(self):
        return self.equipado

    def setKmL(self,kmlitros):
        self.kmlitros = kmlitros
    def getKmL(self):
        return self.kmlitros


Carro1 = ('Nissan','Altima','','','','','')
