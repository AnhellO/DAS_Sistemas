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
    username = input("¿Como te llamas? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        correct = input("¿Eres " + username + "? (y/n) ")
        if correct == 'y':
            print("Bienvenido, " + username)
        else:
            username = get_new_username()
            print("Te recordare la proxima vez " + username)
    else:
        username = get_new_username()
        print("Te recordare la proxima vez " + username)

greet_user()