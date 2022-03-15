import abc
from abc import ABC, abstractmethod
 
class A(ABC):
    def print_function(self):
        print("Abstract Base Class")
        

class SubClassB(A):
    
    def print_function(self):
        A.print_function(self)
        print("Subclass")

if __name__ == "__main__":
    B = SubClassB()
    B.print_function()