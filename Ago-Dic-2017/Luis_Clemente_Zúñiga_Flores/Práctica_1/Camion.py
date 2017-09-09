from Vehiculo import Vehiculo

class Camion(Vehiculo):
    """Class Camion
    """
    # Attributes:
    __ejes = ""  # (String) 
    __potencia = ""  # (String) 
    __capacidad = ""  # (String) 
    
    # Operations    
  
    def __init__(self, marca, modelo,color,motor,trans,ejes,potencia,capacidad,cantidad,precio):
        super().__init__(marca,modelo,color,motor,trans,cantidad,precio)
        self.__ejes = ejes
        self.__potencia = potencia
        self.__capacidad = capacidad        
        
    def setEjes(self, ejes):
        self.__ejes = ejes        
    
    def getEjes(self):        
        return self.__ejes
    
    def setPotencia(self, potencia):
        self.__potencia = potencia
    
    def getPotencia(self):
        return self.__potencia
    
    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad
    
    def getCapacidad(self):
        return self.__capacidad
  
    def datosDeCamion(self):
        datos_camion = 'Camión.\n'
        datos_camion+= 'Marca: ' + self.getMarca()       
        datos_camion+= '\nModelo: ' + self.getModelo()       
        datos_camion+= '\nColor: ' + self.getColor()        
        datos_camion+= '\nMotor: ' + self.getMotor()
        datos_camion+= '\nTransmisión: ' + self.getTransmision()       
        datos_camion+= '\nSKU: ' + self.getSku()
        datos_camion+= '\nEjes: ' + self.getEjes()
        datos_camion+= '\nPotencia: ' + self.getPotencia()
        datos_camion+= '\nCapacidad: ' + self.getCapacidad()        
        datos_camion+= '\nCantidad: ' + str(self.getExistencias())                
        datos_camion+= '\nPrecio: ' + str(self.getPrecio())        
        return datos_camion

