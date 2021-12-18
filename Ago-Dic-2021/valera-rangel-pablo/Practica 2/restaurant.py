class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        return(f'Name: {self.restaurant_name} cuisine type is: {self.cuisine_type}')

    def open_restaurant(self):
        return(f'The next restaurant is open: {self.restaurant_name}')

# 9.4 Number Served:
    def set_number_served(self, number_served):
        self.number_served = number_served
        return(f'Number served: {self.number_served}')

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
