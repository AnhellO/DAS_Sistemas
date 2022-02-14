""" 10-12. Favorite Number Remembered: Combine the two programs from 
Exercise 10-11 into one file. If the number is already stored, report
the favorite number to the user. If not, prompt for the user's favorite
number and store it in a file. Run the program twice to see that it works. """
import json

filename = "favorite_number.json"

try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    number = input("What's your favorite number?: ")
    with open(filename, "w") as file_object:
        json.dump(number, file_object)
else:
    print(f"I know your favorite number! It's {number}")

# What's your favorite number?: 22
# I know your favorite number! It's 22
