from __future__ import print_function
from abc import ABCMeta, abstractmethod


class Car(object):
    def __init__(self, wheels=4, seats=4, color="Black"):
        self.wheels = wheels
        self.seats = seats
        self.color = color

    def __str__(self):
        return "This is a {0} car with {1} wheels and {2} seats.".format(
            self.color, self.wheels, self.seats
        )


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


class CarBuilderDirector(object):
    @staticmethod
    def construct():
        builder = CarBuilder()
        builder.set_wheels(8)
        builder.set_seats(4)
        builder.set_color("Red")
        return builder.get_result()


car = CarBuilderDirector.construct()
print(car)