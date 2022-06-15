class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of restaurant : {self.restaurant_name} , couisine type : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

r1 = Restaurant("Mario", "Italian")
r2 = Restaurant("Pancho Pistolas", "Mexican")
r3 = Restaurant("The Parce" , "Colombiana")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()