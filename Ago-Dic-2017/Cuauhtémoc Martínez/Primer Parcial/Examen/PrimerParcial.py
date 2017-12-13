# Clase Electrodomestico tendrá metodo factory.
class Electrodomestico(object):
    # Metodo __init__ con calores por defecto.
    def __init__(self, marca="", modelo="", tipo="", lugar="", altura=""):
        # Se inicializan los atributos.
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.lugar = lugar
        self.altura = altura

    # Metodo factory, envía los parametros que el usuario le envie.
    def factory(clase = "refrigerador", **parametros):
        # upper, para evitar errores.
        cl = clase.upper()
        if cl == "LAVADORA":
            return Lavadora(**parametros)
        elif cl == "TELEVISION":
            return Television(**parametros)
        elif cl == "REFRIGERADOR":
            return Refrigerador(**parametros)

    # Getters de Electrodomestico.
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getTipo(self):
        return self.tipo

    def getLugar(self):
        return self.lugar

    def getAltura(self):
        return self.altura

    # Setters de Electrodomestico.
    def setMarca(marca):
        self.marca = marca

    def setModelo(modelo):
        self.modelo = modelo

    def setTipo(tipo):
        self.tipo = tipo

    def setLugar(lugar):
        self.lugar = lugar

    def setAltura(altura):
        self.altura = altura

    # Metodo encender, solo manda mensaje.
    def encender(self):
        print("Hola, me estoy encendiendo")

    # Metodo apagar, solo manda mensaje.
    def apagar(self):
        print("Adios, me estoy apagando")


# Clase Lavadora hereda de Electrodomestico.
class Lavadora(Electrodomestico):
    # Metodo __init__ con calores por defecto.
    def __init__(self, marca="", modelo="", tipo="", lugar="", altura="", numFunciones=""):
        # Un super para el alma.
        super().__init__(marca, modelo, tipo, lugar, altura)
        # Se inicializan atributos de Lavadora.
        self.numFunciones = numFunciones

    def getNumFunciones(self):
        return self.numFunciones

    def setNumFunciones(numFunciones):
        self.numFunciones = numFunciones

    # Una lavadora debe de lavar, apoco no carnal.
    def lavar(self, ropa):
        print("Hola, estoy lavando {}".format(ropa))


# Clase Refrigerador hereda de Electrodomestico.
class Refrigerador(Electrodomestico):
    # Metodo __init__ con calores por defecto.
    def __init__(self, marca="", modelo="", tipo="", lugar="", altura="", numPuertas=""):
        # Otro super para el alma.
        super().__init__(marca, modelo, tipo, lugar, altura)
        # Se inicializan atributos de Refrigerador.
        self.numPuertas = numPuertas

    def getNumPuertas(self):
        return self.numPuertas

    def setNumPuertas(numPuertas):
        self.numPuertas = numPuertas

    # Metodo propio de Refrigerador.
    def almacenarComida(self, comida):
        print ("Hola, estoy almacenando {}".format(comida))

# Clase Refrigerador hereda de Electrodomestico.
class Television(Electrodomestico):
    # Metodo __init__ con calores por defecto.
    def __init__(self, marca="", modelo="", tipo="", lugar="", altura="", resolucion=""):
        # Último super para el corazón.
        super().__init__(marca, modelo, tipo, lugar,altura)
        # Se inicializan atributos de Television.
        self.resolucion = resolucion

    def getResolucion(self):
        return self.resolucion

    def setResolucion(resolucion):
        self.resolucion = resolucion

    # Cambia canal sin control. Metodo anti-chaviza.
    def cambiarCanal(self,canal):
        print("Hola, estoy cambiando al canal {0}".format(canal))


# TEST LOKOCHONES.
if __name__ == '__main__':
    '''Diagrama de objetos toma estos valores ya que usando factory y el menú, no hay ningún valor fijo.'''
    lav = Electrodomestico.factory("Lavadora", marca="AshenOne", modelo="Anor Londo", tipo="Lavadora con secadora y planchadora", lugar="Cuarto de lavado y tu corazón", altura="3 metros", numFunciones="50 funciones diferentes")
    #refri = Electrodomestico.factory("Refrigerador", marca="Patito", modelo="x-23", tipo="Sencillo", lugar="Cocina", altura="1.5 metros", numPuertas="Solo dos :c")
    #tv = Electrodomestico.factory("Television", marca="Kematian", modelo="Hevnoraak", tipo="Pantalla mas plana que tablón", lugar="Cuarto del Brayan", altura=".5 metros", resolucion="Chafa")
    print(lav.getMarca())
