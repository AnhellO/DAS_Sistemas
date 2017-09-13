from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    """Class Automovil
    """
    # Attributes:
    __puertas = ""  # (String) 
    __equipado = True  # (bool) 
    __kilometrosPorLitro = ""  # (String) 
    
    # Operations
    def __init__(self,marca,modelo,color,motor,trans,puertas,equipado,kml,cantidad,precio):
        super().__init__(marca,modelo,color,motor,trans,cantidad,precio)
        self.__puertas = puertas
        if equipado == 'si' or equipado == 'sí':
            self.__equipado = True
        else:
            self.__equipado = False
        self.__kilometrosPorLitro = kml    
        
    def getPuertas(self, puertas):
        self.__puertas = puertas 
    
    def getPuertas(self):
        return self.__puertas        
        
    def getEquipado(self, equipado):
        if equipado == 'si' or equipado == 'sí':
            self.__equipado = True
        else:
            self.__equipado = False

    def getEquipado(self):
        return self.__equipado
    
    def getKmLitro(self, kmLitro):
        self.__kilometrosPorLitro = kmLitro
        
    def getKmLitro(self):
        return self.__kilometrosPorLitro   

    def datosDeAuto(self):
        equipado = ""
        if self.getEquipado() == True:
            equipado = "sí"
        else:
            equipado = "no"            
        datos_auto = 'Automóvil.\n'
        datos_auto+= 'Marca: ' + self.getMarca()
        datos_auto+= '\nModelo: ' + self.getModelo()
        datos_auto+= '\nColor: ' + self.getColor()
        datos_auto+= '\nMotor: ' + self.getMotor()
        datos_auto+= '\nTransmisión: ' + self.getTransmision()
        datos_auto+= '\nPuertas: ' + self.getPuertas()
        datos_auto+= '\nEquipado: ' + equipado 
        datos_auto+= '\nKilómetros por litro: ' + self.getKmLitro()
        datos_auto+= '\nSKU: ' + self.getSku()
        datos_auto+= '\nCantidad: ' + str(self.getExistencias())
        datos_auto+= '\nPrecio: ' + str(self.getPrecio())        
        return datos_auto
        

