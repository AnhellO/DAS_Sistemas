from abc import ABC, abstractmethod

class cliente():
    def main(self):
        fig=PoligonoFactory.getPoligono("Pentagon")
        print(fig().getType())
        fig2=PoligonoFactory.getPoligono("Square")
        print(fig2().getType())
        fig3=PoligonoFactory.getPoligono("Triangle")
        print(fig3().getType())

class PoligonoFactory ():
    def getPoligono(figura):
        if figura=="Pentagon":
            return Pentagono
        elif figura=="Square":
            return Cuadrardo
        elif figura=="Triangle":
            return Triangulo

class IPoligono(ABC):
    @abstractmethod
    def getType(self)-> str:
       pass

class Triangulo(IPoligono):
    def getType(self) -> str:
        return "triangulo"

class Cuadrardo(IPoligono):
    def getType(self) -> str:
        return "cuadrado"

class Pentagono(IPoligono):
    def getType(self) -> str:
        return "pentagono"

if __name__ == "__main__":
   cliente().main() 