class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: {}".format(self.restaurant_name))
        print("The cuisine type is: {}".format(self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant {} is now open!! :D".format(self.restaurant_name))

restaurant = Restaurant("Tacos de grasa", "Mexican")
restaurant_2 = Restaurant("Nuvole Bianche", "Italian")
restaurant_3 = Restaurant("豐富的老鼠", "Chinese")
restaurant_4 = Restaurant("Pâtes pour votre coeur", "French")

restaurant.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()
