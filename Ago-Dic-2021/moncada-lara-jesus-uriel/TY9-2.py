"""Try it yourself 9-2 """

class Restaurant():
    def  __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        desc = self.restaurant_name + " nuestra comida es " +  self.cuisine_type + "."
        print("\n" + desc)

    def open_restaurant(self):
        openR = self.restaurant_name + " Bienvenido nuestro restaurante esta abierto."
        print("\n"+ openR)
    
restaurante1 = Restaurant("El gran buda de oro","Asiática")
restaurante1.describe_restaurant()

restaurante2 = Restaurant("pizza planeta","Comida rapida")
restaurante2.describe_restaurant()

restaurante3 = Restaurant("Los troncos","Mexicana")
restaurante3.describe_restaurant()