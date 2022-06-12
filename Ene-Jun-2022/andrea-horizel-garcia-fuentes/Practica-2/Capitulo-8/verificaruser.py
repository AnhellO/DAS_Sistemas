import json

def get_stored_username():
    
    filenombre = 'username.json'
    try:
        with open(filenombre) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Cual es tu nombre? ")
    filenombre = 'username.json'
    with open(filenombre, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
     username = get_stored_username()
     if username:
        correct = input("Eres tu" + username + "? ")
        if correct == 'y':
            print("Bienvenido, " + username + "!")
        else:
            username = get_new_username()
            print("Lo recordare cuando lo necesites" + username + "!")
     else:
        username = get_new_username()
        print("Lo recordare cuando lo necesistes" + username + "!")

greet_user()