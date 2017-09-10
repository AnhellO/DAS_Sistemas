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

---------------------------------
from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, puertas, equipado, kmL):
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        self.puertas = puertas
        self.equipado = equipado
        self.kmL = kmL

    def getPuertas(self):
        return self.puertas

    def getEquipado(self):
        return self.equipado

    def getKmL(self):
        return self.kmL
---------------------------------
from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, ejes, potencia):
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        self.ejes = ejes
        self.potencia = potencia

    def getEjes(self):
        return self.ejes

    def getPotencia(self):
        return self.potencia
--------------------------------
from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, transmision, cilindros, precio, motor, existencia, tipo, cc):
        super().__init__(marca, modelo, color, transmision, cilindros, precio, motor, existencia)
        self.tipo = tipo
        self.cc = cc

    def getTipo(self):
        return self.tipo

    def getCC(self):
        return self.cc
--------------------------------
class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.edad = edad
        self.domicilio = domicilio
        self.telefono = telefono

    def getNombre(self):
        return self.nombre

    def getApellidoPaterno(self):
        return self.apellidoPaterno

    def getApellidoMaterno(self):
        return self.apellidoMaterno

    def getEdad(self):
        return self.edad

    def getDomicilio(self):
        return self.domicilio

    def getTelefono(self):
        return self.telefono
---------------------------------
from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)
---------------------------------
from persona import Persona

class Vendedor(Persona):
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono, numVendedor):
        super().__init__(nombre, apellidoPaterno, apellidoMaterno, edad, domicilio, telefono)
        self.numVendedor = numVendedor

    def getNumVendedor(self):
        return self.numVendedor
----------------------------------
class Agencia:

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion
