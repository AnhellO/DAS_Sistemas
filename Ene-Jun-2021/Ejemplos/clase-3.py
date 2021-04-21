'''
--- Tuplas
'''
# NO podemos modificar los valores de las tuplas
mi_tupla = (2, 4, 6, 8, 10)
print(mi_tupla)
# mi_tupla[0] = 0 -> Esto va a fallar

'''
--- Diccionarios
'''
mi_diccionario = {
   'x': 5,
   'y': 10
}

# Accedemos a las llaves del diccionario
print(mi_diccionario)
print(mi_diccionario['x'])
print(mi_diccionario['y'])

# Asignamos una nueva llave
mi_diccionario['z'] = 20
print(mi_diccionario['z'])
# Utilizamos algunas funciones clásicas de diccionarios
print(mi_diccionario.values())
print(mi_diccionario.keys())
print(mi_diccionario.items())
print(mi_diccionario.get('a', -1))

'''
--- Ciclos
'''
# Clásico ciclo for de python; OJO, funciona como foreach en otros lenguajes
for value in mi_diccionario.values():
    print(value)

# Accedemos a los pares llave => valor por medio del 'argument unpacking' de Python
# Aprovechamos para utilizar formateo de strings con la función .format()
for llave, valor in mi_diccionario.items():
    print("La llave de mi diccionario es: {}\nY el valor es: {}".format(llave, valor))

# Iteramos la tupla por medio de un ciclo for a la vieja escuela
# Aprovechamos de nuevo para utilizar formateo de strings, pero ahora con los 'f' strings
for indice in range(0, len(mi_tupla)):
    print(f"El valor en el índice #{indice} es de: {mi_tupla[indice]}")

# Mismo proceso que el ciclo anterior, pero utilizando un while
i = 0
while i < len(mi_tupla):
    print(f"El valor en el índice #{i} es de: {mi_tupla[i]}")
    i += 1

'''
--- Funciones
'''
# Simple función que suma dos números 'a' y 'b'
def suma(a, b):
    return a+b

print(suma(5, 6))

# OJO con las listas al pasarlas como parámetros en Python
mi_lista = ['a', 'b', 'c']
def juega_con_lista(lista):
    lista.append('d')
    print(f"La nueva lista tiene los valores: {lista}")

juega_con_lista(mi_lista[:])
print(f"La lista original tiene los valores: {mi_lista}")

# Argumentos Variables
def suma_mejorada(*numeros):
    # Python lo traduce a una 'tupla'
    print(numeros)
    total = 0
    for numero in numeros:
        total += numero

    return total
print(suma_mejorada(1, 2, 3, 4, 5, 6))

# Argumentos Llave/Valor
# Nuestra función 'suma_vocales' retorna la suma de los valores que sean vocales
def suma_vocales(**valores):
    # Python lo traduce a un 'diccionario'
    print(valores)
    total = 0
    for llave, valor in valores.items():
        if llave in 'aeiou':
            total += valor

    return total

print(f"El resultado es: {suma_vocales(b=2, c=3, d=4, e=5, x=6, y=7, z=8, r=0, u=10, a=1)}")

'''
--- Clases y Objetos
'''
class Persona:
    x = 'soy un atributo de clase'
    
    def __init__(self, nombre: str, edad: int, peso: float, estatura: float) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self._protegido = 'protected'
        self.__privado = 'private'

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nPeso: {self.peso}kg\nEstatura: {self.estatura}m"

p = Persona(
    'Jacinto',
    15,
    65.5,
    1.67
)

persona_2 = Persona(
    'Casimiro',
    16,
    68.5,
    1.7
)

# Para los atributos de clase, aquí x será igual a 'soy un atributo de clase'
print(p)
print(p.nombre, p.edad, p.peso, p.estatura, p.x)

print(persona_2)
print(persona_2.nombre, persona_2.edad, persona_2.peso, persona_2.estatura, persona_2.x)