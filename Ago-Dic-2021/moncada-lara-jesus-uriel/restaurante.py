"""Clase que representa el restaurante """

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