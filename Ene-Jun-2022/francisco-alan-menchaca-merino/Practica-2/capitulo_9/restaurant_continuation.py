class Restaurant:
    """9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
    Add an attribute called number_served with a default value of 0. 
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}\n"
              + f"Cuisine type: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("The restaurant is now open!!")

    # Add a method called set_number_served() that lets you set the number of
    # customers that have been served. Call this method with a new number and
    # print the value again.
    def set_number_served(self, num_served):
        self.number_served = num_served

    # Add a method called increment_number_served() that lets you increment the
    # number of customers who've been served. Call this method with any number
    # you like that could represent how many customers were served in, say, a
    # day of business
    def increment_number_served(self, served):
        self.number_served += served


restaurant = Restaurant("Alan's Japanese Restaurant",
                        "Traditional Cuisine of Japan")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# MODIFYING ATTRIBUTE VALUES
# Create an instance called restaurant from this class. Print the number
# of customers the restaurant has served, and then change this value and
# print it again.
print(f"* Number served: {restaurant.number_served}")

# Modifying an Attribute’s Value Directly
restaurant.number_served = 1
print(f"* Number served: {restaurant.number_served}")

# Modifying an Attribute’s Value Through a Method
restaurant.set_number_served(17)
print(f"* Number served: {restaurant.number_served}")

# Incrementing an Attribute’s Value Through a Method
restaurant.increment_number_served(5)
print(f"* Number served: {restaurant.number_served}")
