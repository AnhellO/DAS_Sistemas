
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
        self.setSku()    
        
    def setMarca(self, marca):
        self.__marca = marca       
    
    def getMarca(self):
        return self.__marca
        
    def setModelo(self, modelo):
        self.__modelo = modelo        
    
    def getModelo(self):
        return self.__modelo
        
    def setSku(self):
        self.__sku = self.__marca[0:3] + self.__modelo + self.__motor[0:3] + self.__transmision[0:3] + self.__color
          
    def getSku(self):
        return self.__sku.lower()
           
    def setColor(self, color):
        self.__color = color        
    
    def getColor(self):
        return self.__color
        
    def setMotor(self, motor):
        self.__motor = motor        
    
    def getMotor(self):
        return self.__motor
        
    def setTransmision(self, transmision):
        self.__transmision = transmision       
    
    def getTransmision(self):
        return self.__transmision        
      
    def setExistencias(self, existencias):
        self.__existencia = existencias
    
    def getExistencias(self):
        return self.__existencia
    
    def reduceExistencias(self):
        self.__existencia-=1
            
    def setPrecio(self,precio):
        self.__precio = precio
        
    def getPrecio(self):
        return self.__precio
        
    
    

