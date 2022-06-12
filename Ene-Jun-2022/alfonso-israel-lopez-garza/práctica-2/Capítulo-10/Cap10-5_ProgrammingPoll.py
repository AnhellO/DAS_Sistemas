registro = True
archivo = 'reason.txt'
q = ""
while registro:
    nombre = input("Ingrese su nombre: ")
    razon = input("Porque le gusta programar? ")
    with open(archivo,'a') as file_object:
        file_object.write(nombre +".\n")
        file_object.write(razon +".\n")
    
    print("Ingrese (q) si ya no quiere ingresar mas usuarios.")
    q = input()
    if q:
        registro = False