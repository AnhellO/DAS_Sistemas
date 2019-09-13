class Restaurant():

    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print("The restaurant name is: {}".format(self.restaurant_name))
        print("The cuisine type is: {}".format(self.cuisine_type))

    def open_restaurant(self):
        print("The restaurant {} is now open!! :D".format(self.restaurant_name))

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, inc):
        self.number_served += inc


restaurant = Restaurant("Tacos de grasa","Mexicana")
print("Number of customers served: ", restaurant.number_served)
restaurant.number_served = 5
print("Number of customers served: ", restaurant.number_served)
restaurant.set_number_served(9)
print("Number of customers served: ", restaurant.number_served)
restaurant.increment_number_served(31)
print("Number of customers served: ", restaurant.number_served)
