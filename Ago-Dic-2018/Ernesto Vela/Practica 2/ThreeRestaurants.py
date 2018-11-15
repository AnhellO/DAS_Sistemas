class Restaurant:

    def __init__(self, restaurant_name='', cuisine_type=''):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('El nombre del restaurante es: ', self.restaurant_name)
        print('El tipo de cocina del restaurante es: ', self.cuisine_type)

    def open_restaurant(self):
        print('El restaurante esta abierto')

restaurante_1 = Restaurant('Los mariachis', 'Mexicana')
restaurante_1.describe_restaurant()


restaurante_2 = Restaurant('Que elegancia la de francia', 'Francesa')
restaurante_2.describe_restaurant()

restaurante_3 = Restaurant('El dorado', 'Mariscos')
restaurante_3.describe_restaurant()
