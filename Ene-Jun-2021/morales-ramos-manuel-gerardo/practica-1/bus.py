from vehicle import Vehicle

# Class Bus inheriting from Vehicle class

class Bus(Vehicle):
    
    # Inherited constructor, method and attributes

    def __init__(self, max_speed, mileage, capacity):
        super().__init__(max_speed, mileage, capacity)

    def __str__(self):
        return f"I'm a bus! ->\nMax. Speed: {self.max_speed} Km/h\nMileage: {self.mileage} Km\nCapacity: {self.capacity} persons"