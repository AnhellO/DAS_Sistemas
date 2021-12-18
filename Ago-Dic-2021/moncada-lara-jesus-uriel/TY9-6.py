"""Try it yourself 9-6 """

class Restaurant():
    def  __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        desc = self.restaurant_name + " nuestra comida es " +  self.cuisine_type + "."
        print(desc)

    def open_restaurant(self):
        openR = self.restaurant_name + " Bienvenido nuestro restaurante esta abierto."
        print("\n"+ openR)
    
restaurant = Restaurant("El gran buda de oro","Asiática")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type= "Helao :D"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vainilla","pistache","chocolate","fresa","chicle","Oreo"]

    def show_flavors(self):
        print("Mire mijo tenemos estos sabores pa su deleite")
        for i in range(len(self.flavors)):
            print(" * " + str(self.flavors[i]))

Mi_Helao = IceCreamStand("La michoacana \n")
Mi_Helao.describe_restaurant()
Mi_Helao.show_flavors()
