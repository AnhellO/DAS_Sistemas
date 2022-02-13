class Restaurant:
    
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")
    
    def client_served(self):
        print("clients served: " + str(self.number_served))

    def set_number_served(self, changed_number_served):
        self.number_served = changed_number_served

    def increment_number_served(self, increment_served):
        self.number_served = self.number_served + increment_served

restaurant = Restaurant('pedro', 'tacos')
restaurant.client_served()

restaurant.number_served = 20
restaurant.client_served()

restaurant.set_number_served(40)
restaurant.client_served()

restaurant.increment_number_served(50)
restaurant.client_served()

