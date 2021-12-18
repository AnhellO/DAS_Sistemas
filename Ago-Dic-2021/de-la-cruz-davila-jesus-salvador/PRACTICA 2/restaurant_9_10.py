# Clase Restaurant
class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("Nombre: ", self.restaurant_name)
        print("Tipo de cocina: ", self.cuisine_type)

    def open_restaurant(self):
        print("That the restaurant is open")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, clients_served):
        self.number_served += clients_served