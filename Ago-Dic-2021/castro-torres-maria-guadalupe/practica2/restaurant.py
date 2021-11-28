class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} sirve maravillosas {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} esta abierto, pasele!"
        print(f"\n{msg}")

restaurant = Restaurant('Pepes', 'hamburguesas')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

########################################
#9.2
########################################

class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name} sirve maravillosas {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} esta abierto, pasele!"
        print(f"\n{msg}")

pepes=Restaurant('pepes','hamburguesas')
pepes.describe_restaurant()

tortasp=Restaurant('tortas_popeye','tortas')
tortasp.describe_restaurant()

invasor=Restaurant('El invasor','mariscos')
invasor.describe_restaurant()




    
