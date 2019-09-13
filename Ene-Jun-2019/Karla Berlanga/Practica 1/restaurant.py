""" An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better.
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method. """

class Restaurant(object):
    """Representa cualquier restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        description="Nombre del restaurante: " + self.restaurant_name.title() + "\nTipo de cocina: " + self.cuisine_type
        return description

    def open_restaurant(self):
        print("El restaurante está abierto")

    def read_number_served(self):
        print("Se han atendido " + str(self.number_served)+ " persona(s)")

    def set_number_served(self, number):
        self.number_served=number

    def increment_number_server(self, more_served):
        self.number_served+=more_served

class IceCreamStand(Restaurant):
    """Representa un tipo de restaurant, especificamente de helados"""
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def set_flavors(self, *list_flavors):
        self.flavors=list_flavors

    def read_flavors(self):
        print("\nSabores de helados:")
        for flavor in self.flavors:
            print("- "+ flavor)


ice_cream_stand=IceCreamStand('helados morelia', 'helados')
print(ice_cream_stand.describe_restaurant())
ice_cream_stand.set_flavors('chocolate', 'vainilla', 'fresa', 'coco')
ice_cream_stand.read_flavors()
