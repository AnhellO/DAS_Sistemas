
class Vehiculo:
    """Abstract class Vehiculo
    """
    # Attributes:
    __marca = ""  # (String) 
    __modelo = ""  # (String) 
    __color = ""  # (String) 
    __transmision = ""  # (String) 
    __motor = ""  # (String) 
    __sku = ""  # (String) 
    __existencia = 0  # (int)
    __precio = 0 
    
    # Operations
    
    def __init__(self, marca, modelo, color, motor, transmision, existencia, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__motor = motor
        self.__transmision = transmision
        self.__existencia = existencia
        self.__precio = precio
        self.estableceSku()    
        
    def estableceMarca(self, marca):
        self.__marca = marca       
    
    def obtenMarca(self):
        return self.__marca
        
    def estableceModelo(self, modelo):
        self.__modelo = modelo        
    
    def obtenModelo(self):
        return self.__modelo
        
    def estableceSku(self):
        self.__sku = self.__marca[0:3] + self.__modelo + self.__motor[0:3] + self.__transmision[0:3] + self.__color
          
    def devuelveSku(self):
        return self.__sku.lower()
           
    def estableceColor(self, color):
        self.__color = color        
    
    def obtenColor(self):
        return self.__color
        
    def estableceMotor(self, motor):
        self.__motor = motor        
    
    def obtenMotor(self):
        return self.__motor
        
    def estableceTransmision(self, transmision):
        self.__transmision = transmision       
    
    def obtenTransmision(self):
        return self.__transmision        
      
    def estableceExistencias(self, existencias):
        self.__existencia = existencias
    
    def obtenExistencias(self):
        return self.__existencia
    
    def reduceExistencias(self):
        self.__existencia-=1
            
    def establecePrecio(self,precio):
        self.__precio = precio
        
    def devuelvePrecio(self):
        return self.__precio
        
    
    

