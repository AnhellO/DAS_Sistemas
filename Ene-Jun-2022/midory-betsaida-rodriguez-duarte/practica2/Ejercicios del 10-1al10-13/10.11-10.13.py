#10.11

import json

numero = input("Cual es tu numero favorito? ")

with open('favorite_number.json', 'w') as f:
    json.dump(numero, f)
    print("gracias! lo recordare.")



with open('favorite_number.json') as filenombre:
    numero = json.load(filenombre)

print("Recuerdo tu numero favorito! " + str(numero) + ".")

#10.12
import json

try:
    with open('favorite_number.json') as filenombre:
        numero = json.load(filenombre)
except FileNotFoundError:
    numero = input("Cual es tu numero favorito? ")
    with open('favorite_number.json', 'w') as filenombre:
        json.dump(numero, filenombre)
    print("gracias!, Lo recordare.")
else:
    print("recuerdo tu numero favorito " + str(numero) + ".")

#10.13
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