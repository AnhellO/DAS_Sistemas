from abc import ABCMeta, abstractmethod
 
class A(metaclass = ABCMeta):

    @abstractmethod
    def print_function(self):
        print("Abstract Base Class")

class B(A):

    def print_function(self):
        return super().print_function()

if __name__ == '__main__':

    test_B = B()
    test_B.print_function()
    if issubclass(B,A) == True:
        print("Subclass")
