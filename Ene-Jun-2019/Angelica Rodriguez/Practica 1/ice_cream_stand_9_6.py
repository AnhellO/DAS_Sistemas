"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class
you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either
version of the class will work; just pick the one you like better. Add an
attribute called flavors that stores a list of ice cream flavors. Write a
method that displays these flavors. Create an instance of IceCreamStand,
and call this method.
Exercise chosen: Exercise 9-1
"""

class Restaurant(object):
    """Represent aspects of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Description of a restaurant"""
        return """
        Restaurant name: {}\nCuisine type: {}
        """.format(self.restaurant_name, self.cuisine_type).strip()

    def open_restaurant(self):
        """Restaurant open"""
        return "Restaurant is open"

class IceCreamStand(Restaurant):
    """Represent aspects of a Restaurant, specific to ice cream"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attibutes of the parent class.
        Then initialize attibutes specific to an ice cream Stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def store_flavors(self, *flavors_list):
        """Set flavors in a list"""
        self.flavors = flavors_list
        return self

    def get_flavors(self):
        """See the flavors stored in the list"""
        for flavor in self.flavors:
            print(flavor)

# Instance of IceCreamStand class
iceCream = IceCreamStand('Nieve Ramos', 'mexican ice cream')
print(iceCream.describe_restaurant()) # super class method
print(iceCream.open_restaurant()) # super class method
iceCream.store_flavors('Melon', 'Almond', 'Chocolate') # set flavors
iceCream.get_flavors() # print flavors
