class Restaurant():
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("Nombre: ", self.restaurant_name)
        print("Tipo de cocina: ", self.cuisine_type)

    def open_restaurant(self):
        print("That the restaurant is open")
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, clients_served):
        self.number_served += clients_served
    
restaurant = Restaurant("El restaurante de la nana", "chino")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n Numero de platillos servidos: ", restaurant.number_served) #Imprime 0 platillos
restaurant.number_served = 100
print("\n Numero de platillos servidos: ", restaurant.number_served) #Imprime 100 platillos

restaurant.set_number_served(500)
print("\n Numero de platillos servidos", restaurant.number_served) #Imprime la cantidad de platillos que le madnes ak metodo

restaurant.increment_number_served(400) #Suma la cantidad de platillos del metodo anterior mas los que se le asignen a este nuevo metodo
print("\n Numero de platillos vendidos en el dia:", restaurant.number_served)
