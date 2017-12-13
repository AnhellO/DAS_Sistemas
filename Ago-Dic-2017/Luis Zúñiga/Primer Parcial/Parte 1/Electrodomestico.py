class Electrodomestico(object):
    """description of class"""
    
    __color = ''
    __precio = ''
    __sku = ''
    __fecha_creacion = ''
    __pais_de_origen = ''
    __marca = ''

    def __init__(self,color,precio,sku,fecha_creacion,pais_de_origen,marca):
        self.__color = color
        self.__precio = precio
        self.__sku = sku
        self.__fecha_creacion = fecha_creacion
        self.__pais_de_origen = pais_de_origen
        self.__marca = marca

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_precio(self,precio):
        self.__precio = precio

    def get_precio(self):
        return self.__color

    def set_sku(self,fecha):
        self.__sku = sku

    def get_sku(self):
        return self.__sku
 
    def set_fecha_creacion(self,fecha):
        self.__fecha_creacion = fecha

    def get_fecha_creacion(self):
        return self.__fecha_creacion
    
    def set_pais(self,pais):
        self.__pais_de_origen = pais

    def get_pais(self):
        return self.__pais_de_origen

    def get_fecha_creacion(self):
        return self.__pais_de_origen

    def imprimeAtributos(self):
        print(
            '''
            Detalles del producto:
            Marca: {}
            Color: {}
            precio: {}
            sku: {}
            fecha de creación: {}
            pais de origen: {}
            '''.format(self.__marca,self.__color,self.__precio,self.__sku,self.__fecha_creacion,self.__pais_de_origen)      
            
            )

    
    
    







