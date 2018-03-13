class Restaurant():
    """una clase que representa un restaurante."""

    def __init__(self, name, cuisine_type):
        """Inicializar el restaurante."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """mostrar un resumen del resultado."""
        msg = self.name + " sirve maravilloso " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """mostrar un mensaje que el restaurante esta abierto."""
        msg = self.name + " esta abierto vamos!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Permitir al usuario establecer la cantidad de clientes atendidos"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Permitir que el usuario incremente la cantidad de clientes atendidos."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Representar un puesto de helados."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Mostrar los sabores disponibles."""
        print("\nTenemos disponibles los siguientes sabores:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
