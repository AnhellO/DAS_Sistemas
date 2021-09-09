### 9.2: Three Restaurants ###

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

# Instances
marcelo_restaurant = Restaurant('La Cocinita de Marcelino', 'tawianesa')
phily_restaurant = Restaurant('Aca Phily', 'Hamburgesas y burritas')
jochospepe_restaurant = Restaurant('Joshos Pepe', 'Hot-Dogs')

##Calling Methods
marcelo_restaurant.describe_restaurant()
phily_restaurant.describe_restaurant()
jochospepe_restaurant.describe_restaurant()