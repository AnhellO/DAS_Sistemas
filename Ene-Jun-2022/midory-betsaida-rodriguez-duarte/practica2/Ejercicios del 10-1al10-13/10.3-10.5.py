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






    


