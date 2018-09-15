class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        descripcion = self.name + " Ven! Tenemos los mas ricos " + self.cuisine_type + " para ti."
        print("\n" + descripcion)

    def open_restaurant(self):
        abierto = self.name + "ABIERTO"
        print("\n" + abierto)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('RIOT', 'Bounless y bebidas')
restaurant.describe_restaurant()

print("\nNumero Servido: " + str(restaurant.number_served))
restaurant.number_served = 234
print("Numero Servido: " + str(restaurant.number_served))

restaurant.set_number_served(245)
print("Numero Servido: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Numero Servido: " + str(restaurant.number_served))
