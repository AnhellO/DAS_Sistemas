class Vehiculo:
    # Definicion de __init__ y atributos de la clase Vehiculo
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia):
        # Se inician atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.transmision = transmision
        self.cilindros = cilindros
        self.precio = precio
        self.motor = motor
        self.existencia = existencia

    # Metodo getMarca
    def getMarca(self):
        return self.marca

    # Metodo getModelo
    def getModelo(self):
        return self.modelo

    # Metodo getColor
    def getColor(self):
        return self.color

    # Metodo getTransmision
    def getTransmision(self):
        return self.transmision

    # Metodo getCilindros
    def getCilindros(self):
        return self.cilindros

    # Metodo getPrecio
    def getPrecio(self):
        return self.precio

    # Metodo getMotor
    def getMotor(self):
        return self.motor

    # Metodo getExistencia regresa un reporte con la marca, modelo y existencia
    # del vehiculo
    def getExistencia(self):
        return "Hay {0} {1} {2} disponibles.".format(self.existencia,
                                            self.marca, self.modelo)

    # Metodo getNumExistencia() regresa existencia
    def getNumExistencia(self):
        return self.existencia

    # incrementaExist aumenta la existencia del vehiculo
    def incrementaExist(self, mas):
        self.existencia = mas

    # decrementaExist resta la existencia del vehiculo
    def decrementaExist(self, menos):
        self.existencia = menos

    # informeVehiculo regresa un string con los datos de Vehiculo, el cual será usado
    # en las clases hijo donde se agregarán los datos faltantes
    def informeVehiculo(self):
        return "{0} {1}\nColor: {2}\nTransmision: {3}\nCilindros: {4}\nMotor: {5}\n\t\t\tPRECIO: {6}".format(self.marca,
                        self.modelo,self.color,self.transmision,self.cilindros,self.motor,self.precio)
