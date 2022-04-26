from abc import ABC, abstractmethod


class abs(ABC):
    def print_function(self):
        print("Abstract Base Class")


class sub(abs):
    def print_function(self):
        print("Subclass")


if __name__ == '__main__':
    abs().print_function()
    sub().print_function()