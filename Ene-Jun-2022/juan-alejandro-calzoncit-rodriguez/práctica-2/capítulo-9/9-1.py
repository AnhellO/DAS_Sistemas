class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurante(self):
        print(f"Name of restaurant : {self.restaurant_name} , couisine type : {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")


restaurant = Restaurant("OpenSea", "Sea food")

print(f"Name : {restaurant.restaurant_name}")
print(f"Type of cuisine : {restaurant.cuisine_type}")

restaurant.describe_restaurante()
restaurant.open_restaurant()