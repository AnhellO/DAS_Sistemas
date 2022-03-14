import abc
from abc import ABC, abstractmethod

class A(ABC):
    def print_function(self):
        print("Abstract Base Class")

class subclass(A):
    def print_function(self):
        super().print_function()
        print('subclass')

if __name__ == "__main__":
    sub=subclass()
    sub.print_function() 