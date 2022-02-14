class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\n"
              + f"Cuisine type: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("The restaurant is now open!!")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, served):
        self.number_served += served
