"""Try it yourself 9-4 """

class Restaurant():
    def  __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        desc = self.restaurant_name + " nuestra comida es " +  self.cuisine_type + "."
        print(desc)

    def open_restaurant(self):
        openR = self.restaurant_name + " Bienvenido nuestro restaurante esta abierto."
        print("\n"+ openR)

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,sum_client):
        self.number_served +=sum_client

restaurant = Restaurant("El gran buda de oro","Asiática")

print(restaurant.restaurant_name)
restaurant.describe_restaurant()

print("\n Numero de clientes servidos= " + str(restaurant.number_served))
restaurant.number_served = 50
print("\n Numero de clientes servidos= " + str(restaurant.number_served))

restaurant.set_number_served(150)
print("\n Numero de clientes servidos= " + str(restaurant.number_served))

restaurant.increment_number_served(400)
print("\n Numero de clientes servidos= " + str(restaurant.number_served))
