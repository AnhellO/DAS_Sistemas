# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each
# of the following at least once:

# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

p = "\nEnter 'quit' if you finished:\n "
print(p)

numb = int(input("How many ingredients do you want? "))

while numb > 0:
    msj = input(" What topping would you like on your pizza? ")
    msj = msj.lower()

    if msj != "quit":
        print("Now your pizza has " + msj)
    else:
        break
    numb -= 1
