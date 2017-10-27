class Electrodomestico(objeto):
    def __init__ (self, marca, modelo, color, numSerie,voltaje ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numSerie = numSerie
        self.voltaje= voltaje

#Metodos getters y setter de los atributos
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def getNumSerie(self):
        return self.numeSerie
    def setNumSerie(self, numSerie):
        self.numSerie = numSerie

    def getVoltaje(self):
        return self.voltaje
    def setVoltaje(self, voltaje):
        self.volataje = volateje

#Metodo encender solo es un mensaje
    def encender(self):
         print("Encendido")
 
#Metodo apagar solo es un mensaje
    def apagar(self):
    print("Apagado")
            



