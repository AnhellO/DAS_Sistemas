#10.1
with open("ProgramasC8910/aprende.txt") as archivo : 
    lectura = archivo.read()

    print(lectura)

#10.2

lectura = lectura.replace("python", " c++")
print(lectura)
