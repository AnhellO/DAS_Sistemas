'''Abriendo un archivo, y leyendo todo el contenido.'''
filename = 'learning_python.txt'
#Archivo completo
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#Linea por linea
with open(filename) as file_object:
    for line in file_object:
        print(line)

#Con una lista
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())