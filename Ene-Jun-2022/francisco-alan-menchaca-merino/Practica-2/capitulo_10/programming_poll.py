""" 10-5. Programming Poll: Write a while loop that asks people why they
like programming. Each time someone enters a reason, add their reason to
a file that stores all the responses. """

filename = "programming_poll.txt"

while True:
    response = input("\nWhy do you like programming?: ")
    with open(filename, "a") as file_object:
        file_object.write(response + "\n")

    leave = input("Do you want to leave the program?: ")
    if leave.lower() == "yes":
        break

# Why do you like programming?: I like coding because it allows me to create something in stages.
# Do you want to leave the program?: no

# Why do you like programming?: I like creating something out of nothing.
# Do you want to leave the program?: no

# Why do you like programming?: I like coding because I like puzzles and it makes my life easier.
# Do you want to leave the program?: yes
