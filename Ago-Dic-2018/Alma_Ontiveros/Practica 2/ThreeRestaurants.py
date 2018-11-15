class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Nombre del restaurante: ', self.restaurant_name)
        print('Tipo de cocina: ', self.cuisine_type)

    def open_restaurant(self):
        print('RESTAURANTE ABIERTO')

restaurant = Restaurant('Mac Donalds', 'Hamburguesas')
restaurant2 = Restaurant("Pizza Hut", "Pizzas")
restaurant3 = Restaurant("Subway", "Tortas")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()