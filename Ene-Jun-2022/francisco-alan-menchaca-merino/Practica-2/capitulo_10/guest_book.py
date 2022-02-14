""" 10-4. Guest Book: Write a while loop that prompts users for their name. When 
they enter their name, print a greeting to the screen and add a line recording 
their visit in a file called guest_book.txt. Make sure each entry appears on a 
new line in the file. """

filename = "guest_book.txt"

while True:
    print("(Enter 'quit' at any time to quit)")
    user_name = input("What is your name?: ")

    if user_name == "quit":
        break

    print("\nThanks for entering your name.")
    print("Now, you can see your name in the guest book!!\n")

    with open(filename, "a") as file_object:
        file_object.write(user_name + "\n")

# (Enter 'quit' at any time to quit)
# What is your name?: Alan Menchaca

# Thanks for entering your name.
# Now, you can see your name in the guest book!!

# (Enter 'quit' at any time to quit)
# What is your name?: Alfonso Garza

# Thanks for entering your name.
# Now, you can see your name in the guest book!!

# (Enter 'quit' at any time to quit)
# What is your name?: Ricardo Romo

# Thanks for entering your name.
# Now, you can see your name in the guest book!!

# (Enter 'quit' at any time to quit)
# What is your name?: Armando Soriano

# Thanks for entering your name.
# Now, you can see your name in the guest book!!

# (Enter 'quit' at any time to quit)
# What is your name?: quit
