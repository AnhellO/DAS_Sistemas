"""9-1. store two attributes: restaurant_name and cousine_type
 make a method called describe_restaurant() that prints
 this two pieces of information, and a method called open_restaurant()
 this prints a message indicating that the restaurant is open
    Make an instance called restaurant from your class. Print the two
    attributes individually, and then call both methods"""
class Restaurant():
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is the name of the restaurant\n")
        print(self.cousine_type.title() + " is the type of cousine\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() +" is open\n")

"""my_restaurant = Restaurant('El imperio', 'Cortes de carne')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()"""

"""9-6. An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class.
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""

class IceCreamStand(Restaurant):
    "Inherits from restaurant"
    def __init__(self,restaurant_name, cousine_type, flavors):
        super().__init__(restaurant_name, cousine_type)
        self.flavors = flavors

    def Listflavors(self):
        print("This are the ice cream flavors:\n" + self.flavors.title()+"\n")

IceCream = IceCreamStand('Fancy Ice', 'Desserts', "vanilla, chocolate, peanut, strawberry")
IceCream.describe_restaurant()
IceCream.Listflavors()
