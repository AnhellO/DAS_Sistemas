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
    
    def estableceCentrimetrosCubicos(self, cc):
        self.__centimetrosCubicos = cc
        
    def obtenCentimetrosCubicos(self):
        return self.__centimetrosCubicos
        
    def datosDeMoto(self):
        datos_moto = 'Motocicleta.\n'
        datos_moto+= 'Marca: ' + self.obtenMarca()
        datos_moto+= '\nModelo: ' + self.obtenModelo()
        datos_moto+= '\nColor: ' + self.obtenColor()
        datos_moto+= '\nMotor: ' + self.obtenMotor()
        datos_moto+= '\nTransmisión: ' + self.obtenTransmision()       
        datos_moto+= '\nSKU: ' + self.devuelveSku()
        datos_moto+= '\nCentímetros Cúbicos (cc): ' + self.obtenCentimetrosCubicos()       
        datos_moto+= '\nCantidad: ' + str(self.obtenExistencias())
        datos_moto+= '\nPrecio: ' + str(self.devuelvePrecio())        
        return datos_moto

