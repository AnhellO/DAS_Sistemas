class Restaurant:

    def __init__(self, restaurant_name='', cuisine_type=''):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('El nombre del restaurante es: ', self.restaurant_name)
        print('El tipo de cocina del restaurante es: ', self.cuisine_type)

    def open_restaurant(self):
        print('El restaurante esta abierto')

restaurante = Restaurant('Los mariachis', 'Mexicana')
print(restaurante.restaurant_name)
print(restaurante.cuisine_type)
restaurante.describe_restaurant()
restaurante.open_restaurant()
