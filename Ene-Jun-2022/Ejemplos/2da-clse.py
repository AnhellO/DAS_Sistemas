# Strings

from operator import le


mi_string = "Esto es un string"
otro_string = 'Esto es otro string'

# Formateando strings
print(f"{mi_string}\n{otro_string}")
print("{0}\n{1}".format(mi_string, otro_string))

# "Manipulando" strings
print(mi_string[3])
print(mi_string[4:8])
print(mi_string[5:])
print(mi_string.lower())
print(mi_string.upper())
print(mi_string.title())
print(mi_string.split())
print(mi_string.split("s"))
print(len(mi_string))

# Esto devuelve un error
# mi_string[3] = 'a'

# Listas

mi_lista = [1, 2, 4, 8, 32]
print(f"Lista: {mi_lista}")

mi_lista_vacia = []
print(f"Lista vacía: {mi_lista_vacia}")

mi_lista_vacia.append('hola')
mi_lista_vacia.append('mundo')
mi_lista_vacia.append(True)
mi_lista_vacia.append(mi_lista)
print(f"Lista después de agregarle algunos elementos: {mi_lista_vacia}")

mi_lista_vacia.insert(3, False)
print(f"Lista después de insertarle un elemento: {mi_lista_vacia}")

mi_lista_vacia.clear()
print(f"Lista después de vaciarla: {mi_lista_vacia}")

# Condicionales

if len(mi_lista_vacia) == 0:
    print(f"mi_lista_vacia está vacía: {mi_lista_vacia}")
else:
    print(f"mi_lista_vacia contiene elementos: {mi_lista_vacia}")

# Esto es un la "lista comprimida"
mi_lista_vacia = [2 ** i for i in range(0, 9)]
if len(mi_lista_vacia) == 0:
    print(f"mi_lista_vacia está vacía: {mi_lista_vacia}")
elif len(mi_lista_vacia) < 10:
    print(f"mi_lista_vacia es pequeña: {mi_lista_vacia}")
else:
    print(f"mi_lista_vacia contiene muchos elementos: {mi_lista_vacia}")
