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

    def datosCamion(self):
    datos_camion = 'Camión.\n'
    datos_camion+= 'Marca: ' + super(Camion,self).getMarca()
    datos_camion+= '\nModelo: ' + super(Camion,self).getModelo()
    datos_camion+= '\nColor: ' + super(Camion,self).getColor()
    datos_camion+= '\nMotor: ' + super(Camion,self).getMotor()
    datos_camion+= '\nTransmisión: ' + super(Camion,self).getTransmision()
    datos_camion+= '\nSKU: ' + super(Camion,self).devuelveSku()
    datos_camion+= '\nEjes: ' + self.getEjes()
    datos_camion+= '\nPotencia: ' + self.getPotencia()
    datos_camion+= '\nCantidad: ' + str(super(Camion,self).getExistencias())
    return datos_camion
