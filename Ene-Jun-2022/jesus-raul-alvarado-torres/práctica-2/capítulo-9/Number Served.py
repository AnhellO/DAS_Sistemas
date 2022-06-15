"""9-4. Clientes atendidos:

Start with your program from Exercise 9-1 (page 166) .
Add an attribute called number_served with a default value of 0 . Create an
instance called restaurant from this class . Print the number of customers the
restaurant has served, and then change this value and print it again .
Add a method called set_number_served() that lets you set the number
of customers that have been served . Call this method with a new number and
print the value again .
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served . Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business ."""

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name} tiene los mejores {self.cuisine_type} del condado."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} ya abrio sus puertas al publico!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant('Doña chencha', 'pozole')
restaurant.describe_restaurant()
print(f"\nClientes atendidos: {restaurant.number_served}")

restaurant.number_served = 430
print(f"Clientes atendidos: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Clientes atendidos: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Clientes atendidos: {restaurant.number_served}")