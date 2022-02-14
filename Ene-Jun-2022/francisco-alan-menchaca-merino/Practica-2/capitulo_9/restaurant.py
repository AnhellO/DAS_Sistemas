class Restaurant:
    """9-1. Restaurant: Make a class called Restaurant. The __init__() method
    for Restaurant should store two attributes: a restaurant_name and a
    cuisine_type. Make a method called describe_restaurant() that prints these
    two pieces of information, and a method called open_restaurant() that prints 
    a message indicating that the restaurant is open."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurant name: {self.restaurant_name}\n"
              + f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now open!!")


# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.
restaurant = Restaurant("Alan's Japanese Restaurant",
                        "Traditional Cuisine of Japan")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
restaurant_one = Restaurant("Papa's Grill", "Caribbean Cuisine")
restaurant_one.describe_restaurant()

restaurant_two = Restaurant("Chinese Food Feilong", "Chinese Cuisine")
restaurant_two.describe_restaurant()

restaurant_three = Restaurant("Curry Sultan", "Traditional Indian Cuisine")
restaurant_three.describe_restaurant()
# Alan's Japanese Restaurant
# Traditional Cuisine of Japan

# Restaurant name: Alan's Japanese Restaurant
# Cuisine type: Traditional Cuisine of Japan
# The restaurant is now open!!

# Restaurant name: Papa's Grill
# Cuisine type: Caribbean Cuisine

# Restaurant name: Chinese Food Feilong
# Cuisine type: Chinese Cuisine

# Restaurant name: Curry Sultan
# Cuisine type: Traditional Indian Cuisine
