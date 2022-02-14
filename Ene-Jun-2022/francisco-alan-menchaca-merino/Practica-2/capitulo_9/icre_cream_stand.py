class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\n"
              + f"Cuisine type: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("The restaurant is now open!!")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, served):
        self.number_served += served


class IceCreamStand(Restaurant):
    """9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
    a class called IceCreamStand that inherits from the Restaurant class you wrote in
    Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will
    work; just pick the one you like better. Add an attribute called flavors that stores
    a list of ice cream flavors. Write a method that displays these flavors. Create an
    instance of IceCreamStand, and call this method."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Our flavors available are:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_flavors = ["Strawberry", "Chocolate", "Vanilla",
                     "Lemon", "Neapolitan", "Raspberry Cherpet"]

hometown_creamery = IceCreamStand("Hometown Creamery",
                                  "Ice cream", ice_cream_flavors)
hometown_creamery.describe_restaurant()
hometown_creamery.show_flavors()

# Restaurant name: Hometown Creamery
# Cuisine type: Ice cream

# Our flavors available are:
# - Strawberry
# - Chocolate
# - Vanilla
# - Lemon
# - Neapolitan
# - Raspberry Cherpet
