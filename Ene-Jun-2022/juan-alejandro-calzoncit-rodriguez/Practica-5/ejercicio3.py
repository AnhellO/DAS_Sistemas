import abc
from abc import ABC, abstractmethod
 
class A(ABC):
    def print_function(self):
        print("Abstract Base Class")
        print("Subclass")

a = A()
a.print_function()
   