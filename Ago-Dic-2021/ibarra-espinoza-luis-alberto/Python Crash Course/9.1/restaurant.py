class Restaurant():

    ## Inicializar atributos
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    ## Metodo descripcion
    def describe_restaurant(self):
        print('The Restaurant name is: ' + self.restaurant_name + '\n'
        + 'and the cuisine type are: ' + self.cuisine_type)

    ## Metodo abrir restaurant
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name + " now it's open!")

restaurant = Restaurant('La cocina de Luisito', 'Mexicana')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()