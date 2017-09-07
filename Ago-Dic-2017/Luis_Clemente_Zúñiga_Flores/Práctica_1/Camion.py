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
        
    def estableceEjes(self, ejes):
        self.__ejes = ejes        
    
    def obtenEjes(self):        
        return self.__ejes
    
    def establecePotencia(self, potencia):
        self.__potencia = potencia
    
    def obtenPotencia(self):
        return self.__potencia
    
    def estableceCapacidad(self, capacidad):
        self.__capacidad = capacidad
    
    def obtenCapacidad(self):
        return self.__capacidad
  
    def datosDeCamion(self):
        datos_camion = 'Camión.\n'
        datos_camion+= 'Marca: ' + self.obtenMarca()       
        datos_camion+= '\nModelo: ' + self.obtenModelo()       
        datos_camion+= '\nColor: ' + self.obtenColor()        
        datos_camion+= '\nMotor: ' + self.obtenMotor()
        datos_camion+= '\nTransmisión: ' + self.obtenTransmision()       
        datos_camion+= '\nSKU: ' + self.devuelveSku()
        datos_camion+= '\nEjes: ' + self.obtenEjes()
        datos_camion+= '\nPotencia: ' + self.obtenPotencia()
        datos_camion+= '\nCapacidad: ' + self.obtenCapacidad()        
        datos_camion+= '\nCantidad: ' + str(self.obtenExistencias())                
        datos_camion+= '\nPrecio: ' + str(self.devuelvePrecio())        
        return datos_camion

