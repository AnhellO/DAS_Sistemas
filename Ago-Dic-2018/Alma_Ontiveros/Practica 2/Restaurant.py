class Restaurant:

    def __init__(self, restaurant_name='', cuisine_type=''):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Nombre del restaurante es: ', self.restaurant_name)
        print('Tipo de cocina: ', self.cuisine_type)

    def open_restaurant(self):
        print('RESTAURANTE ABIERTO')

restaurante = Restaurant('MacDonalds', 'Hamburguesas')
print(restaurante.restaurant_name)
print(restaurante.cuisine_type)
restaurante.describe_restaurant()
restaurante.open_restaurant()