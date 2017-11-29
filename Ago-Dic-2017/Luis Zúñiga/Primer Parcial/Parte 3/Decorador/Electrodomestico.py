class Electrodomestico(object):

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
			
class Refrigerador(Electrodomestico):

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
		

class Television(Electrodomestico):
    __HDMI = True
    __SMART = True   


    def __init__(self,color,precio,sku,fecha_creacion,pais_de_origen,marca,smart,hdmi):
        super().__init__(color,precio,sku,fecha_creacion,pais_de_origen,marca)
        self.__SMART = smart
        self.__HDMI = hdmi
    
    def set_hdmi(self,hdmi):
        self.__HDMI = hdmi

    def get_hdmi(self):
        return self.__HDMI


    def get_smart(self):
        return self.__SMART

    def datos_tv(self):
        smart = 'Sí'
        hdmi = 'Sí'        
        if self.__HDMI == False:
            hdmi = 'No'
        if self.__SMART == False:
            smart = 'No'
        datos = '''
        Smart: {}
        Entrada HDMI: {}
        '''.format(smart,hdmi)
        return datos     


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


