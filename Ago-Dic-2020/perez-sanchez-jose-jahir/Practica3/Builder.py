import abc
from abc import abstractclassmethod, ABCMeta , abstractmethod    

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder=builder
    
    def getMoto(self):
        moto = Moto()

        cuerpo = self.__builder.getCuerpo()
        moto.setCuerpo(cuerpo)

        motor = self.__builder.getMotor()
        moto.setMotor(motor)

        i = 0
        while i < 2:
            llanta = self.__builder.getLLanta()
            moto.setLLanta(llanta)
            i +=1

        return moto

class Moto:
    def __init__(self):
        self.__llantas = list()
        self.__motor = None
        self.__cuerpo = None
    
    def setCuerpo(self, cuerpo):
        self.__cuerpo = cuerpo
    
    def setLLanta(self, llanta):
        self.__llantas.append(llanta)

    def setMotor(self, motor):
        self.__motor = motor
    
    def especificaciones(self):
        print(f"cuerpo: {self.__cuerpo.tipo}")
        print(f"caballos de fuerza del motor: {self.__motor.caballos}")
        print(f"Tamaño de llanta: {self.__llantas[0].tamaño}")

class Builder(metaclass=abc.ABCMeta):

    @abstractmethod
    def getLLanta(self): pass
    @abstractmethod
    def getMotor(self): pass
    @abstractmethod
    def getCuerpo(self): pass


class ItalikaBuilder(Builder):
    def getLLanta(self):
        llanta = Llanta()
        llanta.tamaño = 15
        return llanta
    
    def getMotor(self):
        motor = Motor()
        motor.caballos = 250
        return motor   

    def getCuerpo(self):
        cuerpo = Cuerpo()
        cuerpo.tipo = "C90"
        return cuerpo

class HarleyBuilder(Builder):
    def getLLanta(self):
        llanta = Llanta()
        llanta.tamaño = 20
        return llanta
    
    def getMotor(self):
        motor = Motor()
        motor.caballos = 300
        return motor   

    def getCuerpo(self):
        cuerpo = Cuerpo()
        cuerpo.tipo = "Chopper"
        return cuerpo

class Llanta:
    tamaño = None

class Motor:
    caballos = None

class Cuerpo:
    tipo = None


def main():
    italikaBuilder = ItalikaBuilder()
    director = Director()
    print("Italika")
    director.setBuilder(italikaBuilder)
    italika = director.getMoto()
    italika.especificaciones()

    harleyBuilder = HarleyBuilder()
    director = Director()
    print("Harley")
    director.setBuilder(harleyBuilder)
    harley = director.getMoto()
    harley.especificaciones()

if __name__ == "__main__":
    main()


    

