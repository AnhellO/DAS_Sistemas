class Vehiculo:
    def __init__(self,marca, modelo, color, transmision, sku):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
        self.sku = sku

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo
    def setMarca(self,modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color

    def getTransmision(self):
        return self.transmision
    def setTransmision(self,transmision):
        self.transmision = transmision

    def getSku(self):
        return self.sku
    def setSku(self,color):
        self.sku = sku

    def atribVehiculo(self):
        return "Marca: {}\nModelo: {}\nColor: {}\nTransmisión: {}\nSKU: {}\n".format(self.marca,
        self.modelo, self.color, self.transmision, self.sku)
