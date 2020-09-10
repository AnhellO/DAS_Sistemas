# Importando librerías
from numpy import array

# Listas y arreglos
a = array(['h', 101, 'l', 'l', 'o'])
x = ['h', 101, 'l', 'l', 'o']

print(a)
print(x)
print("Tamaño: ", len(x))

# Condicionales

if isinstance(x[1], int):
    x[1] = chr(x[1])
elif isinstance(x[1], str):
    pass
else:
    raise TypeError("Tipo no soportado!. No te pases! >:c")

print(' uwu '.join(x))

# Ciclos

for item in x:
    print(item)
    
for i in range(len(x)):
    print(x[i])
    
for i in range(1, 10, 2):
    print(i)
    
while len(x):
    print(x.pop(0))
    
while len(x):
    print(x.pop(0))
else:
    print('F para x :C')

# Operaciones con listas
x.append('H')
x.append('o')
x.append('l')
x.append('a')
x.insert(1, 'o')

# Entrada de datos

print(x)
respuesta = input("Hola?")
print(respuesta)

# Operadores aritméticos y booleanos
print(x)
print(10.1)
print(1 + 2 - 4 * 5 / 8 % 2)
print(2 ** 5)
print(True and True)
print(False and True)
print(False or True)
print(not False)

# Listas comprimidas
print([i for i in range(1, 11) if i % 2 == 0])
print([j for j in range(2, 101) if all(j % i != 0 for i in range(2, j))])
print([j for j in range(2, 101) if not(j % 2 or j % 3 or j % 5)])