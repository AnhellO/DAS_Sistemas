### 9.6: Ice Cream Stand ###

class Restaurant():

    ## Inicializar atributos
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        ### 9.4 ###
        self.number_served = 0

    ## Metodo descripcion
    def describe_restaurant(self):
        print('The Restaurant name is: ' + self.restaurant_name + '\n'
        + 'and the cuisine type are: ' + self.cuisine_type
        )

    ## Metodo abrir restaurant
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name + " now it's open!")

    ### 9.4 ###
    def set_number_served(self, num_costumers: int):
        # Set the number of costomers served to the given value.
        self.number_served = num_costumers

    def increment_number_served(self, increment_num: int):
        # Add the given amout to the number served value.
        self.number_served += increment_num
# create child class
class IceCream(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print('The flavors available are: ')
        for i in self.flavors:
            print('- ' + i)

michoacana = IceCream('La Michoacana', 'Ice Cream')
michoacana.flavors = ['Vainilla', 'Chocolate', 'Fresa', 'Limon']
michoacana.describe_restaurant()
michoacana.show_flavors()