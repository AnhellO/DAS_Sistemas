from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia,tipo,cenCub):
        super().__init__(marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia)
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

Moto1 = Motocicleta('Suzuki','Intruder M1800R','Negro','Manual (5 marchas)','2','14.637 €','4 T','0200','4','custom','1.783cc')
Moto2 = Motocicleta('Harley Davidson','Softail','Gris','Manual (6 marchas)','2','23.300 €','4 T','0201','3','custom','1.690cc')
Moto3 = Motocicleta('Triumph','TIGER 800 XC','Plata','Manual (6 marchas)','3','9.395 €','4 T','0202','5','trail','799cc')
