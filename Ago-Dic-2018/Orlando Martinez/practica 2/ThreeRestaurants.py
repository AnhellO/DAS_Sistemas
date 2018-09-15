class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        descripcion = self.restaurant_name + " " + "El mejor lugar para comer " + self.cuisine_type
        print("\n" + descripcion)

    def open_restaurant(self):

        abierto = self.restaurant_name + " " "Esta abierto"
        print("\n" + abierto)

restaurant = Restaurant('Burger King', 'Hamburguesas')
restaurant.describe_restaurant()

restaurant2=Restaurant('Tacos checo','Tacos')
restaurant2.describe_restaurant()

restaurant3=Restaurant('Pollo Feliz','Pollo')
restaurant3.describe_restaurant()
