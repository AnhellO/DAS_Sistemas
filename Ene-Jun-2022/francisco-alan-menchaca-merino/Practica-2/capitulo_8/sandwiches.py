"""8-12. Sandwiches: Write a function that accepts a list of items a person
wants on a sandwich. The function should have one parameter that collects as
many items as the function call provides, and it should print a summary of the
sandwich that is being ordered. Call the function three times, using a different
number of arguments each time.
"""


def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich("Jam", "Cheese slice", "Mayonnaise")
make_sandwich("Jam", "Extra Cheese slice", "Mayonnaise", "Mustard",)
make_sandwich("Jam", "Mayonnaise", "Mustard", "Lettuce", "Tomatoe")
# Making a sandwich with the following toppings:
# - Jam
# - Cheese slice
# - Mayonnaise

# Making a sandwich with the following toppings:
# - Jam
# - Extra Cheese slice
# - Mayonnaise
# - Mustard

# Making a sandwich with the following toppings:
# - Jam
# - Mayonnaise
# - Mustard
# - Lettuce
# - Tomatoe
