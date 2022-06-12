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
        print("El restaurante " +self.restaurant_name +" esta abierto.\n")


#Creando 3 instancias diferentes
first_restaurant = Restaurant("Chickenlittle","Casera")
second_restaurant = Restaurant("ToGo","Mexicana")
thirt_restaurant = Restaurant("KFC","Italiana")

##Describiendolos 3 restaurantes y abriendo cada uno de ellos.
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()

thirt_restaurant.describe_restaurant()
thirt_restaurant.open_restaurant()