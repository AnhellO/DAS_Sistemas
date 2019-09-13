# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they
# enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

p = "\nWhat topping would you like on your pizza?"
p += "\nEnter 'quit' if you finished: "

while True:
    topping = input(p)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break