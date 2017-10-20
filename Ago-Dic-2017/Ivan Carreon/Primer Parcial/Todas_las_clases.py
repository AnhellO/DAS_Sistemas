class Electrodomestico:
    def __init__(self, marca , modelo , color , consumo , tipo , precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.consumo = consumo
        self.tipo = tipo
        self.precio = precio

    def factory(clase = "lavadora",**kargs):
        cl= clase.upper()
        if cl == "LAVADORA":
            return Lavadora(**kargs)
        elif cl == "TELEVISION":
            return Television(**kargs)
        elif cl == "REFRIGERADOR":
            return Refrigerador(**kargs)

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getColor(self):
        return self.color

    def getConsumo(self):
        return self.consumo

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setColor(self, color):
        self.color = color

    def setConsumo(self,consumo):
        self.consumo = consumo

    def setTipo(self, tipo):
        self.tipo = tipo

    def setPrecio(self, precio):
        self.precio = precio

    def prender(self):
        encender = "{} {} Encendido y listo para el servicio".format(self.marca,self.modelo)
        return(encender)
    def apagar(self):
        apagar = "{} {} ~c apago~".format(self.marca, self.modelo)
        return(apagar)

class Lavadora(Electrodomestico):
    def __init__(self, marca , modelo , color, consumo, tipo, precio, capacidad, velocidades):
        super().__init__(marca, modelo, color, consumo, tipo, precio)
        self.capacidad = capacidad
        self.velocidades = velocidades

    def getCapacidad(self):
        return self.capacidad
    def setCapacidad(self,capacidad):
        self.capacidad = capacidad

    def getVelocidades(self):
        return self.velocidades
    def setVelocidades(self, velocidades):
        self.velocidades = velocidades

    def EnUso(self, prendas):
        print("en estos momentos me encuentro en atzion turbo ".format(prendas))

class Television(Electrodomestico):
    def __init__(self, marca , modelo , color, consumo , tipo , precio, pulgadas , smartTV):
        super().__init__(marca, modelo, color, consumo, tipo, precio)
        self.pulgadas = pulgadas
        self.smartTV = smartTV

    def getPulgadas(self):
        return self.pulgadas
    def getSmartTv(self):
        return self.smartTV

    def setPulgadas(self, pulgadas):
        self.pulgadas = pulgadas
    def setSmartTv(self, smartTV):
        self.smartTV = smartTV

    def cambiar_de_canal(self):
        canal = "cambiaste el canal de la television {}".format(self.modelo)
        return(canal)

class Refrigerador(Electrodomestico):
    def __init__(self, marca , modelo , color ,consumo , tipo , precio , altura , componentes ):
        super().__init__(marca, modelo, color, consumo, tipo, precio)
        self.altura = altura
        self.componentes = componentes

    def getAltura(self):
        return self.altura
    def getComponentes(self):
        return self.componentes

    def setAltura(self, altura):
        self.altura = altura
    def setComponentes(self, componentes):
        self.componentes = componentes

    def guardar_comida(self):
        comida = "se guardo algo en {}".format(self.modelo)
        return(comida)

if __name__ == '__main__':
    elect = Electrodomestico.factory("Lavadora",marca="leñador", modelo="supah", color = "rosa",consumo = "500.43watts", tipo="Lavadora con secadora" , precio = "$chorrocientosmil", capacidad = "2personas", velocidades = "1,no menos, como 5")
    elect1 = Electrodomestico.factory("Television",marca="soni",modelo="24-7",color="negro",consumo = "100watts",tipo = "digital" , precio = "$10500" , pulgadas = "14 pulgadas" , smartTV = "si")
    elect2 = Electrodomestico.factory("Refrigerador",marca="kiki",modelo="o-m-g",color="blanco",consumo = "678.098watts",tipo = "Electrico-Ecologico" , precio = "$11543" , altura = "1.97mts", componentes = "con dispensador de hielitos")
    print(elect.getMarca())
    print(elect.getModelo())
    print(elect.getColor())
    print(elect.getConsumo())
    print(elect.getTipo())
    print(elect.getPrecio())
    print(elect.getCapacidad())
    print(elect.getVelocidades())
    print("="*80)
    print(elect1.getMarca())
    print(elect1.getModelo())
    print(elect1.getColor())
    print(elect1.getConsumo())
    print(elect1.getTipo())
    print(elect1.getPrecio())
    print(elect1.getPulgadas())
    print(elect1.getSmartTv())
    print("="*80)
    print(elect2.getMarca())
    print(elect2.getModelo())
    print(elect2.getColor())
    print(elect2.getConsumo())
    print(elect2.getTipo())
    print(elect2.getPrecio())
    print(elect2.getAltura())
    print(elect2.getComponentes())
