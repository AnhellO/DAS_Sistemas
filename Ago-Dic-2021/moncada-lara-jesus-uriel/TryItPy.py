"""Try it yourself 9-1 """

class Restaurant():
    def  __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        desc = self.restaurant_name + " nuestra comida es " +  self.cuisine_type + "."
        print(desc)

    def open_restaurant(self):
        openR = self.restaurant_name + " Bienvenido nuestro restaurante esta abierto."
        print("\n"+ openR)
    
restaurant = Restaurant("El gran buda de oro","Asiática")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()