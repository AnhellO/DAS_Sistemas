filename = 'Learning Python.txt'

print("--- Leyendo en todo el archivo:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Haciendo un bucle sobre el objeto de archivo:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Almacenando las líneas en una lista:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())