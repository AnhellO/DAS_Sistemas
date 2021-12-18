class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        
    def describe_restaurant(self):
        print("Nombre: ", self.restaurant_name)
        print("Tipo de cocina: ", self.cuisine_type)

    def open_restaurant(self):
        print("That the restaurant is open")
    
restaurant = Restaurant("El restaurante de la nana", "chino")
restaurant.describe_restaurant()
restaurant.open_restaurant()


        
        
   
        
    