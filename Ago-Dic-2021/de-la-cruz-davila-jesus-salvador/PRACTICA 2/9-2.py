class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        
    def describe_restaurant(self):
        print("Nombre: ", self.restaurant_name)
        print("Tipo de cocina: ", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurants are open")
    
# Restaurante numero 1
restaurant = Restaurant("El restaurante de la nana", "chino")
restaurant.describe_restaurant()

# Restaurante numero 2
restaurant2 = Restaurant("Restaurante de Snoopy", "Italiano")
restaurant2.describe_restaurant()

# Restaurante numero 3
restaurant3 = Restaurant("Restaurante de Kira", "Japones")
restaurant3.describe_restaurant()

# Mensaje
restaurant.open_restaurant()