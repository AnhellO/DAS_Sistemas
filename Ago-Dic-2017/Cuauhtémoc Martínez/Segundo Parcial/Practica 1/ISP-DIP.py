import abc

# Se crean tres 'Interfaces' cada una con una funcion diferente
class Vehiculo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def arrancarMotor(self):
        pass

class VehiculoPuerta(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def abrirPuerta(self):
        pass

class VehiculoEmbarque(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def embarque(self):
        pass

class Motor:
    def getVelocidad(self):
        velocidad = 250
        return velocidad


class Motocicleta(Vehiculo):
    # La clase se quita la respondsabilidad de instanciar
    # se pone como parametro al constructor quitando la dependencia de clase
    def __init__(self, motor):
        self.motor = motor

    def getVel(self):
        print("Velocidad: {}Km/H".format(self.motor.getVelocidad()))

    # Implemento lo que necesita
    def arrancarMotor(self):
        print("Moto:\nMira como arranco papá")

class Automovil(Vehiculo,VehiculoPuerta):
    def __init__(self, motor):
        self.motor = motor

    def getVel(self):
        print("Velocidad: {}Km/H".format(self.motor.getVelocidad()))

    def arrancarMotor(self):
        print("Auto:\nMira Como arranco papá")

    def abrirPuerta(self):
        print("Estoy abriendo una puerta...de noche")

class Trailer(Vehiculo,VehiculoPuerta,VehiculoEmbarque):
    def __init__(self, motor):
        self.motor = motor

    def getVel(self):
        print("Velocidad: {}Km/H".format(self.motor.getVelocidad()))

    def arrancarMotor(self):
        print("Trailer:\nMira como arranco papá")

    def abrirPuerta(self):
        print("Abriendo puertas fierro viejon parienton")

    def embarque(self):
        print("Ola ke ase, embarcando o ke ase")


if __name__ == '__main__':
    mot = Motor()
    m = Motocicleta(mot)
    a = Automovil(mot)
    t = Trailer(mot)

    m.arrancarMotor()
    m.getVel()

    a.abrirPuerta()
    a.arrancarMotor()
    a.getVel()

    t.arrancarMotor()
    t.abrirPuerta()
    t.embarque()
    t.getVel()
'''
Salida esperada:

    Moto:
    Mira como arranco papá
    Velocidad: 250Km/H

    Estoy abriendo una puerta...de noche
    Auto:
    Mira Como arranco papá
    Velocidad: 250Km/H

    Trailer:
    Mira como arranco papá
    Abriendo puertas fierro viejon pariento
    Ola ke ase, embarcando o ke ase
    Velocidad: 250Km/H
                                                    '''
