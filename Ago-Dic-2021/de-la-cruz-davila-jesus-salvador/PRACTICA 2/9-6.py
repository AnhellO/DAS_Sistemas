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
    

# Clase IceCreamStand que hereda de la clase Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, name, type = "Ice Cream"):
        super().__init__(name, type)
        self.flavors = []
    
    def show_flavors(self):
        print("  Sabores disponibles")
        for flavor in self.flavors :
            print("     Helado sabor ",flavor)


ice_cream = IceCreamStand("Heladeria Meliodas")
ice_cream.flavors = ['Vainilla', 'Chocolate', 'Fresa']

ice_cream.describe_restaurant()
ice_cream.show_flavors()
    


