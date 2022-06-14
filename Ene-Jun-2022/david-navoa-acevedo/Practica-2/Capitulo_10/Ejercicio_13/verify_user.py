import json

def get_stored_username():

    filename = 'Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_13/username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():

    username = input("What is your name? ")
    filename = 'Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_13/username.json'

    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)

    return username

def greet_user():

    username = get_stored_username()

    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
            return
    
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")

greet_user()
