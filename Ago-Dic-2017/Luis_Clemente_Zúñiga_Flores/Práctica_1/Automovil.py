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
        
    def establecePuertas(self, puertas):
        self.__puertas = puertas 
    
    def obtenPuertas(self):
        return self.__puertas        
        
    def estableceEquipado(self, equipado):
        if equipado == 'si' or equipado == 'sí':
            self.__equipado = True
        else:
            self.__equipado = False

    def obtenEquipado(self):
        return self.__equipado
    
    def estableceKmLitro(self, kmLitro):
        self.__kilometrosPorLitro = kmLitro
        
    def obtenKmLitro(self):
        return self.__kilometrosPorLitro   

    def datosDeAuto(self):
        equipado = ""
        if self.obtenEquipado() == True:
            equipado = "sí"
        else:
            equipado = "no"            
        datos_auto = 'Automóvil.\n'
        datos_auto+= 'Marca: ' + self.obtenMarca()
        datos_auto+= '\nModelo: ' + self.obtenModelo()
        datos_auto+= '\nColor: ' + self.obtenColor()
        datos_auto+= '\nMotor: ' + self.obtenMotor()
        datos_auto+= '\nTransmisión: ' + self.obtenTransmision()
        datos_auto+= '\nPuertas: ' + self.obtenPuertas()
        datos_auto+= '\nEquipado: ' + equipado 
        datos_auto+= '\nKilómetros por litro: ' + self.obtenKmLitro()
        datos_auto+= '\nSKU: ' + self.devuelveSku()
        datos_auto+= '\nCantidad: ' + str(self.obtenExistencias())
        datos_auto+= '\nPrecio: ' + str(self.devuelvePrecio())        
        return datos_auto
        

