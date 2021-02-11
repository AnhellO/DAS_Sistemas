import abc
from abc import abstractclassmethod, ABCMeta , abstractmethod    

class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder
    
    def get_moto(self):
        moto = Moto()

        cuerpo = self.__builder.get_cuerpo()
        moto.set_cuerpo(cuerpo)

        motor = self.__builder.get_motor()
        moto.set_motor(motor)

        i = 0
        while i < 2:
            llanta = self.__builder.get_llanta()
            moto.set_llanta(llanta)
            i += 1

        return moto

class Moto:
    def __init__(self):
        self.__llantas = list()
        self.__motor = None
        self.__cuerpo = None
    
    def set_cuerpo(self, cuerpo):
        self.__cuerpo = cuerpo
    
    def set_llanta(self, llanta):
        self.__llantas.append(llanta)

    def set_motor(self, motor):
        self.__motor = motor
    
    def especificaciones(self):
        print(f"cuerpo: {self.__cuerpo.tipo}")
        print(f"caballos de fuerza del motor: {self.__motor.caballos}")
        print(f"Tamaño de llanta: {self.__llantas[0].tamaño}")

class Builder(metaclass=abc.ABCMeta):

    @abstractmethod
    def get_llanta(self): pass
    @abstractmethod
    def get_motor(self): pass
    @abstractmethod
    def get_cuerpo(self): pass


class ItalikaBuilder(Builder):
    def get_llanta(self):
        llanta = Llanta()
        llanta.tamaño = 15
        return llanta
    
    def get_motor(self):
        motor = Motor()
        motor.caballos = 250
        return motor   

    def get_cuerpo(self):
        cuerpo = Cuerpo()
        cuerpo.tipo = "C90"
        return cuerpo

class HarleyBuilder(Builder):
    def get_llanta(self):
        llanta = Llanta()
        llanta.tamaño = 20
        return llanta
    
    def get_motor(self):
        motor = Motor()
        motor.caballos = 300
        return motor   

    def get_cuerpo(self):
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
    director.set_builder(italikaBuilder)
    italika = director.get_moto()
    italika.especificaciones()

    harleyBuilder = HarleyBuilder()
    director = Director()
    print("Harley")
    director.set_builder(harleyBuilder)
    harley = director.get_moto()
    harley.especificaciones()

if __name__ == "__main__":
    main()


    

