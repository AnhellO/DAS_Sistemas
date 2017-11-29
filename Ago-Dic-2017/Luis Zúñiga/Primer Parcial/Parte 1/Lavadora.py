from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):

    __ciclos = 0
    __kilos = 0
   


    def __init__(self,color,precio,sku,fecha_creacion,pais_de_origen,marca,kilos,ciclos):
        super().__init__(color,precio,sku,fecha_creacion,pais_de_origen,marca)
        self.__ciclos = ciclos
        self.__kilos = kilos
        
    
    def set_ciclos(self,ciclos):
        self.__ciclos = ciclos

    def get_ciclos(self):
        return self.__ciclos
    
    def set_kilos(self,kilos):
        self.__kilos = kilos

    def get_kilos(self):
        return self.__kilos

    def datos_lavadora(self):
       self.imprimeAtributos()
       print(
            '''
            Ciclos: {}
            Kilos: {}
            '''.format(self.__ciclos,self.__kilos)            
            )

