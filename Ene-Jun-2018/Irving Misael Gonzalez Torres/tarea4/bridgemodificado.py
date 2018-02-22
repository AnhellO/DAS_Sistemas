from abc import ABC, abstractmethod


class Figura: #AbstractInterface
    
    @abstractmethod
    def dibujar(self):
        pass


class Bridge(Figura):

    def __init__(self):
        self.__implementation = None

######################################################################
######################################################################

class Circulo(Bridge): #UseCase1
  
    def __init__(self, implementation):
        self.__implementation = implementation

    def dibujar(self): #someFunctionality
        print ("Dibujando Circulo...."),
        self.__implementation.pintar()

######################################################################

class Triangulo(Bridge):#UseCase2

    def __init__(self, implementation):
        self.__implementation = implementation

    def dibujar(self): #someFunctionality
        print ("Dibujando Trinagulo..."),
        self.__implementation.pintar()

######################################################################
######################################################################

class Color: #ImplementationInterface
    
    @abstractmethod
    def pintar(self): #anotherFunctionality
        pass

######################################################################
######################################################################

class Negro(Color):

    def pintar(self):
        print ("pintando figura de negro.")

######################################################################

class Azul(Color):

    def pintar(self):
        print ("Pintando figura de azul.")

######################################################################
######################################################################

def main():
    color_n = Negro()
    color_a = Azul()



    figura1 = Circulo(color_n)
    figura1.dibujar()

    figura1 = Circulo(color_a)
    figura1.dibujar()

    figura2 = Triangulo(color_n)
    figura2.dibujar()

    figura2 = Triangulo(color_a)
    figura2.dibujar()


if __name__ == "__main__":
    main()