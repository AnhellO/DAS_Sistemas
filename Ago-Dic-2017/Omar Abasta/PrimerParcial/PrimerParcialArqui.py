class Electrodomestico(object):
    def_init_(self, marca="", color="",modelo="", tipo="", size=""):
    self.marca = marca
    self.color = color
    self.modelo = modelo
    self.tipo = tipo
    self.size = size

    def factory(clase = "television", **parametros):
        c = clase.upper()
        if c == "lavadora":
            return Lavadora(**parametros)
    elif c == "televsion":
            return Television(**parametros)
    elif c == "regriferador":
            return Refrigerador(**parametros)

    def getMarca(self):
        return self.marca

    def getColor(self):
        retur self.color

    def getModelo(self):
        return self.modelo

    def getTipo(self):
        return self.tipo

    def getSize(self):
        return self.size

    def setMarca(marca):
        self.marca = marca

    def setColor(self):
        self.color = color

    def setModelo(modelo):
        self.modelo = modelo

    def setTipo(tipo):
        self.tipo = tipo

    def setSize(size):
        self.size = size

    def encender(self):
        print("Se a encendido la tele")

    def apagar(self):
        print("Se a apagado la tele")


class Lavadora(Electrodomestico):
    def __init__(self, marca="", color="", modelo="", tipo="", size="", numModos=""):
        super().__init__(marca, color, modelo, tipo, size)
        self.numModos = numModos

    def getnumModos(self):
        return self.numModos

    def setnumModos(numModos):
        self.numModos = numModos

    def secar(self, ropa):
        print("Lavando(Lavanda nortena los carros del ano) {}".format(ropa))



class Refrigerador(Electrodomestico):
    def __init__(self, marca="", color="", modelo="", tipo="", size="", cantPuertas=""):
        super().__init__(marca, color, modelo, tipo, size)
        self.cantPuertas = cantPuertas

    def getcantPuertas(self):
        return self.cantPuertas

    def setcantPuertas(cantPuertas):
        self.cantPuertas = cantPuertas

    def RefgrigeraComida(self, comida):
        print ("Hola, soy un refri :v {}".format(comida))


class Television(Electrodomestico):
    def __init__(self, marca="", color="", modelo="", tipo="", size="", resolucion=""):
        super().__init__(marca, color, modelo, tipo, size)
        self.resolucion = resolucion

    def getResolucion(self):
        return self.resolucion

    def setResolucion(resolucion):
        self.resolucion = resolucion

    def cambiarCanal(self,canal):
        print("Cambiaste de canal a las novelas {0}".format(canal))


if __name__ == '__main__':
    #Este solo es un ejemplo, ya que podemos hacer lo mismo con Lavadora y Regriferador
    ElectrodomesticoAlpha = Electrodomestico.factory("Television",marca="LG", color="Negro como el mal", modelo="LaWeaCuatica", tipo="Plasma", size="Grande", resolucion="4K")
    print(ElectrodomesticoAlpha.getMarca())
