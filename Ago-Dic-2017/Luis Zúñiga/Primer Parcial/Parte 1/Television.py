from Electrodomestico import Electrodomestico

class Television(Electrodomestico):
    """description of class"""
    

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