#DAS Práctica 5.2.3

import abc
from abc import ABC, abstractmethod
 
class A(ABC):
    def print_function(self):
        print("Abstract Base Class")
        
class B(A):
    def print_function(self):
        super().print_function()
        print("Subclass")
        
SC=B()
SC.print_function()