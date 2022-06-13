#=============  ejercicio 9-4 ===========
class Restaurant1():

    def __init__(self,restaurant_name,cuisine_type):
        #"""Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant1(self):
        print("\n========== archivo de restaurante para importar del ==========")
        print("========== ejercicio 9-4 ==========")
        print("Restaurant name: "+self.restaurant_name.title())
        print("Restaurant name: "+self.cuisine_type.title()+"\n")
    
    def open_restaurant1(self):
        print("Restaurant '"+self.restaurant_name.title()+"' is open!!!\n")

    def set_number_served1(self):
        print("clients: "+str(self.number_served)+"\n")
    
    def increment_number_served1(self,miles):
        """Add the given amount to the odometer reading."""
        self.number_served += miles

