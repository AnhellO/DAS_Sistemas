import abc
from unittest.main import main

class Bike:
    def __init__(self, seats=None, wheels=None, pedals = None , handle =None) -> None:
        self.seats = seats
        self.wheels = wheels
        self.pedals = pedals
        self.handle = handle
    
    def set_seats(self, seats):
        self.seats = seats

    def set_wheels(self, wheels):
        self.wheels = wheels

    def set_pedals(self, pedals):
        self.pedals = pedals

    def set_handle(self, handle):
        self.handle = handle

# Product 2        
class Electric_Bike:
    def __init__(self, e_seats=None, e_wheels=None, e_pedals=None, e_handle=None, battery=None, motor=None) -> None:
        self.e_seats = e_seats
        self.e_wheels = e_wheels
        self.e_pedals = e_pedals
        self.e_handle = e_handle
        self.battery = battery
        self.motor = motor
    
    def set_seats(self, e_seats):
        self.e_seats = e_seats

    def set_wheels(self, e_wheels):
        self.e_wheels = e_wheels

    def set_pedals(self, e_pedals):
        self.e_pedals = e_pedals

    def set_handle(self, e_handle):
        self.e_handle = e_handle
    
    def set_battery(self, battery):
        self.battery = battery

    def set_motor(self, motor):
        self.motor = motor

# Builder interface
class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass
    
    @abc.abstractmethod
    def set_seats(self, number):
        pass
    
    @abc.abstractmethod
    def set_wheels(self, wheels):
        pass
    
    @abc.abstractmethod
    def set_pedals(self, pedals):
        pass
    
    @abc.abstractmethod
    def set_handle(self, handle):
        pass
    
    @abc.abstractmethod
    def get_result(self):
        pass

# ConcreteBuilder 1
class Bike_Builder(Builder):
    def __init__(self) -> None:
        self.bike = Bike()

    def reset(self):
        self.bike = Bike()

    def set_seats(self, number):
        self.bike.set_seats(number)

    def set_wheels(self, wheels):
        self.bike.set_wheels(wheels)

    def set_pedals(self, pedals):
        self.bike.set_pedals(pedals)

    def set_handle(self, handle):
        self.bike.set_handle(handle)
    
    def get_result(self):
        return self.bike

# ConcreteBuilder 2
class Electric_Bike_Builder(Builder):
    def __init__(self) -> None:
        self.electric_bike = Electric_Bike()

    def reset(self):
        self.electric_bike = Electric_Bike()

    def set_seats(self, e_seats):
        self.electric_bike.set_seats(e_seats)

    def set_wheels(self, e_wheels):
        self.electric_bike.set_wheels(e_wheels)

    def set_pedals(self, e_pedals):
        self.electric_bike.set_pedals(e_pedals)

    def set_handle(self, e_handle):
        self.electric_bike.set_handle(e_handle)
    
    def set_battery(self, battery):
        self.electric_bike.set_battery(battery)
    
    def set_motor(self, motor):
        self.electric_bike.set_motor(motor)

    def get_result(self):
        return self.electric_bike

if __name__ == "__main__":
    main()
