import abc

# Product 1
class Car:
    def __init__(self, seats=None, engine=None, trip_computer=None, gps=None) -> None:
        self.seats = seats
        self.engine = engine
        self.trip_computer = trip_computer
        self.gps = gps
    
    def set_seats(self, seats):
        self.seats = seats

    def set_engine(self, engine):
        self.engine = engine

    def set_trip_computer(self, trip_computer):
        self.trip_computer = trip_computer

    def set_gps(self, gps):
        self.gps = gps

# Product 2        
class Manual:
    def __init__(self, desc_seats=None, desc_engine=None, desc_trip_computer=None, desc_gps=None) -> None:
        self.desc_seats = desc_seats
        self.desc_engine = desc_engine
        self.desc_trip_computer = desc_trip_computer
        self.desc_gps = desc_gps
    
    def set_seats(self, desc_seats):
        self.desc_seats = desc_seats

    def set_engine(self, desc_engine):
        self.desc_engine = desc_engine

    def set_trip_computer(self, desc_trip_computer):
        self.desc_trip_computer = desc_trip_computer

    def set_gps(self, desc_gps):
        self.desc_gps = desc_gps


# Builder interface
class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass
    
    @abc.abstractmethod
    def set_seats(self, number):
        pass
    
    @abc.abstractmethod
    def set_engine(self, engine):
        pass
    
    @abc.abstractmethod
    def set_trip_computer(self, km):
        pass
    
    @abc.abstractmethod
    def set_gps(self, has_gps):
        pass
    
    @abc.abstractmethod
    def get_result(self):
        pass

# ConcreteBuilder 1
class CarBuilder(Builder):
    def __init__(self) -> None:
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.set_seats(number)

    def set_engine(self, engine):
        self.car.set_engine(engine)

    def set_trip_computer(self, km):
        self.car.set_trip_computer(km)

    def set_gps(self, has_gps):
        self.car.set_gps(has_gps)
    
    def get_result(self):
        return self.car

# ConcreteBuilder 2
class CarManualBuilder(Builder):
    def __init__(self, ) -> None:
        self.car_manual = Manual()

    def reset(self):
        self.car_manual = Manual()

    def set_seats(self, desc_number):
        self.car_manual.set_seats(desc_number)

    def set_engine(self, desc_engine):
        self.car_manual.set_engine(desc_engine)

    def set_trip_computer(self, desc_km):
        self.car_manual.set_trip_computer(desc_km)

    def set_gps(self, desc_gps):
        self.car_manual.set_gps(desc_gps)

    def get_result(self):
        return self.car_manual