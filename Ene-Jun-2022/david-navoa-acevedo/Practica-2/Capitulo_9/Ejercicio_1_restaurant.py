
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")

#the calls are commented to use this class for other things. If u want to check the uses uncomment the calls
Oxxo = Restaurant('oxxo', 'hotdogs')
#print("Restaurant name is " + Oxxo.restaurant_name.title())
#print("Cuisine type " + Oxxo.cuisine_type.title())

#Oxxo.describe_restaurant()
#Oxxo.open_restaurant()