""" 10-11. Favorite Number: Write a program that prompts for the user's
favorite number. Use json.dump() to store this number in a file. Write a
separate program that reads in this value and prints the message, “I know
your favorite number! It's _____.” """

import json

filename = "favorite_number.json"

with open(filename) as file_object:
    number = json.load(file_object)
    print(f"I know your favorite number! It's {number}")

# I know your favorite number! It's 22
