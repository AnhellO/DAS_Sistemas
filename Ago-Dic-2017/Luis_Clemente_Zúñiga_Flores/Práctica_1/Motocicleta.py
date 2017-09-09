from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    """Class Motocicleta
    """
    # Attributes:
    __centimetrosCubicos = ""  # (String) 
    
    # Operations
    
    def __init__(self,marca,modelo,color,motor,trans,cc,cantidad,precio):       
        super().__init__(marca,modelo,color,motor,trans,cantidad,precio)
        self.__centimetrosCubicos = cc          
    
    def setCentrimetrosCubicos(self, cc):
        self.__centimetrosCubicos = cc
        
    def getCentimetrosCubicos(self):
        return self.__centimetrosCubicos
        
    def datosDeMoto(self):
        datos_moto = 'Motocicleta.\n'
        datos_moto+= 'Marca: ' + self.getMarca()
        datos_moto+= '\nModelo: ' + self.getModelo()
        datos_moto+= '\nColor: ' + self.getColor()
        datos_moto+= '\nMotor: ' + self.getMotor()
        datos_moto+= '\nTransmisión: ' + self.getTransmision()       
        datos_moto+= '\nSKU: ' + self.getSku()
        datos_moto+= '\nCentímetros Cúbicos (cc): ' + self.getCentimetrosCubicos()       
        datos_moto+= '\nCantidad: ' + str(self.getExistencias())
        datos_moto+= '\nPrecio: ' + str(self.getPrecio())        
        return datos_moto

