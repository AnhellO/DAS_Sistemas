
class Restaurant():

    def __init__(self, name, cuisine_type):

        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        msg = self.name + " Es el onmbre del restaurante," + self.cuisine_type + " Es el tipo de comida."
        print("\n" + msg)

    def open_restaurant(self):

        msg = self.name + " Esta Abierto!!!"
        print("\n" + msg)


restaurante = Restaurant(' La Marea ', ' Mariscos ')
restaurante.describe_restaurant()
restaurante.open_restaurant()

##################################################################################
##################################################################################

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type,):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def list_flavors(self):

        print("\nEstos son los sabores de helados:")
        for flavor in self.flavors:
            print(flavor)

Helados = IceCreamStand("Helados doña Yolis", "Helados")
Helados.flavors = ["vainilla", "chocolate", "fresa", "napolitano"]
Helados.describe_restaurant()
Helados.list_flavors()