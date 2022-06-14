from Ejercicio_1_restaurant import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, coussine_type, flavors):

        super().__init__(restaurant_name, coussine_type)
        self.flavors = flavors

    def showFlavors(self):
        print("this are the flavors")
        print(self.flavors)

#hotDogsFlavors = ['pig', 'beef']
#Oxxo = IceCreamStand('oxxo', 'hotdogs', hotDogsFlavors)

#Oxxo.showFlavors()