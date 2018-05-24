class Car(object):

    def factory(type):
        if type == "Racecar":
            return Racecar()
        if type == "Van":
            return Van()
        assert 0, "Bad car creation: " + type

    factory = staticmethod(factory)

class Racecar(Car):
    def drive(self): print("Racecar driving.")

class Van(Car):
    def drive(self): print("Van driving.")

# Create object using factory.
obj = Car.factory("Racecar")
obj.drive()
