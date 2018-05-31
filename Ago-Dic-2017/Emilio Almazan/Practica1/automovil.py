from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, modelo, marca, transmision, color, cilindros, precio, motor, existencia, puertas, equipado, kmxL):
        super().__init__(modelo, marca, transmision, color, cilindros, precio, motor, existencia)
        self.puertas = puertas
        self.equipado = equipado
        self.kmxL = kmxL

    def getPuertas(self):
        return self.puertas

    def getEquipado(self):
        return self.equipado

    def getKmL(self):
        return self.kmxL
