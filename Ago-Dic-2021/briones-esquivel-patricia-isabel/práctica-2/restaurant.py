                # Ejercicios del libro Python Crash Course 
# ------- Ejercicio 9,1- Restaurant -------
class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 100 # ------- Ejercicio 9,4- Number served -------
 
    def describe_restaurant(self):
        print("\nRestaurant's name: " + self.name.title() + ".")
        print("Cuisine type: " + self.cuisine_type.title() + ".")
    
    def open_restaurant(self):
        print(self.name.title() + " it's open now!")

# ------- Ejercicio 9,4- Number served -------
    def read_customers(self):
        print(self.name.title() + " has atended " + str(self.number_served) + " customers in the day.")

    def set_number_served(self, customers):
            self.number_served = customers

    def increment_number_served(self, platos):
        self.number_served += platos

# ------- Ejercicio 9,1- Restaurant -------
my_restaurant = Restaurant('Lirul sisa', 'Italian food')
print("My restaurant's name is " + my_restaurant.name.title() + ".")
print("My cuisine type is " + my_restaurant.cuisine_type.title() + ".")    

print("\n-------- Por métodos ----------")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# ------- Ejercicio 9,2- Three Restaurants ------- 
restaurant_1 = Restaurant('Happy puppy','Chinese Cuisine')
restaurant_2 = Restaurant('We do not know how to cook','American food')
restaurant_3 = Restaurant('Arriba los tacos','Mexican Cuisine')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# ------- Ejercicio 9,4- Number served -------
print("\nInicial customers:")
restaurant_1.read_customers()

print("Update customers:")
restaurant_1.set_number_served(150)
restaurant_1.read_customers()

print("Increment customers:")
restaurant_1.increment_number_served(100)
restaurant_1.read_customers()

# ------- Ejercicio 9,6- Ice Cream Stand -------
class IceCreamStand (Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def describe_flavors(self):
        print(self.name + " has those flavors: ")
        for f in self.flavors:
            print(f"- {f.title()}")

my_icecream = IceCreamStand('Michoacana', 'Ice Cream')
my_icecream.flavors = ['Fresa','Chocolate','Vainilla']
my_icecream.describe_restaurant()
my_icecream.describe_flavors()
