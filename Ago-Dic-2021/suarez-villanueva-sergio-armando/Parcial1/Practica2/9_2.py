class Restaurant():
    
    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type
        
    def describe_R(self):
        print("Name: " + self.name+"\nCuisine type: " + self.c_type)
    
    def open_R(self):
        print(self.name + " Open.")

Restaurants = []
Restaurants.append(Restaurant("Ramen Ichiraku","Japanese"))
Restaurants.append(Restaurant("Las costillas de Sancho","Mexican"))
Restaurants.append(Restaurant("Il Mercato","Italian"))

for i in Restaurants:
    i.describe_R()
    i.open_R()
