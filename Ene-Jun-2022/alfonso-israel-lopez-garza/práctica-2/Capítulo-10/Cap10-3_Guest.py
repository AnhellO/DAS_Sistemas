nombre = input("Ingrese su nombre: ")
archivo = 'Guest.txt'

with open(archivo,'w') as file_object:
    file_object.write(nombre)