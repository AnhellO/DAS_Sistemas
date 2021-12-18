class Restaurant():
    
    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type
        self.served = 0
        
    def describe_R(self):
        print("\nName: " + self.name + "\nCuisine Type: " + self.c_type + "\nCustomers: " + str(self.served))
    
    def open_R(self):
        print(self.name + " is Open.\n")
        
    def get_served(self):
        print(str(self.served)+" were served.")
    
    def set_served(self, n):
        self.served = n
    
    def increment_served(self, n):
        self.served += n
    

My_R = Restaurant("Cheese Burgers","Fast Food")

print(My_R.name + " " + My_R.c_type)

My_R.get_served()
My_R.set_served(15)
My_R.get_served()
My_R.increment_served(50)
My_R.get_served()