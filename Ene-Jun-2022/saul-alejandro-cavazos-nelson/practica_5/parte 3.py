from abc import ABC, abstractmethod
 
class A(ABC):
    @abstractmethod
    def print_function(self):
        print('Abstract Base Class')
        pass

class subclassA(A):
    def print_function(self):
      super().print_function()
      print('subclass')
a=subclassA()
a.print_function()