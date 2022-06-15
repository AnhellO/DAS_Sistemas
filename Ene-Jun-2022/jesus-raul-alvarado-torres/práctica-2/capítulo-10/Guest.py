Nombre = input("¿Cual es tu nombre?")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(Nombre)