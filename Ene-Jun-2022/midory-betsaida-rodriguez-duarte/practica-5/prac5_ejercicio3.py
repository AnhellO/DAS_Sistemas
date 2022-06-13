import abc
from abc import ABC, abstractmethod

#A la interfaz se le agrego el metodo abstracto
class A(ABC):
    @abstractmethod
    def print_function(self):
        pass



#Esto es una subclase, hereda de la interfaz de A el mismo metodo.
class B(A):
    def print_function(self):
        print("Abstract Base Class")
        print("subclase")
    

b = B()
b.print_function()