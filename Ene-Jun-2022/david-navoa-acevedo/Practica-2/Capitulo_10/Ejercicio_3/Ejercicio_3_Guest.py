
File = "Ene-Jun-2022/david-navoa-acevedo/Practica-2/Capitulo_10/Ejercicio_3/Guest.txt"

def write_name(name):

    with open(File, 'w') as opened_file:
        opened_file.write(name)

    with open(File) as read_file:
        file = read_file.read()
    
    print(file)

name = input("Type your name please ")
write_name(name)
