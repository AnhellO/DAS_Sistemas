class Electrodomestico(object):

    def __init__(self, marca, color, consumo, potencia, precio):
        self.marca = marca
        self.color = color
        self.consumo = consumo
        self.potencia = potencia
        self.precio = precio

    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getConsumo(self):
        return self.consumo
    def setConsumo(self, consumo):
        self.consumo = consumo

    def getPotencia(self):
        return self.potencia
    def setPotencia(self, potencia):
        self.potencia = potencia

    def getPrecio(self):
        return self.Precio
    def setPrecio(self, precio):
        self.precio = precio

    def conectar(self):
        return "El aparato ha sido conectado."

    def apagar(self):
        return "El aparato está apagado."

    def atribElectrodomestico(self):
        return "Marca: {}\nColor: {}\nConsumo: {}\nPotencia {}\nPrecio: {}\n".format(self.marca,
        self.color, self.consumo, self.potencia, self.precio)

    def factory(clase):
            if clase == "Lavadora":
                return Lavadora()
            elif clase == "Refrigerador":
                return Refrigerador()
            elif clase == "Television":
                return Television()

#-----------------------------------------
class Lavadora(Electrodomestico):

    def __init__(self, marca, color, consumo, potencia, precio, capacidad):
        Electrodomestico.__init__(self,marca, color, consumo, potencia, precio)
        self.capacidad = capacidad

    def getCapacidad(self):
        return self.capacidad
    def setLavar(self, capacidad):
        self.capacidad = capacidad

    def lavar(self):
        return "Se está lavando ropa."

    def atribLavadora(self):
        return "Marca: {}\nColor: {}\nConsumo: {}\nPotencia {}\nPrecio: {}\nCapacidad: {}\n".format(self.marca,
        self.color, self.consumo, self.potencia, self.precio, self.capacidad)

    def mensaje(self):
        return "Este es un mensaje"

#-----------------------------------------
class Refrigerador(Electrodomestico):

    def __init__(self, marca, color, consumo, potencia, precio, num_puertas):
        Electrodomestico.__init__(self,marca, color, consumo, potencia, precio)
        self.num_puertas = num_puertas

    def getNumPuertas(self):
        return self.num_puertas
    def setNumPuertas(self, num_puertas):
        self.num_puertas = num_puertas

    def congelar(self):
        return "Los viveres se están congelando."

    def atribRefrigerador(self):
        return "Marca: {}\nColor: {}\nConsumo: {}\nPotencia {}\nPrecio: {}\nNumero de Puertas: {}\n".format(self.marca,
        self.color, self.consumo, self.potencia, self.precio, self.num_puertas)

    def mensaje(self):
        return "Este es un mensaje"

#-----------------------------------------
class Television(Electrodomestico):

    def __init__(self, marca, color, consumo, potencia, precio, pulgadas):
        Electrodomestico.__init__(self,marca, color, consumo, potencia, precio)
        self.pulgadas = pulgadas

    def getPulgadas(self):
        return self.pulgadas
    def setPulgadas(self, pulgadas):
        self.pulgadas = pulgadas

    def cambiar_canal(self):
        return "Se ha cambiado el canal"

    def mensaje(self):
        return "Television"

    def atribTelevision(self):
        return "Marca: {}\nColor: {}\nConsumo: {}\nPotencia {}\nPrecio: {}\nPulgadas: {}\n".format(self.marca,
        self.color, self.consumo, self.potencia, self.precio, self.pulgadas)

    def mensaje(self):
        return "Este es un mensaje"

def main():
    lavadora = Lavadora('Easy', 'Plateado', '13kw/h', '400w', '11000$', '25kg')
    #print(lavadora.atribLavadora())
    #print(lavadora.lavar())
    tele = Television('Panasonic', 'Negro', '65kw/h', '360w', '16000$', '49¨')
    #print(tele.atribTelevision())
    #print(tele.cambiar_canal())
    refri = Refrigerador('Mabe', 'Blanco', '90kw/h', '375w', '20000$', '3')
    #print(refri.atribRefrigerador())
    #print(refri.congelar())}

if __name__ == "__main__":
    main()
