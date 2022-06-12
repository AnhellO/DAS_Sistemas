class Restaurant():
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    
    def describe_restaurant(self):
        '''Describe el restaurante.'''
        print("Nombre del restaurante: " +self.restaurant_name)
        print("Tipo de cocina: " +self.cuisine_type)

    def open_restaurant(self):
        '''Pone el restaurante como abierto'''
        print("El restaurante " +self.restaurant_name +" esta abierto.")


#Creando la instancia
my_restaurant = Restaurant("Chickenlittle","Casera")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()