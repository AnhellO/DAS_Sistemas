import abc

# 'Interfaz' Vehiculo la cual las demas clases implementaran
class Vehiculo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def arrancarMotor(self):
        pass

    @abc.abstractmethod
    def abrirPuerta(self):
        pass

    @abc.abstractmethod
    def embarque(self):
        pass

class Motor:
    def getVelocidad(self):
        velocidad = 250
        return velocidad


class Motocicleta(Vehiculo):
    # La clase Motocicleta depende de Motor
    def __init__(self):
        self.motor = Motor()

    def getVel(self):
        print(self.motor.getVelocidad())

    def arrancarMotor(self):
        print("Moto:\nMira como arranco papá")

    # Estoy obligando a la clase a implementar dos metodos que nunca usará.
    def abrirPuerta(self):
        print("Me obligan a implementar esto :c")

    def embarque(self):
        print("Me obligan a implementar esto :c")



if __name__ == '__main__':
