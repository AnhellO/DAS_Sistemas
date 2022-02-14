""" 10-3. Guest: Write a program that prompts the user for their name.
When they respond, write their name to a file called guest.txt. """

filename = "guest.txt"
user_name = input("What is your name?: ")

with open(filename, "w") as file_object:
    file_object.write(user_name)
print(f"Name saved on the text file \"{filename}\" ")
