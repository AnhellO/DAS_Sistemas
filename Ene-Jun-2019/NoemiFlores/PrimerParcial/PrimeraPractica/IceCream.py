#An ice cream stand is a specific kind of restaurant. Write
#a class called IceCreamStand that inherits from the Restaurant class you wrote
#in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
#the class will work; just pick the one you like better. Add an attribute called
#flavors that stores a list of ice cream flavors. Write a method that displays
#these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant():

    def __init__(self, name, cuisine_type):
        """Inicializando"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Descripción del restaurant"""
        msg = self.name + " sirve un delicioso " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Muestra mensaje de restaurante abierto"""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Numero de clientes atendidos"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Incremento de clientes atendidos"""
        self.number_served += additional_served


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='helado doble!!'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Mostrar los sabores disponibles"""
        print("\nSabores disponibles:")
        for flavor in self.flavors:
            print("- " + flavor.title())


helado_feliz = IceCreamStand('Helado Feliz')
helado_feliz.flavors = ['Vanilla', 'Chocolate', 'Fresa']

helado_feliz.describe_restaurant()
helado_feliz.show_flavors()