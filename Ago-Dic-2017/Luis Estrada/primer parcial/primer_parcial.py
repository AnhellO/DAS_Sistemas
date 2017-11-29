class electrodomestico():
    def __init__(self,marca, color,modelo,tamano,fecha):
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.tamano=tamano
        self.fecha=fecha


    def Factory(clase="refrigerador",**parametros):
        cl= clase.upper()
        if cl=="LAVADORA":
            return lavadora(**parametros)
        elif cl=="TELEVISION":
            return television(**parametros)
        elif cl=="REFRIGERADOR":
            return refrigerador(**parametros)

        

    def encender(self):
        print('encendido')

    def apagar(self):
        print('apagado')

    def set_marca(self,marca):
        self.marca=marca
    def get_marca(self):
        return self.marca

    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color

    def set_modelo(self,modelo):
        self.modelo=modelo
    def get_modelo(self):
        return self.modelo

    def set_tamano(self,tamano):
        self.tamano=tamano
    def get_tamano(self):
        return self.tamano

    def set_fecha(self,fecha):
        self.fecha=fecha
    def get_fecha(self):
        return self.fecha

class lavadora(electrodomestico):
    def __init__(self,marca,color,modelo,tamano,fecha,potencia):
        super().__init__(marca,color,modelo,tamano,fecha)
        self.potencia=potencia

    def set_potencia(self,potencia):
        self.potencia=potencia
    def get_potencia(self):
        return self.potencia
    
    def lavar(self):
        print('estoy lavando')

class television(electrodomestico):
    def __init__(self,marca,color,modelo,tamano,fecha,num_canales):
        super().__init__(marca,color,modelo,tamano,fecha)
        self.num_canales=num_canales

    def set_num_canales(self,num_canales):
        self.num_canales=num_canales
    def get_num_canales(self):
        return self.num_canales

    def ver_cable(self):
        print('estoy viendo cable')

class refrigerador(electrodomestico):
    def __init__(self,marca,color,modelo,tamano,fecha,peso):
        super().__init__(marca,color,modelo,tamano,fecha)
        self.peso=peso
    def set_peso(self,peso):
        self.peso=peso
    def get_peso(self):
        return self.peso

    def enfriar(self):
        print('estoy enfriando')


if __name__ == '__main__':
    

    electrodomestico1=electrodomestico.Factory("lavadora",marca="easy",color="negro",modelo="123",tamano="med",fecha="march",potencia="23w")

    electrodomestico2=electrodomestico.Factory("television",marca="easy",color="bco",modelo="323",tamano="med",fecha="march",num_canales="9")

    electrodomestico3=electrodomestico.Factory("refrigerador",marca="across",color="rosa",modelo="124",tamano="chico",fecha="april",peso="34")

    print(electrodomestico1.get_potencia())
    print(electrodomestico1.lavar())
    print(electrodomestico2.get_num_canales())
    print(electrodomestico2.ver_cable())
    print(electrodomestico3.get_peso())
    print(electrodomestico3.enfriar())
    print(electrodomestico1.get_marca())
    print(electrodomestico1.get_color())
    print(electrodomestico1.get_fecha())
    print(electrodomestico1.get_modelo())
    print(electrodomestico1.get_tamano())
    
        
        



    
    
