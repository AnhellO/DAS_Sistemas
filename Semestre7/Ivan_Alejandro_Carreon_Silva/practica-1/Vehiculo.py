class Vehiculo:
    def __init__(self,marca,modelo,color,transmision,cilindros,precio,motor,sku,existencia):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
        self.cilindros = cilindros
        self.precio = precio
        self.motor = motor
        self.sku = sku
        self.existencia = existencia

    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def setModelo(self,modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

    def setColor(self,color):
        self.color = color
    def getColor(self):
        return self.color

    def setTransmision(self,transmision):
        self.transmision = transmision
    def getTransmision(self):
        return self.transmision

    def setCilindros(self,cilindros):
        self.cilindros = cilindros
    def getCilindros(self):
        return self.cilindros

    def setPrecio(self,precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio

    def setMotor(self,motor):
        self.motor = motor
    def getMotor(self):
        return self.motor

    def setSku(self,sku):
        self.sku = sku
    def getSku(self):
        return self.sku

    def setExistencia(self,existencia):
        self.existencia = existencia
    def getExistencia(self):
        return self.existencia

    def incrementaExist(self,n):
        self.existencia = n
    def decrementaExist(self,n):
        self.existencia = n
