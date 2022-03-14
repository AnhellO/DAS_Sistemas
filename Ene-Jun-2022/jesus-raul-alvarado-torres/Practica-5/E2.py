from abc import ABC, abstractmethod

class Criatura(ABC):

    @abstractmethod
    def Movimiento(self):
        pass

class Humano(Criatura):
    def Movimiento(self):
        super().Movimiento()
        print("Puedo caminar y correr")
 
class Serpiente(Criatura):
    def Movimiento(self):
        super().Movimiento()
        print("Puedo deslizarme")
 
class Perro(Criatura):
    def Movimiento(self):
        super().Movimiento()
        print("Puedo ladrar")
 
class Leon(Criatura):
    def Movimiento(self):
        super().Movimiento()
        print("Puedo rugir")

if __name__ == "__main__":
    Humano = Humano()
    Humano.Movimiento()

    Serpiente = Serpiente()
    Serpiente.Movimiento()

    Perro = Perro()
    Perro.Movimiento()

    Leon = Leon()
    Leon.Movimiento()