'''
--- Ejemplo D.R.Y.
'''

# Bad
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
# Utilizando operadores aritméticos
print(a+b-c*d/e**f//g%h)

# VS

# Good
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum(nums))

'''
--- Listas
'''
lista = [1, "2", 3.4, [1, 2, 3]]
print(lista)

'''
--- Strings
'''
string = "Hola Clase DAS"
string_2 = "Hola Clase DAS 2"

'''
--- Operaciones con Strings
'''
# Utilizando operadores booleanos
print(string == "Hola Clase DAS")
print(string != string_2)
print(string.lower() == string_2.lower())
print(string_2.lower()[0:14]) # igual a print(string_2.lower()[0:-2])
print(string.lower() == string_2.lower()[0:-2])

# Slicing es igual a [i,j)
print(nums[:5])
print(nums[4:])

'''
--- Operaciones con Listas
'''
# Tamaño de la lista
print(len(nums))
# Agregar un nuevo elemento a la lista
nums.append(9)
print(nums)
# Removiendo un elemento de la lista
nums.remove(5)
print(nums)