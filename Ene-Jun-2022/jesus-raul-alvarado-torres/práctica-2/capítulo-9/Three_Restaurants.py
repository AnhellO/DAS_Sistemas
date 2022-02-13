"""9-2. Three Restaurants:

Start with your class from Exercise 9-1 . Create three
different instances from the class, and call describe_restaurant() for each
instance ."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type} del condado."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} ya abrio sus puertas al publico!"
        print(f"\n{msg}")

KFC = Restaurant('KFC', 'nuggets de pollo')
KFC.describe_restaurant()

Tobi = Restaurant("Burritos Tobi", 'burritos')
Tobi.describe_restaurant()

Applebees = Restaurant('Applebees', 'boneless')
Applebees.describe_restaurant()