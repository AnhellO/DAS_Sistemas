registro = True
archivo = 'guest_book.txt'
q = ""
while registro:
    nombre = input("Ingrese su nombre: ")
    
    with open(archivo,'a') as file_object:
        file_object.write(nombre +".\n")
    
    print("Ingrese (q) si ya no quiere ingresar mas usuarios.")
    q = input()
    if q:
        registro = False