class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0

    def set_number_serverd(self,num):
        self.number_serverd = num

    def incremet_number_served(self, num):
        self.number_serverd += num

    def describe_restaurante(self):
        print(f"Name of restaurant : {self.restaurant_name} , couisine type : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
