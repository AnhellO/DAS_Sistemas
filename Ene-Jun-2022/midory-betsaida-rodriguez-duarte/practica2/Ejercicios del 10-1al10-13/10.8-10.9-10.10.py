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


