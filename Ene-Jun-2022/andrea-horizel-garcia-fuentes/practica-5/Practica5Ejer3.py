import abc
from abc import ABC, abstractmethod

#A esta interfaz se le agrega el metodo abstracto
class A(ABC):
    @abstractmethod
    def print_function(self):
        pass



#Una subclase, hereda de la interfaz de A el mismo metodo.
class B(A):
    def print_function(self):
        print("Abstract Base Class")
        print("subclase")
    

b = B()
b.print_function()