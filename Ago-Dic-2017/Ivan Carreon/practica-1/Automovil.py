from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,puertas,equipado,kmlitros):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia)
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


Carro1 = Automovil('Nissan','Altima SE','Negro','XTRONIC CVT','6','$461,400','270 HP y 251 lb-pie de torque','0100','5','5','si','17.15kml')
Carro2 = Automovil('Volkswagen','Jetta GLI','Blanco','DSG de 6 velocidades','4','$417,330','turbo TSI','0101','5','5','no','15.31kml')
Carro3 = Automovil('Toyota','Camry LE','Rojo','Súper ECT-i','4','$374,300','VVT-i Dual con ETCS-i','0102','6','5','si','16.53kml')
