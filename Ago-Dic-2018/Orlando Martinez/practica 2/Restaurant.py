class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        descripcion = self.restaurant_name + " " + "Donde se sirven las mejores " + self.cuisine_type
        print("\n" + descripcion)

    def open_restaurant(self):

        abierto = self.restaurant_name + " " "Esta abierto"
        print("\n" + abierto)

restaurant = Restaurant('Burger King', 'Hamburguesas')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
