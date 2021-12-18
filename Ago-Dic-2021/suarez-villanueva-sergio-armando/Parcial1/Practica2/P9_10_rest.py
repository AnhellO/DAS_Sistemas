class Restaurant():
    
    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type
        
    def describe_R(self):
        print("Name: " + self.name + "\nCuisine Type: " + self.c_type)
    
    def open_R(self):
        print(self.name + " is open.")
        
class IceCreamStand(Restaurant):
    
    def __init__(self, name):
        super().__init__(name, "Ice Cream Shop")
        self.flavors=["Chocolate", "Cookies and Cream", "Lemon", "Strawberry"]
    
    def show_flavors(self):
        for i in self.flavors:
            print(i)