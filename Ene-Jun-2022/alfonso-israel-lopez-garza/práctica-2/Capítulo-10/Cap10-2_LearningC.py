'''Abriendo un archivo, y leyendo todo el contenido.'''
filename = 'learning_python.txt'
#Archivo completo
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('python','java'))