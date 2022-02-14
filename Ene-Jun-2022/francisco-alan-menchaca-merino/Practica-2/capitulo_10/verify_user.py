""" 10-13. Verify User: The final listing for remember_me.py assumes either
that the user has already entered their username or that the program is running
for the first time. We should modify it in case the current user is not the
person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this
is the correct username. If it's not, call get_new_username() to get the correct 
username. """

import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("\nWhat is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    if username:
        print(f"Current user: {username}")
        answer = input("Is this the correct username?: ")

        if answer == "yes":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()

# What is your name? Alan Menchaca
# We'll remember you when you come back, Alan Menchaca!

# Current user: Alan Menchaca
# Is this the correct username?: yes
# Welcome back, Alan Menchaca!

# Current user: Alan Menchaca
# Is this the correct username?: no

# What is your name? Alfonso Garza
# We'll remember you when you come back, Alfonso Garza!
