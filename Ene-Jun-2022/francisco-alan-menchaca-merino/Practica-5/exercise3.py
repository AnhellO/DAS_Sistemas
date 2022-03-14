from abc import ABC, abstractmethod


class A(ABC):
    def print_function(self):
        print("Abstract Base Class")


class B(A):
    def print_function(self):
        print("Subclass")


if __name__ == '__main__':
    A().print_function()
    B().print_function()
