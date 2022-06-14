#10.1
with open("ProgramasC8910/aprende.txt") as archivo : 
    lectura = archivo.read()

    print(lectura)

#10.2

lectura = lectura.replace("python", " c++")
print(lectura)

#10.11

import json

numero = input("Cual es tu numero favorito? ")

with open('favorite_number.json', 'A') as f:
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
    with open(filenombre, 'A') as f_obj:
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

#10.3
nombre = input("Deme su nombre :")

with open("ProgramasC8910/nombre.txt", "w") as escribe: # la w es para escribir en el archivo
    escribe.write(nombre)

#10.4
with open("ProgramasC8910/nomsalu.txt", "w") as esc: 
    contador = 0

    while contador < 2:
        esc.writelines(input("Escribe nombre:"))
        esc.writelines("\n")
        contador += 1

#10.5
with open("ProgramasC8910/nomsalu.txt", "w") as es: 
    contador = 0

    while contador < 2:
        es.writelines(input("Que te gusta de python:"))
        es.writelines("\n")
        contador += 1
#10.6
        try: 
    numero = int(input("Dame numero 1 :"))
    numero2 = int(input("Dame numero 2 :"))

    suma = numero + numero2
    print(suma)

except ValueError:
    print("Ese no es un numero entero.")

#10.7
while True:
    try: 
        numero = int(input("Dame numero 1 :"))
        numero2 = int(input("Dame numero 2 :"))

        suma = numero + numero2
        print(suma)
        break
    except ValueError:
        print("Ese no es un numero entero.")
#10.8
try: 
    with open("ProgramasC8910/perros.txt") as perros:
        print(perros.read())
    with open("ProgramasC8910/gatos.txt") as gatos:
        print(gatos.read())

except FileNotFoundError:
    print("Archivo no encontrado.")

#10.9
try: 
    with open("ProgramasC8910/perros.txt") as perros:
        print(perros.read())
    with open("ProgramaC8910/gatos.txt") as gatos:
        print(gatos.read())

except FileNotFoundError:
    pass 

#10.10
with open("ProgramasC8910/lectura.txt") as contarpala:
    print(contarpala.read().count(" el "))

    
