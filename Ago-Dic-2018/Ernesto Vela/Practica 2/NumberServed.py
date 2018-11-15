class Restaurant:

    def __init__(self, restaurant_name='', cuisine_type='', number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

restaurante = Restaurant('Los mariachis', 'Mexicana')
print(restaurante.number_served)
restaurante.number_served=5
print(restaurante.number_served)

restaurante.set_number_served(3)
print(restaurante.number_served)

restaurante.increment_number_served(5)
print(restaurante.number_served)
