import abc
from abc import ABC, abstractmethod
 
class A(ABC):
    def print_function(self):
        print("Abstract Base Class")

class HeredandoA(A):
    def print_function(self) -> str:
        super().print_function()
        msj ="Subclass"
        return msj


if __name__ == "__main__":

    Clase = HeredandoA()
    print(Clase.print_function())