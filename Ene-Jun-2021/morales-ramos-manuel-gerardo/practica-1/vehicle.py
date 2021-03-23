class Vehicle:

    # Class attribute

    random = 0

    # Constructor and instance attributes
    
    def __init__(self, max_speed, mileage, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    # The string representation of the object

    def __str__(self):
        return f"Max. Speed: {self.max_speed} km/h\nMileage: {self.mileage} Km\nCapacity: {self.capacity} persons"

    # Getters and Setters

    def get_max_speed(self):
        return self.max_speed
    
    def set_max_speed(self, value):
        self.max_speed = value

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, value):
        self.mileage = value
    
    def get_capacity(self):
        return self.capacity

    def set_capacity(self, value):
        self.capacity = value