filename = 'guest_book.txt'

print("Escribe 'exit' cuando termines por favor")
while True:
    Nombre = input("\n¿Cual es tu nombre?")
    if Nombre == 'exit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(Nombre+"\n")
        print(f"Hola {Nombre} tu nombre se añadio al libro de visitas.")