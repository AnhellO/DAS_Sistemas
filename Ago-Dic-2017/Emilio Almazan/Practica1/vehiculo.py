class Vehiculo:
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
        self.cilindros = cilindros
        self.precio = precio
        self.motor = motor
        self.existencia = existencia

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getColor(self):
        return self.color

    def getTransmision(self):
        return self.transmision

    def getCilindros(self):
        return self.cilindros

    def getPrecio(self):
        return self.precio

    def getMotor(self):
        return self.motor

    def getExistencia(self):
        return self.existencia

    def incrementaExist(self, n):
        self.existencia = n

    def decrementaExist(self, n):
        self.existencia = n
