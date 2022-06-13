#10.4
filenombre= 'guest_book.txt'

print("Escribe quit para poder finalizar.")
while True:
    nombre = input("\nCual es tu nombre? ")
    if nombre == 'quit':
        break
    else:
        with open(filenombre, 'a') as filenombre:
            filenombre.write(nombre + "\n")
        print("Hola! " + nombre + ", fuiste agregado al libro de visitas, gracias!.")