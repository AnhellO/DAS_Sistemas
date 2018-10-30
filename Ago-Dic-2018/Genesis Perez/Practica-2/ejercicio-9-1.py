class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        presentacion = self.name + " sirve comida " + self.cuisine_type
        print(presentacion)

    def open_restaurant(self):
        estado = self.name + " está abierto"
        print(estado)

restaurante = Restaurant('Mi tierra', 'mexicana')
print(restaurante.name)
print(restaurante.cuisine_type)

restaurante.describe_restaurant()
restaurante.open_restaurant()
