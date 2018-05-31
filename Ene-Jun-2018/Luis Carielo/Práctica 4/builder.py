from __future__ import print_function
from abc import ABCMeta, abstractmethod

# Producto
class Car(object):
    def __init__(self, wheels=4, seats=4, color="Black"):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return "Este es un carro de color {0} con {1} llantas y {2} asientos.".format(self.color, self.wheels, self.seats)


#Clase Builder (abstracta)
class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_wheels(self, value):
        pass

    @abstractmethod
    def set_seats(self, value):
        pass

    @abstractmethod
    def set_color(self, value):
        pass

    @abstractmethod
    def get_result(self):
        pass


#Concrete Builder
class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_wheels(self, value):
        self.car.wheels = value

    def set_seats(self, value):
        self.car.seats = value

    def set_color(self, value):
        self.car.color = value

    def get_result(self):
        return self.car

#Director
class CarBuilderDirector(object):
    @staticmethod
    def construct():
        builder = CarBuilder()
        builder.set_wheels(8)
        builder.set_seats(4)
        builder.set_color("Rojo")
        return builder.get_result()


car = CarBuilderDirector.construct()
print(car)