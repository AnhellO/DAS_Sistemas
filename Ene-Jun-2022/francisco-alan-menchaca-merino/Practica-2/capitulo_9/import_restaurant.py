"""9-10. Imported Restaurant: Using your latest Restaurant class, store
it in a module. Make a separate file that imports Restaurant. Make a
Restaurant instance, and call one of Restaurant's methods to show that
the import statement is working properly."""
from latest_restaurant import Restaurant

restaurant = Restaurant("Alan's Japanese Restaurant",
                        "Traditional Cuisine of Japan")
restaurant.describe_restaurant()
restaurant.open_restaurant()
# Restaurant name: Alan's Japanese Restaurant
# Cuisine type: Traditional Cuisine of Japan

# The restaurant is now open!!
