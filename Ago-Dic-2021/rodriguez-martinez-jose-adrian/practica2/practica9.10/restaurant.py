
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def increment_num_served(self, update):
        self.number_served = update
        return f"Number served: {self.number_served}"

    def describe_restaurant(self):
        return f"Restaurant name: {self.name}\nCuisine type: {self.cuisine}"
    
    def open_restaurant(self):
        return f"Restaurant {self.name} is now open"
