#10.3
nombre = input("Cual es tu nombre?")

filename = 'guest.txt'

with open(filename, 'w') as filename:
    filename.write(nombre)