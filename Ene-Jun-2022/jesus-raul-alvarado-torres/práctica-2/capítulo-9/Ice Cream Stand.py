"""9-6. Ice Cream Stand:

An ice cream stand is a specific kind of restaurant . Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171) . Either version of
the class will work; just pick the one you like better . Add an attribute called
flavors that stores a list of ice cream flavors . Write a method that displays
these flavors . Create an instance of IceCreamStand, and call this method."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type} del condado."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} ya abrio sus puertas al publico!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='Helado'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nTenemos los siguientes sabores disponibles:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

SultanaStd = IceCreamStand('Sultana')
SultanaStd.flavors = ['Nata', 'Chocolate', 'Fresa']

SultanaStd.describe_restaurant()
SultanaStd.show_flavors()