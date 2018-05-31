from Electrodomestico import Electrodomestico

class Refrigerador(Electrodomestico):
    """description of class"""

    __pies = ''
    __escarcha= False
    __temperatura = 0

    def __init__(self,color,precio,sku,fecha_creacion,pais_de_origen,marca,pies,escarcha,temperatura):
        super().__init__(color,precio,sku,fecha_creacion,pais_de_origen,marca)
        self.__pies = pies
        self.__escarcha = escarcha
                
    def set_pies(self,pies):
        self.__pies = pies
    
    def get_pies(self):
        return self.__pies

    def set_escarcha(self, escarcha):
        self.__escarcha = escarcha

    def get_escarcha(self):
        return self.__escarcha

    def imprime_especificaciones(self):
        escarcha = 'No'
        if self.__escarcha == True:
            escarcha = 'Sí'
        self.imprimeAtributos()
        print(
            '''
            pies: {}
            Produce escarcha: {}
            '''.format(self.__pies,escarcha)
            )
    
    def menu_temperatura(self):
        self.__temperatura = float(input('Temperatura a la que desea que el refrigerador se encuentre:'))

    def get_temperatura(self):
        return self.__temperatura