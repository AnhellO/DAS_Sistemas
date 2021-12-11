class Restaurant():
    
    def __init__(self, name, c_type):
        self.name = name
        self.c_type = c_type
        
    def describe_R(self):
        print("Name: " + self.name+"\nCuisine type: " + self.c_type)
    
    def open_R(self):
        print(self.name + " Open.")
        

My_R = Restaurant("Las Costillas de Sancho","Mexican")

print(My_R.name + " " + My_R.c_type)
My_R.describe_R()
My_R.open_R()