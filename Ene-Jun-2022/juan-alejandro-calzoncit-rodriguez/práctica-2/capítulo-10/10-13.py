import json

def get_stored_username():    
    filename = 'username.json'
    
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username

def greet_user():

    username = get_stored_username()
    if username:

        print(username)

        op = input("Is this your username? \nType 'y' if it is , 'n' is not.\n")

        if op == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()