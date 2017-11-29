class Electrodomestico(object):
    def __init__ (self,marca="",color="",modelo="",TipoElectrodomestico=""):

        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.TipoElectrodomestico = TipoElectrodomestico

    def factory(clase = "Televisor",**Parametro):
          c= clase.upper()
          if c == "Televisor":
              return Televisor(**Parametro)
          elif c == "Lavadora":
              return Lavadora(**Parametro)
          elif c == "Refrigerador":
              return Refrigerador(**Parametro)

    def getmarca(self):
        return self.marca

    def setmarca(marca):
        self.marca = marca

    def getcolor(self):
        return self.color

    def setcolor(color):
        self.color = color

    def getModelo(self):
        return self.modelo

    def setModelo(modelo):
        self.modelo = modelo

    def getTipoElectro(self):
        return self.TipoElectrodomestico

    def setTipoElectro(TipoElectrodomestico):
        self.TipoElectrodomestico = TipoElectrodomestico

    def on(self):
        print("Electrodomestico encendido")

    def off(self):
        print("Electrodomestico apagado")

class Televisor(Electrodomestico):
    def __init__ (self,marca="",color="",modelo="",TipoElectrodomestico="",Pulgadas=""):
        super().__init__(marca, color, modelo, TipoElectrodomestico)
        self.Pulgadas = Pulgadas

    def getPulgadas(self):
        return self.Pulgadas
    def setPulgadas(Pulgadas):
        self.Pulgadas = Pulgadas

    def SubirVolume(self,VolUp):
        print("Subiendo Volumen :´v {}".format(VolUp))

    def BajarVolume(self,VolDown):
        print("Bajandole al ruido :c {}".format(VolDown))

    def CambioDCanal(self,Cambio):
        print("Ya le cambie {0}".format(Cambio))

class Lavadora(Electrodomestico):
    def __init__ (self,marca="",color="",modelo="",TipoElectrodomestico="",Capacidad="",VelocidadDeLavado=""):
        super().__init__(marca, color, modelo, TipoElectrodomestico)
        self.Capacidad = Capacidad
        self.VelocidadDeLavado = VelocidadDeLavado

    def getCapacidad(self):
        return self.Capacidad
    def setCapacidad(Capacidad):
        self.Capacidad = Capacidad
    def getVelocidad(self):
        return self.VelocidadDeLavado
    def setVelocidad(VelocidadDeLavado):
        self.VelocidadDeLavado = VelocidadDeLavado

    def Llenado(self,llenar):
        print("se llena de awa {}".format(llenar))
    def CicloDeLavado(self,lavar):
        print("girando la wea de enmedio para lavar {}".format(lavar))

class Refrigerador(Electrodomestico):
    def __init__ (self,marca="",color="",modelo="",TipoElectrodomestico="",NumDePuertas="",NumDeCajones=""):
        super().__init__(marca, color, modelo, TipoElectrodomestico)

    def getNumPuertas(self):
        return self.NumDePuertas
    def setNumPuertas(NumDePuertas):
        self.NumDePuertas = NumDePuertas
    def getNumCajones(self):
        return self.NumDeCajones
    def setVelocidad(NumDeCajones):
        self.NumDeCajones = NumDeCajones

    def Congelado(self,congelar):
        print("ps congelando los yelitos {}".format(congelar)

    def Refrigerado(self,Refrigerar):
        print("enfriando todo adentro :v {}".format(Refrigerar))


if __name__ == '__main__':
    p = Electrodomestico.factory("Televisor",marca="Zony",color="blacky",modelo="shido",TipoElectrodomestico="SmartTv",Pulgadas="40")
    print(p.getmarca())
    print(p.getcolor())
    print(p.getModelo())
    print(p.getTipoElectro())
    print(p.getPulgadas())

    p2 = Electrodomestico.factory("Lavadora",marca="ElGy",color="blanky",modelo="viejito",TipoElectrodomestico="LavaSola",Capacidad="30lts",VelocidadDeLavado="Vel5")
    print(p2.getmarca())
    print(p2.getcolor())
    print(p2.getModelo())
    print(p2.getTipoElectro())
    print(p2.getCapacidad())
    print(p2.getVelocidad())

    p3 = Electrodomestico.factory("Refrigerador",marca="guirpul",color="Gray",modelo="superEnfria",TipoElectrodomestico="jrjr",NumDePuertas="2",NumDeCajones="2")
    print(p3.getmarca())
    print(p3.getcolor())
    print(p3.getModelo())
    print(p3.getTipoElectro())
    print(p3.getNumPuertas())
    print(p3.getNumCajones())
